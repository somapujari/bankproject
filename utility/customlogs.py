import logging
import inspect


class LogGen:
    @staticmethod
    def loggen():
        name = inspect.stack()[1][3]
        logger = logging.getLogger(name)
        logger.setLevel(logging.INFO)
        file = logging.FileHandler(r'C:\Users\Dell\PycharmProjects\bankproject\logs\bank_project_log.log')
        formatter = logging.Formatter('%(message)s : %(levelname)s : %(asctime)s : %(funcName)s : %(lineno)s')
        file.setFormatter(formatter)
        logger.addHandler(file)
        return logger
