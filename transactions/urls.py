from django.urls import path

from transactions.views import transactions, accounts

app_name = "users"
urlpatterns = [
    path("", view=transactions, name="home"),
    path("accounts/", view=accounts, name="accounts"),
]
