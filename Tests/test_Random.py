import unittest
from RNG.randNum import RandNum
from RNG.randList import RandList

class MyTestCase(unittest.TestCase):

    def setUp(self) -> None:
        self.test = [0, 1, 2, 3, 4]

    def test_randNum(self):
        result = RandNum.randNum(0, 5)
        self.assertEqual(int, type(result))

    def test_randNumSeed(self):
        result1 = RandNum.randNumSeed(5, 0, 20)
        result2 = RandNum.randNumSeed(5, 0, 20)
        self.assertEqual(True, result1 == result2)

    def test_randFloat(self):
        result = RandNum.randFloat(0, 10)
        self.assertEqual(float, type(result))

    def test_randFloatSeed(self):
        result1 = RandNum.randFloatSeed(5, 0, 20)
        result2 = RandNum.randFloatSeed(5, 0, 20)
        self.assertEqual(True, result1 == result2)

    def test_randNumList(self):
        result1 = RandList.randList(1, 5, 0, 5)
        result2 = RandList.randList(1, 5, 0, 5)
        self.assertEqual(True, result1 == result2)

    def test_randFloatList(self):
        result1 = RandList.randList(1, 5, 0, 5)
        result2 = RandList.randList(1, 5, 0, 5)
        self.assertEqual(True, result1 == result2)

if __name__ == '__main__':
    unittest.main()