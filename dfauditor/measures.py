import scipy.stats
import pandas as pd


def kullback_leibler_divergence(p_df, q_df):
    """
    A thin wrapper deriving the KLD (to allow switching
    out and layer abstraction)
    :param p_df: a dataframe representing the 'true' distribution or reference distribution (discrete)
    :param q_df: a dataframe on the same probability space representing an approximation of p_df
    :return: the divergence in [0,1]
    """
    if not (isinstance(p_df, pd.DataFrame) and isinstance(q_df, pd.DataFrame)):
        raise NotImplementedError('')
    return scipy.stats.entropy(p_df, q_df)


def median_iqr(series):
    """
    The interquartile range (Q3-Q1) and median are computed on a pandas series
    :param df:
    :return:
    """
    iqr_median = [.25, .5, .75]
    series = series.quantile(iqr_median)
    iqr = series.iloc[2] - series.iloc[0]
    median = series.iloc[1]
    return median, iqr
