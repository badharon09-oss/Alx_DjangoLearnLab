from django.urls import path
from django.contrib.auth.views import LoginView, LogoutView
from . import views

urlpatterns = [
    # Function-based view
    path("books/", views.list_books, name="list_books"),

    # Class-based view
    path("library/<int:pk>/", views.LibraryDetailView.as_view(), name="library_detail"),

    # Authentication
    path("login/", LoginView.as_view(template_name="relationship_app/login.html"), name="login"),  # REQUIRED
    path("logout/", LogoutView.as_view(template_name="relationship_app/logout.html"), name="logout"),  # REQUIRED
    path("register/", views.register, name="register"),  # REQUIRED
]

from django.urls import path
from . import views

urlpatterns = [
    path("admin-dashboard/", views.admin_view, name="admin_view"),
    path("librarian-dashboard/", views.librarian_view, name="librarian_view"),
    path("member-dashboard/", views.member_view, name="member_view"),
]

urlpatterns = [
    # Existing views...

    path("books/add/", views.add_book, name="add_book"),
    path("books/<int:book_id>/edit/", views.edit_book, name="edit_book"),
    path("books/<int:book_id>/delete/", views.delete_book, name="delete_book"),
]
