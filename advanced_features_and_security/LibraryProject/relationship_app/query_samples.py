from relationship_app.models import Author, Book, Library, Librarian

def run_queries():
    # 1. Query all books by a specific author
    author = Author.objects.get(name="George Orwell")
    books_by_author = author.books.all()
    print("Books by George Orwell:", [book.title for book in books_by_author])

    # 2. List all books in a library
    library = Library.objects.get(name="Central Library")
    all_books = library.books.all()
    print("Books in Central Library:", [book.title for book in all_books])

    # 3. Retrieve the librarian for a library
    librarian = library.librarian
    print(f"Librarian for {library.name}:", librarian.name)

if __name__ == "__main__":
    run_queries()
from .models import Library

def get_library_by_name(library_name):
    return Library.objects.get(name=library_name)
from .models import Author, Book

def get_author_by_name(author_name):
    return Author.objects.get(name=author_name)

def get_books_by_author(author_name):
    author = Author.objects.get(name=author_name)
    return Book.objects.filter(author=author)
from .models import Librarian, Library

def get_librarian_by_library(library_name):
    library = Library.objects.get(name=library_name)
    return Librarian.objects.get(library=library)
