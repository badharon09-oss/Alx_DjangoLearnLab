from django.shortcuts import render

# Create your views here.
from django.contrib.auth.decorators import permission_required
from django.shortcuts import render
from .models import Book

# View Books (requires can_view)
@permission_required('bookshelf.can_view', raise_exception=True)
def view_books(request):
    books = Book.objects.all()
    return render(request, "bookshelf/view_books.html", {"books": books})

# Create Book (requires can_create)
@permission_required('bookshelf.can_create', raise_exception=True)
def create_book(request):
    return render(request, "bookshelf/create_book.html")

# Edit Book (requires can_edit)
@permission_required('bookshelf.can_edit', raise_exception=True)
def edit_book(request, pk):
    return render(request, "bookshelf/edit_book.html")

# Delete Book (requires can_delete)
@permission_required('bookshelf.can_delete', raise_exception=True)
def delete_book(request, pk):
    return render(request, "bookshelf/delete_book.html")
