from django.contrib.auth.views import LogoutView
from rest_framework.generics import CreateAPIView, RetrieveUpdateDestroyAPIView, UpdateAPIView
from rest_framework.permissions import BasePermission

from django.contrib.auth import login
from .models import MyUser
from .serializers import ProfileSerializer, ProfileImageSerializer


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

class AppLogoutView(LogoutView):
    pass
