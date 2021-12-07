from django.contrib.auth import get_user_model
from rest_framework import status
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from datetime import datetime, timezone, timedelta
from calendar import day_name

from account.serializers import ProfileSerializer
from account.permissions import AdminOnly, StaffOnly
from account.models import Profile
from .models import Order, ProductOrder, ShipDistance
from .serializers import ShipDistanceSerializer, OrderSerializer, OrderPreviewSerializer

User = get_user_model()


@api_view(["GET", "POST"])
def shippingPrice(request):
    """
    Accept a numeric string as a query parameters preresent a distance (kilometer)
    Response will return a price according to that distance
    If there is no parameters, the whole price tag will be return
    ?distance=100000
    """
    if request.method == "POST":
        if not request.user.is_admin:
            return Response(status=status.HTTP_401_UNAUTHORIZED)

        priceId = request.data.get("id")

        if priceId:
            priceObj = ShipDistance.objects.get(id=priceId)
            serializer = ShipDistanceSerializer(priceObj, data=request.data)
        else:
            serializer = ShipDistanceSerializer(data=request.data)

        if serializer.is_valid():
            serializer.save()
        else:
            print(f"[SERVER]: Error  {serializer.errors}")
            return Response(status=status.HTTP_400_BAD_REQUEST, data=serializer.errors)

        return Response(status=status.HTTP_200_OK)

    allPrices = ShipDistance.objects.all().order_by("lowerLimit")
    distance = request.GET.get("distance")

    if distance:
        try:
            distance = float(distance)
            allPrices = allPrices.filter(
                lowerLimit__lte=distance, upperLimit__gt=distance
            )
        except Exception as e:
            pass

    serializers = ShipDistanceSerializer(allPrices, many=True)
    return Response(status=status.HTTP_200_OK, data=serializers.data)


@api_view(["DELETE", "PUT"])
@permission_classes([IsAuthenticated, AdminOnly])
def priceEdit(request, id):
    try:
        price = ShipDistance.objects.get(id=id)
    except ShipDistance.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == "PUT":
        serializer = ShipDistanceSerializer(price, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    if request.method == "DELETE":
        price.delete()

    return Response(status=status.HTTP_200_OK)


@api_view(["GET"])
@permission_classes([IsAuthenticated])
def ordersList(request):
    """
    Get the list of all orders base on the user's authorization
    If the user is the admin, return all orders or filters the orders accordingly
    else return only the order that belong to the user correspond customer
    """

    orders = Order.objects.all().order_by("-dateCreated")

    if not request.user.is_staff:  # if not staff member
        orders = orders.filter(user=request.user)
    else:  # if the user is staff member
        # Filter orders on profile
        profileId = request.GET.get("profileId")
        if profileId and profileId.isnumeric():
            orders = orders.filter(user__profile__id=profileId)

        # Filter orders on shipper
        shipper = request.GET.get("shipper")
        if shipper and shipper.isnumeric():
            orders = orders.filter(shipper__profile__id=shipper)

    # Filter orders on status
    orders = filterOrders(request, orders)

    serializers = OrderSerializer(orders, many=True)
    return Response(status=status.HTTP_200_OK, data=serializers.data)


@api_view(["GET", "DELETE", "POST"])
@permission_classes([IsAuthenticated])
def order(request, id):
    """
    Get order by giving order id
    Unless you are logged in as admin, you are only allowed to view your own order
    """

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

    if request.method == "DELETE":
        order.delete()
        return Response(status=status.HTTP_200_OK)

    if request.method == "POST":
        editOrder(order, request.data)
        return Response(status=status.HTTP_200_OK)

    serializers = OrderSerializer(order, many=False)
    return Response(status=status.HTTP_200_OK, data=serializers.data)


@api_view(["GET"])
def orderPreview(request, id):
    """Return the brief preview of an order for non-account user"""

    try:
        order = Order.objects.get(id=id)
    except Order.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    serializer = OrderPreviewSerializer(order, many=False)
    return Response(status=status.HTTP_200_OK, data=serializer.data)


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
        # Creating new order
        newOrder = Order.objects.create(
            user=request.user,
            consignee=None,
            paymentMethod=request.data.get("paymentMethod"),
            productPreview=request.data.get("productPreview"),
            note=request.data.get("note"),
            estimateDistance=request.data.get("estimateDistance"),
            deliverTime=request.data.get("deliverTime"),
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


@api_view(["POST"])
@permission_classes([IsAuthenticated, AdminOnly])
def ordersAssign(request):
    """Assign proccessing orders to driver"""
    driverId = request.data.get("driverId")
    orders = request.data.get("orders")

    driver = User.objects.get(profile__id=driverId)

    for orderId in orders:
        order = Order.objects.get(id=orderId)
        order.shipper = driver
        order.status = 2
        order.save()

    return Response(
        status=status.HTTP_200_OK, data={"message": "Succesfully place order"}
    )


@api_view(["POST"])
@permission_classes([IsAuthenticated, AdminOnly])
def ordersUnassign(request):
    """Edit and delete order"""
    if request.method == "POST":
        if request.data.get("orders"):
            for orderId in request.data.get("orders"):
                unassignedOrder(orderId)

        if request.data.get("order"):
            unassignedOrder(request.data.get("order"))

    return Response(
        status=status.HTTP_200_OK, data={"message": "Succesfully edited orders"}
    )


@api_view(["GET"])
@permission_classes([IsAuthenticated, AdminOnly])
def reports(request):
    """Calculate analytics results for reports"""
    allOrders = Order.objects.all()

    data = {}
    data.update(
        {
            "allTime": {
                "processing": allOrders.filter(status=1).count(),
                "delivering": allOrders.filter(status=2).count(),
                "delivered": allOrders.filter(status=3).count(),
                "failed": allOrders.filter(status=4).count(),
                "revenue": calculateRevenue(allOrders),
            }
        }
    )

    today = datetime.now()
    dailyRecords = getDateRecords(today, allOrders)
    data.update({"daily": dailyRecords})

    last7Records = getPast7DaysRecords(allOrders)
    data.update({"last7Days": last7Records})

    thisMonth = getMonthRecords(allOrders)
    data.update({"thisMonth": thisMonth})

    return Response(status=status.HTTP_200_OK, data=data)


@api_view(["POST"])
@permission_classes([IsAuthenticated, StaffOnly])
def orderUpdateLocation(request, id):
    """Update location of the order"""

    try:
        order = Order.objects.get(id=id)
    except Order.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    locationJSONString = request.data.get("location")

    if locationJSONString:
        order.location = locationJSONString
        order.save()
    else:
        return Response(status=status.HTTP_400_BAD_REQUEST)

    return Response(status=status.HTTP_200_OK)


@api_view(["POST"])
@permission_classes([IsAuthenticated, StaffOnly])
def orderFinish(request, id):
    try:
        order = Order.objects.get(id=id)
    except Order.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    orderStatus = request.data.get("status")

    if orderStatus:
        order.status = 3
        order.save()

    return Response(status=status.HTTP_200_OK)


# Utils Functions
def filterOrders(request, orderQuery):
    """Filter order from get method"""
    orderStatus = request.GET.get("status")
    paymentMethod = request.GET.get("payment")
    startDate = request.GET.get("start")
    endDate = request.GET.get("end")

    if orderStatus and orderStatus.isnumeric():
        orderQuery = orderQuery.filter(status=orderStatus)
    if paymentMethod and paymentMethod.isnumeric():
        orderQuery = orderQuery.filter(paymentMethod=paymentMethod)

    if startDate and endDate:
        startDate = datetime.strptime(startDate, "%Y-%m-%d")
        endDate = datetime.strptime(endDate, "%Y-%m-%d")

        # Add timezone sensitive to datetime obj
        startDate = startDate.replace(tzinfo=timezone.utc)
        endDate = endDate.replace(tzinfo=timezone.utc)

        endDate += timedelta(days=1)  # add 1 day to include the endate from query

        orderQuery = orderQuery.filter(dateCreated__range=(startDate, endDate))

    return orderQuery


def editOrder(order, data):
    """Edit some field of an order"""
    newStatus = data.get("status")
    if newStatus:
        order.status = newStatus

    newPayment = data.get("paymentMethod")
    if newPayment:
        order.paymentMethod = newPayment

    driverId = data.get("driverId")
    if driverId:
        driverProfile = Profile.objects.get(id=driverId)
        order.shipper = driverProfile.user

    order.save()
    return True


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


def unassignedOrder(orderId):
    """Unassigned any order that has a driver"""

    order = Order.objects.get(id=orderId)
    order.shipper = None
    order.status = 1
    order.save()

    return True


def getDateRecords(date, allOrders):
    """Count orders on the daily"""
    startTime = date.replace(hour=0, minute=0, tzinfo=timezone.utc)
    endTime = date.replace(hour=23, minute=59, tzinfo=timezone.utc)

    orders = allOrders.filter(dateCreated__range=(startTime, endTime))

    return {
        "processing": orders.filter(status=1).count(),
        "delivering": orders.filter(status=2).count(),
        "delivered": orders.filter(status=3).count(),
        "failed": orders.filter(status=4).count(),
        "revenue": calculateRevenue(orders),
    }


def getPast7DaysRecords(allOrders):
    """
    Retrieve last 7 days orders records

    Format:
    {
        "categories": [ ...days ],
        "series": [
            {
                "name": {order.status}
                "data": { data for each categories }
            }, ...
        ]
    }
    """
    startDate = datetime.now().replace(tzinfo=timezone.utc) - timedelta(days=6)

    weekDays = []
    processingCount = []
    deliveringCount = []
    deliveredCount = []
    failedCount = []
    revenue = 0

    for day in range(7):
        date = startDate + timedelta(days=day)

        weekDays.append(day_name[date.weekday()])
        dateRecords = getDateRecords(date, allOrders)

        processingCount.append(dateRecords.get("processing"))
        deliveringCount.append(dateRecords.get("delivering"))
        deliveredCount.append(dateRecords.get("delivered"))
        failedCount.append(dateRecords.get("failed"))
        revenue += dateRecords.get("revenue")

    formattedData = {
        "categories": weekDays,
        "series": [
            {"name": "Processing", "data": processingCount},
            {"name": "Delivering", "data": deliveringCount},
            {"name": "Delivered", "data": deliveredCount},
            {"name": "Failed", "data": failedCount},
        ],
        "revenue": revenue,
    }

    return formattedData


def getMonthRecords(allOrders):
    """Get records from 4 weeks of the current month"""
    weekMonths = ["First Week", "Second Week", "Third Week", "Fourth Week"]
    processingCount = []
    deliveringCount = []
    deliveredCount = []
    failedCount = []
    revenue = 0

    startTime = datetime.now().replace(hour=0, minute=0, day=1, tzinfo=timezone.utc)
    for _ in weekMonths:
        endTime = startTime + timedelta(days=7)
        orders = allOrders.filter(dateCreated__range=(startTime, endTime))

        processingCount.append(orders.filter(status=1).count())
        deliveringCount.append(orders.filter(status=2).count())
        deliveredCount.append(orders.filter(status=3).count())
        failedCount.append(orders.filter(status=4).count())
        revenue += calculateRevenue(orders)

        startTime = endTime

    formattedData = {
        "categories": weekMonths,
        "series": [
            {"name": "Processing", "data": processingCount},
            {"name": "Delivering", "data": deliveringCount},
            {"name": "Delivered", "data": deliveredCount},
            {"name": "Failed", "data": failedCount},
        ],
        "revenue": revenue,
    }

    return formattedData


def calculateRevenue(orders):
    """Calculate revenue from a number of orders"""
    totalRevenue = 0

    for order in orders:
        totalRevenue += order.shippingPrice if order.status == 3 else 0

    return totalRevenue
