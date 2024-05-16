# Stock Trading
# Created by Maximillian M. Estrada on 2024-05-17

from django.db.models.signals import post_save
from django.dispatch import receiver

from core.models import Transaction
from core.services import PortfolioService


@receiver(post_save, sender=Transaction)
def post_save_transaction(sender, instance, **kwargs):
    PortfolioService.update_portfolio(
        transation=instance,
    )
