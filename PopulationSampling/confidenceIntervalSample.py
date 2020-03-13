from PopulationSampling.confidenceIntervalPopulation import ConfidenceIntervalPopulation
from PopulationSampling.simpRandSamp import SimpRandSamp


class ConfidenceIntervalSample:
    @staticmethod
    def confidenceIntervalSample(confidence, seed, nums, data):
        samp = SimpRandSamp.simpRandSamp(seed, nums, data)
        return ConfidenceIntervalPopulation.confidenceIntervalPopulation(confidence, samp)
