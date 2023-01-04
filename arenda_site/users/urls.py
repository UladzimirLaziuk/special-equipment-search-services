from django.urls import path, include
from rest_framework.routers import DefaultRouter


from .views import UserProfileCreateView, RetrieveUpdateDeleteItem, SetProfileImageView

#
# router = DefaultRouter()
# router.register(r'', UserViewSet, basename='user')
urlpatterns = [
    path('api-auth/', include('rest_framework.urls')),
    path("create-profiles/", UserProfileCreateView.as_view(), name="create-profiles"),
    path("update-destroy-profiles/", RetrieveUpdateDeleteItem.as_view(), name="update-destroy-profiles"),
    path("set_image_profiles/", SetProfileImageView.as_view(), name="set_image_profiles"),



]


