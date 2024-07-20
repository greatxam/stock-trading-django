# Stock Trading
# Created by Maximillian M. Estrada on 2024-05-15

import uuid

from django.conf import settings
from django.db import models
from decimal import Decimal


class BaseAbstract(models.Model):
    class Meta:
        abstract = True

    # Fields
    id = models.UUIDField(
        primary_key=True,
        default=uuid.uuid4,
        editable=False)
    created = models.DateTimeField(
        auto_now_add=True)
    modified = models.DateTimeField(
        auto_now=True)


class Stock(BaseAbstract):
    class Meta:
        db_table = 'core_stocks'
        ordering = ['name']

    # Fields
    code = models.CharField(
        unique=True,
        max_length=4)
    name = models.CharField(
        unique=True,
        max_length=100)
    price = models.DecimalField(
        max_digits=12,
        decimal_places=2,
        default=Decimal(0.00))

    def __str__(self):
        return self.code


class Transaction(BaseAbstract):
    # Transaction Type
    class Type:
        BUY = 0
        SELL = 1

        CHOICES = (
            (BUY, "Buy"),
            (SELL, "Sell"))

    # Transaction Status
    class Status:
        PENDING = 0
        CLEARED = 1

        CHOICES = (
            (PENDING, "Pending"),
            (CLEARED, "Cleared"))

    class Meta:
        db_table = 'core_transactions'
        ordering = ['-created']

    # Fields
    is_order = models.BooleanField(default=True)
    type = models.PositiveSmallIntegerField(
        default=Type.BUY,
        choices=Type.CHOICES)
    status = models.PositiveSmallIntegerField(
        default=Status.PENDING,
        choices=Status.CHOICES)
    stock = models.ForeignKey(
        'Stock',
        on_delete=models.DO_NOTHING)
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.DO_NOTHING)
    quantity = models.PositiveIntegerField(
        default=0)
    price = models.DecimalField(
        max_digits=12,
        decimal_places=2,
        default=Decimal(0.00))
    amount = models.DecimalField(
        max_digits=12,
        decimal_places=2,
        default=Decimal(0.00))

    trades = models.ManyToManyField(
        'self',
        blank=True)

    def __str__(self):
        return "({}) {} {}: {} | {} | {}".format(
            self.get_status_display(),
            self.get_type_display(),
            self.stock.code,
            self.quantity,
            self.price,
            self.amount)

    def cleared_quantity(self):
        return self.trades.all().aggregate(
            models.Sum('quantity', default=0)
        ).get('quantity__sum')

    def remainder_quantity(self):
        return self.quantity - self.cleared_quantity()


class OrderManager(models.Manager):
    def get_queryset(self):
        return super().get_queryset().filter(
            is_order=True,
            status=Transaction.Status.PENDING)


class Order(Transaction):
    class Meta:
        proxy = True

    objects = OrderManager()

    def save(self, *args, **kwargs):
        self.status = Transaction.Status.PENDING
        super().save(*args, **kwargs)


class TradeManager(models.Manager):
    def get_queryset(self):
        return super().get_queryset().filter(
            is_order=False,
            status=Transaction.Status.CLEARED)


class Trade(Transaction):
    class Meta:
        proxy = True

    objects = TradeManager()

    def save(self, *args, **kwargs):
        self.status = Transaction.Status.CLEARED
        super().save(*args, **kwargs)


class Portfolio(BaseAbstract):
    class Meta:
        db_table = 'core_portfolios'
        unique_together = (('user', 'stock'),)
        ordering = ['stock__code']

    # fields
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.DO_NOTHING)
    stock = models.ForeignKey(
        'Stock',
        on_delete=models.DO_NOTHING)
    total_share = models.PositiveIntegerField(
        default=0)
    total_value = models.DecimalField(
        max_digits=12,
        decimal_places=2,
        default=Decimal(0.00))
    average_price = models.DecimalField(
        max_digits=12,
        decimal_places=2,
        default=Decimal(0.00))

    def __str__(self):
        return f"{self.user} {self.stock}: {self.total_share} | {self.total_value}"

    def get_market_price(self):
        return self.stock.price

    def get_market_value(self):
        return self.total_share * self.stock.price
