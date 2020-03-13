from PopulationSampling.confidenceIntervalPopulation import ConfidenceIntervalPopulation
from PopulationSampling.simpleRandSamp import SimpleRandSamp


class ConfidenceIntervalSample:
    @staticmethod
    def confidenceIntervalSample(confidence, seed, nums, data):
        samp = SimpleRandSamp.listPickListSeed(seed, nums, data)
        return ConfidenceIntervalPopulation.confidenceIntervalPopulation(confidence, samp)