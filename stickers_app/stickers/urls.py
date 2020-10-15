from django.contrib import admin
from django.urls import path
from .views import (
    StickerDetails, 
    UserBoardDetails, 
    board_details,
    UserBoardList,
    board_stickers_list,
    board_sticker_create,
)


urlpatterns = [
    path('', 
        UserBoardList.as_view(), 
        name='board-list'), # ['GET', 'POST'] lists and creates boards

    path('<int:board_pk>/', 
        board_details, 
        name='board-details'), # ['get', 'put', 'delete'] methods on board

    path('<int:board_pk>/list/', 
        board_stickers_list, 
        name='board-stickers-list'), # ['get'] lists stickers on given board

    path('sticker/create/', # <int:board_pk/create/ ?
        board_sticker_create,
        name='board-sticker-create'), # ['POST'] creates sticker on board

    path('sticker/<int:pk>/', # <int:board_pk>/<int:sticker_pk>/ ?
        StickerDetails.as_view(), 
        name='sticker-details'), # ['GET', 'PUT', 'DELETE'] show, edit or delete given sticker

]
