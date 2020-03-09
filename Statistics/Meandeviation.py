
import numpy as np


class Meandeviation():
    @staticmethod
    def meandeviation (data):
        return np.mean(np.absolute(data - np.mean(data)))

#https://www.geeksforgeeks.org/absolute-deviation-and-absolute-mean-deviation-using-numpy-python/