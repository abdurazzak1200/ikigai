from django.urls import path
from .views import *

urlpatterns = [
    path('update-custom/<int:pk>', UpdateCustomView.as_view(), name='update-custom')
]