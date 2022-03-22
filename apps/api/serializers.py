from rest_framework import  serializers
from django.contrib.auth.models import User
from posts.models import Post, Category, Comment
from follow.models import Follower


class UsersSerializers(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username']


class CategorySerializers(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ['id', 'name', 'slug']


class PostSerializer(serializers.ModelSerializer):
    user = UsersSerializers(read_only=False)
    category = CategorySerializers(read_only=True)

    class Meta:
        model = Post
        fields = ['id', 'user', 'category', 'title', 'img', 'description', 'likes', 'archived', 'created']



class UserByFollowerSerializer(serializers.ModelSerializer):
    image = serializers.ImageField(read_only=True)

    class Meta:
        model = User
        fields = ('id', 'user', 'image')
