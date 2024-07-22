import csv
import os


class InstantiateCSVError(Exception):
    """Класс выводит сообщение пользователю при исключении ошибки 'KeyError'"""
    def __init__(self, *args, **kwargs):
        self.message = 'Файл csv_data.csv поврежден'

    def __str__(self):
        return self.message


class LoadPricingModelDatabase:
    """
    'Класс для загрузки данных о компаниях ее продуктах и ценах, из файла "csv_data.csv".'
    """

    def __str__(self):
        return 'Класс для загрузки данных о компаниях ее продуктах и ценах, из файла "csv_data.csv".'

    @staticmethod
    def instantiate_from_csv(path='csv_data.csv'):
        """
        Класс-метод, создает список о компаниях ее продуктах и ценах, загруженных из файла 'csv_data.csv'.
        :param path: Путь для получения данных функцией из файла 'csv'.
        list_pricing_model: Список всех данных из файла 'csv'.
        :return: Возвращает список всех данных 'list_pricing_model' из файла 'csv'.
        """
        list_pricing_model = []

        try:
            path = os.path.join(os.path.dirname(__file__), path)

            # Открытие файла 'csv' по указанному пути 'path' и запись данных из него в список 'list_pricing_model'.
            with open(path, 'r', newline='\n', encoding='windows- 1251') as file:
                reader = csv.DictReader(file)

                # Запись данных в список 'list_pricing_model'.
                for line in reader:
                    list_pricing_model.append({'price': line['price'], 'count': line['count'],
                                               'add_cost': line['add_cost'], 'company': line['company'],
                                               'product': line['product']})

                return list_pricing_model

        except KeyError:
            raise InstantiateCSVError()

        except FileNotFoundError:
            raise FileNotFoundError("Нет такого файла")
