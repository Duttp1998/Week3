from Statistics.Zscore import Zscore
from Statistics.Marginoferror import Marginoferror
from Statistics.Standarddeviation import Standarddeviation

class Unknownpopulation():
    @staticmethod
    def unknownpopulation(data):
        z = Zscore.zscore(data)
        m = Marginoferror.marginoferror(data)
        std = Standarddeviation.standarddeviation(data)
        val = (z/m)*std*100

        return val