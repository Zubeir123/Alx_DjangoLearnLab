from rest_framework import generics, status
from django.shortcuts import get_object_or_404
from rest_framework.response import Response
from rest_framework.authtoken.models import Token
from rest_framework import permissions
from rest_framework.views import APIView
from django.contrib.auth import authenticate
from django.contrib.auth import get_user_model
from .serializers import RegisterSerializer, UserSerializer
from .models import CustomUser

User = get_user_model()

class RegisterView(generics.CreateAPIView):
    serializer_class = RegisterSerializer

class LoginView(APIView):
    def post(self, request):
        username = request.data.get('username')
        password = request.data.get('password')
        user = authenticate(username=username, password=password)
        if user:
            token, _ = Token.objects.get_or_create(user=user)
            return Response({'token': token.key})
        return Response({'error': 'Invalid Credentials'}, status=status.HTTP_401_UNAUTHORIZED)

class ProfileView(APIView):
    permission_classes = [permissions.IsAuthenticated]

    def get(self, request):
        serializer = UserSerializer(request.user)
        return Response(serializer.data)

class FollowUserView(generics.GenericAPIView):
    permission_classes = [permissions.IsAuthenticated]

    def post(self, request, user_id):
        user_to_follow = get_object_or_404(CustomUser.objects.all(), id=user_id)
        if request.user == user_to_follow:
            return Response({"error": "You cannot follow yourself."}, status=status.HTTP_400_BAD_REQUEST)

        request.user.following.add(user_to_follow)
        return Response({"message": f"You are now following {user_to_follow.username}"}, status=status.HTTP_200_OK)


class UnfollowUserView(generics.GenericAPIView):
    permission_classes = [permissions.IsAuthenticated]

    def post(self, request, user_id):
        user_to_unfollow = get_object_or_404(CustomUser.objects.all(), id=user_id)
        if request.user == user_to_unfollow:
            return Response({"error": "You cannot unfollow yourself."}, status=status.HTTP_400_BAD_REQUEST)

        request.user.following.remove(user_to_unfollow)
        return Response({"message": f"You have unfollowed {user_to_unfollow.username}"}, status=status.HTTP_200_OK)