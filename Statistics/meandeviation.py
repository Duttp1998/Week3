import pandas as pd
import numpy as np
from numpy import mean, absolute

class madt():
    @staticmethod
    def meanabsdev(data):
        df = pd.DataFrame(data)
        df.mad()

# https://www.geeksforgeeks.org/absolute-deviation-and-absolute-mean-deviation-using-numpy-python/