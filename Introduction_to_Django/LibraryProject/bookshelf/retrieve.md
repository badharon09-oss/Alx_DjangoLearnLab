
# Retrieve a book by its ID
from bookshelf.models import Book

book = Book.objects.get(id=1)
print(book.title)
