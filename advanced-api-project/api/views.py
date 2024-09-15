from django.shortcuts import render
from rest_framework import generics
from rest_framework import status
from rest_framework.response import Response
from .models import Book
from .serializers import BookSerializer
from rest_framework.permissions import IsAuthenticated
from rest_framework.permissions import IsAuthenticatedOrReadOnly

"""
BookListView: Handles GET requests to list all books and POST requests to create a new book.
Permission: Authenticated users can create books, while others can only view.
"""
class BookListView(generics.ListCreateAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]  # Allow authenticated users to create; others can only view.

"""
BookDetailView: Handles GET, PUT, DELETE requests to retrieve, update, or delete a book by its ID.
Permission: Only authenticated users can update or delete books.
"""
class BookDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [IsAuthenticated]  # Allow updates/deletes for authenticated users.


class CustomBookCreateView(generics.CreateAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)  # Custom validation can be added here.
        self.perform_create(serializer)
        return Response(serializer.data, status=status.HTTP_201_CREATED)

class CustomBookUpdateView(generics.UpdateAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer

    def update(self, request, *args, **kwargs):
        instance = self.get_object()
        serializer = self.get_serializer(instance, data=request.data, partial=True)
        serializer.is_valid(raise_exception=True)
        self.perform_update(serializer)
        return Response(serializer.data)