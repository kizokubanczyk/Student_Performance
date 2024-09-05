from sklearn.linear_model import LinearRegression
import pandas as pd

def train(x_train:  pd.DataFrame, y_train:  pd.DataFrame) -> LinearRegression:
    lr = LinearRegression()
    lr.fit(x_train, y_train)
    return lr