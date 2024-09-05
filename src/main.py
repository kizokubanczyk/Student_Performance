from import_and_clean_data import import_data, clean_data
from model import train_test_split
from model import train_model
from model import  check_model
import click
import yaml


@click.command()
@click.option('--config', '-c', default='../config.yaml', help='Path to the configuration file')
def run(config) -> None:
    with open(config, 'r') as file:
        config_data = yaml.safe_load(file)

        data_path = config_data.get('dataset_path')

        dataFrame = import_data.read_data(data_path)

        X, Y = clean_data.clean_data(dataFrame)

        x_train, x_test, y_train, y_test = train_test_split.split_dataFrame(X, Y)

        lr = train_model.train(x_train, y_train)

        check_model.check(lr, x_test, y_test)

if __name__ == "__main__":
    run()