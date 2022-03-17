from rest_framework import  serializers
from django.contrib.auth.models import User
from posts.models import Post, Category, Comment


class UsersSerializers(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['username']


class CategorySerializers(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ['name', 'slug']


class AllPostSerializer(serializers.ModelSerializer):
    user = serializers.StringRelatedField()
    category = CategorySerializers(read_only=True)

    class Meta:
        model = Post
        fields = ['user', 'category', 'title', 'img', 'description', 'likes', 'archived', 'created']


class PostCreateSerializer(serializers.ModelSerializer):

    class Meta:
        model = Post
        exclude = ('user', 'category', 'title', 'img', 'description', 'likes', 'archived', 'created')
