import pandas as pd
import measures


def numeric(series):
    """
    compute summary and descriptive statistics on a pandas series
    #TODO add the history component
    :param series: a pandas series
    :return: a dictionary with {'name': {metrics_i: x_i}}
    """
    stats = dict()
    stats[series.name] = dict()
    sub = stats[series.name]
    sub['type'] = 'NUMERIC'
    sub['mean'] = series.mean()
    sub['std'] = series.std()
    sub['variance'] = series.var()
    sub['min'] = series.min()
    sub['max'] = series.max()
    sub['range'] = sub['max'] - sub['min']
    sub['median'], sub['iqr'] = measures.median_iqr(series)
    sub['kurtosis'] = series.kurt()
    sub['skewness'] = series.skew()
    sub['sum'] = series.sum()
    # the mean absolute deviation is around the mean here
    sub['mad'] = series.mad()
    sub['n_zeros'] = len(series.index) - series[series == 0].count()
    sub['p_zeros'] = float(sub['n_zeros']) / len(series.index) * 100

    return stats



