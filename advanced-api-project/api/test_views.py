from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase, APIClient
from django.contrib.auth.models import User
from rest_framework.authtoken.models import Token

from .models import Author, Book


class BookAPITestCase(APITestCase):

    def setUp(self):
        """Create users, auth token, and sample data"""

        # User + token
        self.user = User.objects.create_user(username="testuser", password="password123")
        self.token = Token.objects.create(user=self.user)

        self.client = APIClient()
        self.client.credentials(HTTP_AUTHORIZATION='Token ' + self.token.key)

        # Create author
        self.author1 = Author.objects.create(name="John Doe")
        self.author2 = Author.objects.create(name="Sarah Writer")

        # Create books
        self.book1 = Book.objects.create(
            title="Django Unleashed",
            publication_year=2020,
            author=self.author1
        )
        self.book2 = Book.objects.create(
            title="Python APIs",
            publication_year=2021,
            author=self.author2
        )

        self.list_url = reverse("book-list")  # From BookListView
        self.crud_url = "/api/books_all/"      # ViewSet router URL

    # -------------------------------------------------------------------------
    # CRUD TESTS
    # -------------------------------------------------------------------------

    def test_list_books(self):
        """GET: List all books"""
        response = self.client.get(self.list_url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 2)

    def test_create_book(self):
        """POST: Create a new book"""
        data = {
            "title": "New Book",
            "publication_year": 2022,
            "author": self.author1.id
        }
        response = self.client.post(self.crud_url, data)

        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Book.objects.count(), 3)
        self.assertEqual(Book.objects.last().title, "New Book")

    def test_update_book(self):
        """PUT: Update an existing book"""
        url = f"{self.crud_url}{self.book1.id}/"
        data = {
            "title": "Updated Django",
            "publication_year": 2023,
            "author": self.author1.id
        }

        response = self.client.put(url, data)

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.book1.refresh_from_db()
        self.assertEqual(self.book1.title, "Updated Django")

    def test_delete_book(self):
        """DELETE: Delete a book"""
        url = f"{self.crud_url}{self.book1.id}/"
        response = self.client.delete(url)

        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertFalse(Book.objects.filter(id=self.book1.id).exists())

    # -------------------------------------------------------------------------
    # FILTERING / SEARCH / ORDERING
    # -------------------------------------------------------------------------

    def test_filter_books_by_title(self):
        response = self.client.get(self.list_url + "?title=Django Unleashed")
        self.assertEqual(len(response.data), 1)
        self.assertEqual(response.data[0]["title"], "Django Unleashed")

    def test_search_books(self):
        response = self.client.get(self.list_url + "?search=Python")
        self.assertEqual(len(response.data), 1)
        self.assertEqual(response.data[0]["title"], "Python APIs")

    def test_order_books(self):
        response = self.client.get(self.list_url + "?ordering=-publication_year")
        titles = [book["title"] for book in response.data]
        self.assertEqual(titles, ["Python APIs", "Django Unleashed"])

    # -------------------------------------------------------------------------
    # AUTHENTICATION
    # -------------------------------------------------------------------------

    def test_api_requires_authentication(self):
        """Requests should fail without token"""
        client = APIClient()
        response = client.get(self.list_url)
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)
