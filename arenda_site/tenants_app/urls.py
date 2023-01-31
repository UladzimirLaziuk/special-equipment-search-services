from django.urls import path
from . import views

urlpatterns = [
    path('search_renter/', views.SearchRentorCreateView.as_view(), name='create_search_table'),
    path('update/<int:pk>', views.SearchRentorRetrieveUpdateView.as_view(), name='search_renter_ad_update'),
    path('delete/', views.SearchRentorDeleteView.as_view(), name='search_renter_ad_delete'),
    path('ad_detail/<int:pk>', views.SearchRentorDetailView.as_view(), name='search_renter_ad_detail'),

]
