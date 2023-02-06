import logging


logger = logging.getLogger()

logger.setLevel(logging.DEBUG)
formatter = logging.Formatter('[%(asctime)s]  [%(funcName)s] [%(message)s]')
streamHandler = logging.StreamHandler()

streamHandler.setFormatter(formatter)
logger.addHandler(streamHandler)

i = 'a'

if i == 'a':
    result = 'b'


logger.info(f'result is {result}')


k = 'a'

if k == 'a':
    result = 'h'

logger.info(f'result is {result}')
