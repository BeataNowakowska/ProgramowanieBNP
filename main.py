import unittest
from sort_test import TestBubbleSort

# Uruchomienie testów
if __name__ == '__main__':
  suite = unittest.TestLoader().loadTestsFromTestCase(TestBubbleSort)
  unittest.TextTestRunner().run(suite)
