from django.db.models import Count
from rest_framework import serializers
from .models import ShipDistance, Customer


class CustomerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Customer
        fields = "__all__"


class ShipDistanceSerializer(serializers.ModelSerializer):
    class Meta:
        model = ShipDistance
        fields = "__all__"
