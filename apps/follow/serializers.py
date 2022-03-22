from rest_framework import serializers
from api.serializers import UserByFollowerSerializer
from .models import Follower


class ListFollowerSerializer(serializers.ModelSerializer):
    # subscribers = UserByFollowerSerializer(many=True, read_only=True)

    class Meta:
        model = Follower
        fields = ('subscriber', 'user')