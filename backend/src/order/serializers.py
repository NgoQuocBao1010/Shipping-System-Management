from django.db.models import Count
from rest_framework import serializers
from .models import ShipDistance, Order, ProductOrder, Customer


class CustomerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Customer
        fields = "__all__"
