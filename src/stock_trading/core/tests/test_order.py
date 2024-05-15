# Stock Trading
# Created by Maximillian M. Estrada on 2024-05-15

import uuid

from django.urls import reverse

from rest_framework.test import APITestCase

from core.tests.mixins import APITestCaseMixin
from core.tests.helpers import (
    UserTestHelper,
    StockTestHelper,
    OrderTestHelper,
)


class OrderAPITestCase(APITestCaseMixin, APITestCase):
    def test_list_order(self):
        """
        List orders without authenticated user, should not be allow.

        :return:
        """
        self.assertUnauthorizedView(reverse(OrderTestHelper.API_NAME_ORDER_LIST))

    def test_list_order_with_user(self):
        """
        List orders with authenticated user, should be allow.

        :return:
        """
        self.client.force_login(UserTestHelper.create_test_user())
        self.assertUserCanView(reverse(OrderTestHelper.API_NAME_ORDER_LIST))

    def test_list_order_with_super_user(self):
        """
        List orders with authenticated super user, should be allow.

        :return:
        """
        self.client.force_login(UserTestHelper.create_test_super_user())
        self.assertUserCanView(reverse(OrderTestHelper.API_NAME_ORDER_LIST))

    def test_create_order(self):
        """
        Creating order without authenticated user, should not be allow.

        :return:
        """
        stock = StockTestHelper.create_test_stock()
        order_data = OrderTestHelper.ORDER_DATA_1
        order_data['stock_id'] = stock.pk

        self.assertUnauthorizedAdd(
            reverse(OrderTestHelper.API_NAME_ORDER_LIST),
            order_data)

    def test_create_order_with_user(self):
        """
        Creating order with authenticated user, should be allow.

        :return:
        """
        stock = StockTestHelper.create_test_stock()
        order_data = OrderTestHelper.ORDER_DATA_1
        order_data['stock'] = stock.pk

        self.client.force_login(UserTestHelper.create_test_user())
        self.assertUserCanAdd(
            reverse(OrderTestHelper.API_NAME_ORDER_LIST),
            order_data)

    def test_create_order_with_super_user(self):
        """
        Creating order with authenticated super user, should be allow.

        :return:
        """
        stock = StockTestHelper.create_test_stock()
        order_data = OrderTestHelper.ORDER_DATA_1
        order_data['stock'] = stock.pk

        self.client.force_login(UserTestHelper.create_test_super_user())
        self.assertUserCanAdd(
            reverse(OrderTestHelper.API_NAME_ORDER_LIST),
            order_data)

    def test_create_order_amount(self):
        """
        Creating order amount with authenticated user, should be allow.

        :return:
        """
        stock = StockTestHelper.create_test_stock()
        order_data = {
            'type': OrderTestHelper.ORDER_DATA_1['type'],
            'stock': stock.pk,
            'quantity': 10,
            'price': 50.00
        }

        self.client.force_login(UserTestHelper.create_test_user())
        response = self.assertUserCanAdd(
            reverse(OrderTestHelper.API_NAME_ORDER_LIST),
            order_data)
        self.assertEqual(
            float(response.data.get('amount', 0.00)),
            order_data.get('quantity') * order_data.get('price'))

    def test_detail_order(self):
        """
        Getting order without authenticated user, should not be allow.

        :return:
        """
        self.assertUnauthorizedView(
            reverse(OrderTestHelper.API_NAME_ORDER_DETAIL, kwargs={'pk': uuid.uuid4()})
        )

    def test_detail_order_with_user(self):
        """
        Getting order with authenticated user, should not be allow.

        :return:
        """
        user = UserTestHelper.create_test_user(username="testowner")
        stock = StockTestHelper.create_test_stock()
        order = OrderTestHelper.create_test_order(user=user, stock=stock)

        self.client.force_login(UserTestHelper.create_test_user())
        self.assertForbidView(
            reverse(OrderTestHelper.API_NAME_ORDER_DETAIL, kwargs={'pk': order.pk})
        )

    def test_detail_order_with_owner(self):
        """
        Getting order with authenticated owner, should be allow.

        :return:
        """
        user = UserTestHelper.create_test_user(username="testowner")
        stock = StockTestHelper.create_test_stock()
        order = OrderTestHelper.create_test_order(user=user, stock=stock)

        self.client.force_login(user)
        self.assertUserCanView(
            reverse(OrderTestHelper.API_NAME_ORDER_DETAIL, kwargs={'pk': order.pk})
        )

    def test_detail_order_with_super_user(self):
        """
        Getting order with authenticated super user, should be allow.

        :return:
        """
        user = UserTestHelper.create_test_user(username="testowner")
        stock = StockTestHelper.create_test_stock()
        order = OrderTestHelper.create_test_order(user=user, stock=stock)

        self.client.force_login(UserTestHelper.create_test_super_user())
        self.assertUserCanView(
            reverse(OrderTestHelper.API_NAME_ORDER_DETAIL, kwargs={'pk': order.pk})
        )

    def test_change_order(self):
        """
        Changing order without authenticated user, should not be allow.

        :return:
        """
        user = UserTestHelper.create_test_user(username="testowner")
        stock = StockTestHelper.create_test_stock()
        order = OrderTestHelper.create_test_order(user=user, stock=stock)
        order_data = {
            'quantity': 120
        }

        self.assertUnauthorizedChange(
            reverse(OrderTestHelper.API_NAME_ORDER_DETAIL, kwargs={'pk': order.pk}),
            data=order_data
        )

    def test_change_order_with_user(self):
        """
        Changing order with authenticated user, should not be allow.

        :return:
        """
        user = UserTestHelper.create_test_user(username="testowner")
        stock = StockTestHelper.create_test_stock()
        order = OrderTestHelper.create_test_order(user=user, stock=stock)
        order_data = {
            'quantity': 120
        }

        self.client.force_login(UserTestHelper.create_test_user())
        self.assertUserForbidChange(
            reverse(OrderTestHelper.API_NAME_ORDER_DETAIL, kwargs={'pk': order.pk}),
            data=order_data
        )

    def test_change_order_with_owner(self):
        """
        Changing order with authenticated owner, should be allow.

        :return:
        """
        user = UserTestHelper.create_test_user(username="testowner")
        stock = StockTestHelper.create_test_stock()
        order = OrderTestHelper.create_test_order(user=user, stock=stock)
        order_data = {
            'quantity': 120
        }

        self.client.force_login(user)
        self.assertUserCanChange(
            reverse(OrderTestHelper.API_NAME_ORDER_DETAIL, kwargs={'pk': order.pk}),
            data=order_data
        )

    def test_change_order_with_super_user(self):
        """
        Changing order with authenticated super user, should be allow.

        :return:
        """
        user = UserTestHelper.create_test_user(username="testowner")
        stock = StockTestHelper.create_test_stock()
        order = OrderTestHelper.create_test_order(user=user, stock=stock)
        order_data = {
            'quantity': 120
        }

        self.client.force_login(UserTestHelper.create_test_super_user())
        self.assertUserCanChange(
            reverse(OrderTestHelper.API_NAME_ORDER_DETAIL, kwargs={'pk': order.pk}),
            data=order_data
        )

    def test_change_order_amount(self):
        """
        Changing order amount with authenticated owner, should be allow.

        :return:
        """
        user = UserTestHelper.create_test_user(username="testowner")
        stock = StockTestHelper.create_test_stock()
        order = OrderTestHelper.create_test_order(user=user, stock=stock)
        order_data = {
            'quantity': 500
        }

        self.client.force_login(user)
        response = self.assertUserCanChange(
            reverse(OrderTestHelper.API_NAME_ORDER_DETAIL, kwargs={'pk': order.pk}),
            order_data)
        self.assertEqual(
            float(response.data.get('amount', 0.00)),
            order_data.get('quantity') * order.price)

    def test_delete_order(self):
        """
        Deleting order without authenticated user, should not be allow.

        :return:
        """
        user = UserTestHelper.create_test_user(username="testowner")
        stock = StockTestHelper.create_test_stock()
        order = OrderTestHelper.create_test_order(user=user, stock=stock)

        self.assertUnauthorizedDelete(
            reverse(OrderTestHelper.API_NAME_ORDER_DETAIL, kwargs={'pk': order.pk})
        )

    def test_delete_order_with_user(self):
        """
        Deleting order with authenticated user, should not be allow.

        :return:
        """
        user = UserTestHelper.create_test_user(username="testowner")
        stock = StockTestHelper.create_test_stock()
        order = OrderTestHelper.create_test_order(user=user, stock=stock)

        self.client.force_login(UserTestHelper.create_test_user())
        self.assertUserForbidDelete(
            reverse(OrderTestHelper.API_NAME_ORDER_DETAIL, kwargs={'pk': order.pk})
        )

    def test_delete_order_with_owner(self):
        """
        Deleting order with authenticated owner, should be allow.

        :return:
        """
        user = UserTestHelper.create_test_user(username="testowner")
        stock = StockTestHelper.create_test_stock()
        order = OrderTestHelper.create_test_order(user=user, stock=stock)

        self.client.force_login(user)
        self.assertUserCanDelete(
            reverse(OrderTestHelper.API_NAME_ORDER_DETAIL, kwargs={'pk': order.pk})
        )

    def test_delete_order_with_super_user(self):
        """
        Deleting order with authenticated super user, should be allow.

        :return:
        """
        user = UserTestHelper.create_test_user(username="testowner")
        stock = StockTestHelper.create_test_stock()
        order = OrderTestHelper.create_test_order(user=user, stock=stock)

        self.client.force_login(UserTestHelper.create_test_super_user())
        self.assertUserCanDelete(
            reverse(OrderTestHelper.API_NAME_ORDER_DETAIL, kwargs={'pk': order.pk})
        )
