import logging
import esg_bash2py
import datetime
import os
# import coloredlogs
from logging.handlers import RotatingFileHandler

parent_dir = os.path.join(os.path.dirname(__file__), os.pardir)
logging_dir = os.path.join(parent_dir, "logs")
PATH = os.path.join(logging_dir, "esgf_log_{date}.out".format(date=str(datetime.date.today())))

#----------------------------------------------------------------------
def create_rotating_log(name="esgf_logger", path=PATH):
    """Creates a rotating log"""
    logger = logging.getLogger(name)

    # create formatter
    formatter = logging.Formatter("%(levelname)s - %(filename)s - %(lineno)s - %(funcName)s - %(asctime)s - %(message)s", datefmt='%m/%d/%Y %I:%M:%S %p')

    # add a rotating handler
    if not os.path.isfile(path):
        handler = RotatingFileHandler(path, maxBytes=10*1024*1024,
                                  backupCount=5)
        handler.setFormatter(formatter)
        handler.setLevel(logging.DEBUG)
        logger.addHandler(handler)

    console_handler = logging.StreamHandler()
    console_handler.setLevel(logging.DEBUG)

    # colored_log_file = open("esgf_colored_log.out", "w")
    # coloredlogs.install(level='DEBUG', logger=logger, stream=colored_log_file)
    # add formatter to handler


    console_handler.setFormatter(formatter)
    logger.addHandler(console_handler)

    return logger


def main():
    create_rotating_log()

if __name__ == '__main__':
    main()
