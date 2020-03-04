from Statistics.standarddeviation import standard
from Statistics.zscore import zScore

class marginerror():
    def mar( seed,data):
        zscore= zScore.zscOre(seed,data)
        std= standard.stdveiance(data)
        return zscore*std