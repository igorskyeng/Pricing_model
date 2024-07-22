"""Скрипт для возвращения данных на подключение к БД, на создание БД и удаления БД в 'PostgreSQL'."""
import psycopg2
import os


def connect():
    """
    Считывает данные из файла 'database' для подключения к БД и их возвращения.
    param: Список данных на подключения к БД.
    path: Путь для считывания данных из файла 'database'.
    :return: Возвращает список данных для подключения к БД и их возвращения.
    """
    param = []
    path = os.path.join(os.path.dirname(__file__), 'database')

    with open(path, 'r', encoding='utf-8') as file:
        for line in file:
            param.append(line.rstrip('\n'))

    host = param[0][5:]
    database = param[1][9:]
    user = param[2][5:]
    password = param[3][9:]

    param = [host, database, user, password]

    return param


def create_base(name_database='pricing_model', name_table='company_prices'):
    """
    Создает БД и таблицу в ней.
    :param name_database: Название БД для ее создания.
    :param name_table: Название таблицы в БД для ее создания.
    message: Переменная для записи результата выполнения функции.
    database: Получает список значений для подключения к БД из фнешней функции 'connect()'.
    conn: Подключение к БД.
    :return: Возвращает сообщение о результате выполнения функции.
    """
    message = ''
    database = connect()
    conn = psycopg2.connect(host=database[0], database=database[1], user=database[2], password=database[3])
    cursor = conn.cursor()
    conn.autocommit = True

    try:
        cursor.execute(f"CREATE DATABASE {name_database}")
        message = "База данных успешно создана."
        print("База данных успешно создана.\n")

        database = connect()
        conn = psycopg2.connect(host=database[0], database=name_database, user=database[2], password=database[3])

        with conn:
            with conn.cursor() as cur:
                cur.execute(f"CREATE TABLE {name_table}"
                            f"(price varchar(100) NOT NULL,"
                            f"count varchar(100) NOT NULL,"
                            f"add_cost varchar(100) NOT NULL,"
                            f"company varchar(100) NOT NULL,"
                            f"product varchar(100) NOT NULL)")

    except psycopg2.errors.DuplicateDatabase:
        print("База данных уже существует.")
        message = "База данных уже существует."

    finally:
        cursor.close()
        conn.close()
        return message


def drop_data_base(name_database='pricing_model'):
    """
    Удаляет базу данных.
    :param name_database: Название БД для ее удаления.
    message: Переменная для записи результата выполнения функции.
    database: Получает список значений для подключения к БД из фнешней функции 'connect()'.
    conn: Подключение к БД.
    :return: Возвращает сообщение о результате выполнения функции.
    """
    message = ''
    database = connect()
    conn = psycopg2.connect(host=database[0], database=database[1], user=database[2], password=database[3])
    cursor = conn.cursor()

    conn.autocommit = True

    try:
        cursor.execute(f"DROP DATABASE {name_database} WITH (FORCE)")
        message = "База данных успешно удалена."
        print("База данных успешно удалена.\n")

    except psycopg2.errors.InvalidCatalogName:
        print("База данных не существует.")
        message = "База данных не существует."

    finally:
        conn.close()
        return message
