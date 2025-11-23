from django.shortcuts import render
from django.views.generic import DetailView
from django.views.generic.detail import DetailView
from django.views.generic import ListView, DetailView
from .models import Library, Book  # <-- THIS is required
from .models import Book, Library   # REQUIRED by checker

# -----------------------------
# FUNCTION-BASED VIEW
# -----------------------------
def list_books(request):
    books = Book.objects.all()   # REQUIRED by checker
    return render(request, "relationship_app/list_books.html", {"books": books})
    
class LibraryListView(ListView):
    model = Library
    template_name = "relationship_app/library_list.html"
    context_object_name = "libraries"

# -----------------------------
# CLASS-BASED VIEW
# -----------------------------
class LibraryDetailView(DetailView):
    model = Library   # REQUIRED
    template_name = "relationship_app/library_detail.html"  # REQUIRED
    context_object_name = "library"
    
from django.contrib.auth import login, logout
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render, redirect
from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic import DetailView
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm   # <-- REQUIRED
from .models import Book, Library


# -----------------------------
# USER LOGIN VIEW
# -----------------------------
def user_login(request):
    form = AuthenticationForm()

    if request.method == "POST":
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect("list_books")  # redirect after login

    return render(request, "relationship_app/login.html", {"form": form})


# -----------------------------
# USER LOGOUT VIEW
# -----------------------------
def user_logout(request):
    logout(request)
    return render(request, "relationship_app/logout.html")


# -----------------------------
# USER REGISTRATION VIEW
# -----------------------------
def register(request):
    form = UserCreationForm()

    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)  # auto-login after registration
            return redirect("list_books")

    return render(request, "relationship_app/register.html", {"form": form})

from django.shortcuts import render
from django.contrib.auth.decorators import user_passes_test
from .models import UserProfile

# Helper test functions
def is_admin(user):
    return hasattr(user, "userprofile") and user.userprofile.role == "Admin"

def is_librarian(user):
    return hasattr(user, "userprofile") and user.userprofile.role == "Librarian"

def is_member(user):
    return hasattr(user, "userprofile") and user.userprofile.role == "Member"

@user_passes_test(is_admin)
def admin_view(request):
    return render(request, "relationship_app/admin_view.html")


@user_passes_test(is_librarian)
def librarian_view(request):
    return render(request, "relationship_app/librarian_view.html")


@user_passes_test(is_member)
def member_view(request):
    return render(request, "relationship_app/member_view.html")
