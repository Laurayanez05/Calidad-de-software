import unittest
from ejercicios import divide

class TestDivide(unittest.TestCase):
    def test_4(self):
        a = 1
        b = 1
        result = divide(a, b)
        self.assertEqual(1, result)

if __name__ == "__main__":
    unittest.main()
