import pandas as pd


def read_data(dataFrame: str) -> pd.DataFrame:
    return pd.read_csv(dataFrame)