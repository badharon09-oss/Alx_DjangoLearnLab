from rest_framework import serializers
from django.utils import timezone
from .models import Author, Book

"""
BookSerializer:
- Serializes all fields of the Book model.
- Includes custom validation to ensure publication_year is not in the future.
"""

class BookSerializer(serializers.ModelSerializer):

    class Meta:
        model = Book
        fields = ['id', 'title', 'publication_year', 'author']

    # Custom validation
    def validate_publication_year(self, value):
        current_year = timezone.now().year
        if value > current_year:
            raise serializers.ValidationError("Publication year cannot be in the future.")
        return value


"""
AuthorSerializer:
- Serializes author name.
- Includes nested serialization of all books linked to this author.
- Uses BookSerializer to show each book's details.
"""

class AuthorSerializer(serializers.ModelSerializer):

    # Nesting the BookSerializer to show related book data
    books = BookSerializer(many=True, read_only=True)

    class Meta:
        model = Author
        fields = ['id', 'name', 'books']

