from abc import ABC, abstractmethod


class LoggerInterface(ABC):
    @abstractmethod
    def info(self, message: str):
        raise NotImplementedError
