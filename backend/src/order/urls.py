from django.urls import path
from . import views

urlpatterns = [
    # Price List
    path("shipping-money/", views.shippingPrice, name="shippingPrice"),
    path("price-edit/<str:id>/", views.priceEdit, name="priceEdit"),
    # Order
    path("reports/", views.reports, name="reports"),
    path("list/", views.ordersList, name="ordersList"),
    path("detail/<str:id>/", views.order, name="order"),
    path("preview/<str:id>/", views.orderPreview, name="orderPreview"),
    path("create/", views.orderCreateApi, name="orderCreate"),
    path("unassign/", views.ordersUnassign, name="ordersUnassign"),
    path("assign/", views.ordersAssign, name="ordersAssign"),
    path("location/<str:id>/", views.orderUpdateLocation, name="orderUpdateLocation"),
    path("finish/<str:id>/", views.orderFinish, name="orderFinish"),
]
