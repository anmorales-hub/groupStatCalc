import numpy as np


class ThirdQuartiles:

    @staticmethod
    def thirdQuartile(data):
        q3 = np.percentile(data, [75])
        return q3