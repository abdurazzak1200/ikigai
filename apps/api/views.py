from rest_framework.generics import ListAPIView, RetrieveAPIView, CreateAPIView, ListCreateAPIView
from django.contrib.auth.models import User
from .serializers import (
    AllPostSerializer,
    CategorySerializers,
    UsersSerializers,
    PostCreateSerializer
)
from posts.models import Post, Category
from rest_framework.response import  Response
from rest_framework import  status
class AllUserView(ListAPIView):
    serializer_class = UsersSerializers
    queryset = User.objects.all()


class AllPostView(ListAPIView):
    serializer_class = AllPostSerializer
    queryset = Post.objects.filter(archived=False)


class CategoryView(ListAPIView):
    serializer_class = CategorySerializers
    queryset = Category.objects.all()


# class PostCreateAPIView(CreateAPIView):
#     serializer_class = PostCreateSerializer
#     queryset = Post.objects.all()
#

class PostCreatesApiView(ListCreateAPIView):
    queryset = Post.objects.all()
    serializer_class = PostCreateSerializer

    def list(self, request):
        # Note the use of `get_queryset()` instead of `self.queryset`
        queryset = self.get_queryset()
        serializer = PostCreateSerializer(queryset, many=True)
        return Response(serializer.data)
