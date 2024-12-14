import unittest
from ejercicios import reverse

class TestReverse(unittest.TestCase):
    def test_6(self):
        result = reverse("ola")
        self.assertNotEqual("ola", result)

if __name__ == "__main__":
    unittest.main()
