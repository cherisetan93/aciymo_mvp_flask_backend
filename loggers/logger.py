import logging
from datetime import datetime

# Create a common logger
logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)

# Define the log file path
log_file_path = 'loggers/logs/app_%s.log' % str(datetime.now().strftime("%Y_%m_%d"))

# Create a file handler and set its level
handler = logging.FileHandler(log_file_path)
handler.setLevel(logging.INFO)

# Create a logging format
formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
handler.setFormatter(formatter)

# Add the handler to the logger
logger.addHandler(handler)