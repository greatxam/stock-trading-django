# Stock Trading
# Created by Maximillian M. Estrada on 2024-05-17

from django.core.management import call_command
from core.management.commands import (
    process_order_transaction,
    process_bulk_order_file
)


def schedule_process_order_transaction():
    call_command(process_order_transaction.Command())


def schedule_process_bulk_order_file():
    call_command(process_bulk_order_file.Command())
