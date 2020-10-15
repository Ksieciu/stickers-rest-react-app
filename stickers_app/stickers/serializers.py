from rest_framework import serializers
from django.contrib.auth.models import User
from stickers.models import Sticker, Board


class UserBoardSerializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username')

    class Meta:
        model = Board
        fields = ['owner', 'name']


class StickerSerializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username')
    board = serializers.ReadOnlyField(source='board.pk')

    class Meta:
        model = Sticker
        fields = ['id', 'owner', 'board', 'title', 'content', 'alert_time']





# class UserSerializer(serializers.ModelSerializer):
