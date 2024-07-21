# Stock Trading
# Created by Maximillian M. Estrada on 2024-05-15

from django.contrib import admin

from core.models import \
    Stock, \
    Transaction, \
    Portfolio


@admin.register(Stock)
class StockAdmin(admin.ModelAdmin):
    list_display = (
        'code',
        'name',
        'price')
    search_fields = [
        'name',
        'code',
    ]


@admin.register(Transaction)
class Transaction(admin.ModelAdmin):
    list_display = (
        'type',
        'status',
        'stock',
        'user',
        'is_order',
        'type',
        'remainder_quantity',
        'quantity',
        'price',
        'amount')
    search_fields = [
        'stock__code',
        'user__username'
    ]


@admin.register(Portfolio)
class Portfolio(admin.ModelAdmin):
    list_display = (
        'user',
        'stock',
        'total_share',
        'average_price')
    search_fields = [
        'stock__code',
        'user__username'
    ]
