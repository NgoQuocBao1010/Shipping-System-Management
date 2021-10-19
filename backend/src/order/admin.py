from django.contrib import admin

from .models import ShipDistance, Order, ProductOrder


admin.site.register(ShipDistance)
admin.site.register(Order)
admin.site.register(ProductOrder)
