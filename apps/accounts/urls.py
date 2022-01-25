from django.urls import path
from .views import *
from django.contrib.auth.views import LogoutView

urlpatterns = [
    path('login/', ProfileLogin.as_view(), name='login'),
    path('logout/', LogoutView.as_view(next_page='login'), name='logout'),
    path('register/', RegisterPage.as_view(), name='register'),
    path('update-profile/<int:pk>/', UpdateProfileView.as_view(), name='update_profile'),
    path('detail-profile/<int:pk>/', ProfileDetailView.as_view(), name='detail-profile'),
]