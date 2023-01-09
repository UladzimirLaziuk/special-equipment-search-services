from django.urls import path


from .views import UserProfileCreateView, RetrieveUpdateDeleteProfile, SetProfileImageView, AppLogoutView, UserLogin

urlpatterns = [
    path("create-profiles/", UserProfileCreateView.as_view(), name="create-profiles"),
    path("login/", UserLogin.as_view(), name='login_user'),
    path("update-destroy-profiles/", RetrieveUpdateDeleteProfile.as_view(), name="update-destroy-profiles"),
    path("set_image_profiles/", SetProfileImageView.as_view(), name="set_image_profiles"),

    path('logout/', AppLogoutView.as_view(), name='app-logout'),

]
