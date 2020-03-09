import statistics

from Statistics import Mean
from Statistics.Zscore import Zscore
import math
class Confidenceinterval:
    @staticmethod
    def confidenceinterval(data):
        mean= Mean.mean(data)
        z= Zscore.zscore(data)
        stande= mean/z
        final= mean + stande
        final2= final *3
        return (final,final2)



