from django.contrib import admin
from django.urls import path
from .views import UserCreate, UserList

urlpatterns = [
    path('create/', UserCreate.as_view(), name='user-create'),
    path('list/', UserList.as_view(), name='user-list'),
]
