from django.db import models
from django.db.models import CheckConstraint, Q, F, constraints
from django.contrib.auth import get_user_model

User = get_user_model()


class Customer(models.Model):
    CUSTOMER_ROLES = (
        ("cnor", "Consignor"),
        ("cnee", "Consignee"),
    )
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    role = models.CharField(choices=CUSTOMER_ROLES, max_length=25)
    name = models.CharField(max_length=100, blank=True, null=True)
    phone = models.CharField(max_length=20, blank=True, null=True)
    address = models.CharField(max_length=255, blank=True, null=True)
    provinceId = models.IntegerField(null=True, blank=True)
    districtId = models.IntegerField(null=True, blank=True)
    subDistrictId = models.IntegerField(null=True, blank=True)

    def __str__(self):
        return f"{self.get_role_display()}: {self.name}"


class ShipDistance(models.Model):
    MAX_VALUE = 1000

    lowerLimit = models.IntegerField(null=True, blank=True)
    upperLimit = models.IntegerField(null=True, blank=True, default=MAX_VALUE)
    price = models.IntegerField(null=True, blank=True)

    class Meta:
        constraints = [
            CheckConstraint(
                check=Q(upperLimit__gt=F("lowerLimit")), name="check_valid_limit"
            )
        ]

    def __str__(self):
        return f"Distance: {self.lowerLimit} km - {self.upperLimit} km"


class Order(models.Model):
    STATUS = (
        (0, "Failed"),
        (1, "Processing"),
        (2, "Delivering"),
        (3, "Delivered"),
    )
    PAYMENT_METHODS = (
        (0, "Pay by consignor"),
        (1, "Pay by consignee"),
    )
    PRODUCT_PREVIEW = (
        (0, "Customer not allow to observe products"),
        (1, "Customer allow to observe products but not to try them"),
        (2, "Customer allow to try products"),
    )
    SHIPPING_TYPE = (
        (0, "Standard"),
        (1, "Advanced"),
    )

    consignor = models.ForeignKey(
        Customer, null=True, on_delete=models.SET_NULL, related_name="consignor"
    )
    consignee = models.ForeignKey(
        Customer, null=True, on_delete=models.SET_NULL, related_name="consignee"
    )
    status = models.IntegerField(default=1, choices=STATUS)
    paymentMethod = models.IntegerField(null=True, choices=PAYMENT_METHODS)
    productPreview = models.IntegerField(null=True, choices=PRODUCT_PREVIEW)
    shippingType = models.IntegerField(null=True, choices=SHIPPING_TYPE)
    shipDistance = models.ForeignKey(ShipDistance, on_delete=models.CASCADE, null=True)
    note = models.TextField(null=True, blank=True)
    dateCreated = models.DateTimeField(auto_now_add=True)

    def __get_price(self):
        if not self.shipDistance:
            return "Unknow"

        price = (
            self.shipDistance.price
            if self.shippingType == 0
            else self.shipDistance.price * 115 / 100
        )
        return int(price * 1000)

    price = property(__get_price)

    def __str__(self):
        return f"Order {self.id} ({self.status}), price {self.price} VND"


class ProductOrder(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE)
    name = models.CharField(max_length=255, blank=True, null=True)
    price = models.IntegerField(null=True, default=0)
    note = models.TextField(null=True, blank=True)

    def __str__(self):
        return f"Product {self.name}"
