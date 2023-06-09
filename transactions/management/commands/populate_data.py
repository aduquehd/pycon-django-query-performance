import random

from django.core.management.base import BaseCommand

from django_seed import Seed

# Models
from transactions.models import (
    Client,
    Account,
    AccountStatus,
    City,
    Provider,
    AccountType,
    Transaction,
    TransactionStatus,
)

# Utils
from transactions.management.commands.utils import (
    populate_transaction_status,
    populate_account_status,
    populate_account_type,
    populate_countries_and_cities,
    populate_provider,
)


class Command(BaseCommand):
    def handle(self, *args, **options):
        seeder = Seed.seeder()

        populate_account_status()
        populate_account_type()
        populate_transaction_status()
        populate_countries_and_cities()
        populate_provider()

        account_status_ids = AccountStatus.objects.all()
        city_list = City.objects.all()
        provider_list = Provider.objects.all()
        account_type_list = AccountType.objects.all()
        transaction_status_list = TransactionStatus.objects.all()

        seeder.add_entity(
            Client,
            100,
            {
                "name": lambda x: seeder.faker.name(),
                "email": lambda x: seeder.faker.email(),
                "birth_date": lambda x: seeder.faker.date(),
            },
        )
        client_ids = seeder.execute()

        client_list = Client.objects.filter(id__in=client_ids[Client])

        seeder.add_entity(
            Account,
            2000,
            {
                "name": lambda x: seeder.faker.company(),
                "created_at": lambda x: seeder.faker.date(),
                "client": lambda x: seeder.faker.random_element(client_list),
                "status": lambda x: seeder.faker.random_element(account_status_ids),
                "city": lambda x: seeder.faker.random_element(city_list),
                "provider": lambda x: seeder.faker.random_element(provider_list),
                "type": lambda x: seeder.faker.random_element(account_type_list),
            },
        )

        account_ids = seeder.execute()
        account_list = Account.objects.filter(id__in=account_ids[Account])

        seeder.add_entity(
            Transaction,
            100000,
            {
                "amount": lambda x: random.randint(10, 70000),
                "created_at": lambda x: seeder.faker.date(),
                "origin_account": lambda x: seeder.faker.random_element(account_list),
                "destination_account": lambda x: seeder.faker.random_element(
                    account_list
                ),
                "status": lambda x: seeder.faker.random_element(
                    transaction_status_list
                ),
            },
        )
        transaction_ids = seeder.execute()
