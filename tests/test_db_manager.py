from data.config import create_base, drop_data_base
from src.db_manager import DBManager
from io import StringIO

name_database = 'test_pricing_model'
name_table = 'test_company_prices'
company = 'self'
product = 'self'


def test_checking_completeness_database():
    create_base(name_database, name_table)
    assert (DBManager.checking_completeness_database(StringIO("""2"""), name_database, name_table) ==
            'База данных успешно заполнена.')
    assert (DBManager.checking_completeness_database(StringIO("""1"""), name_database, name_table) ==
            'База данных успешно заполнена (с добавлением новых значений).')
    assert (DBManager.checking_completeness_database(StringIO("""2"""), name_database, name_table) ==
            'База данных уже заполнена заполнена.')
    drop_data_base(name_database)


def test_the_entire_output():
    create_base(name_database, name_table)
    DBManager.checking_completeness_database(StringIO("""2"""), name_database, name_table)
    assert type(DBManager.the_entire_output(name_database, name_table)) is list
    assert len(DBManager.the_entire_output(name_database, name_table)) != 0
    drop_data_base(name_database)


def test_withdrawal_by_product():
    create_base(name_database, name_table)
    DBManager.checking_completeness_database(StringIO("""2"""), name_database, name_table)
    assert type(DBManager.withdrawal_by_product(name_database, name_table, product)) is list
    assert len(DBManager.withdrawal_by_product(name_database, name_table, product)) != 0
    drop_data_base(name_database)


def test_withdrawal_by_company():
    create_base(name_database, name_table)
    DBManager.checking_completeness_database(StringIO("""2"""), name_database, name_table)
    assert type(DBManager.withdrawal_by_company(name_database, name_table, company)) is list
    assert len(DBManager.withdrawal_by_company(name_database, name_table, company)) != 0
    drop_data_base(name_database)


def test_withdrawal_by_company_and_product():
    create_base(name_database, name_table)
    DBManager.checking_completeness_database(StringIO("""2"""), name_database, name_table)
    assert type(DBManager.withdrawal_by_company_and_product(name_database, name_table, company, product)) is list
    assert len(DBManager.withdrawal_by_company_and_product(name_database, name_table, company, product)) != 0
    drop_data_base(name_database)
