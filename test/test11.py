import unittest
from ejercicios import is_even

class TestIsEven(unittest.TestCase):
    def test_11(self):
        result = is_even(2)
        self.assertTrue(result)

if __name__ == "__main__":
    unittest.main()
