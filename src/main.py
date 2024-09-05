from import_and_clean_data import import_data, clean_data
from model import train_test_split

def run() -> None:
    data_path = "D:/project/Student_Performance.csv"
    dataFrame = import_data.read_data(data_path)
    X, Y = clean_data.clean_data(dataFrame)

    x_train, x_test, y_train, y_test = train_test_split.split_dataFrame(X, Y)


if __name__ == "__main__":
    run()