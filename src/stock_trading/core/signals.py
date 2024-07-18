# Stock Trading
# Created by Maximillian M. Estrada on 2024-05-17

from django.db.models.signals import pre_save, post_save
from django.dispatch import receiver

from core.models import Transaction, Order
from core.services import TransactionService, PortfolioService


@receiver(pre_save, sender=Order)
@receiver(pre_save, sender=Transaction)
def pre_save_transaction(sender, instance, **kwargs):
    TransactionService.save_transaction(instance, False)


@receiver(post_save, sender=Transaction)
def post_save_transaction(sender, instance, **kwargs):
    PortfolioService.update_portfolio(
        transaction=instance,
    )
