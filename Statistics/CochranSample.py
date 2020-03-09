import statistics
import random
from Statistics.Zscore import Zscore
from Statistics.Marginoferror import Marginoferror

class CochranSample:
    @staticmethod
    def cohransample(data):
        z= Zscore.zscore(data)
        m= Marginoferror.marginoferror(data)
        p= 15

        final= (1-p*z)/(m)

        return final


