from DescriptiveStatictics.zsc import Zsc
from PopulationSampling.marginOfError import MarginOfError
from DescriptiveStatictics.populationProportion import PopulationProportion
from MathOperations.exponent import Exponent
from MathOperations.subtraction import Subtraction


class Cochran:
    @staticmethod
    def cochran(data, seeds, nums):
        ZScore = Zsc.zsc(seeds,data)
        pp = PopulationProportion.populationPorportion(seeds, nums, data)
        MarOfError = MarginOfError.marginOfError(seeds, data)
        sub = Subtraction.difference(1, pp)
        cochran = (Exponent.exponent(ZScore, 2) * pp * sub) / Exponent.exponent(MarOfError, 2)
        return cochran