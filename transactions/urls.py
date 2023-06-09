from django.urls import path

from transactions.views import transactions

app_name = "users"
urlpatterns = [
    path("", view=transactions, name="home"),
]
