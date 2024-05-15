# Stock Trading
# Created by Maximillian M. Estrada on 2024-05-16

from core.models import Transaction


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
