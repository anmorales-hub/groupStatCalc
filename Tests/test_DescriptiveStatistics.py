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
from DescriptiveStatictics.meanDeviation import MeanDeviation
from DescriptiveStatictics.covariance import Covariance
from DescriptiveStatictics.populationcorrelation import PopulationCorrelation
from DescriptiveStatictics.skewness import Skewness
from DescriptiveStatictics.zsc import Zsc
from DescriptiveStatictics.samplecorrelation import SampleCorrelation
from DescriptiveStatictics.populationProportion import PopulationProportion


class MyTestCase(unittest.TestCase):

    def setUp(self) -> None:
        self.test = [1, 2, 3, 4, 5]
        self.test1 = [1, 2, 2, 3, 4]
        self.test2 = [1, 2, 3]
        self.test3 = [1, 2, 3, 4, 5, 6, 7]
        self.test4 = [1, 2, 3, 4, 5, 6]
        self.test5 = [1, 2, 3, 3, 3, 4, 5]

    def test_Mean(self):
        self.assertEqual(3, Mean.mean(self.test))

    def test_mode(self):
        self.assertEqual(2, Mode.mode(self.test1))

    def test_median(self):
        self.assertEqual(2, Median.median(self.test2))

    def test_variance(self):
        self.assertEqual(2, Variance.variance(self.test))

    def test_stddev(self):
        self.assertEqual(1.5811388300841898, Stddev.stddev(self.test))

    def test_firstQuartile(self):
        self.assertEqual(2.5, FirstQuartiles.firstQuartile(self.test3))

    def test_secondQuartile(self):
        self.assertEqual(4, SecondQuartiles.secondQuartile(self.test3))

    def test_thirdQuartile(self):
        self.assertEqual(5.5, ThirdQuartiles.thirdQuartile(self.test3))

    def test_meanDeviation(self):
        self.assertEqual(1.5, MeanDeviation.meanDeviation(self.test4))

    def test_covariance(self):
        covariance = Covariance.covariance(self.test, self.test1)
        self.assertEqual(covariance, 1.75)

    def test_populationcorrelation(self):
        result = PopulationCorrelation.populationcorrelation(self.test4, self.test4)
        self.assertEqual(result, 1)

    def test_skewness(self):
        self.assertEqual(0, Skewness.skewness(self.test5))
        
    def test_zsc(self):
        zsc = Zsc.zsc(1, self.test)
        self.assertEqual(zsc, -1.3228756555322954)
        
    def test_sampleCorrelation(self):
        self.assertEqual(1.0000000000000002, SampleCorrelation.samplecorrelation(2, 5, self.test4, self.test4))
        
    def test_populationProportion(self):
        result = PopulationProportion.populationPorportion(data=self.test1, nums=6, seeds=4)
        self.assertEqual(result, 0.75)





if __name__ == '__main__':
    unittest.main()
