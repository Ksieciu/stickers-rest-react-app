from django.contrib import admin
from django.urls import path
from .views import UserStickerList, UserStickerDetails

urlpatterns = [
    path('stickers/', UserStickerList.as_view(), name='sticker-list'),
    path('stickers/<int:pk>/', UserStickerDetails.as_view(), name='sticker-detail'),
]
