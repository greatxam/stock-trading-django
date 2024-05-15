# Stock Trading
# Created by Maximillian M. Estrada on 2024-05-15

from django.urls import path

from rest_framework.urlpatterns import format_suffix_patterns

from core.views.v1 import (
    stock
)

urlpatterns = [
    path(
        'stocks/',
        stock.StockListView.as_view(),
        name='core-api-stock-list'),
    path(
        'stocks/<uuid:pk>/',
        stock.StockDetailView.as_view(),
        name='core-api-stock-detail'),
]

urlpatterns = format_suffix_patterns(urlpatterns)
