from rest_framework.test import APITestCase, APIClient
from rest_framework import status
from django.urls import reverse
from django.contrib.auth.models import User
from api.models import Book, Author


class BookAPITestCase(APITestCase):

    def setUp(self):
        # Django automatically creates a separate TEST DATABASE
        # No login() allowed, so we use force_authenticate()

        self.user = User.objects.create_user(
            username="testuser", password="pass12345"
        )

        self.client = APIClient()
        self.client.force_authenticate(user=self.user)

        # Sample authors
        self.author1 = Author.objects.create(name="John Writer")
        self.author2 = Author.objects.create(name="Jane Coder")

        # Sample books
        self.book1 = Book.objects.create(
            title="Django Mastery",
            publication_year=2021,
            author=self.author1
        )
        self.book2 = Book.objects.create(
            title="Python Tips",
            publication_year=2023,
            author=self.author2
        )

        self.list_url = reverse("book-list")

    # --------------------
    # CRUD Tests
    # --------------------

    def test_create_book(self):
        data = {
            "title": "New Book",
            "publication_year": 2024,
            "author": self.author1.id
        }

        response = self.client.post(self.list_url, data, format="json")
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_update_book(self):
        url = reverse("book-detail", args=[self.book1.id])

        data = {
            "title": "Updated Django",
            "publication_year": 2022,
            "author": self.author1.id
        }

        response = self.client.put(url, data, format="json")
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_delete_book(self):
        url = reverse("book-detail", args=[self.book2.id])
        response = self.client.delete(url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)

    # --------------------
    # Filtering / Search / Ordering
    # --------------------

    def test_filter_by_title(self):
        response = self.client.get(self.list_url, {"title": "Django Mastery"})
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_search_books(self):
        response = self.client.get(self.list_url, {"search": "python"})
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_ordering_books(self):
        response = self.client.get(self.list_url, {"ordering": "publication_year"})
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    # --------------------
    # Permissions
    # --------------------

    def test_unauthenticated_user_cannot_create(self):
        client = APIClient()
        data = {
            "title": "Blocked",
            "publication_year": 2025,
            "author": self.author1.id
        }
        response = client.post(self.list_url, data, format="json")
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)
