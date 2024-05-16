# Stock Trading
# Created by Maximillian M. Estrada on 2024-05-16

import logging
import pandas as pd
import uuid
import hashlib
from decimal import Decimal

from django.core.files.storage import default_storage

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
        folder = generate_uuid(f"{user.pk}_{user.username}")
        file_path = f"{folder}/{filename}"
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
                except Stock.DoesNotExist as ex:
                    logger.error(f"ERROR: Stock code {l.STOCK} not found, skipping. {ex}")
        except Exception as ex:
            logger.error(f"ERROR: Failed to read line in CSV file. {ex}")
        return Transaction.objects.filter(pk__in=created_orders)


class PortfolioService:
    """
    PortfolioService process the business logic regarding the portfolio.
    """
    @staticmethod
    def update_portfolio(
            transation
    ):
        """
        Update portfolio.

        :param transation:
        :return:
        """
        if transation.status is not Transaction.Status.CLEARED:
            return None

        portfolio, created = Portfolio.objects.get_or_create(
            user=transation.user,
            stock=transation.stock,
            defaults={'user': transation.user, 'stock': transation.stock})

        portfolio.total_share += transation.quantity
        portfolio.total_value = portfolio.total_value + transation.amount
        portfolio.average_price = (portfolio.average_price + transation.price) * Decimal(0.50)
        portfolio.save()
        return portfolio
