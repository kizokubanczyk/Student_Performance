import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
from sklearn.metrics import r2_score

def check(lr: LinearRegression, x_test, y_test) -> None:
    predictions = lr.predict(x_test)
    score = r2_score(y_test, predictions)
    print(score)
    file_path = "../../LinearRegression_score.txt"

    with open(file_path, "w") as file:  # Save score to txt
        file.write("Scores for Linear Regression: " + str(score))

    file_path_plot = "../../LinearRegression_plot.png"
    plt.figure(figsize=(10, 6))
    plt.scatter(y_test, predictions)
    plt.xlabel('X')
    plt.ylabel('Y')
    plt.title('Scatter Plot of Actual vs Predicted')
    plt.savefig(file_path_plot)  # Save plot to PNG
    plt.close()



