import numpy as np

class quartiles():
    @staticmethod
    def Quar1(data):
        return np.quartile(data,[25])
    
    def Quar3(data):
        return np.quartile(data,[75])
