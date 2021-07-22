from socket import gethostname
from logging import (getLogger, NullHandler, StreamHandler, Formatter,
                     DEBUG, INFO, WARNING, ERROR, CRITICAL)


HOST = gethostname()
handler = StreamHandler()
formatter = Formatter(f'%(asctime)s {HOST} %(levelname)s [%(name)s] %(message)s',
                      datefmt='%Y-%m-%d %H:%M:%S')
handler.setFormatter(formatter)


# NOTE: NullHandler for library-only use
logger = getLogger('python201')
logger.addHandler(NullHandler())


levels = {'debug': DEBUG, 'info': INFO, 'warning': WARNING,
          'error': ERROR, 'critical': CRITICAL}


def initialize_logging(level: str) -> None:
    """Initialize the top-level logger with the stream handler and a `level`."""
    if handler not in logger.handlers:
        logger.addHandler(handler)
        logger.setLevel(levels.get(level))
