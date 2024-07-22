"""Скрипт для заполнения данными таблицы в БД 'PostgreSQL'."""
import psycopg2
from sys import stdin
from pathlib import Path
from data.config import connect


class DBManager:
    """
    Класс для записи данных из файла 'csv' в БД и их возвращения в виде всего списка или определенным продуктам
    или компанией.
    """
    def __str__(self):
        return ("Класс для записи данных из файла 'csv' в БД и их возвращения в виде всего списка или определенным "
                "продуктам или компанией.")

    @staticmethod
    def checking_completeness_database(_in=stdin, name_database='pricing_model', name_table='company_prices'):
        """
        Записывает данные полученные из класс-метода 'instantiate_from_csv' в БД.
        :param _in: Переменная для получения значений от тестов для имитирования ввода с клавиатуры.
        :param name_database: Название БД в которую будет производиться запись данных.
        :param name_table: Название таблицы в БД в которую будет производиться запись данных.
        message: Переменная для записи результата выполнения функции.
        database: Получает список значений для подключения к БД из фнешней функции 'connect()'.
        conn: Подключение к БД.
        path: Путь для получения данных функцией из файла 'csv'.
        exit_script: Переменная для завершения цикла опроса пользователя.
        choice: Переменная для записи выбора пользоветелем.
        :return: Возвращает сообщение о результате выполнения функции.
        """
        message = ''
        database = connect()
        conn = psycopg2.connect(host=database[0], database=name_database, user=database[2], password=database[3])
        path = f'{Path(__file__).resolve().parents[1]}\data\csv_data.csv'

        try:
            # Подключение к БД для заполнения ее данными из файла 'csv'.
            with conn.cursor() as cur, open(path, 'r', newline='\n', encoding='windows- 1251') as file:
                cur.execute(f"SELECT price FROM {name_table} WHERE price = '12859' "
                            f"AND count = '90' AND add_cost = '4739'")
                rows = cur.fetchall()

                # Проверка имеются ли данные в БД.
                if len(rows) == 0:
                    cur.copy_from(file, name_table, sep=",")
                    # Удаление значений из строки таблицы, если в ней присутствует название столбца.
                    cur.execute(f"DELETE FROM  {name_table} WHERE price = 'price'", )
                    conn.commit()
                    message = 'База данных успешно заполнена.'
                    print('База данных успешно заполнена.')

                # Если данные в БД имеются, то выводится вопрос о продолжении ее заполнения.
                else:
                    exit_script = 0

                    while exit_script == 0:
                        print('\nУ вас уже заполнена база данных! Добавить новые значения?\n'
                              '1 - Да.\n'
                              '2 - Нет.\n')

                        choice = int(_in.readline())

                        if choice == 1:
                            cur.copy_from(file, name_table, sep=",")
                            # Удаление значений из строки таблицы, если в ней присутствует название столбца.
                            cur.execute(f"DELETE FROM  {name_table} WHERE price = 'price'", )
                            conn.commit()
                            exit_script = 1
                            message = 'База данных успешно заполнена (с добавлением новых значений).'

                        elif choice == 2:
                            exit_script = 1
                            message = 'База данных уже заполнена заполнена.'

        except psycopg2.errors.UniqueViolation as error:
            print(error)

        finally:
            conn.close()
            return message

    @staticmethod
    def the_entire_output(name_database='pricing_model', name_table='company_prices'):
        """
        Возвращает весь список данных из БД.
        :param name_database: Название БД в которую будет производиться запись данных.
        :param name_table: Название таблицы в БД в которую будет производиться запись данных.
        database: Получает список значений для подключения к БД из фнешней функции 'connect()'.
        conn: Подключение к БД.
        list_pricing_model: Список всех данных из БД.
        :return: Возвращает список всех данных 'list_pricing_model' из БД.
        """
        database = connect()
        conn = psycopg2.connect(host=database[0], database=name_database, user=database[2], password=database[3])
        list_pricing_model = []

        try:
            # Подключение к БД с их записью в список 'list_pricing_model'.
            with (conn):
                with conn.cursor() as cur:
                    cur.execute(f"SELECT price, count, add_cost, company, product FROM {name_table}")
                    list_pricing_model = cur.fetchall()

        except psycopg2.errors.UniqueViolation as error:
            print(error)

        finally:
            conn.close()
            return list_pricing_model

    @staticmethod
    def conclusion_by_product(name_database='pricing_model', name_table='company_prices', product='self'):
        """
        Возвращает список данных из БД по определенному продукту.
        :param name_database: Название БД в которую будет производиться запись данных.
        :param name_table: Название таблицы в БД в которую будет производиться запись данных.
        :param product: Перебенная для указания определенного продукта для вывода из БД.
        database: Получает список значений для подключения к БД из фнешней функции 'connect()'.
        conn: Подключение к БД.
        list_pricing_model: Список данных из БД по определенному продукту.
        :return: Возвращает список данных 'list_pricing_model' из БД по определенному продукту.
        """
        database = connect()
        conn = psycopg2.connect(host=database[0], database=name_database, user=database[2], password=database[3])
        list_pricing_model = []

        try:
            # Подключение к БД с их записью в список 'list_pricing_model'.
            with (conn):
                with conn.cursor() as cur:
                    cur.execute(f"SELECT price, count, add_cost, company, product "
                                f"FROM {name_table} WHERE product LIKE '%{product}%'")
                    list_pricing_model = cur.fetchall()

        except psycopg2.errors.UniqueViolation as error:
            print(error)

        finally:
            conn.close()
            return list_pricing_model

    @staticmethod
    def conclusion_by_company(name_database='pricing_model', name_table='company_prices', company='self'):
        """
        Возвращает список данных из БД по определенной компании.
        :param name_database: Название БД в которую будет производиться запись данных.
        :param name_table: Название таблицы в БД в которую будет производиться запись данных.
        :param company: Перебенная для указания определенной компании для вывода из БД.
        database: Получает список значений для подключения к БД из фнешней функции 'connect()'.
        conn: Подключение к БД.
        list_pricing_model: Список данных из БД по определенной компании.
        :return: Возвращает список данных 'list_pricing_model' из БД по определенному компании.
        """
        database = connect()
        conn = psycopg2.connect(host=database[0], database=name_database, user=database[2], password=database[3])
        list_pricing_model = []

        try:
            # Подключение к БД с их записью в список 'list_pricing_model'.
            with (conn):
                with conn.cursor() as cur:
                    cur.execute(f"SELECT price, count, add_cost, company, product "
                                f"FROM {name_table} WHERE company LIKE '%{company}%'")
                    list_pricing_model = cur.fetchall()

        except psycopg2.errors.UniqueViolation as error:
            print(error)

        finally:
            conn.close()
            return list_pricing_model

    @staticmethod
    def conclusion_by_company_and_product(name_database='pricing_model', name_table='company_prices',
                                          company='self', product='self'):
        """
        Возвращает список данных из БД по определенному продукту и компании.
        :param name_database: Название БД в которую будет производиться запись данных.
        :param name_table: Название таблицы в БД в которую будет производиться запись данных.
        :param company: Перебенная для указания определенной компании для вывода из БД.
        :param product: Перебенная для указания определенного продукта для вывода из БД.
        database: Получает список значений для подключения к БД из фнешней функции 'connect()'.
        conn: Подключение к БД.
        list_pricing_model: Список данных из БД по определенному продукту и компании.
        :return: Возвращает список данных 'list_pricing_model' из БД по определенному продукту и компании.
        """
        database = connect()
        conn = psycopg2.connect(host=database[0], database=name_database, user=database[2], password=database[3])
        list_pricing_model = []

        try:
            # Подключение к БД с их записью в список 'list_pricing_model'.
            with (conn):
                with conn.cursor() as cur:
                    cur.execute(f"SELECT price, count, add_cost, company, product "
                                f"FROM {name_table} WHERE company LIKE '%{company}%'"
                                f"AND product LIKE '%{product}%'")
                    list_pricing_model = cur.fetchall()

        except psycopg2.errors.UniqueViolation as error:
            print(error)

        finally:
            conn.close()
            return list_pricing_model
