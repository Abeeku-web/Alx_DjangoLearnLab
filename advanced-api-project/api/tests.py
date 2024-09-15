from django.test import TestCase
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from .models import Book, Author
from django.contrib.auth.models import User

class BookAPITestCase(APITestCase):

    def setUp(self):
        # Create test data
        self.author = Author.objects.create(name="Test Author")
        self.book = Book.objects.create(
            title="Test Book", publication_year=2023, author=self.author
        )
        self.user = User.objects.create_user(username="testuser", password="testpass")

    def test_list_books(self):
        url = reverse('book-list')
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)

    def test_create_book(self):
        url = reverse('book-list')
        data = {
            "title": "New Book",
            "publication_year": 2022,
            "author": self.author.id,
        }
        self.client.login(username="testuser", password="testpass")
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Book.objects.count(), 2)

    def test_update_book(self):
        url = reverse('book-detail', kwargs={'pk': self.book.pk})
        data = {
            "title": "Updated Test Book",
            "publication_year": 2021,
            "author": self.author.id,
        }
        self.client.login(username="testuser", password="testpass")
        response = self.client.put(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.book.refresh_from_db()
        self.assertEqual(self.book.title, "Updated Test Book")

    def test_delete_book(self):
        url = reverse('book-detail', kwargs={'pk': self.book.pk})
        self.client.login(username="testuser", password="testpass")
        response = self.client.delete(url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(Book.objects.count(), 0)

    def test_filter_books(self):
        url = reverse('book-list')
        response = self.client.get(f"{url}?publication_year=2023")
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)

    def test_search_books(self):
        url = reverse('book-list')
        response = self.client.get(f"{url}?search=Test Book")
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)

    def test_order_books(self):
        url = reverse('book-list')
        response = self.client.get(f"{url}?ordering=title")
        self.assertEqual(response.status_code, status.HTTP_200_OK)
