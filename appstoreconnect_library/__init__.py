import os
import logging

PRIVATE_KEY_FOLDER = 'private_key'
REPORTS_FOLDER = 'reports'
LOGS_FOLDER = 'logs'

LOG_FOLDER_PATH = os.path.join(os.curdir, LOGS_FOLDER)
LOG_FILENAME_PATH = os.path.join(LOG_FOLDER_PATH, 'service.log')
FORMAT = '%(asctime)-15s %(levelname)-5s %(message)s'
logging.basicConfig(filename=LOG_FILENAME_PATH, format=FORMAT, level=logging.INFO)
LOGGER = logging.getLogger('__name__')
