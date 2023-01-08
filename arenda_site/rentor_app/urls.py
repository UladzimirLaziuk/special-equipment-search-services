from django.urls import path
from . import views

urlpatterns = [
    path('create_ad/', views.AdRenterCreateView.as_view(), name='create_ads'),
    path('create_obj_vehicle/', views.VehicleRenterCreateView.as_view(), name='create_obj_vehicle'),
    path('update/<int:pk>', views.AdRenterRetrieveUpdateView.as_view(), name='renter_ad_update'),
    path('delete/', views.AdRenterDeleteView.as_view(), name='renter_ad_delete'),
    path('ad_detail/<int:pk>', views.AdRenterDetailView.as_view(), name='renter_ad_detail'),
    # path('', views.RenterAdListViews.as_view(), name='renter_ads_list'),
]
