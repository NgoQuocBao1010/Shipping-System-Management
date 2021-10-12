from django.urls import path
from . import views

urlpatterns = [
    path("calc-money/", views.getShipMoney, name="calcMoney"),
    path("create/", views.orderCreateApi, name="orderCreate"),
]