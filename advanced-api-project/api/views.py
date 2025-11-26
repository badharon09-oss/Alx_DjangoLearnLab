from django.shortcuts import render

# Create your views here.
from rest_framework import generics
from .models import Book
from .serializers import BookSerializer
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import SearchFilter, OrderingFilter


class BookListView(generics.ListAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer

    # Enable filtering, searching, ordering
    filter_backends = [DjangoFilterBackend, SearchFilter, OrderingFilter]

    # -------- FILTERING --------
    filterset_fields = ['title', 'publication_year', 'author__name']

    # -------- SEARCHING --------
    search_fields = ['title', 'author__name']

    # -------- ORDERING --------
    ordering_fields = ['title', 'publication_year']
    ordering = ['title']  # default ordering
