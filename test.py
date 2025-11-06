import pytest
import pandas as pd
from data.dataframes import PandasHandler

def test_read_csv_has_correct_columns():
    """Verifica que el DataFrame tiene la columna 'values'"""
    result = PandasHandler.read_csv()
    assert 'values' in result.columns
    assert len(result.columns) == 1
