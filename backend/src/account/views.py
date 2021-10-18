from django.contrib.auth import get_user_model, authenticate, login
from django.http import JsonResponse
from rest_framework import status
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.authtoken.models import Token

from .models import Profile
from .serializers import UserSerializer, ProfileSerializer
from .permissions import AdminOnly

User = get_user_model()


@api_view(["POST"])
def loginApi(request):
    """Token login"""
    email = request.data.get("email", None)
    password = request.data.get("password", None)

    user = authenticate(request, email=email, password=password)

    if user is not None:
        login(request, user)
        print(f"[SERVER] Login successfully from {user}\n")
        token = Token.objects.get(user=user)
        return Response({"auth_token": token.key}, status=status.HTTP_200_OK)

    return JsonResponse(
        status=status.HTTP_400_BAD_REQUEST,
        data={"status": "false", "message": "Invalid email or password"},
    )


@api_view(["POST"])
def registerApi(request):
    """Create new account and response token"""
    serializer = UserSerializer(data=request.data)

    if serializer.is_valid():
        user = serializer.save()
        print(f"User {user} is created\n")

    else:
        print(f"[SERVER]: Error registering user {serializer.errors}")
        return JsonResponse(
            status=status.HTTP_400_BAD_REQUEST, data={"errors": serializer.errors}
        )

    return JsonResponse(status=status.HTTP_200_OK, data={"message": "User is created"})


@api_view(["GET", "POST"])
def profileApi(request):
    """
    Get or update profile
    """
    if request.user.is_authenticated:
        profile = Profile.objects.get(user=request.user)

        # Update profile
        if request.method == "POST":
            serializer = ProfileSerializer(profile, data=request.data)
            if serializer.is_valid():
                serializer.save()
            else:
                print(f"[SERVER]: Error updating profile {serializer.errors}")

            return JsonResponse(
                status=status.HTTP_200_OK, data={"message": "Profile updated!"}
            )

        # Get profile
        else:
            serializer = ProfileSerializer(
                profile, many=False, context={"request": request}
            )
            return Response(serializer.data)

    else:
        print("[SERVER]: Invalid token", request.headers)
        return JsonResponse(
            status=status.HTTP_401_UNAUTHORIZED,
            data={"message": "You are not authorized to view this profile"},
        )


@api_view(["GET"])
@permission_classes([IsAuthenticated, AdminOnly])
def staffProfile(request):
    profiles = Profile.objects.filter(user__admin=True)

    serializers = ProfileSerializer(profiles, many=True)
    return Response(status=status.HTTP_200_OK, data=serializers.data)
