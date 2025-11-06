from abc import ABC, abstractmethod

class DataInterface(ABC):
    @abstractmethod
    def show_data(self):
        raise NotImplementedError


class DataframeHandlerInterface(ABC):
    @staticmethod
    @abstractmethod
    def read_csv():
        raise NotImplementedError
