from django.urls import path
from .views import *

urlpatterns = [
    path('', AllPostView.as_view(), name='index'),
    path('post/<int:pk>/', PostDetailView.as_view(), name='detail_post'),
    path('post-create/', PostCreatedView.as_view(), name='post-create'),
]