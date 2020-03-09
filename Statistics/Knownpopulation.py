from Statistics.Zscore import Zscore
from Statistics.Marginoferror import Marginoferror
from Statistics.Standarddeviation import Standarddeviation

class Knownpopulation():
    @staticmethod
    def knownpopulation(data):
        z = Zscore.zscore(data)
        m = Marginoferror.marginoferror(data)
        std = Standarddeviation.standarddeviation(data)
        val = ((z * std) /m)**2

        return val