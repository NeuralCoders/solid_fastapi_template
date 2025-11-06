import pandas as pd
import polars as ps
from .interfaces import DataInterface, DataframeHandlerInterface

class DataProcessor(DataInterface):

    def __init__(self, dataframe_processor: DataframeHandlerInterface):
        self.dataframe_processor = dataframe_processor

    def show_data(self):
        self.dataframe_processor.read_csv()


class PandasHandler(DataframeHandlerInterface):

    @staticmethod
    def read_csv():
        lista = [1, 2, 3, 4, 5]
        df = pd.DataFrame(lista, columns=['values'])
        return df

    def read_csv_to_json(self):
        data = self.read_csv()
        data.json()


class PolarsHandler(DataframeHandlerInterface):

    @staticmethod
    def read_csv():
        lista = [1, 2, 3, 4, 5]
        df = ps.DataFrame({'values': lista})
        return df
