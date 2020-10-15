from django.shortcuts import render
from rest_framework import generics, status, permissions
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import Board, Sticker
from .permissions import IsOwnerOrReadOnly
from .serializers import UserBoardSerializer, StickerSerializer


class UserBoardList(generics.ListCreateAPIView):
    serializer_class = UserBoardSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        """
        This view returns a list of all user's boards
        """
        user = self.request.user
        return Board.objects.filter(owner=self.request.user)

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)


@api_view(['GET', 'PUT', 'DELETE'])
@permission_classes([IsOwnerOrReadOnly])
def board_details(request, board_pk, format=None):
    try:
        board = Board.objects.get(pk=board_pk)
        print(board)
    except Board.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = UserBoardSerializer(board)
        return Response(serializer.data)

    elif request.method == 'PUT':
        serializer = UserBoardSerializer(board, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
    
    elif request.method == 'DELETE':
        board.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


@api_view(['GET'])
@permission_classes([IsAuthenticated])
def board_stickers_list(request, board_pk):
    try:
        board = Board.object.get(pk=board_pk)
    except Board.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    qs = Sticker.filter(board=board)
    serializer = StickerSerializer(qs, many=True)
    return Response(serializer.data)


@api_view(['POST'])
@permission_classes([IsAuthenticated])
def board_sticker_create(request, *args, **kwargs):
    serializer = StickerSerializer(data=request.data)
    if serializer.is_valid(raise_exception=True):
        serializer.save(owner=request.user)
        return Response(serializer.data, status=201)
    return Response({}, status=400)


class StickerDetails(generics.RetrieveUpdateDestroyAPIView):
    queryset = Sticker.objects.all()
    serializer_class = StickerSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly,
                          IsOwnerOrReadOnly]


class UserBoardDetails(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = UserBoardSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        """
        This view returns user's single board - detailed view
        """
        user = self.request.user
        return Board.objects.filter(owner=user)


# class StickerList(generics.ListCreateAPIView):
#     serializer_class = StickerSerializer
#     permission_classes = [IsAuthenticated]

#     def get_queryset(self):
#         """
#         This view returns a list of all the given
#         user stickers
#         """
#         user = self.request.user
#         return Sticker.objects.filter(owner=user)

#     def perform_create(self, serializer):
#         serializer.save(owner=self.request.user)


# class StickerDetails(generics.RetrieveUpdateDestroyAPIView):
#     serializer_class = StickerSerializer
#     permission_classes = [IsAuthenticated]

#     def get_queryset(self):
#         """
#         This view returns user's single sticker - detailed view
#         """
#         user = self.request.user
#         print(self.board_name)
#         return Sticker.objects.filter(owner=user, board=self.board_pk)