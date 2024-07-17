import logging

# Setup logger
logging.basicConfig(filename='app.log', level=logging.ERROR)

def log_error(message):
    logging.error(message)
