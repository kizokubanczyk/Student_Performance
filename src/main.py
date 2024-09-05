from import_and_clean_data import import_data

def run() -> None:
    data_path = "D:/project/Student_Performance.csv"
    dataFrame = import_data.read_data(data_path)


if __name__ == "__main__":
    run()