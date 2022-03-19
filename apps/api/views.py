from rest_framework.generics import ListAPIView, RetrieveAPIView, CreateAPIView, ListCreateAPIView
from django.contrib.auth.models import User
from .serializers import (
    PostSerializer,
    CategorySerializers,
    UsersSerializers,
)
from posts.models import Post, Category
from rest_framework.response import  Response
from rest_framework import  status
class AllUserView(ListAPIView):
    serializer_class = UsersSerializers
    queryset = User.objects.all()


class PostAPIView(ListCreateAPIView):
    serializer_class = PostSerializer
    queryset = Post.objects.filter(archived=False)


class CategoryView(ListAPIView):
    serializer_class = CategorySerializers
    queryset = Category.objects.all()

