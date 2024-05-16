# Stock Trading
# Created by Maximillian M. Estrada on 2024-05-15

import uuid

from django.urls import reverse

from rest_framework.test import APITestCase

from core.tests.mixins import APITestCaseMixin
from core.tests.helpers import (
    UserTestHelper,
    StockTestHelper,
    TradeTestHelper,
)


class TradeAPITestCase(APITestCaseMixin, APITestCase):
    def test_list_trade(self):
        """
        List trades without authenticated user, should not be allow.

        :return:
        """
        self.assertUnauthorizedView(reverse(TradeTestHelper.API_NAME_TRADE_LIST))

    def test_list_trade_with_user(self):
        """
        List trades with authenticated user, should be allow.

        :return:
        """
        self.client.force_login(UserTestHelper.create_test_user())
        self.assertUserCanView(reverse(TradeTestHelper.API_NAME_TRADE_LIST))

    def test_list_trade_with_super_user(self):
        """
        List trades with authenticated super user, should be allow.

        :return:
        """
        self.client.force_login(UserTestHelper.create_test_super_user())
        self.assertUserCanView(reverse(TradeTestHelper.API_NAME_TRADE_LIST))

    def test_create_trade(self):
        """
        Creating trade without authenticated user, should not be allow.

        :return:
        """
        stock = StockTestHelper.create_test_stock()
        trade_data = TradeTestHelper.TRADE_DATA_1
        trade_data['stock_id'] = stock.pk

        self.assertUnauthorizedAdd(
            reverse(TradeTestHelper.API_NAME_TRADE_LIST),
            trade_data)

    def test_create_trade_with_user(self):
        """
        Creating trade with authenticated user, should not be allow.

        :return:
        """
        stock = StockTestHelper.create_test_stock()
        trade_data = TradeTestHelper.TRADE_DATA_1
        trade_data['stock'] = stock.pk

        self.client.force_login(UserTestHelper.create_test_user())
        self.assertDisabledAction(
            reverse(TradeTestHelper.API_NAME_TRADE_LIST),
            trade_data)

    def test_create_trade_with_super_user(self):
        """
        Creating trade with authenticated super user, should not be allow.

        :return:
        """
        stock = StockTestHelper.create_test_stock()
        trade_data = TradeTestHelper.TRADE_DATA_1
        trade_data['stock'] = stock.pk

        self.client.force_login(UserTestHelper.create_test_super_user())
        self.assertDisabledAction(
            reverse(TradeTestHelper.API_NAME_TRADE_LIST),
            trade_data)

    def test_detail_trade(self):
        """
        Getting trade without authenticated user, should not be allow.

        :return:
        """
        self.assertUnauthorizedView(
            reverse(TradeTestHelper.API_NAME_TRADE_DETAIL, kwargs={'pk': uuid.uuid4()})
        )

    def test_detail_trade_with_user(self):
        """
        Getting trade with authenticated user, should not be allow.

        :return:
        """
        user = UserTestHelper.create_test_user(username="testowner")
        stock = StockTestHelper.create_test_stock()
        trade = TradeTestHelper.create_test_trade(user=user, stock=stock)

        self.client.force_login(UserTestHelper.create_test_user())
        self.assertForbidView(
            reverse(TradeTestHelper.API_NAME_TRADE_DETAIL, kwargs={'pk': trade.pk})
        )

    def test_detail_trade_with_owner(self):
        """
        Getting trade with authenticated owner, should be allow.

        :return:
        """
        user = UserTestHelper.create_test_user(username="testowner")
        stock = StockTestHelper.create_test_stock()
        trade = TradeTestHelper.create_test_trade(user=user, stock=stock)

        self.client.force_login(user)
        self.assertUserCanView(
            reverse(TradeTestHelper.API_NAME_TRADE_DETAIL, kwargs={'pk': trade.pk})
        )

    def test_detail_trade_with_super_user(self):
        """
        Getting trade with authenticated super user, should be allow.

        :return:
        """
        user = UserTestHelper.create_test_user(username="testowner")
        stock = StockTestHelper.create_test_stock()
        trade = TradeTestHelper.create_test_trade(user=user, stock=stock)

        self.client.force_login(UserTestHelper.create_test_super_user())
        self.assertUserCanView(
            reverse(TradeTestHelper.API_NAME_TRADE_DETAIL, kwargs={'pk': trade.pk})
        )

    def test_change_trade(self):
        """
        Changing trade without authenticated user, should not be allow.

        :return:
        """
        user = UserTestHelper.create_test_user(username="testowner")
        stock = StockTestHelper.create_test_stock()
        trade = TradeTestHelper.create_test_trade(user=user, stock=stock)
        trade_data = {
            'quantity': 120
        }

        self.assertUnauthorizedChange(
            reverse(TradeTestHelper.API_NAME_TRADE_DETAIL, kwargs={'pk': trade.pk}),
            data=trade_data
        )

    def test_change_trade_with_user(self):
        """
        Changing trade with authenticated user, should not be allow.

        :return:
        """
        user = UserTestHelper.create_test_user(username="testowner")
        stock = StockTestHelper.create_test_stock()
        trade = TradeTestHelper.create_test_trade(user=user, stock=stock)
        trade_data = {
            'quantity': 120
        }

        self.client.force_login(UserTestHelper.create_test_user())
        self.assertDisabledAction(
            reverse(TradeTestHelper.API_NAME_TRADE_DETAIL, kwargs={'pk': trade.pk}),
            data=trade_data
        )

    def test_change_trade_with_owner(self):
        """
        Changing trade with authenticated owner, should not be allow.

        :return:
        """
        user = UserTestHelper.create_test_user(username="testowner")
        stock = StockTestHelper.create_test_stock()
        trade = TradeTestHelper.create_test_trade(user=user, stock=stock)
        trade_data = {
            'quantity': 120
        }

        self.client.force_login(user)
        self.assertDisabledAction(
            reverse(TradeTestHelper.API_NAME_TRADE_DETAIL, kwargs={'pk': trade.pk}),
            data=trade_data
        )

    def test_change_trade_with_super_user(self):
        """
        Changing trade with authenticated super user, should not be allow.

        :return:
        """
        user = UserTestHelper.create_test_user(username="testowner")
        stock = StockTestHelper.create_test_stock()
        trade = TradeTestHelper.create_test_trade(user=user, stock=stock)
        trade_data = {
            'quantity': 120
        }

        self.client.force_login(UserTestHelper.create_test_super_user())
        self.assertDisabledAction(
            reverse(TradeTestHelper.API_NAME_TRADE_DETAIL, kwargs={'pk': trade.pk}),
            data=trade_data
        )

    def test_delete_trade(self):
        """
        Deleting trade without authenticated user, should not be allow.

        :return:
        """
        user = UserTestHelper.create_test_user(username="testowner")
        stock = StockTestHelper.create_test_stock()
        trade = TradeTestHelper.create_test_trade(user=user, stock=stock)

        self.assertUnauthorizedDelete(
            reverse(TradeTestHelper.API_NAME_TRADE_DETAIL, kwargs={'pk': trade.pk})
        )

    def test_delete_trade_with_user(self):
        """
        Deleting trade with authenticated user, should not be allow.

        :return:
        """
        user = UserTestHelper.create_test_user(username="testowner")
        stock = StockTestHelper.create_test_stock()
        trade = TradeTestHelper.create_test_trade(user=user, stock=stock)

        self.client.force_login(UserTestHelper.create_test_user())
        self.assertDisabledAction(
            reverse(TradeTestHelper.API_NAME_TRADE_DETAIL, kwargs={'pk': trade.pk})
        )

    def test_delete_trade_with_owner(self):
        """
        Deleting trade with authenticated owner, should not be allow.

        :return:
        """
        user = UserTestHelper.create_test_user(username="testowner")
        stock = StockTestHelper.create_test_stock()
        trade = TradeTestHelper.create_test_trade(user=user, stock=stock)

        self.client.force_login(user)
        self.assertDisabledAction(
            reverse(TradeTestHelper.API_NAME_TRADE_DETAIL, kwargs={'pk': trade.pk})
        )

    def test_delete_trade_with_super_user(self):
        """
        Deleting trade with authenticated super user, should not be allow.

        :return:
        """
        user = UserTestHelper.create_test_user(username="testowner")
        stock = StockTestHelper.create_test_stock()
        trade = TradeTestHelper.create_test_trade(user=user, stock=stock)

        self.client.force_login(UserTestHelper.create_test_super_user())
        self.assertDisabledAction(
            reverse(TradeTestHelper.API_NAME_TRADE_DETAIL, kwargs={'pk': trade.pk})
        )
