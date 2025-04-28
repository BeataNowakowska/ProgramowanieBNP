# Klasa testująca
import unittest
from sort import bubble_sort


class TestBubbleSort(unittest.TestCase):

    def test_sorted(self):
        self.assertEqual(bubble_sort([5, 3, 1, 4, 2]), [1, 2, 3, 4, 5])


# Uruchomienie testów
if __name__ == '__main__':
    unittest.main()
