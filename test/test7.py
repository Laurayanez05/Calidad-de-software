import unittest
from ejercicios import remove_letter

class TestRemoveLetter(unittest.TestCase):
    def test_7(self):
        resul = remove_letter("o", "ola")
        self.assertEqual("la", resul)

if __name__ == "__main__":
    unittest.main()
