from django.contrib.auth import get_user_model, authenticate, login
from django.http import JsonResponse
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.authtoken.models import Token

from .serializers import UserSerializer

User = get_user_model()


@api_view(["POST"])
def loginApi(request):
    serializer = UserSerializer(data=request.data)

    if serializer.is_valid():
        email = serializer.validated_data.get("email")
        password = serializer.validated_data.get("password")

        user = authenticate(request, email=email, password=password)

        if user is not None:
            login(request, user)
            print(f"[SERVER] Login successfully from {user}\n")
            token = Token.objects.get(user=user)

            return Response({"auth_token": token.key}, status=status.HTTP_200_OK)
        else:
            return JsonResponse(
                status=status.HTTP_401_UNAUTHORIZED,
                data={"status": "false", "message": "Invalid email or password"},
            )

    else:
        return JsonResponse(
            status=status.HTTP_401_UNAUTHORIZED,
            data={"status": "false", "message": "Invalid email or password"},
        )
