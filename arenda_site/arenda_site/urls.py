from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings

from basic_app import views

urlpatterns = [

    path('admin/', admin.site.urls),
    path('users/', include('users.urls')),
    path('renters/', include('rentor_app.urls')),
    path('tenants/', include('tenants_app.urls')),
    path('', views.Home.as_view(), name='home'),


]
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
