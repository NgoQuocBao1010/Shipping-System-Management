from django.contrib import admin

from .models import ShippingType, ShipDistance, Order, ProductOrder, Customer


admin.site.register(ShippingType)
admin.site.register(ShipDistance)
admin.site.register(Order)
admin.site.register(ProductOrder)
admin.site.register(Customer)
