from django.urls import path
from .views import *
from . import views

urlpatterns = [
    path('', AllPostView.as_view(), name='index'),
    path('post-create/', PostCreatedView.as_view(), name='post-create'),
    path('<str:category_slug>/', AllPostView.as_view(), name='category_list'),
    path('post/<int:pk>/', PostDetailView.as_view(), name='detail_post'),
    path('post-edit/<int:pk>/', views.UpdatePost.as_view(), name='edit-post'),
]