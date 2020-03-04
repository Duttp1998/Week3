import random

class SelectRan():
    @staticmethod
    def Select(list1, list2):
        selectitem1 = random.choice(list1)
        selectitem2 = random.choice(list2)
        return selectitem1, selectitem2

