import random
from RandomLib.Selectitem import SelectRan

class SeedSelect():
        @staticmethod
        def seedselect(seed,list1,list2):
            random.seed(seed)

            return SelectRan.choice(list1), SeedSelect.choice(list2)



