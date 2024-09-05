from sklearn.linear_model import LinearRegression
from sklearn.metrics import r2_score

def check(lr: LinearRegression, x_test, y_test) -> None:
    predictions = lr.predict(x_test)
    score = r2_score(y_test, predictions)
    print(score)
    file_path = "D:\\projekty python\\pythonProject6\\scores\\LinearRegression_score.txt"

    with open(file_path, "w") as file:  # Save score to txt
        file.write("Scores for Linear Regression: " + str(score))


