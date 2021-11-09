from order.models import Order
from account.models import Profile
from scripts.generateEmploy import nameGenerator

from vietnam_provinces import NESTED_DIVISIONS_JSON_PATH
from vietnam_provinces.enums import (
    ProvinceEnum,
    ProvinceDEnum,
    DistrictEnum,
    DistrictDEnum,
)

import random, rapidjson
import orjson
from datetime import datetime, timedelta


def random_date(start, end):
    """
    This function will return a random datetime between two datetime
    objects.
    """
    delta = end - start
    int_delta = (delta.days * 24 * 60 * 60) + delta.seconds
    random_second = random.randrange(int_delta)
    return start + timedelta(seconds=random_second)


def randomPlace():
    print(DistrictEnum.D_764)


def run():
    d1 = datetime.strptime("1/1/2021 1:30 PM", "%m/%d/%Y %I:%M %p")
    d2 = datetime.now()

    print(random_date(d1, d2))

    # everyThing = orjson.loads(NESTED_DIVISIONS_JSON_PATH.read_bytes())

    randomPlace()
