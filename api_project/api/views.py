from django.shortcuts import render

# Create your views here.
from rest_framework import generics
from .models import Book
from .serializers import BookSerializer

class BookList(generics.ListAPIView):
    """View to list all books."""
    queryset = Book.objects.all()
    serializer_class = BookSerializer
from rest_framework import generics, viewsets
from .models import Book
from .serializers import BookSerializer

class BookList(generics.ListAPIView):
    """Simple list view (kept for compatibility)."""
    queryset = Book.objects.all()
    serializer_class = BookSerializer


class BookViewSet(viewsets.ModelViewSet):
    """ViewSet for full CRUD operations on Book."""
    queryset = Book.objects.all()
    serializer_class = BookSerializer

