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
        super(DecileBins, self).__init__()
        self.__dict__.update(dict().fromkeys(
            {'attr','perc_1', 'perc_2', 'perc_3',
             'perc_4', 'perc_5', 'perc_6', 'perc_7', 'perc_8',
             'perc_9', 'perc_10'
             }
        ))
        self.type = 'NUMERIC'
