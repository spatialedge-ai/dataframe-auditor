class StatsResponse(object):

    def __init__(self):
        self.__dict__.update(dict().fromkeys({'attr', 'type'}))


class Numeric(StatsResponse):

    def __init__(self):
        super(Numeric, self).__init__()
        self.__dict__.update(dict().fromkeys(
            {'mean', 'std', 'variance',
             'min', 'max', 'range', 'kurtosis', 'skewness',
             'mad', 'p_zeros', 'p_nan', 'median', 'iqr'
             }
        ))
        self.type = 'NUMERIC'


class String(StatsResponse):

    def __init__(self):
        super(String, self).__init__()
        self.__dict__.update(dict().fromkeys(
            {'distinct', 'freq'}
        ))
        self.type = 'STRING'
        self.freq = list()


class DecileBins(StatsResponse):
    def __init__(self):
        super(Numeric, self).__init__()
        self.__dict__.update(dict().fromkeys(
            {'1_perc', '2_perc', '3_perc',
             '4_perc', '5_perc', '6_perc', '7_perc', '8_perc',
             '9_perc', '10_perc'
             }
        ))
        self.type = 'NUMERIC'
