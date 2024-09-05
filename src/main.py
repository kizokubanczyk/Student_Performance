from import_and_clean_data import import_data, clean_data

def run() -> None:
    data_path = "D:/project/Student_Performance.csv"
    dataFrame = import_data.read_data(data_path)
    X, Y = clean_data.clean_data(dataFrame)


if __name__ == "__main__":
    run()