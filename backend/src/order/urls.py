from django.urls import path
from . import views

urlpatterns = [
    path("shipping-money/", views.shippingPrice, name="shippingPrice"),
    path("list/", views.ordersList, name="ordersList"),
    path("create/", views.orderCreateApi, name="orderCreate"),
]
