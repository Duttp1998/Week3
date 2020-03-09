from Statistics.Standarddeviation import Standarddeviation
from Statistics.Zscore import Zscore
import math
class Marginoferror():
    @staticmethod
    def marginoferror (data):
        std=Standarddeviation.standarddeviation(data)
        z= Zscore.zscore(data)
        a= std*z
        return a
