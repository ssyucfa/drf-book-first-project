from django.test import TestCase

from books_store.models import Book
from books_store.serializers import BookSerializer


class BookSerializerTestCase(TestCase):
    def test_serializer(self):
        book1 = Book.objects.create(name='1', price=2)
        book2 = Book.objects.create(name='2', price=3)

        data = BookSerializer([book1, book2], many=True).data

        expected_data = [
            {
              'id': book1.id,
              'name': '1',
              'price': '2.00'
            },
            {
                'id': book2.id,
                'name': '2',
                'price': '3.00'
            },
        ]

        self.assertEqual(expected_data, data)