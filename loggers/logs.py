import logging
import sys
from .interfaces import LoggerInterface


class Logger(LoggerInterface):
    _instances = {}

    def __init__(self, name: str, level: int = logging.INFO):
        self._logger = logging.getLogger(name)
        self._logger.setLevel(level)

        if not self._logger.handlers:
            self._configure_handler()

    def _configure_handler(self):
        handler = logging.StreamHandler(sys.stdout)
        formatter = logging.Formatter(
            '%(asctime)s - %(message)s',
            datefmt='%Y-%m-%d %H:%M:%S'
        )
        handler.setFormatter(formatter)
        self._logger.addHandler(handler)

    def info(self, message: str):
        self._logger.info(message)
