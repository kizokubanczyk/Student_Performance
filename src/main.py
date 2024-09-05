from import_and_clean_data import import_data, clean_data
from model import train_test_split
from model import train_model
from model import  check_model

def run() -> None:
    data_path = "D:/project/Student_Performance.csv"
    dataFrame = import_data.read_data(data_path)
    X, Y = clean_data.clean_data(dataFrame)

    x_train, x_test, y_train, y_test = train_test_split.split_dataFrame(X, Y)

    lr = train_model.train(x_train, y_train)

    check_model.check(lr, x_test, y_test)

if __name__ == "__main__":
    run()