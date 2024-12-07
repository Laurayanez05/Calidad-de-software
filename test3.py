import unittest
from ejercicios import mult

class TestMult(unittest.TestCase):
    def test_3(self):
        x = 2
        reultad = mult(x)
        self.assertNotEqual(2, reultad)
        self.assertEqual(14, reultad)

if __name__ == "__main__":
    unittest.main()
