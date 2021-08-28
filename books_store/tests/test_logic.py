from django.test import TestCase

from books_store.logic import operations


class LogicTestCase(TestCase):
    def test_plus(self):
        result = operations(5, 5, '+')
        self.assertEqual(10, result)

    def test_minus(self):
        result = operations(5, 5, '-')
        self.assertEqual(0, result)

    def test_multiply(self):
        result = operations(5, 5, '*')
        self.assertEqual(25, result)
