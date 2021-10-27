from django.urls import path
from . import views

urlpatterns = [
    path("shipping-money/", views.shippingPrice, name="shippingPrice"),
    path("list/", views.ordersList, name="ordersList"),
    path("detail/<str:id>/", views.order, name="order"),
    path("create/", views.orderCreateApi, name="orderCreate"),
    path("assign/", views.ordersAssign, name="ordersAssign"),
]
