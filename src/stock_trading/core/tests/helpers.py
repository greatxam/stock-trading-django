# Stock Trading
# Created by Maximillian M. Estrada on 2024-05-15

from django.contrib.auth import get_user_model

from core.models import *

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
