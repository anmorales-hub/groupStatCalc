import unittest
from random import random

from DescriptiveStatictics.mean import Mean
from DescriptiveStatictics.median import Median
from DescriptiveStatictics.mode import Mode
from DescriptiveStatictics.variance import Variance
from DescriptiveStatictics.stddev import Stddev
from DescriptiveStatictics.firstQuartile import FirstQuartiles
from DescriptiveStatictics.secondQuartile import SecondQuartiles
from DescriptiveStatictics.thirdQuartile import ThirdQuartiles


class MyTestCase(unittest.TestCase):

    def setUp(self) -> None:
        self.test = [1, 2, 3, 4, 5]
        self.test1 = [1, 2, 2, 3, 4]
        self.test2 = [1, 2, 3]
        self.test3 = [1, 2, 3, 4, 5, 6, 7]

    def test_Mean(self):
        self.assertEqual(3, Mean.mean(self.test))

    def test_mode(self):
        self.assertEqual(2, Mode.mode(self.test1))

    def test_median(self):
        self.assertEqual(2, Median.median(self.test2))
    def test_variance(self):
        self.assertEqual(2, Variance.variance(self.test))

    def test_stddev(self):
        self.assertEqual(1.4142135623731, Stddev.stddev(self.test))

    def test_firstQuartile(self):
        self.assertEqual(2, FirstQuartiles.firstQuartile(self.test3))

    def test_secondQuartile(self):
        self.assertEqual(4, SecondQuartiles.secondQuartile(self.test3))

    def test_thirdQuartile(self):
        self.assertEqual(6, ThirdQuartiles.thirdQuartile(self.test3))


if __name__ == '__main__':
    unittest.main()
