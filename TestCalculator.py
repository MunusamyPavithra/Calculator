import unittest
from Calculator import add, subtract

class CalculatorTests(unittest.TestCase):
    def test_add(self):
      self.assertEqual(add(3, 2), 5)

    def test_addFailure(self):
        self.assertEqual(add(3, 2), 6)

    def test_subtract(self):
        self.assertEqual(subtract(5, 2), 3)

if __name__ == '__main__':
    unittest.main()

