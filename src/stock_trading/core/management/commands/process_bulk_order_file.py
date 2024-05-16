# Stock Trading
# Created by Maximillian M. Estrada on 2024-05-17

from django.core.management.base import BaseCommand
from django.core.files.storage import default_storage
from django.contrib.auth import get_user_model

from core.services import TransactionService

User = get_user_model()


def process_folder_files(dir):
    dirs, files = default_storage.listdir(dir)
    for d in dirs:
        process_folder_files(d)

    for f in files:
        if 'CSV' not in f.upper():
            continue
        file_path = f"{dir}/{f}"
        print(f"{file_path}")
        file = default_storage.open(file_path)

        user = User.objects.get(pk=dir)
        TransactionService.bulk_orders(
            user=user,
            filename=f,
            file=file
        )
        default_storage.delete(file_path)


class Command(BaseCommand):
    help = "Process bulk order file."

    def handle(self, *args, **options):
        process_folder_files('.')
