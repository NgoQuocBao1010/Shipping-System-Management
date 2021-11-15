from order.models import Order



def updateLocationOrder():
    orders = Order.objects.all()

    for order in orders:
        order.location = '{"lat":10.0171277,"lon":105.7842959}'
        order.save()


def run():
    updateLocationOrder()