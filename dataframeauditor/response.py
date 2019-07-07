
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


# move this guy to its own object with proper class inheritance
# reason being that I want count in the parents, and I want to be
# able to extend this without breaking a shitload of stuff. This should then be
# Metrics -> NonNumericBasic
class String(StatsResponse):

    def __init__(self):
        super(String, self).__init__()
        self.__dict__.update(dict().fromkeys(
            {'distinct', 'count', 'null', 'freq'}
        ))
        self.type = 'STRING'
        self.freq = list()

# {
    # 'attr': 'dates',
    # 'distinct': 7,
    # 'count': 7,
    # 'null': 1,
    # 'freq': {'top':
    #               [
    #                {'name': '1800-01-01 00:00:00', 'count': 2},
    #                {'name': '2020-01-01 13:57:00', 'count': 1},
    #                {'name': '2001-12-31 00:00:00', 'count': 1}
    #               ]
    #          }
# }
