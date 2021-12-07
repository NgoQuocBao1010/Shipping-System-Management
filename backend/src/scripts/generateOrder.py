from django.db.models import Q
from django.contrib.auth import get_user_model

from order.models import Order, ProductOrder
from account.models import Profile
from scripts.generateEmploy import phoneGenerator

import random
from datetime import datetime, timedelta, timezone

User = get_user_model()


def nameGenerator():
    """Generate a Vietnamese name"""
    GIRLS = {
        "FIRST_NAMES": ["Ngô Thị", "Nguyễn Thị", "Trần Thị", "Lê Thị"],
        "LAST_NAMES": ["Lan", "Vy", "Huệ", "Đan"],
        "MIDDLE_NAMES": ["Phương", "Xuân", "Khánh", "Phương", "Tiểu"],
    }

    BOYS = {
        "FIRST_NAMES": ["Ngô", "Nguyễn", "Trần", "Huỳnh"],
        "LAST_NAMES": ["Huy", "Lâm", "Long", "Nguyên", "Trịnh"],
        "MIDDLE_NAMES": ["Quốc", "Văn", "Anh", "Minh", "Hoàng"],
    }

    gender = random.choice([GIRLS, BOYS])

    firstName = random.choice(gender.get("FIRST_NAMES"))
    midName = random.choice(gender.get("MIDDLE_NAMES"))
    lastName = random.choice(gender.get("LAST_NAMES"))

    return " ".join([firstName, midName, lastName])


def getRamdomDriver():
    drivers = User.objects.filter(staff=True, admin=False)

    return random.choice(drivers)


def random_date():
    """
    This function will return a random datetime between two datetime
    objects.
    2 weeks from now
    """
    end = datetime.now()
    start = end - timedelta(days=14)

    delta = end - start
    int_delta = (delta.days * 24 * 60 * 60) + delta.seconds
    random_second = random.randrange(int_delta)

    result = start + timedelta(seconds=random_second)
    result = result.replace(tzinfo=timezone.utc)
    return result


def productGenerate(order):

    DUMP_PRODUCTS = [
        {"name": "Chair", "price": 100_000},
        {"name": "Table", "price": 250_000},
        {"name": "Clothes", "price": 400_000},
        {"name": "Books", "price": 2_500_000},
        {"name": "Dell Laptop", "price": 12_990_000},
    ]

    product = random.choice(DUMP_PRODUCTS)

    ProductOrder.objects.create(
        order=order,
        name=product.get("name"),
        price=product.get("price"),
    )


def generate(email="ntklinh@gmail.com"):
    rebuildOrders = Order.objects.filter(user__email__icontains="nhqtrong@gmail.com")

    # New order
    newOrder = random.choice(rebuildOrders)
    newOrder.pk = None

    # New consignee
    newConsignee = newOrder.consignee
    newConsignee.pk = None
    newConsignee.fullName = nameGenerator()
    newConsignee.phone = phoneGenerator()
    newConsignee.save()

    # Order's information
    consignor = User.objects.get(email__icontains=email)
    status = 3 if random.randint(0, 201) > 10 else 4
    note = (
        ""
        if status == 3
        else random.choice(
            ["Cannot contact the customer", "Customer is unhappy with the order"]
        )
    )
    paymentMethod = random.choice([1, 2])
    shipper = getRamdomDriver()
    dateCreated = random_date()

    newOrder.user = consignor
    newOrder.status = status
    newOrder.paymentMethod = paymentMethod
    newOrder.shipper = shipper
    newOrder.consignee = newConsignee
    newOrder.note = note
    newOrder.save()

    newOrder.dateCreated = dateCreated
    newOrder.save()

    productGenerate(newOrder)


def massGenerate():
    consignors = User.objects.exclude(
        Q(email__icontains="nhqtrong@gmail.com") | Q(staff=True)
    )

    for consignor in consignors:
        generate(consignor.email)
        generate(consignor.email)
        generate(consignor.email)


def deleteGeneratedOrders():
    orders = Order.objects.exclude(user__email__icontains="nhqtrong@gmail.com")

    for order in orders:
        order.delete()


def run():

    # print(random_date())

    # print(getRamdomDriver())

    massGenerate()
    # deleteGeneratedOrders()

    # cons = User.objects.exclude(
    #     Q(email__icontains="nhqtrong@gmail.com") | Q(staff=True)
    # )
    # for con in cons:
    #     con.delete()
