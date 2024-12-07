import unittest
from ejercicios import total

class TestTotal(unittest.TestCase):
    def test_1(self):
        lst = [1, 2, 3, 4]
        resultado = total(lst)
        self.assertEqual(10, resultado)

if __name__ == "__main__":
    unittest.main()
