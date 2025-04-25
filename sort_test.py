# Klasa testująca
import unittest
from sort import bubble_sort


class TestBubbleSort(unittest.TestCase):

    def test_sorted(self):
        self.assertEqual(bubble_sort([5, 3, 1, 4, 2]), [1, 2, 3, 4, 5])

    def test_empty(self):
        self.assertEqual(bubble_sort([]), [])

    def test_negative_numbers(self):
        self.assertEqual(bubble_sort([-2, -5, -1]), [-5, -2, -1])

    def test_duplicates(self):
        self.assertEqual(bubble_sort([3, 1, 2, 3]), [1, 2, 3, 3])


# Uruchomienie testów
if __name__ == '__main__':
    unittest.main()
