

def median_iqr(series):
    iqr_median = [.25, .5, .75]
    series = series.quantile(iqr_median)
    iqr = series.iloc[2] - series.iloc[0]
    median = series.iloc[1]
    return median, iqr
