import numpy as np
from scipy import stats

class zScore():
    @staticmethod
    def zscOre(data):
        return stats.zscore(data)