from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)
from django.urls import path, include, re_path
from .views import *

urlpatterns = [

    path('drf-auth/', include('rest_framework.urls')),
    path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),\
    path('post/', PostAPIList.as_view()),
    path('post-update/<int:pk>/', PostAPIUpdate.as_view()),
    path('auth/', include('djoser.urls')),  # new
    re_path(r'^auth/', include('djoser.urls.authtoken')),

]