import unittest

import numpy as np
import scipy.stats
import pandas as pd

import dfauditor.measures


class TestKLDivergence(unittest.TestCase):
    """
    This is currently a thin wrapper around the stats.entropy function,
    but the basic expectations of what is computed are verified here.
    """

    def test_equality(self):
        """
        expectation is that a reference distribution with itself has zero divergence
        :return:
        """
        x_axis = np.arange(-10, 10, 0.01)
        # Mean = 0, SD = 2.
        dist = pd.DataFrame(scipy.stats.norm.pdf(x_axis, 0, 2))
        self.assertAlmostEqual(dfauditor.measures.kullback_leibler_divergence(dist, dist), 0.0)
