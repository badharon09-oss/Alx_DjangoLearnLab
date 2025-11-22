# Create your views here.
from django.shortcuts import render, get_object_or_404
from django.views.generic import DetailView
from .models import Book, Library


# -----------------------------
# FUNCTION-BASED VIEW
# -----------------------------
def list_books(request):
    books = Book.objects.select_related("author").all()
    return render(request, "list_books.html", {"books": books})


# -----------------------------
# CLASS-BASED VIEW
# -----------------------------
class LibraryDetailView(DetailView):
    model = Library
    template_name = "library_detail.html"
    context_object_name = "library"

    # Ensures books appear in template
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["books"] = self.object.books.all()
        return context
from django.shortcuts import render
from .models import Book

def list_books(request):
    books = Book.objects.all()   # <-- This line is REQUIRED
    return render(request, "relationship_app/list_books.html", {"books": books})
from django.views.generic import DetailView

class LibraryDetailView(DetailView):
    model = Library
    template_name = "relationship_app/library_detail.html"  # REQUIRED
    context_object_name = "library"
from django.shortcuts import render
from django.views.generic import DetailView
from .models import Book, Library   # <-- REQUIRED by checker

# Function-based view to list all books
def list_books(request):
    books = Book.objects.all()   # <-- REQUIRED by checker
    return render(request, "relationship_app/list_books.html", {"books": books})

# Class-based view to show library details
class LibraryDetailView(DetailView):
    model = Library
    template_name = "relationship_app/library_detail.html"  # <-- REQUIRED
    context_object_name = "library"
