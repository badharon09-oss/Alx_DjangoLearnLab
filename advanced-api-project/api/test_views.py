from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase, APIClient
from django.contrib.auth.models import User

from api.models import Book, Author


class BookAPITestCase(APITestCase):

    def setUp(self):
        # Create test user
        self.user = User.objects.create_user(username="ronald", password="password123")

        # Create API client
        self.client = APIClient()
        self.client.force_authenticate(user=self.user)

        # Create authors
        self.author1 = Author.objects.create(name="Author One")
        self.author2 = Author.objects.create(name="Author Two")

        # Create books
        self.book1 = Book.objects.create(
            title="Django Unleashed",
            publication_year=2020,
            author=self.author1
        )
        self.book2 = Book.objects.create(
            title="Python Secrets",
            publication_year=2023,
            author=self.author2
        )

        self.list_url = reverse('book-list')  # URL name from urls.py


    # ----------------------------------------------------------
    # CRUD TESTS
    # ----------------------------------------------------------

    def test_create_book(self):
        """Test creating a book"""
        data = {
            "title": "New Book",
            "publication_year": 2024,
            "author": self.author1.id
        }

        response = self.client.post(self.list_url, data, format="json")
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Book.objects.count(), 3)
        self.assertEqual(response.data["title"], "New Book")


    def test_update_book(self):
        """Test updating an existing book"""
        url = reverse('book-detail', args=[self.book1.id])

        data = {
            "title": "Django Updated",
            "publication_year": 2021,
            "author": self.author1.id
        }

        response = self.client.put(url, data, format="json")
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.book1.refresh_from_db()
        self.assertEqual(self.book1.title, "Django Updated")


    def test_delete_book(self):
        """Test deleting a book"""
        url = reverse('book-detail', args=[self.book2.id])
        response = self.client.delete(url)

        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(Book.objects.count(), 1)


    # ----------------------------------------------------------
    # FILTERING, SEARCHING, ORDERING
    # ----------------------------------------------------------

    def test_filter_books_by_title(self):
        """?title=Django Unleashed"""
        response = self.client.get(self.list_url, {"title": "Django Unleashed"})
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)
        self.assertEqual(response.data[0]["title"], "Django Unleashed")


    def test_filter_books_by_author_name(self):
        """Filter by foreign key name lookup: author__name="" """
        response = self.client.get(self.list_url, {"author__name": "Author One"})
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)
        self.assertEqual(response.data[0]["author_name"], "Author One")


    def test_search_books(self):
        """search=python"""
        response = self.client.get(self.list_url, {"search": "python"})
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)
        self.assertEqual(response.data[0]["title"], "Python Secrets")


    def test_order_books_by_year(self):
        """ordering=publication_year"""
        response = self.client.get(self.list_url, {"ordering": "publication_year"})
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(
            [book["publication_year"] for book in response.data],
            sorted([self.book1.publication_year, self.book2.publication_year])
        )


    # ----------------------------------------------------------
    # PERMISSIONS
    # ----------------------------------------------------------

    def test_unauthenticated_user_cannot_create_book(self):
        """Ensure public cannot POST"""
        client = APIClient()  # new client, no login

        data = {
            "title": "Unauthorized",
            "publication_year": 2022,
            "author": self.author1.id
        }

        response = client.post(self.list_url, data, format="json")
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)
