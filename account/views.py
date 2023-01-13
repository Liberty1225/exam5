from django.shortcuts import render
from rest_framework import viewsets
from rest_framework import mixins
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework import status

from .models import Author
from .serializers import RegisterAuthorSerializer


class RegisterAuthorAPIView(viewsets.GenericViewSet):
    queryset = Author.objects.all()
    serializer_class = RegisterAuthorSerializer

    def create_author(self, request, is_author):
        serializer = self.get_serializer_class()(data=request.data)
        if serializer.is_valid():
            serializer.save(is_author=is_author)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    @action(methods=['POST'], detail=False)
    def author(self, request, pk=None):
        return self.create_author(request, True)

    @action(methods=['POST'], detail=False)
    def guest(self, request, pk=None):
        return self.create_author(request, False)

