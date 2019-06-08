


def median_iqr(series):
    iqr_median = [.25, .5, .75]
    series = series.quantile(iqr_median)
    stats = {}
    # stats['q1'] = series.iloc[0]
    # stats['q3'] = series.iloc[2]
    stats['iqr'] = series.iloc[2] - series.iloc[0]
    stats['median'] = series.iloc[1]
    return stats