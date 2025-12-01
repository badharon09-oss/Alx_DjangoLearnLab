from django.shortcuts import render

# Create your views here.
from rest_framework import serializers
from .models import Book

class BookSerializer(serializers.ModelSerializer):
    """Serializer for the Book model including all fields."""

    class Meta:
        model = Book
        fields = "__all__"
