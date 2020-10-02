from rest_framework import serializers
from django.contrib.auth.models import User
from sticker.models import Sticker


class UserStickerSerializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username')

    class Meta:
        model = Sticker
        fields = ['id', 'owner', 'title', 'content', 'alert_time']


# class UserSerializer(serializers.ModelSerializer):
