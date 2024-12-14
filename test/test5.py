import unittest
from ejercicios import length

class TestLength(unittest.TestCase):
    def test_5(self):
        res = length([2])
        self.assertEqual("Less than 5", res)

        res = length("JhonMarioOchoa")
        self.assertEqual("Longer than 5", res)

if __name__ == "__main__":
    unittest.main()
