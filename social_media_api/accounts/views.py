from rest_framework import generics, permissions
from rest_framework.response import Response
from .models import User
from .serializers import (
    RegisterSerializer,
    LoginSerializer,
    UserProfileSerializer
)

from django.contrib.auth import get_user_model

CustomUser = get_user_model()
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response


@api_view(['GET'])
@permission_classes([IsAuthenticated])
def list_users(request):
    """
    Returns a list of all users.
    This view exists to support user discovery and follow functionality.
    """
    users = CustomUser.objects.all()
    data = [{"id": user.id, "username": user.username} for user in users]
    return Response(data)

class RegisterView(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = RegisterSerializer
    permission_classes = [permissions.AllowAny]


class LoginView(generics.GenericAPIView):
    serializer_class = LoginSerializer
    permission_classes = [permissions.AllowAny]

    def post(self, request):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        return Response(serializer.validated_data)


class ProfileView(generics.RetrieveUpdateAPIView):
    serializer_class = UserProfileSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_object(self):
        return self.request.user
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from django.shortcuts import get_object_or_404
from django.contrib.auth import get_user_model

User = get_user_model()


@api_view(['POST'])
@permission_classes([IsAuthenticated])
def follow_user(request, user_id):
    user_to_follow = get_object_or_404(User, id=user_id)

    if user_to_follow == request.user:
        return Response(
            {"detail": "You cannot follow yourself."},
            status=400
        )

    request.user.following.add(user_to_follow)
    return Response({"detail": f"You are now following {user_to_follow.username}"})


@api_view(['POST'])
@permission_classes([IsAuthenticated])
def unfollow_user(request, user_id):
    user_to_unfollow = get_object_or_404(User, id=user_id)

    request.user.following.remove(user_to_unfollow)
    return Response({"detail": f"You unfollowed {user_to_unfollow.username}"})
