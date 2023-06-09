from django.shortcuts import render
from django.db.models import Prefetch

from transactions.models import Transaction, Account


def transactions(request):
    transaction_list = Transaction.objects.all()[:100]

    context = {"transactions": transaction_list}

    return render(request, "pages/transactions.html", context)


def accounts(request):
    origin_prefetch = Prefetch(
        "origin_transactions",
        queryset=Transaction.objects.filter(status__name="APPROVED")
        .select_related("status")
        .order_by("-amount"),
    )

    destination_prefetch = Prefetch(
        "destination_transactions",
        queryset=Transaction.objects.filter(status__name="APPROVED")
        .select_related("status")
        .order_by("-amount"),
    )

    accounts_list = (
        Account.objects.all()
        .select_related("client", "status", "provider", "type")
        .prefetch_related(origin_prefetch, destination_prefetch)[:100]
    )

    for account in accounts_list:
        account.last_3_origin_transactions = account.origin_transactions.all()[:3]
        account.last_3_destination_transactions = account.origin_transactions.all()[:3]

    context = {"accounts": accounts_list}

    return render(request, "pages/accounts.html", context)
