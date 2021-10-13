from django.contrib.auth import get_user_model, authenticate
from django.http import JsonResponse
from django.conf import settings
from django.db.models import F
from rest_framework import status
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
import json, requests, pprint

from .models import Order, ShipDistance
from .serializers import CustomerSerializer, ShipDistanceSerializer


@api_view(["GET"])
def getShipMoney(request):
    """
    Calculate distance between the shop's location and the destination of the order
    Params: query url with long and lat
    """
    latitude = request.GET.get("lat")
    longitude = request.GET.get("long")

    if not latitude or not longitude:
        return JsonResponse(
            status=status.HTTP_400_BAD_REQUEST,
            data={"error": "Invalid query parameters"},
        )

    destination = [float(longitude), float(latitude)]

    routingResult = routing(destination)

    if not routingResult:
        return JsonResponse(
            status=status.HTTP_409_CONFLICT, data={"error": "Could not calculate route"}
        )

    return JsonResponse(status=status.HTTP_200_OK, data=routingResult)


@api_view(["GET"])
def shippingPrice(request):
    """
    Accept a numeric string as a query parameters preresent a distance
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
    order = request.data.get("info")

    try:
        newOrder = Order.objects.create(
            consignor=consignor,
            consignee=consignee,
            paymentMethod=order.get("paymentMethod"),
            productPreview=order.get("productPreview"),
            shippingType=order.get("shippingType"),
            note=order.get("note"),
        )
    except Exception as e:
        print(str(e))
        return Response(status=status.HTTP_400_BAD_REQUEST)

    return Response(
        status=status.HTTP_200_OK,
    )


# Utils Functions
def routing(destination, origin=settings.CURRENT_LOCATION, summary=True):
    """
    Using OpenRoute Service API to calculate the distance between 2 places
    Params:
    - Coordinate (latitude, longtitude) of desination places
    - Coordinate (latitude, longtitude) of origin places, default to the device current location
    """
    body = {"coordinates": [origin, destination]}

    headers = {
        "Accept": "application/json, application/geo+json, application/gpx+xml, img/png; charset=utf-8",
        "Authorization": settings.OPEN_ROUTE_SERVICE_API_KEY,
        "Content-Type": "application/json; charset=utf-8",
    }

    response = requests.post(
        "https://api.openrouteservice.org/v2/directions/driving-car/geojson",
        json=body,
        headers=headers,
    )

    if response.reason == "OK" and response.status_code == 200:
        data = json.loads(response.text)
        routingInfo = data.get("features")[0].get("properties")

        return routingInfo.get("summary") if summary else routingInfo

    return None
