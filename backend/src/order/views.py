from django.contrib.auth import get_user_model, authenticate
from django.http import JsonResponse
from django.conf import settings
from django.db.models import F
from rest_framework import status
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
import json, requests, pprint

from .models import Order, ProductOrder, ShipDistance
from .serializers import CustomerSerializer, ShipDistanceSerializer, OrderSerializer


@api_view(["GET"])
def shippingPrice(request):
    """
    Accept a numeric string as a query parameters preresent a distance (kilometer)
    Response will return a price according to that distance
    If there is no parameters, the whole price tag will be return
    ?distance=100000
    """
    allPrices = ShipDistance.objects.all()
    distance = request.GET.get("distance")

    if distance:
        try:
            distance = float(distance)
        except Exception as e:
            return Response(
                status=status.HTTP_400_BAD_REQUEST,
                data={
                    "error": "Invalid Input. Distance query parameters should be an number"
                },
            )

        allPrices = allPrices.filter(lowerLimit__lte=distance, upperLimit__gt=distance)

    serializers = ShipDistanceSerializer(allPrices, many=True)
    return Response(status=status.HTTP_200_OK, data={"data": serializers.data})


@api_view(["GET"])
def ordersList(request):
    orders = Order.objects.all()

    serializers = OrderSerializer(orders, many=True)
    return Response(status=status.HTTP_200_OK, data=serializers.data)


@api_view(["POST"])
@permission_classes([IsAuthenticated])
def orderCreateApi(request):
    """
    Saving information of an orders
    Consignor, Consignee, Package, other ...
    """
    # Get and save consignor and consignee information
    consignorInfo = request.data.get("consignor")
    consignorInfo.update(
        {
            "user": request.user.id,
            "role": "cnor",
        }
    )
    consignor = CustomerSerializer(data=consignorInfo)

    consigneeInfo = request.data.get("consignee")
    consigneeInfo.update(
        {
            "role": "cnee",
        }
    )
    consignee = CustomerSerializer(data=consigneeInfo)

    if consignor.is_valid() and consignee.is_valid():
        consignor = consignor.save()
        consignee = consignee.save()
    else:
        print(consignor.errors)
        print(consignee.errors)
        return Response(status=status.HTTP_400_BAD_REQUEST)

    # Get order information
    products = request.data.get("products")

    try:
        newOrder = Order.objects.create(
            consignor=consignor,
            consignee=consignee,
            paymentMethod=request.data.get("paymentMethod"),
            productPreview=request.data.get("productPreview"),
            note=request.data.get("note"),
            estimateDistance=request.data.get("estimateDistance"),
            shippingPrice=request.data.get("shippingPrice"),
        )

        if not savePackageInfo(products, newOrder):
            return Response(status=status.HTTP_500_INTERNAL_SERVER_ERROR)

    except Exception as e:
        print("Error creating new order", str(e))
        return Response(status=status.HTTP_400_BAD_REQUEST)

    return Response(
        status=status.HTTP_200_OK,
    )


# Utils Functions
def savePackageInfo(products, order):
    """
    Save all products in the new order
    """

    try:
        for product in products:
            ProductOrder.objects.create(
                order=order,
                name=product.get("name"),
                price=int(product.get("price")),
            )
    except Exception as e:
        print("Error saving products", e)
        return False

    return True
