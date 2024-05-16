# Stock Trading
# Created by Maximillian M. Estrada on 2024-05-16

from django.core.management.base import BaseCommand

from core.services import TransactionService


class Command(BaseCommand):
    help = "Process places orders."

    def add_arguments(self, parser):
        parser.add_argument(
            "--stock_code",
            help="Stock code to process.",
        )

    def handle(self, *args, **options):
        TransactionService.process_order_transaction(
            options.get('stock_code', None))
