from django.shortcuts import render

from rest_framework import viewsets
from .models import News, Comment
from .serializers import NewsSerializer,CommentSerializer
from rest_framework.permissions import IsAuthenticated, IsOwnerOrReadOnly, AllowAny
from rest_framework.pagination import LimitOffsetPagination

class NewsViewSet(viewsets.ModelViewSet):
    queryset = News.objects.all()
    serializer_class = NewsSerializer
    permission_classes = [IsAuthenticated, IsOwnerOrReadOnly]

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)


class CommentViewSet(viewsets.ModelViewSet):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
    pagination_class = LimitOffsetPagination
    permission_classes = [AllowAny, IsAuthenticated]

    def get_queryset(self):
        news_id = self.kwargs['news_id']
        return Comment.objects.filter(news=news_id)

    def perform_create(self, serializer):
        news_id = self.kwargs['news_id']
        serializer.save(author=self.request.user, news_id=news_id)