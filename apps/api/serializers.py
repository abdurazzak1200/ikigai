from rest_framework import serializers
from rest_framework.parsers import JSONParser
from rest_framework.renderers import JSONRenderer

from posts.models import Post
from comments.models import Comment


class PostSerializer(serializers.ModelSerializer):
    # user = serializers.HiddenField(default=serializers.CurrentUserDefault())

    class Meta:
        model = Post
        fields = "__all__"




class CommentsSerializer(serializers.ModelSerializer):

    class Meta:
        model = Comment
        fields = ('username', 'text')
