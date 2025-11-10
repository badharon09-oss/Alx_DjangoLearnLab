from bookshelf.models import Book
Delete the book
book = Book.objects.get(title="Nineteen Eighty-Four")
book.delete()
Output: Book deleted successfully
