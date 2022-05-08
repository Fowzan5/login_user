from django.urls import path, include
from user.views import MyObtainTokenPairView
from rest_framework_simplejwt.views import TokenRefreshView
from rest_framework import routers
from . import views
from django.conf import settings


router = routers.DefaultRouter()

router.register('user', views.UserViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('login/', MyObtainTokenPairView.as_view(), name='token_obtain_pair'),
    path('login/refresh/', TokenRefreshView.as_view(), name='token_refresh')
]