from sklearn.model_selection import train_test_split
import pandas as pd

def split_dataFrame(X:  pd.DataFrame, Y: pd.DataFrame) -> tuple[pd.DataFrame, pd.DataFrame, pd.DataFrame, pd.DataFrame]:
    return train_test_split(X, Y, test_size=0.2, random_state=42)
# function return x_train, x_test, y_train, y_test