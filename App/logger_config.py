import logging

def setup_logger(name):
    logger = logging.getLogger(name)
    handler = logging.FileHandler("./logs/app.log")
    formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
    handler.setFormatter(formatter)
    logger.addHandler(handler)
    logger.setLevel(logging.DEBUG)
    return logger
