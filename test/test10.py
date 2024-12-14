import unittest
from ejercicios import odd_numbers

class TestOddNumbers(unittest.TestCase):
    def test_10(self):
        resut = odd_numbers([1, 2, 3, 4, 5])
        self.assertEqual(len(resut), 3)

if __name__ == "__main__":
    unittest.main()
