from DescriptiveStatictics.stddev import Stddev
from DescriptiveStatictics.zsc import Zsc


class MarginOfError:
    @staticmethod
    def marginOfError(seed, data):
        zsc = Zsc.zsc(seed, data)
        stddev = Stddev.stddev(data)
        return zsc * stddev