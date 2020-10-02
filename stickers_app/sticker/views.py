from django.shortcuts import render
from rest_framework.permissions import IsAuthenticated
from rest_framework.views import APIView
from rest_framework import generics


from .models import Sticker
from .serializers import UserStickerSerializer


class UserStickerList(generics.ListCreateAPIView):
    serializer_class = UserStickerSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        """
        This view returns a list of all the given
        user stickers
        """
        user = self.request.user
        return Sticker.objects.filter(owner=user)

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)


class UserStickerDetails(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = UserStickerSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        """
        This view returns user's single sticker - detailed view
        """
        user = self.request.user
        return Sticker.objects.filter(owner=user)