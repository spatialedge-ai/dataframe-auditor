import logging
import dfauditor.metrics
import dfauditor.response
import pandas as pd

import dfauditor.app_logger

log = dfauditor.app_logger.get(log_level=logging.INFO)

"""
take a pandas series and extract stats according to column type
"""


# def _get_strings_array(sdf: SparkDataFrame) -> list:
#     """
#     Get an array of column names for columns that are strings in a Spark DataFrame
#     :param sdf: A Spark DataFrame
#     :return: A list of string attributes
#     """
#     attribute_list = list()
#     for elem in sdf.schema:
#         if elem.jsonValue()['type'] == 'string':
#             attribute_list.append(elem.name)
#     attribute_list = [x.lower() for x in attribute_list]
#     attribute_list.sort()
#     return attribute_list
#
#
# def _get_numbers_array(sdf: SparkDataFrame) -> list:
#     """
#     Get an array of column names for columns that are numbers in a Spark DataFrame
#     :param sdf: A Spark DataFrame
#     :return: A list of numerical attributes
#     """
#     attribute_list = list()
#     for elem in sdf.schema:
#         if elem.jsonValue()['type'] in {'byte', 'short', 'integer', 'long', 'bigint', 'float', 'double'} or elem.jsonValue()['type'].startswith('decimal'):
#             attribute_list.append(elem.name)
#     attribute_list = [x.lower() for x in attribute_list]
#     attribute_list.sort()
#     return attribute_list


def numeric(series):
    stats = dfauditor.response.Numeric()
    stats.attr = series.name
    stats.mean = series.mean()
    stats.std = series.std()
    stats.variance = series.var()
    stats.min = series.min()
    stats.max = series.max()
    stats.range = stats.max - stats.min
    stats.median, stats.iqr = dfauditor.metrics.median_iqr(series)
    stats.kurtosis = series.kurt()
    stats.skewness = series.skew()
    # todo change responses object after first order solution to contain this logic - how it computes itself
    # stats['kl_divergence'] = measures.kullback_leibler_divergence()
    # the mean absolute deviation is around the mean here
    stats.mad = series.mad()
    stats.p_zeros = float(series[series == 0].count()) / len(series.index) * 100
    stats.p_nan = float(series.isna().sum()) / len(series.index) * 100
    # todo - leave this here for __str__ of the eventual object
    # stats.p_zeros = '{0:.2f}'.format()
    # stats.p_nan = '{0:.2f}'.format()

    return stats


def string(series, head=3):
    # Only run if at least 1 non-missing value
    stats = dfauditor.response.String()
    stats.attr = series.name
    value_counts = series.value_counts(dropna=False)
    distinct = value_counts.count()
    stats.distinct = distinct
    for n, v in zip(value_counts.index[0:head], value_counts.iloc[0:head].values):
        stats.freq.append({'name': n, 'value': v})
    return stats


def decile_bins(series):
    stats = dfauditor.response.DecileBins()
    bins = pd.cut(series, 10)
    bins = pd.DataFrame(bins)
    stats.attr = series.name
    stats.perc_1 = bins.groupby(series.name).size()[1]
    stats.perc_2 = bins.groupby(series.name).size()[2]
    stats.perc_3 = bins.groupby(series.name).size()[3]
    stats.perc_4 = bins.groupby(series.name).size()[4]
    stats.perc_5 = bins.groupby(series.name).size()[5]
    stats.perc_6 = bins.groupby(series.name).size()[6]
    stats.perc_7 = bins.groupby(series.name).size()[7]
    stats.perc_8 = bins.groupby(series.name).size()[8]
    stats.perc_9 = bins.groupby(series.name).size()[9]
    stats.perc_10 = bins.groupby(series.name).size()[10]

    return stats
