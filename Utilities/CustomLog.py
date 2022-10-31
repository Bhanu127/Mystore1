import inspect
import logging


class CustomLog:
    @staticmethod
    def getlogger():
        # logger_name = inspect.stack()[3][2]
        logger = logging.getLogger()
        filehandler = logging.FileHandler("C:\\Users\\Bhanu\\PycharmProjects\\Mystore\\Logs\\logfile.log")
        formatter = logging.Formatter("%(asctime)s:, %(levelname)s:,%(name)s:,%(message)s")
        filehandler.setFormatter(formatter)
        logger.addHandler(filehandler)
        logger.setLevel(logging.INFO)
        return logger