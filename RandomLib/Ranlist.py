import random
from RandomLib.Noseedrange import Noseed
from RandomLib.Seedrange import Withseed

class RanList:
    @staticmethod
    def ran_list(a,b,digit,seed):
        list1=[]
        list2=[]

        while len(list1) != digit:
            list1.append(Withseed.Ranfloatseed(a,b,seed))
            list2.append(Withseed.RanInt(a,b,seed))

            if len(list1,list2) == digit:
                break

        return list1
        return list2



