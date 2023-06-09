# Models
from transactions.models_enum import (
    AccountStatusEnum,
    AccountTypeEnum,
    TransactionStatusEnum,
)
from transactions.models import (
    AccountStatus,
    AccountType,
    TransactionStatus,
    Country,
    City,
    Provider,
)


def populate_account_status():
    AccountStatus.objects.get_or_create(
        name=AccountStatusEnum.ACTIVE.value,
        defaults={"name": AccountStatusEnum.ACTIVE.value},
    )
    AccountStatus.objects.get_or_create(
        name=AccountStatusEnum.INACTIVE.value,
        defaults={"name": AccountStatusEnum.INACTIVE.value},
    )


def populate_account_type():
    AccountType.objects.get_or_create(
        name=AccountTypeEnum.SAVINGS.value,
        defaults={"name": AccountTypeEnum.SAVINGS.value},
    )
    AccountType.objects.get_or_create(
        name=AccountTypeEnum.CHECKING.value,
        defaults={"name": AccountTypeEnum.CHECKING.value},
    )


def populate_transaction_status():
    TransactionStatus.objects.get_or_create(
        name=TransactionStatusEnum.PENDING.value,
        defaults={"name": TransactionStatusEnum.PENDING.value},
    )

    TransactionStatus.objects.get_or_create(
        name=TransactionStatusEnum.APPROVED.value,
        defaults={"name": TransactionStatusEnum.APPROVED.value},
    )

    TransactionStatus.objects.get_or_create(
        name=TransactionStatusEnum.DECLINED.value,
        defaults={"name": TransactionStatusEnum.DECLINED.value},
    )

    TransactionStatus.objects.get_or_create(
        name=TransactionStatusEnum.CANCELED.value,
        defaults={"name": TransactionStatusEnum.CANCELED.value},
    )


def populate_countries_and_cities():
    col, created = Country.objects.get_or_create(
        name="Colombia", defaults={"name": "Colombia"}
    )
    usa, created = Country.objects.get_or_create(
        name="United States", defaults={"name": "United States"}
    )

    City.objects.get_or_create(
        name="Bogota", country=col, defaults={"name": "Bogota", "country": col}
    )

    City.objects.get_or_create(
        name="Medellín", country=col, defaults={"name": "Medellín", "country": col}
    )

    City.objects.get_or_create(
        name="Barranquilla",
        country=col,
        defaults={"name": "Barranquilla", "country": col},
    )

    City.objects.get_or_create(
        name="Cartagena", country=col, defaults={"name": "Cartagena", "country": col}
    )

    City.objects.get_or_create(
        name="Miami", country=usa, defaults={"name": "Miami", "country": usa}
    )

    City.objects.get_or_create(
        name="New York", country=usa, defaults={"name": "New York", "country": usa}
    )

    City.objects.get_or_create(
        name="Washington", country=usa, defaults={"name": "Washington", "country": usa}
    )


def populate_provider():
    col = Country.objects.get(name="Colombia")
    usa = Country.objects.get(name="United States")

    Provider.objects.get_or_create(
        name="PAYU",
        country=col,
        defaults={"name": "PAYU", "country": col},
    )

    Provider.objects.get_or_create(
        name="NEQUI",
        country=col,
        defaults={"name": "NEQUI", "country": col},
    )

    Provider.objects.get_or_create(
        name="EPAYCO",
        country=col,
        defaults={"name": "EPAYCO", "country": col},
    )

    Provider.objects.get_or_create(
        name="STRIPE",
        country=usa,
        defaults={"name": "STRIPE", "country": usa},
    )

    Provider.objects.get_or_create(
        name="LEMUR",
        country=usa,
        defaults={"name": "LEMUR", "country": usa},
    )
