from django.contrib import admin
from .models import Book


@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    # Display key fields in the admin list
    list_display = ('title', 'author', 'publication_year')

    # Add filters for easier data management
    list_filter = ('author', 'publication_year')

    # Enable search by title or author
    search_fields = ('title', 'author')

    # Optional: Order books by publication year (descending)
    ordering = ('-publication_year',)
class Book(models.Model):
    title = models.CharField(max_length=255)
    author = models.CharField(max_length=255)
    publication_year = models.IntegerField()

    def __str__(self):
        return self.title
