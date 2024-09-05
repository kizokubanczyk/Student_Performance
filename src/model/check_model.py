from sklearn.linear_model import LinearRegression
from sklearn.metrics import r2_score

def check(lr: LinearRegression, x_test, y_test) -> float:
    predictions = lr.predict(x_test)
    return r2_score(y_test, predictions)


