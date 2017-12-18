import logging
import esg_bash2py
import datetime
import os
# import coloredlogs
from logging.handlers import RotatingFileHandler

parent_dir = os.path.join(os.path.dirname(__file__), os.pardir)
logging_dir = os.path.join(parent_dir, "logs")
PATH = os.path.join(logging_dir, "esgf_log.out_{date}".format(date=str(datetime.date.today())))

def create_logging_directory():
    esg_bash2py.mkdir_p(logging_dir)


#----------------------------------------------------------------------
def create_rotating_log(name="esgf_logger", path=PATH):
    """Creates a rotating log"""
    logger = logging.getLogger(name)


    # add a rotating handler
    if not os.path.isfile(path):
        handler = RotatingFileHandler(path, maxBytes=10*1024*1024,
                                  backupCount=5)

    console_handler = logging.StreamHandler()
    console_handler.setLevel(logging.ERROR)


    # create formatter
    formatter = logging.Formatter("%(levelname)s - %(filename)s - %(lineno)s - %(funcName)s - %(asctime)s - %(message)s", datefmt='%m/%d/%Y %I:%M:%S %p')
    # colored_log_file = open("esgf_colored_log.out", "w")
    # coloredlogs.install(level='DEBUG', logger=logger, stream=colored_log_file)
    # add formatter to handler
    handler.setFormatter(formatter)
    handler.setLevel(logging.DEBUG)

    console_handler.setFormatter(formatter)
    logger.addHandler(console_handler)
    logger.addHandler(handler)
    return logger


def main():
    create_logging_directory()
    create_rotating_log()

if __name__ == '__main__':
    main()
