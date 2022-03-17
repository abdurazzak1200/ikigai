from django.urls import path
from .views import *

urlpatterns = [
    path('all-users', AllUserView.as_view()),
    path('all-post', AllPostView.as_view()),
    path('all-category', CategoryView.as_view()),
    path('post-created', PostCreatesApiView.as_view())
]