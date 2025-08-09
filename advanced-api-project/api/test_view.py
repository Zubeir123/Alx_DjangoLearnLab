from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase, APIClient
from django.contrib.auth.models import User
from .models import Author, Book


class BookAPITests(APITestCase):

    def setUp(self):
        # Create a test user and token
        self.user = User.objects.create_user(username="testuser", password="testpass")
        self.client = APIClient()

        # Create an author
        self.author = Author.objects.create(name="John Doe")

        # Create a book
        self.book = Book.objects.create(
            title="Test Book",
            publication_year=2023,
            author=self.author
        )

        # URLs
        self.list_url = reverse('book-list')
        self.detail_url = reverse('book-detail', args=[self.book.id])
        self.create_url = reverse('book-create')
        self.update_url = reverse('book-update')
        self.delete_url = reverse('book-delete')

    # --- LIST TEST ---
    def test_list_books(self):
        response = self.client.get(self.list_url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertIn('Test Book', str(response.data))

    # --- DETAIL TEST ---
    def test_retrieve_book(self):
        response = self.client.get(self.detail_url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['title'], "Test Book")

    # --- CREATE TEST (requires authentication) ---
    def test_create_book_authenticated(self):
        self.client.login(username="testuser", password="testpass")
        data = {
            "title": "New Book",
            "publication_year": 2022,
            "author": self.author.id
        }
        response = self.client.post(self.create_url, data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Book.objects.count(), 2)

    def test_create_book_unauthenticated(self):
        data = {
            "title": "No Auth Book",
            "publication_year": 2021,
            "author": self.author.id
        }
        response = self.client.post(self.create_url, data)
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

    # --- UPDATE TEST (requires authentication) ---
    def test_update_book_authenticated(self):
        self.client.login(username="testuser", password="testpass")
        data = {
            "id": self.book.id,
            "title": "Updated Book"
        }
        response = self.client.put(self.update_url, data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.book.refresh_from_db()
        self.assertEqual(self.book.title, "Updated Book")

    def test_update_book_unauthenticated(self):
        data = {
            "id": self.book.id,
            "title": "Fail Update"
        }
        response = self.client.put(self.update_url, data)
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

    # --- DELETE TEST (requires authentication) ---
    def test_delete_book_authenticated(self):
        self.client.login(username="testuser", password="testpass")
        data = {"id": self.book.id}
        response = self.client.delete(self.delete_url, data)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(Book.objects.count(), 0)

    def test_delete_book_unauthenticated(self):
        data = {"id": self.book.id}
        response = self.client.delete(self.delete_url, data)
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

    # --- FILTER TEST ---
    def test_filter_books_by_title(self):
        response = self.client.get(f"{self.list_url}?title=Test Book")
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertIn('Test Book', str(response.data))

    # --- SEARCH TEST ---
    def test_search_books(self):
        response = self.client.get(f"{self.list_url}?search=Test")
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertIn('Test Book', str(response.data))

    # --- ORDERING TEST ---
    def test_order_books_by_publication_year(self):
        Book.objects.create(
            title="Older Book",
            publication_year=2000,
            author=self.author
        )
        response = self.client.get(f"{self.list_url}?ordering=publication_year")
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data[0]['title'], "Older Book")
