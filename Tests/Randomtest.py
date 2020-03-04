import unittest
from random import seed, randint

from RandomLib.Nnumber import nNumber
from RandomLib.Nnumberseed import nNumberseed
from RandomLib.Noseedrange import Noseed
from RandomLib.Ranlist import RanList
from RandomLib.Seedrange import Withseed
from RandomLib.Selectitem import SelectRan
from RandomLib.Selectseed import SeedSelect

class MyTestCase(unittest.TestCase):
    def setUp(self) -> None:
        self.seed= seed(5)
        self.aList = randint[1,2,3,4,5,0]

    def test_ranint(self):
        result = nNumber.nnumber(0, 5)
        self.assertEqual(isinstance(result, int), True)

    def test_nnumberseed(self):
        result = nNumberseed.nnumberseed(0, 5)
        self.assertEqual(isinstance(result, float), True)

    def testSeed_Int(self):
        result = nNumber.randomInt(1, 0, 5)
        self.assertEqual(result)

    def testSeed_Float(self):
        result = nNumber.randomInt(1, 0, 5)
        self.assertEqual(result)

    def test_Ints(self):
        result = nNumber.ran_list(0, 10, 10, 3)
        self.assertEqual(result, [3, 9, 8, 2, 5, 9, 7, 10, 9, 1])
