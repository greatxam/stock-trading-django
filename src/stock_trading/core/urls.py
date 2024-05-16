# Stock Trading
# Created by Maximillian M. Estrada on 2024-05-15

from django.urls import path

from rest_framework.urlpatterns import format_suffix_patterns

from core.views.v1 import (
    stock,
    order,
    trade,
)

urlpatterns = [
    # stocks
    path(
        'stocks/',
        stock.StockListView.as_view(),
        name='core-api-stock-list'),
    path(
        'stocks/<uuid:pk>/',
        stock.StockDetailView.as_view(),
        name='core-api-stock-detail'),
    # orders
    path(
        'orders/',
        order.OrderListView.as_view(),
        name='core-api-order-list'),
    path(
        'orders/<uuid:pk>/',
        order.OrderDetailView.as_view(),
        name='core-api-order-detail'),
    # trades
    path(
        'trades/',
        trade.TradeListView.as_view(),
        name='core-api-trade-list'),
    path(
        'trades/<uuid:pk>/',
        trade.TradeDetailView.as_view(),
        name='core-api-trade-detail'),
]

urlpatterns = format_suffix_patterns(urlpatterns)
