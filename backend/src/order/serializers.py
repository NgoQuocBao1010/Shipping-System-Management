from django.db.models import Count
from rest_framework import serializers
from .models import ShipDistance, Customer, Order, ProductOrder


class CustomerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Customer
        fields = "__all__"


class ShipDistanceSerializer(serializers.ModelSerializer):
    class Meta:
        model = ShipDistance
        fields = "__all__"


class ProductOrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductOrder
        exclude = ("order",)


class OrderSerializer(serializers.ModelSerializer):
    products = ProductOrderSerializer(read_only=True, many=True)
    dateCreated = serializers.DateTimeField(format="%d-%m-%Y %H:%M:%S")

    class Meta:
        model = Order
        fields = "__all__"
