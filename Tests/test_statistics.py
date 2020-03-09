import unittest
from numpy.random import seed
from numpy.random import randint

from Statistics.Unknownpopulation import Unknownpopulation
from Statistics.Skewness import Skewness
from Statistics.Statistics import Statistics
from Statistics.Median import Median
from Statistics.Mode import Mode
from Statistics.Variance import Variance
from Statistics.Standarddeviation import Standarddeviation
from Statistics.Zscore import Zscore
from Statistics.Meandeviation import Meandeviation
from Statistics.Quartiles import Quartiles
from Statistics.Samplecorrelation import Samplecorrelation
from Statistics.Marginoferror import Marginoferror
from Statistics.Confidenceinterval import Confidenceinterval
from Statistics.CochranSample import CochranSample
from Statistics.Knownpopulation import Knownpopulation

class MyTestCase(unittest.TestCase):
    def setUp(self) -> None:
        seed(5)
        self.testData = randint(10, 20, 30)
        self.statistics = Statistics()

    def test_instantiate_calculator(self):
        self.assertIsInstance(self.statistics, Statistics)

    def test_mean_calculator(self):
        mean = self.statistics.mean(self.testData)
        self.assertEqual(mean, 14.233333333333333)

    def test_median_calculator(self):
        median = Median.median(self.testData)
        self.assertEqual(median, 14.5)

    def test_mode_calculator(self):
        mode = Mode.mode(self.testData)
        self.assertEqual(mode, 10)

    def test_variance_calculator(self):
        variance = Variance.variance(self.testData)
        self.assertEqual(variance, 11)

    def test_skewness_calculator(self):
        skew = Skewness.skewness(self.testData)
        self.assertEqual(skew, 0.03576490724804414)

    def test_standarddeviation_calculator(self):
        standard = Standarddeviation.standarddeviation(self.testData)
        self.assertEqual(standard, 3.3166247903554)

    def test_quartiles_calculator(self):
        quart = Quartiles.quartiles(self.testData)
        self.assertEqual(quart, (11.0, 14.5, 17.0))

    def test_zscore_calculator(self):
        zscore = Zscore.zscore(self.testData)
        self.assertEqual(zscore, -1.276398025379199)

    def test_meandeviation_calculator(self):
        meand = Meandeviation.meandeviation(self.testData)
        self.assertEqual(meand, 3.033333333333333)

    def test_samplecorrelation_calculator(self):
        samplec = Samplecorrelation.samplecorrelation(self.testData)
        self.assertEqual(samplec, 3.3166247903554)

    def test_marginoferror_calculator(self):
        margine = Marginoferror.marginoferror(self.testData)
        self.assertEqual(margine, -4.2333333333333325)

    def test_ConfidenceInterval_calculator(self):
        confidence = Confidenceinterval.confidenceinterval(self.testData)
        self.assertEqual(confidence, (3.0821617941069075,9.246485382320722))

    def test_Cochransample_calculator(self):
        cochran = CochranSample.cohransample(self.testData)
        self.assertEqual(cochran, -4.758890641107399)

    def test_knownpopulation_calculator(self):
        known = Knownpopulation.knownpopulation(self.testData)
        self.assertEqual(known, 1.0)

    def test_unknownpopulation_calculator(self):
        unknown = Unknownpopulation.unknownpopulation(self.testData)
        self.assertEqual(unknown, 100.0)


if __name__ == '__main__':
    unittest.main()
