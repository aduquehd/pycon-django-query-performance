from django.db import models
from django.utils import timezone

# Enums
from transactions.models_enum import AccountStatusEnum, AccountTypeEnum


class AccountStatus(models.Model):
    name = models.CharField(
        choices=[(tag, tag.value) for tag in AccountStatusEnum], unique=True
    )

    def __str__(self):
        return self.name


class TransactionStatus(models.Model):
    name = models.CharField(
        choices=[(tag, tag.value) for tag in AccountTypeEnum], unique=True
    )

    def __str__(self):
        return self.name


class AccountType(models.Model):
    name = models.CharField(
        choices=[(tag, tag.value) for tag in AccountTypeEnum], unique=True
    )

    def __str__(self):
        return self.name


class Country(models.Model):
    name = models.CharField(max_length=255, unique=True)

    def __str__(self):
        return self.name


class City(models.Model):
    name = models.CharField(max_length=255)
    country = models.ForeignKey(Country, on_delete=models.CASCADE)

    def __str__(self):
        return self.name

    class Meta:
        unique_together = (("name", "country"),)


class Client(models.Model):
    name = models.CharField(max_length=255)
    email = models.EmailField()
    birth_date = models.DateField()


class Provider(models.Model):
    name = models.CharField(max_length=255)
    country = models.ForeignKey(Country, on_delete=models.CASCADE)


class Account(models.Model):
    name = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)

    # Foreign Keys
    client = models.ForeignKey(Client, on_delete=models.CASCADE)
    status = models.ForeignKey(AccountStatus, on_delete=models.CASCADE)
    city = models.ForeignKey(City, on_delete=models.CASCADE)
    provider = models.ForeignKey(Provider, on_delete=models.CASCADE)
    type = models.ForeignKey(AccountType, on_delete=models.CASCADE)

    def __str__(self):
        return self.name


class Transaction(models.Model):
    amount = models.FloatField()
    created_at = models.DateTimeField(auto_now_add=True)

    # Foreign Keys
    origin_account = models.ForeignKey(
        Account, on_delete=models.CASCADE, related_name="origin_transactions"
    )
    destination_account = models.ForeignKey(
        Account, on_delete=models.CASCADE, related_name="destination_transactions"
    )
    status = models.ForeignKey(TransactionStatus, on_delete=models.CASCADE)
