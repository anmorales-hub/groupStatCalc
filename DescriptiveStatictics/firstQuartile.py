import numpy as np


class FirstQuartiles:

    @staticmethod
    def firstQuartile(data):
        q1 = np.percentile(data, [25])
        return q1
