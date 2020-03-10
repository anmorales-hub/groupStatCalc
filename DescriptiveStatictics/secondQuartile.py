import numpy as np


class SecondQuartiles:

    @staticmethod
    def secondQuartile(data):
        q1 = np.percentile(data, [50])
        return q1