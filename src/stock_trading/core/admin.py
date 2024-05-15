# Stock Trading
# Created by Maximillian M. Estrada on 2024-05-15

from django.contrib import admin

from core.models import \
    Stock, \
    Transaction


@admin.register(Stock)
class StockAdmin(admin.ModelAdmin):
    list_display = (
        'code',
        'name',
        'price')


@admin.register(Transaction)
class Transaction(admin.ModelAdmin):
    list_display = (
        'stock',
        'user',
        'type',
        'quantity',
        'price',
        'amount')
