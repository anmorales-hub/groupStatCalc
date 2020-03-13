from DescriptiveStatictics.stddev import Stddev
from RNG.listPick import ListPick
from DescriptiveStatictics.covariance import Covariance


class SampleCorrelation:
    @staticmethod
    def samplecorrelation(seed, sample_size, data1, data2):
        dataA = ListPick.listPickListSeed(seed, sample_size, data1)
        dataB = ListPick.listPickListSeed(seed, sample_size, data2)

        return Covariance.covariance(dataA, dataB) / (Stddev.stddev(dataA) * Stddev.stddev(dataB))
