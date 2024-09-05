import pandas as pd
import yaml

def read_data(dataFrame: str) -> pd.DataFrame:
    return pd.read_csv(dataFrame)
