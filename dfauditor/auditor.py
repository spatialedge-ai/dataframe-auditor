import logging
from multiprocessing import Pool, cpu_count
import dfauditor.extractor
import psutil

import app_logger

log = app_logger.get(log_level=logging.DEBUG)


def profile_number_columns(series_items):
    log.debug('name: {}; row.count: {}; used: {}% free: {:.2f}GB'.format(series_items[0],
                                                                         len(series_items[1].index),
                                                                         psutil.virtual_memory().percent,
                                                                         float(psutil.virtual_memory().free) / 1024 ** 3))
    return dfauditor.extractor.numeric(series_items[1]).__dict__


def profile_string_columns(series_items):
    log.debug('name: {}; row.count: {}; used: {}% free: {:.2f}GB'.format(series_items[0],
                                                                         len(series_items[1].index),
                                                                         psutil.virtual_memory().percent,
                                                                         float(psutil.virtual_memory().free) / 1024 ** 3))
    return dfauditor.extractor.string(series_items[1]).__dict__


def audit_dataframe(dataframe, nr_processes=None):
    """
    produce a profile of the dataframe
    :param dataframe: a pandas dataframe
    :param nr_processes: a integer value specifying the number of processes to use (ideally #{processes}<#{cpus})
    :return: a json body containing the derived metrics
    """
    if not nr_processes:
        num_processes = min(dataframe.shape[1], cpu_count())

        with Pool(num_processes) as pool:
            columns = dataframe.columns
            log.debug('auditing dataframe with {} rows and {} columns'.format(
                len(dataframe.index),
                len(columns)))
            # using generic numpy type labels
            number_df = dataframe.select_dtypes(include=['number'])
            string_df = dataframe.select_dtypes(include=['object'])

            res_list = pool.map(profile_number_columns, number_df.iteritems())
            res_list += pool.map(profile_string_columns, string_df.iteritems())
            return res_list

