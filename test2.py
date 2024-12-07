import unittest
from ejercicios import addit

class TestAddit(unittest.TestCase):
    def test_2(self):
        x = 1
        result = addit(x)
        self.assertEqual(6, result)

if __name__ == "__main__":
    unittest.main()
