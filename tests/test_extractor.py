import unittest

import numpy as np
import pandas as pd

import extractor
import response


class TestExtractorNumeric(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        numeric_data = {
            'x': [50, 50, -10, 0, 0, 5, 15, -3, None, 0],
            'y': [0.00001, 256.128, None, 16.32, 2048, -3.1415926535, 111, 2.4, 4.8, 0.0],
            'trivial': [1]*10
        }
        cls.numeric_df = pd.DataFrame(numeric_data)
        cls.mixed_df = None

    def test_trivial(self):
        resp = extractor.numeric(self.numeric_df.trivial)
        expected = response.Numeric()
        expected.__dict__ = {'attr': 'trivial',
                             'type': 'NUMERIC',
                             'median': 1.0,
                             'variance': 0.0,
                             'std': 0.0,
                             'max': 1,
                             'min': 1,
                             'mad': 0.0,
                             'p_zeros': 0.0,
                             'kurtosis': 0,
                             'skewness': 0,
                             'iqr': 0.0,
                             'range': 0,
                             'p_nan': 0.0,
                             'mean': 1.0}
        self.assertEqual(resp.__dict__, expected.__dict__)

    def test_nans(self):
        """
        confirm that nans are adequately counted
        :return:
        """
        df_nan = self.numeric_df.trivial.copy()
        # unlike `at`, `loc` changes the int type column to float (there is no NaN in panda-land float)
        df_nan.loc[5] = np.nan
        resp = extractor.numeric(df_nan)
        self.assertAlmostEqual(10.0, resp.p_nan)

        # this should agree with None too
        df_none = self.numeric_df.trivial.copy()
        df_none.loc[5] = None
        df_none.loc[4] = None
        resp = extractor.numeric(df_none)
        self.assertAlmostEqual(20.0, resp.p_nan)


class TestExtractorString(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        data = {
            'trivial': ['a'] * 10,
            'mix': ['a'] * 3 + ['b'] * 2 + ['c'] + [None] * 4
        }
        cls.df = pd.DataFrame(data)

    def test_trivial(self):
        resp = extractor.string(self.df.trivial)
        self.assertEqual(resp.distinct, 1)
        self.assertEqual(resp.freq[0]['value'], 10)

    def test_mix(self):
        resp = extractor.string(self.df.mix)
        expected = response.String()
        expected.__dict__.update({'attr': 'mix',
                                  'type': 'STRING',
                                  'distinct': 4,
                                  'freq': [{'name': np.nan, 'value': 4},
                                           {'name': 'a', 'value': 3},
                                           {'name': 'b', 'value': 2}]})
        self.assertEqual(resp.__dict__, expected.__dict__)