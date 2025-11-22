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
