# Stock Trading
# Created by Maximillian M. Estrada on 2024-05-15

from django.contrib.auth import get_user_model

from core.models import *
from core.services import TransactionService

User = get_user_model()


class UserTestHelper:
    @staticmethod
    def create_test_user(
            username='testuser01',
            password='testuser01',
            email='testuser01@stocktrading.test'
    ):
        """
        Create test user.

        :param username:
        :param password:
        :param email:
        :return User:
        """
        return User.objects.create_user(
            username=username,
            password=password,
            email=email
        )

    @staticmethod
    def create_test_super_user(
            username='testuser01',
            password='testuser01',
            email='testuser01@stocktrading.test'
    ):
        """
        Create test super user.

        :param username:
        :param password:
        :param email:
        :return User:
        """
        return User.objects.create_superuser(
            username=username,
            password=password,
            email=email
        )


class StockTestHelper:
    # API URL names
    API_NAME_STOCK_LIST = 'core-api-stock-list'
    API_NAME_STOCK_DETAIL = 'core-api-stock-detail'

    STOCK_DATA_1 = {
        'code': 'APP',
        'name': 'Apple',
        'price': 100.00
    }

    STOCK_DATA_2 = {
        'code': 'TST',
        'name': 'Test Stock',
        'price': 200.00
    }

    @staticmethod
    def create_test_stock(
            code=STOCK_DATA_1['code'],
            name=STOCK_DATA_1['name'],
            price=STOCK_DATA_1['price'],
    ):
        data = {
            'code': code,
            'name': name,
            'price': price
        }
        return Stock.objects.create(**data)


class OrderTestHelper:
    # API URL names
    API_NAME_ORDER_LIST = 'core-api-order-list'
    API_NAME_ORDER_DETAIL = 'core-api-order-detail'

    ORDER_DATA_1 = {
        'type': Transaction.Type.BUY,
        'quantity': 20,
        'price': 100.00
    }

    ORDER_DATA_2 = {
        'type': Transaction.Type.SELL,
        'quantity': 10,
        'price': 100.00
    }

    @staticmethod
    def create_test_order(
            user,
            stock,
            type=ORDER_DATA_1['type'],
            quantity=ORDER_DATA_1['quantity'],
            price=ORDER_DATA_1['price']
    ):
        """
        Create test order transaction.

        :param user:
        :param stock:
        :param type:
        :param quantity:
        :param price:
        :return:
        """
        return TransactionService.create_transaction(
            user=user,
            stock=stock,
            type=type,
            quantity=quantity,
            price=price
        )


class TradeTestHelper:
    # API URL names
    API_NAME_TRADE_LIST = 'core-api-trade-list'
    API_NAME_TRADE_DETAIL = 'core-api-trade-detail'

    TRADE_DATA_1 = {
        'type': Transaction.Type.BUY,
        'status': Transaction.Status.CLEARED,
        'quantity': 20,
        'price': 100.00
    }

    TRADE_DATA_2 = {
        'type': Transaction.Type.SELL,
        'status': Transaction.Status.CLEARED,
        'quantity': 10,
        'price': 100.00
    }

    @staticmethod
    def create_test_trade(
            user,
            stock,
            type=TRADE_DATA_1['type'],
            status=TRADE_DATA_1['status'],
            quantity=TRADE_DATA_1['quantity'],
            price=TRADE_DATA_1['price']
    ):
        """
        Create test order transaction.

        :param user:
        :param stock:
        :param type:
        :param status:
        :param quantity:
        :param price:
        :return:
        """
        return TransactionService.create_transaction(
            user=user,
            stock=stock,
            type=type,
            status=status,
            quantity=quantity,
            price=price
        )
