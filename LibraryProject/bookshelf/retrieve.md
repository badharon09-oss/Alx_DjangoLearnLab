\# Retrieve a book by its ID

from bookshelf.models import Book



book = Book.objects.get(id=1)

book = Book.objects.get(title="1984")

print(book.title)



