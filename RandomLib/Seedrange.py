import random
from random import seed

class Withseed():

    @staticmethod
    def Ranfloatseed(a,b,seed):
        random.seed(seed)
        return Withseed.Ranfloatseed(a,b)


    @staticmethod
    def RanInt(a,b,seed):
        random.seed(seed)
        return Withseed.RanInt(a,b)