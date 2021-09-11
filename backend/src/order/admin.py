from django.contrib import admin

from .models import Consignor, Consignee, ShippingType, ShipDistance, Order, ProductOrder

admin.site.register(Consignor)
admin.site.register(Consignee)
admin.site.register(ShippingType)
admin.site.register(ShipDistance)
admin.site.register(Order)
admin.site.register(ProductOrder)
