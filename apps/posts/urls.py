from django.urls import path
from .views import *

urlpatterns = [
    path('', AllPostView.as_view(), name='index'),
    path('post-create/', PostCreatedView.as_view(), name='post-create'),
    path('<str:category_slug>/', AllPostView.as_view(), name='category_list'),
    path('post/<int:pk>/', PostDetailView.as_view(), name='detail_post'),
]