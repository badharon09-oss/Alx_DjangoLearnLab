from django.shortcuts import render

# Create your views here.
from rest_framework import generics
from .models import Book
from .serializers import BookSerializer

class BookList(generics.ListAPIView):
    """View to list all books."""
    queryset = Book.objects.all()
    serializer_class = BookSerializer

