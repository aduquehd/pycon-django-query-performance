from django.contrib import admin

# from transactions.models import Owner, Pet, PetOwner, Revision, RevisionNotes, PetType
from transactions.models import (
    AccountStatus,
    AccountType,
    TransactionStatus,
    Transaction,
)


@admin.register(AccountStatus)
class AccountStatusAdmin(admin.ModelAdmin):
    fields = ["name"]


@admin.register(AccountType)
class AccountTypeAdmin(admin.ModelAdmin):
    fields = ["name"]


@admin.register(TransactionStatus)
class TransactionStatusAdmin(admin.ModelAdmin):
    fields = ["name"]


@admin.register(Transaction)
class TransactionAdmin(admin.ModelAdmin):
    fields = [
        "amount",
        "origin_account",
        "destination_account",
        "status",
    ]
    list_display = [
        "amount",
        "origin_account",
        "destination_account",
        "status",
    ]


#
# @admin.register(PetType)
# class PetTypeAdmin(admin.ModelAdmin):
#     fields = ["name"]
#
#
# @admin.register(Pet)
# class PetAdmin(admin.ModelAdmin):
#     fields = ["name", "birth_date", "type"]
#
#
# @admin.register(PetOwner)
# class PetOwnerAdmin(admin.ModelAdmin):
#     fields = ["owner", "pet"]
#
#
# @admin.register(Revision)
# class RevisionAdmin(admin.ModelAdmin):
#     fields = ["client", "pet", "time"]
#
#
# @admin.register(RevisionNotes)
# class RevisionNotesAdmin(admin.ModelAdmin):
#     fields = ["revision", "notes"]
