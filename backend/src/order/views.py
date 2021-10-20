from django.contrib.auth import get_user_model, authenticate
from django.http import JsonResponse
from django.conf import settings
from django.db.models import F
from rest_framework import status
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from account.serializers import ProfileSerializer
from .models import Order, ProductOrder, ShipDistance
from .serializers import ShipDistanceSerializer, OrderSerializer


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
            print(distance)
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
@permission_classes([IsAuthenticated])
def ordersList(request):
    """
    Get the list of all orders base on the user's authorization
    If the user is the admin, return all orders
    else return only the order that belong to the user correspond customer
    """
    orders = Order.objects.all().order_by("-dateCreated")

    if not request.user.is_admin:
        orders = orders.filter(consignor=request.user)

    serializers = OrderSerializer(orders, many=True)
    return Response(status=status.HTTP_200_OK, data=serializers.data)


@api_view(["GET", "POST"])
@permission_classes([IsAuthenticated])
def order(request, id):
    """
    Get order by giving order id
    Unless you are logged in as admin, you are only allowed to view your own order
    """
    if not id.isnumeric():
        return Response(
            status=status.HTTP_400_BAD_REQUEST, data={"error": "Invalid query"}
        )

    order = None
    try:
        order = Order.objects.get(id=id)

        if order.user != request.user and not request.user.is_admin:
            return Response(
                status=status.HTTP_401_UNAUTHORIZED,
                data={"error": "You are not the admin nor owner of this order"},
            )

    except Order.DoesNotExist:
        return Response(
            status=status.HTTP_404_NOT_FOUND, data={"error": "Order does not exist"}
        )

    serializers = OrderSerializer(order, many=False)
    return Response(status=status.HTTP_200_OK, data=serializers.data)


@api_view(["POST"])
@permission_classes([IsAuthenticated])
def orderCreateApi(request):
    """
    Saving information of an orders
    Consignor, Consignee, Package, other ...
    """

    # Get order information
    products = request.data.get("products")

    try:
        newOrder = Order.objects.create(
            user=request.user,
            consignee=None,
            paymentMethod=request.data.get("paymentMethod"),
            productPreview=request.data.get("productPreview"),
            note=request.data.get("note"),
            estimateDistance=request.data.get("estimateDistance"),
            shippingPrice=request.data.get("shippingPrice"),
        )

        if not savePackageInfo(products, newOrder):
            return Response(
                status=status.HTTP_500_INTERNAL_SERVER_ERROR,
                data={"error": "Internal error"},
            )
        
        # Get and save consignor and consignee information
        consigneeProfile = makeConsigneeProfile(request.data.get("consignee"))
        if not consigneeProfile:
            newOrder.delete()
            return Response(status=status.HTTP_400_BAD_REQUEST)
        
        newOrder.consignee = consigneeProfile
        newOrder.save()

    except ValueError as e:
        print(f"Error creating new order", str(e))
        return Response(
            status=status.HTTP_400_BAD_REQUEST,
            data={"error": "Invalid field"},
        )

    except Exception as e:
        print(f"Error creating new order {e.__class__.__name__}: ", str(e))
        return Response(
            status=status.HTTP_500_INTERNAL_SERVER_ERROR,
            data={"error": "Internal error"},
        )

    return Response(
        status=status.HTTP_200_OK, data={"message": "Succesfully place order"}
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


def makeConsigneeProfile(info):
    """Creating a profile for a consignee of an order"""
    profile = None
    info.setdefault("consignee", True)

    serializer = ProfileSerializer(data=info)

    if serializer.is_valid():
        profile = serializer.save()

    else:
        print(f"[SERVER]: Error creating profile {serializer.errors}")

    return profile
