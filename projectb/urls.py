from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from django.conf import settings
from django.conf.urls.static import static
from projectb import settings

base_api_path = "api/v1/"

urlpatterns = [
    path('admin/', admin.site.urls),
    path(base_api_path +'users/', include('user.urls')),
]
