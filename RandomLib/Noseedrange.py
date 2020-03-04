import random

class Noseed():

    @staticmethod
    def Ranfloat(a,b):
        return random.uniform(a, b)

    @staticmethod
    def RanInt(a,b):
        return random.randint(a,b)

