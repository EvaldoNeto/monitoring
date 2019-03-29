import logging

"""A simple class to format the logs, still needs improvement
"""
class monLog:
    def info(msg, area = ""):
        logger = logging.getLogger(area)
        if not logger.hasHandlers():
            f_handler = logging.FileHandler(config.log_fullpath)
            f_handler.setLevel(logging.INFO)
            f_format = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
            f_handler.setFormatter(f_format)
            logger.addHandler(f_handler)
        logger.info(msg)
        
    def warning(msg, area = ""):
        logger = logging.getLogger(area)
        if not logger.hasHandlers():
            f_handler = logging.FileHandler(config.log_fullpath)
            f_handler.setLevel(logging.WARNING)
            f_format = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
            f_handler.setFormatter(f_format)
            logger.addHandler(f_handler)
        logger.warning(msg)

    def error(msg, area=""):
        logger = logging.getLogger(area)
        if not logger.hasHandlers():
            f_handler = logging.FileHandler(config.log_fullpath)
            f_handler.setLevel(logging.ERROR)
            f_format = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
            f_handler.setFormatter(f_format)
            logger.addHandler(f_handler)
        logger.error(msg)

    def exception(msg, area=""):
        logger = logging.getLogger(area)
        if not logger.hasHandlers():
            f_handler = logging.FileHandler(config.log_fullpath)
            f_handler.setLevel(logging.ERROR)
            f_format = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
            f_handler.setFormatter(f_format)
            logger.addHandler(f_handler)
        logger.error(msg, exc_info=True)


