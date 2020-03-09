from random import random
from Statistics import Mean
from Statistics.Standarddeviation import Standarddeviation

class Zscore:
    @staticmethod
    def zscore(data):
        value= 10
        u= Mean.mean(data)
        o= Standarddeviation.standarddeviation(data)
        formula= (value-u)/(o)
        return formula


