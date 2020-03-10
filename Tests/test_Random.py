import unittest
from RNG.randNum import RandNum

class MyTestCase(unittest.TestCase):

    def setUp(self) -> None:
        self.test = [0, 1, 2, 3, 4]

    def test_randNum(self):
        result = RandNum.randNum(0, 10)
        self.assertEqual(int, type(result))

    def test_randNumSeed(self):
        result1 = RandNum.randNumSeed(4, 0, 10)
        result2 = RandNum.randNumSeed(4, 0, 10)
        self.assertEqual(True, result1 == result2)

    def test_randFloat(self):
        result = RandNum.randFloat(0, 10)
        self.assertEqual(float, type(result))

    def test_randFloatSeed(self):
        result1 = RandNum.randFloatSeed(4, 0, 10)
        result2 = RandNum.randFloatSeed(4, 0, 10)
        self.assertEqual(True, result1 == result2)


if __name__ == '__main__':
    unittest.main()