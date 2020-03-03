import unittest
from random import random

from DescriptiveStatictics.mean import Mean
from DescriptiveStatictics.median import Median
from DescriptiveStatictics.mode import Mode


class MyTestCase(unittest.TestCase):

    def setUp(self) -> None:
        self.test = [1, 2, 3, 4, 5]
        self.test1 = [1, 2, 2, 3, 4]
        self.test2 = [1, 2, 3]

    def test_Mean(self):
        self.assertEqual(3, Mean.mean(self.test))

    def test_mode(self):
        self.assertEqual(2, Mode.mode(self.test1))

    def test_median(self):
        self.assertEqual(2, Median.median(self.test2))


if __name__ == '__main__':
    unittest.main()
