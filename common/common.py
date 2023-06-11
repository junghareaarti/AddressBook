from os import path
import logging as logging
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base

database_path = path.join('.', 'data', 'addressbook.db')
engine = create_engine(f"sqlite:///{database_path}")
Base = declarative_base()

LOG_FORMAT = "%(levelname)s:\t%(asctime)s:\t%(message)s"
LOG_FORMATTER = logging.Formatter(LOG_FORMAT)


class CustomFormatter(logging.Formatter):
    grey = "\x1b[37m"
    green = "\x1b[32m"
    yellow = "\x1b[33;20m"
    red = "\x1b[31;20m"
    bold_red = "\x1b[31;1m"
    reset = "\x1b[0m"
    format = LOG_FORMAT

    FORMATS = {
        logging.DEBUG: grey + format + reset,
        logging.INFO: green + format + reset,
        logging.WARNING: yellow + format + reset,
        logging.ERROR: red + format + reset,
        logging.CRITICAL: bold_red + format + reset
    }

    def format(self, record):
        log_fmt = self.FORMATS.get(record.levelno)
        formatter = logging.Formatter(log_fmt)
        return formatter.format(record)


def set_logger(logger, out_file=None, logger_level='debug'):
    _logger_level = logging.ERROR
    if logger_level.lower().startswith('d'):
        _logger_level = logging.DEBUG
    elif logger_level.lower().startswith('i'):
        _logger_level = logging.INFO
    else:
        _logger_level = logging.ERROR

    logger.setLevel(_logger_level)
    ch = logging.StreamHandler()
    ch.setFormatter(CustomFormatter())
    logger.addHandler(ch)
    if out_file is not None:
        f_ch1 = logging.FileHandler(filename=out_file)
        f_ch1.setFormatter(LOG_FORMATTER)
        logger.addHandler(f_ch1)


LOGGER = logging.getLogger("AddressBook")
