from django.contrib.auth import get_user_model, authenticate, login
from django.http import JsonResponse
from rest_framework import status
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from .models import Order
from .serializers import CustomerSerializer


@api_view(["POST"])
@permission_classes([IsAuthenticated])
def orderCreateApi(request):
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
