import logging
import dfauditor.__init__


def get(log_file=None, log_level=logging.INFO):
    """
    get a an appliactions logger which outputs to a log_file, or to stdout.
    :param log_file: optional log file name and path (if unset then only stdout is used)
    :param log_level for logger
    """
    # we don't require finely grained contextual info, so using straight string modifier instead of filters
    formatter = logging.Formatter(
        '%(asctime)s [{}] %(levelname)s %(module)s - %(funcName)s: %(message)s'.format(dfauditor.__init__.__version__))
    # we will override an existing root context
    log = logging.getLogger()
    log.setLevel(log_level)

    if len(log.handlers) > 0:
        # override previous handlers
        log.handlers = []

    if log_file:
        file_handler = logging.FileHandler(log_file)
        file_handler.setFormatter(formatter)
        log.addHandler(file_handler)
    else:
        console_handler = logging.StreamHandler()
        console_handler.setFormatter(formatter)
        log.addHandler(console_handler)

    return log
