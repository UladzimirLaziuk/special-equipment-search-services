from django.contrib.auth.views import LogoutView, LoginView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.generics import CreateAPIView, RetrieveUpdateDestroyAPIView, UpdateAPIView, RetrieveAPIView
from rest_framework.permissions import BasePermission

from django.contrib.auth import login, authenticate
from rest_framework.views import APIView

from .models import MyUser
from .serializers import ProfileSerializer, ProfileImageSerializer, LoginSerializer


class IsAuthenticatedAndOwner(BasePermission):
    message = 'You must be the owner of this object.'

    def has_permission(self, request, view):
        return request.user and request.user.is_authenticated

    def has_object_permission(self, request, view, obj):
        return obj == request.user


class UserProfileCreateView(CreateAPIView):
    queryset = MyUser.objects.all()
    serializer_class = ProfileSerializer

    def perform_create(self, serializer):
        user = serializer.save()
        login(request=self.request, user=user)


class RetrieveUpdateDeleteProfile(RetrieveUpdateDestroyAPIView):
    permission_classes = [IsAuthenticatedAndOwner]
    queryset = MyUser.objects.all()
    serializer_class = ProfileSerializer

    def get_object(self, queryset=None):
        obj = self.request.user
        return obj


class SetProfileImageView(UpdateAPIView):
    permission_classes = [IsAuthenticatedAndOwner]
    queryset = MyUser.objects.all()
    serializer_class = ProfileImageSerializer

    def get_object(self, queryset=None):
        obj = self.request.user
        return obj

    def post(self, request, *args, **kwargs):
        return super().update(request, *args, **kwargs)


class AppLogoutView(LogoutView):
    pass


class UserLogin(APIView):
    http_method_names = [
        "post",
    ]
    def post(self, request, format=None):
        serializer = LoginSerializer(data=request.data)
        if serializer.is_valid():
            validate_data = serializer.validated_data
            user = authenticate(request, email=validate_data['email'], password=validate_data['password'])
            if user is not None:
                login(request, user)
                new_data = {**serializer.data, **{'status':user.status}}
                return Response(new_data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
