from django.db.models import Q
from django.contrib.auth import get_user_model

from order.models import Order
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
    """
    end = datetime.now()
    start = end - timedelta(days=60)

    delta = end - start
    int_delta = (delta.days * 24 * 60 * 60) + delta.seconds
    random_second = random.randrange(int_delta)

    result = start + timedelta(seconds=random_second)
    result = result.replace(tzinfo=timezone.utc)
    return result


def generate():
    rebuildOrders = Order.objects.filter(user__email__icontains="nhqtrong@gmail.com")

    newOrder = random.choice(rebuildOrders)
    newOrder.pk = None

    newConsignee = newOrder.consignee
    newConsignee.pk = None
    newConsignee.fullName = nameGenerator()
    newConsignee.phone = phoneGenerator()
    newConsignee.save()

    consignor = User.objects.get(email__icontains="ntklinh@gmail.com")
    status = 3 if random.randint(0, 101) > 10 else 4
    paymentMethod = random.choice([1, 2])
    shipper = getRamdomDriver()
    dateCreated = random_date()

    newOrder.user = consignor
    newOrder.status = status
    newOrder.paymentMethod = paymentMethod
    newOrder.shipper = shipper
    newOrder.dateCreated = dateCreated
    newOrder.consignee = newConsignee

    newOrder.save()


def run():

    # print(random_date())

    # print(getRamdomDriver())

    generate()

    # cons = User.objects.exclude(
    #     Q(email__icontains="nhqtrong@gmail.com") | Q(staff=True)
    # )
    # for con in cons:
    #     con.delete()
