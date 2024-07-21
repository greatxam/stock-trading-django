# Stock Trading
# Created by Maximillian M. Estrada on 2024-05-16

import logging
import pandas as pd
import uuid
import hashlib
from decimal import Decimal

from django.core.files.storage import default_storage
from django.db.models import Q, Sum

from core.models import (
    Stock,
    Portfolio,
    Transaction
)

logger = logging.getLogger(__name__)


def get_type_by_name(name: str):
    types = dict([i[::-1] for i in Transaction.Type.CHOICES])
    return types[name]


def generate_uuid(val: str):
    hex_string = hashlib.md5(val.encode("UTF-8")).hexdigest()
    return uuid.UUID(hex=hex_string)


class TransactionService:
    """
    TransactionService process the business logic regarding the transaction.
    """

    @staticmethod
    def create_transaction(
            user,
            stock,
            quantity,
            price,
            type=Transaction.Type.BUY,
            status=Transaction.Status.PENDING
    ):
        """
        Create order transaction.

        :param user:
        :param stock:
        :param quantity:
        :param price:
        :param type:
        :param status:
        :return:
        """
        transaction = Transaction.objects.create(
            user=user,
            stock=stock,
            quantity=quantity,
            price=price,
            amount=quantity * price,
            type=type,
            status=status
        )

        transaction.save()
        return transaction

    @staticmethod
    def save_transaction(
            transaction,
            commit=True
    ):
        """
        Compute and save transaction.

        :param transaction:
        :param commit:
        :return:
        """
        transaction.amount = transaction.quantity * transaction.price
        if commit:
            transaction.save()
        return transaction

    @staticmethod
    def match_order_transactions(
            order_1: Transaction,
            order_2: Transaction,
            clear_both=False
    ):
        """
        Match order transaction for both buy and sell.

        :param order_1:
        :param order_2:
        :param clear_both:
        :return:
        """
        # trade transaction for order_1
        trade = TransactionService.clone_transaction(order_1)
        trade.is_order = False
        trade.quantity = order_2.remainder_quantity()
        trade.price = order_2.price
        TransactionService.clear_transaction(trade)
        order_1.trades.add(trade)
        if clear_both:
            TransactionService.clear_transaction(order_1)

        # trade transaction for order_2
        trade = TransactionService.clone_transaction(order_2)
        trade.is_order = False
        trade.quantity = order_2.remainder_quantity()
        TransactionService.clear_transaction(trade)
        order_2.trades.add(trade)
        TransactionService.clear_transaction(order_2)

    @staticmethod
    def clone_transaction(
            transaction: Transaction,
    ):
        """
        Create a duplicate of the transaction instance.

        :param transaction:
        :return:
        """
        return TransactionService.create_transaction(
            user=transaction.user,
            stock=transaction.stock,
            quantity=transaction.quantity,
            price=transaction.price,
            type=transaction.type,
            status=transaction.status,
        )

    @staticmethod
    def clear_transaction(
            transaction: Transaction,
            commit=True
    ):
        """
        Clear transaction status.

        :param transaction:
        :param commit:
        :return:
        """
        transaction.status = Transaction.Status.CLEARED
        if commit:
            transaction.save()

            # update stock
            try:
                stock = Stock.objects.get(pk=transaction.stock.pk)
                stock.price = transaction.price
                stock.save(update_fields=['price', 'modified'])
            except Stock.DoesNotExist as e:
                logger.info(f"ERROR clear_transaction: {e}")
                print(f"ERROR clear_transaction: {e}")

            logger.info(f"clear_transaction: {transaction}")
            print(f"clear_transaction: {transaction}")
        return transaction

    @staticmethod
    def store_bulk_order_file(
            user,
            filename,
            file,
    ):
        """
        Stored the bulk order file.

        :param user:
        :param filename:
        :param file:
        :return:
        """
        # folder = generate_uuid(f"{user.pk}_{user.username}")
        file_path = f"{user.pk}/{filename}"
        return default_storage.save(file_path, file)

    @staticmethod
    def bulk_orders(
            user,
            filename,
            file,
    ):
        """
        Process bulk orders.

        :param user:
        :param filename:
        :param file:
        :return:
        """
        logger.info(f"START bulk_orders: {user.username} - {filename}")

        df = pd.read_csv(
            file,
            usecols=["TYPE", "STOCK", "QUANTITY", "PRICE"],
        )

        created_orders = set()
        try:
            for l in df.itertuples():
                try:
                    stock = Stock.objects.get(code=l.STOCK)
                    order = TransactionService.create_transaction(
                        user=user,
                        stock=stock,
                        type=get_type_by_name(l.TYPE),
                        quantity=l.QUANTITY,
                        price=l.PRICE
                    )
                    created_orders.add(order.pk)
                except Stock.DoesNotExist as e:
                    logger.error(f"ERROR: Stock code {l.STOCK} not found, skipping. {e}")
        except Exception as ex:
            logger.error(f"ERROR: Failed to read line in CSV file. {ex}")
        return Transaction.objects.filter(pk__in=created_orders)

    @staticmethod
    def process_order_transaction(
            stock_code
    ):
        """
        Process order transactions for clearing.

        :param stock_code:
        :return:
        """
        logger.info(f"START process_order_transaction: {stock_code}")
        print(f"START process_order_transaction: {stock_code}")

        transactions = Transaction.objects.filter(
            is_order=True,
            status=Transaction.Status.PENDING).order_by('created')
        if stock_code:
            transactions = transactions.filter(stock__code=stock_code)

        for t in transactions:
            TransactionService.process_transaction(t.pk)

        logger.info(f"FINISH process_order_transaction")
        print(f"FINISH process_order_transaction")

    @staticmethod
    def process_transaction(
            transaction_id
    ):
        """
        Process order transaction.

        :param transaction_id:
        :return:
        """
        try:
            transaction = Transaction.objects.get(pk=transaction_id)
            if transaction.status == Transaction.Status.CLEARED:
                return
        except Transaction.DoesNotExist as e:
            return
        logger.info(f"process_transaction {transaction.get_type_display()}: {transaction}")
        print(f"process_transaction {transaction.get_type_display()}: {transaction}")

        if transaction.type is Transaction.Type.SELL:
            orders = Transaction.objects.filter(
                ~Q(user__pk=transaction.user.pk),
                stock__pk=transaction.stock.pk,
                price__gte=transaction.price,
                status=Transaction.Status.PENDING,
                type=Transaction.Type.BUY).order_by('-price', 'created')
        else:
            orders = Transaction.objects.filter(
                ~Q(user__pk=transaction.user.pk),
                stock__pk=transaction.stock.pk,
                price__lte=transaction.price,
                status=Transaction.Status.PENDING,
                type=Transaction.Type.SELL).order_by('price', 'created')

        for order in orders:
            quantity = transaction.remainder_quantity() - order.remainder_quantity()
            if quantity > 0:
                # transaction still have remainder
                TransactionService.match_order_transactions(transaction, order)
            elif quantity < 0:
                # order still have remainder
                TransactionService.match_order_transactions(order, transaction)
                break
            else:
                # cleared both orders
                TransactionService.match_order_transactions(transaction, order, True)
                break


class PortfolioService:
    """
    PortfolioService process the business logic regarding the portfolio.
    """
    @staticmethod
    def update_portfolio(
            transaction
    ):
        """
        Update portfolio.

        :param transaction:
        :return:
        """
        if transaction.status is not Transaction.Status.CLEARED \
                or transaction.is_order:
            return None

        portfolio, created = Portfolio.objects.get_or_create(
            user=transaction.user,
            stock=transaction.stock,
            defaults={'user': transaction.user, 'stock': transaction.stock})

        portfolio.total_share += transaction.quantity
        portfolio.total_value = portfolio.total_value + transaction.amount
        portfolio.average_price = (portfolio.average_price + transaction.price) * Decimal(0.50)
        portfolio.save()
        return portfolio
