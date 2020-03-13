from DescriptiveStatictics.mean import Mean
from DescriptiveStatictics.stddev import Stddev
from RNG.listPick import ListPick


class Zsc:
    @staticmethod
    def zsc(seed, data):
        X = ListPick.listPickSeed(seed, data)
        mean = Mean.mean(data)
        stddev = Stddev.stddev(data)
        return (X - mean) / stddev
