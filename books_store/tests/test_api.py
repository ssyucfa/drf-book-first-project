from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase

from books_store.models import Book
from books_store.serializers import BookSerializer


class BookViewTestCase(APITestCase):
    def test_list(self):
        book1 = Book.objects.create(name='1', price=2)
        book2 = Book.objects.create(name='2', price=3)

        url = reverse('book-list')
        response = self.client.get(url)

        data = BookSerializer([book1, book2], many=True).data

        self.assertEqual(status.HTTP_200_OK, response.status_code)
        self.assertEqual(response.data, data)
