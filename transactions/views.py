from django.shortcuts import render

from transactions.models import Transaction, Account


def transactions(request):
    transaction_list = Transaction.objects.all().select_related(
        "origin_account",
        "origin_account__client",
        "origin_account__city",
        "origin_account__city__country",
        "destination_account",
        "destination_account__client",
        "status",
    )[:100]

    context = {"transactions": transaction_list}

    return render(request, "pages/transactions.html", context)
