import logging

def log():
    return logging.basicConfig(filename="logs.txt", level=logging.WARNING,
                        format='%(asctime)s:%(levelname)s:%(message)s:%(lineno)d', datefmt='%d/%m/%Y%I:%M:%S%p')
