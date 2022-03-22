from rest_framework.generics import ListAPIView, RetrieveAPIView, CreateAPIView, ListCreateAPIView
from django.contrib.auth.models import User
from rest_framework.pagination import PageNumberPagination
from rest_framework.permissions import IsAuthenticatedOrReadOnly, IsAuthenticated
from .serializers import (
    PostSerializer,
)
from posts.models import Post, Category
from rest_framework.response import  Response
from rest_framework import status, generics


class PostAPIListPagination(PageNumberPagination):
    page_size = 20
    page_size_query_param = 'page_size'
    max_page_size = 2


class PostAPIList(generics.ListCreateAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_classes = (IsAuthenticated, )
    pagination_class = PostAPIListPagination


class PostAPIUpdate(generics.RetrieveUpdateAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_classes = (IsAuthenticatedOrReadOnly, )
