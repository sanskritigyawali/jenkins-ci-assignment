import unittest
from app import add_numbers

class TestAddNumbers(unittest.TestCase):
  def test_add_numbers(self):
      self.assertEqual(add_numbers(2, 3), 6)

if __name__ == "__main__":
    unittest.main()
