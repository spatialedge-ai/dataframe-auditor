import metrics
import response


"""
take a pandas series and extract stats according to column type
"""


def numeric(series):
    stats = response.Numeric()
    stats.attr = series.name
    stats.mean = series.mean()
    stats.std = series.std()
    stats.variance = series.var()
    stats.min = series.min()
    stats.max = series.max()
    stats.range = stats.max - stats.min
    stats.median, stats.iqr = metrics.median_iqr(series)
    stats.kurtosis = series.kurt()
    stats.skewness = series.skew()
    # todo change responses object after first order solution to contain this logic - how it computes itself
    #stats['kl_divergence'] = measures.kullback_leibler_divergence()
    # the mean absolute deviation is around the mean here
    stats.mad = series.mad()
    stats.p_zeros = '{0:.2f}'.format(float(series[series == 0].count()) / len(series.index) * 100)
    stats.p_nan = '{0:.2f}'.format(float(series.isna().sum()) / len(series.index) * 100)

    return stats


def string(series, head=3):
    # Only run if at least 1 non-missing value
    stats = dict()
    stats['attr'] = series.name
    stats['type'] = 'STRING'
    value_counts = series.value_counts(dropna=False)
    distinct = value_counts.count()
    stats['distinct'] = distinct
    stats['freq'] = list()
    print(value_counts.index[0:head].values, value_counts.iloc[0:head].values)
    for n, v in zip(value_counts.index[0:head], value_counts.iloc[0:head].values):
        print(n, v)
        stats['freq'].append({'name': n, 'value': v})
    return stats


