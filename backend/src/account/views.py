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
@permission_classes([IsAuthenticated])
def verifyAccount(request):
    """
    Verify token
    If token is valid, return a profile info of that user user
    Change user info if receive a valid POST data
    """
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


@api_view(["GET"])
@permission_classes([IsAuthenticated, AdminOnly])
def profileList(request):
    """Get profile base on role"""
    query = request.GET.get("q") or "employee"

    queries = {
        "employee": Profile.objects.filter(user__admin=True),
        "consignor": Profile.objects.filter(user__admin=False),
        "consignee": Profile.objects.filter(consignee=True),
    }

    profiles = queries.get(query.lower(), None)

    if not profiles:
        return Response(
            status=status.HTTP_400_BAD_REQUEST,
            data={"error": "Invalid query parameters"},
        )

    serializers = ProfileSerializer(profiles, many=True)
    return Response(status=status.HTTP_200_OK, data=serializers.data)


@api_view(["GET"])
@permission_classes([IsAuthenticated, AdminOnly])
def profile(request, email):
    """Return profile information correspond to email parameter"""
    query = Profile.objects.filter(user__email=email)

    if not query.exists():
        return Response(status=status.HTTP_404_NOT_FOUND, data={"error": "Profile did not exists"})
    
    serializer = ProfileSerializer(query[0], many=False)
    return Response(status=status.HTTP_200_OK, data=serializer.data)
