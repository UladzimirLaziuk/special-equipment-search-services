from django.urls import path


from .views import UserProfileCreateView, RetrieveUpdateDeleteProfile, SetProfileImageView, AppLogoutView

urlpatterns = [
    path("create-profiles/", UserProfileCreateView.as_view(), name="create-profiles"),
    path("update-destroy-profiles/", RetrieveUpdateDeleteProfile.as_view(), name="update-destroy-profiles"),
    path("set_image_profiles/", SetProfileImageView.as_view(), name="set_image_profiles"),

    path('logout/', AppLogoutView.as_view(), name='app-logout'),

]
