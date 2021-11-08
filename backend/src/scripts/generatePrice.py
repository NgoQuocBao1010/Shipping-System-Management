from order.models import ShipDistance


def run():
    prebuildPrice = [
        [0, 20, 22000],
        [20, 100, 50000],
        [100, 1000, 57000],
        [1000, 2000, 69000],
    ]

    for lower, upper, price in prebuildPrice:
        ShipDistance.objects.create(lowerLimit=lower, upperLimit=upper, price=price)
