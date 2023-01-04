from rest_framework import status, viewsets, permissions
from rest_framework.decorators import action
from rest_framework.generics import CreateAPIView, RetrieveUpdateDestroyAPIView, UpdateAPIView
from rest_framework.permissions import IsAuthenticatedOrReadOnly, AllowAny, IsAuthenticated, BasePermission
from rest_framework.response import Response

from .models import MyUser
from .serializers import ProfileSerializer, ProfileImageSerializer


class IsAuthenticatedAndOwner(BasePermission):
    message = 'You must be the owner of this object.'

    def has_permission(self, request, view):
        return request.user and request.user.is_authenticated

    def has_object_permission(self, request, view, obj):
        return obj == request.user


# class UserViewSet(viewsets.ModelViewSet):
#     queryset = MyUser.objects.all()
#     serializer_class = MyUserSerializer
#     # permission_classes = [IsAuthenticatedOrReadOnly]
#     # action_permissions = {
#     #     # IsAuthenticated: ['create'],
#     #     IsAuthenticated: ['retrieve', 'list'],
#     #     OwnProfilePermission: ['update', 'partial_update', 'destroy'],
#     # }
#
#     def get_permissions(self):
#         """
#         Instantiates and returns the list of permissions that this view requires.
#         """
#         print(self.action)
#         if self.action == 'list':
#             permission_classes = [IsAuthenticated]
#         else:
#             permission_classes = [IsAuthenticated]
#         return [permission() for permission in permission_classes]
#
#     def list(self, request, *args, **kwargs):
#         return super().list(request, *args, **kwargs)
#
#     @action(detail=True, methods=['post'])
#     def set_password(self, request, pk=None):
#         user = self.get_object()
#         serializer = MyUserSerializer(data=request.data)
#         if serializer.is_valid():
#             user.set_password(serializer.validated_data['password'])
#             user.save()
#             return Response({'status': 'password set'})
#         else:
#             return Response(serializer.errors,
#                             status=status.HTTP_400_BAD_REQUEST)

class UserProfileCreateView(CreateAPIView):
    queryset = MyUser.objects.all()
    serializer_class = ProfileSerializer


class RetrieveUpdateDeleteItem(RetrieveUpdateDestroyAPIView):
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