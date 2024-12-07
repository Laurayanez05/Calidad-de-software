import unittest
from ejercicios import max

class TestMax(unittest.TestCase):
    def test_8(self):
        result = max([1, 10])
        self.assertGreater(result, 2)

if __name__ == "__main__":
    unittest.main()
