
from Statistics.Variance import Variance
from Statistics.Standarddeviation import Standarddeviation
class Samplecorrelation():
    @staticmethod
    def samplecorrelation (data):
        var= Variance.variance(data)
        std= Standarddeviation.standarddeviation(data)
        return var/std
