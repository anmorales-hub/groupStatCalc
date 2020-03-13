from MathOperations.exponent import Exponent
from MathOperations.division import Division
from MathOperations.subtraction import Subtraction
from DescriptiveStatictics.zsc import Zsc
from PopulationSampling.marginOfError import MarginOfError


class UnknownPopulationStdev:
    @staticmethod
    def unknownPopulationStdev(seed, data, percent):
        ZScore = Zsc.zsc(seed, data)
        MarOfError = MarginOfError.marginOfError(seed, data)
        p = percent
        q = Subtraction.difference(1, p)
        pq = Division.division(ZScore, MarOfError)
        samplePopulation = Exponent.exponent(pq, 2) * p * q

        return samplePopulation