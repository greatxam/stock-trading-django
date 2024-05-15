# Stock Trading
# Created by Maximillian M. Estrada on 2024-05-15

import uuid

from django.urls import reverse

from rest_framework.test import APITestCase

from core.tests.mixins import APITestCaseMixin
from core.tests.helpers import (
    UserTestHelper,
    StockTestHelper
)


class StockAPITestCase(APITestCaseMixin, APITestCase):
    def test_list_stock(self):
        """
        List stocks without authenticated user, should not be allow.

        :return:
        """
        self.assertUnauthorizedView(reverse(StockTestHelper.API_NAME_STOCK_LIST))

    def test_list_stock_with_user(self):
        """
        List stocks with authenticated user, should be allow.

        :return:
        """
        self.client.force_login(UserTestHelper.create_test_user())
        self.assertUserCanView(reverse(StockTestHelper.API_NAME_STOCK_LIST))

    def test_list_stock_with_super_user(self):
        """
        List stocks with authenticated super user, should be allow.

        :return:
        """
        self.client.force_login(UserTestHelper.create_test_super_user())
        self.assertUserCanView(reverse(StockTestHelper.API_NAME_STOCK_LIST))

    def test_create_stock(self):
        """
        Creating stock without authenticated user, should not be allow.

        :return:
        """
        self.assertUnauthorizedAdd(
            reverse(StockTestHelper.API_NAME_STOCK_LIST),
            StockTestHelper.STOCK_DATA_1)

    def test_create_stock_with_user(self):
        """
        Creating stock with authenticated user, should not be allow.

        :return:
        """
        self.client.force_login(UserTestHelper.create_test_user())
        self.assertUserForbidAdd(
            reverse(StockTestHelper.API_NAME_STOCK_LIST),
            StockTestHelper.STOCK_DATA_1)

    def test_create_stock_with_super_user(self):
        """
        Creating stock with authenticated super user, should be allow.

        :return:
        """
        self.client.force_login(UserTestHelper.create_test_super_user())
        self.assertUserCanAdd(
            reverse(StockTestHelper.API_NAME_STOCK_LIST),
            StockTestHelper.STOCK_DATA_1)

    def test_detail_stock(self):
        """
        Getting stock without authenticated user, should not be allow.

        :return:
        """
        self.assertUnauthorizedView(
            reverse(StockTestHelper.API_NAME_STOCK_DETAIL, kwargs={'pk': uuid.uuid4()})
        )

    def test_detail_stock_with_user(self):
        """
        Getting stock with authenticated user, should be allow.

        :return:
        """
        stock = StockTestHelper.create_test_stock()
        self.client.force_login(UserTestHelper.create_test_user())
        self.assertUserCanView(
            reverse(StockTestHelper.API_NAME_STOCK_DETAIL, kwargs={'pk': stock.id})
        )

    def test_detail_stock_with_super_user(self):
        """
        Getting stock with authenticated super user, should be allow.

        :return:
        """
        stock = StockTestHelper.create_test_stock()
        self.client.force_login(UserTestHelper.create_test_super_user())
        self.assertUserCanView(
            reverse(StockTestHelper.API_NAME_STOCK_DETAIL, kwargs={'pk': stock.id})
        )

    def test_change_stock(self):
        """
        Changing stock without authenticated user, should not be allow.

        :return:
        """
        stock = StockTestHelper.create_test_stock()
        stock_data = StockTestHelper.STOCK_DATA_1
        stock_data['price'] = 450.00

        self.assertUnauthorizedChange(
            reverse(StockTestHelper.API_NAME_STOCK_DETAIL, kwargs={'pk': stock.pk}),
            data=stock_data
        )

    def test_change_stock_with_user(self):
        """
        Changing stock with authenticated user, should not be allow.

        :return:
        """
        stock = StockTestHelper.create_test_stock()
        stock_data = StockTestHelper.STOCK_DATA_1
        stock_data['price'] = 450.00

        self.client.force_login(UserTestHelper.create_test_user())
        self.assertUserForbidChange(
            reverse(StockTestHelper.API_NAME_STOCK_DETAIL, kwargs={'pk': stock.pk}),
            data=stock_data
        )

    def test_change_stock_with_super_user(self):
        """
        Changing stock with authenticated super user, should be allow.

        :return:
        """
        stock = StockTestHelper.create_test_stock()
        stock_data = StockTestHelper.STOCK_DATA_1
        stock_data['price'] = 450.00

        self.client.force_login(UserTestHelper.create_test_super_user())
        self.assertUserCanChange(
            reverse(StockTestHelper.API_NAME_STOCK_DETAIL, kwargs={'pk': stock.pk}),
            data=stock_data
        )

    def test_delete_stock(self):
        """
        Deleting stock without authenticated user, should not be allow.

        :return:
        """
        stock = StockTestHelper.create_test_stock()
        self.assertUnauthorizedDelete(reverse(
            StockTestHelper.API_NAME_STOCK_DETAIL, kwargs={'pk': stock.pk})
        )

    def test_delete_stock_with_user(self):
        """
        Deleting stock with authenticated user, should not be allow.

        :return:
        """
        stock = StockTestHelper.create_test_stock()

        self.client.force_login(UserTestHelper.create_test_user())
        self.assertUserForbidDelete(reverse(
            StockTestHelper.API_NAME_STOCK_DETAIL, kwargs={'pk': stock.pk})
        )

    def test_delete_stock_with_super_user(self):
        """
        Deleting stock with authenticated super user, should be allow.

        :return:
        """
        stock = StockTestHelper.create_test_stock()

        self.client.force_login(UserTestHelper.create_test_super_user())
        self.assertUserCanDelete(reverse(
            StockTestHelper.API_NAME_STOCK_DETAIL, kwargs={'pk': stock.pk})
        )
