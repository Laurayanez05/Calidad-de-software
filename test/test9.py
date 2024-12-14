import unittest
from ejercicios import even_numbers

class TestEvenNumbers(unittest.TestCase):
    def test_9(self):
        res = even_numbers([2, 4, 3])
        self.assertGreater(len(res), 1)

if __name__ == "__main__":
    unittest.main()
