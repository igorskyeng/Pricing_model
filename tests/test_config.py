from data.config import connect, create_base, drop_data_base


def test_connect():
    assert type(connect()) is list
    assert len(connect()) == 4


def test_create_base():
    name_database = 'test_pricing_model'
    name_table = 'test_company_prices'
    assert create_base(name_database, name_table) == 'База данных успешно создана.'
    assert create_base(name_database, name_table) == 'База данных уже существует.'
    drop_data_base(name_database)


def test_drop_data_base():
    name_database = 'test_pricing_model'
    name_table = 'test_company_prices'
    assert drop_data_base(name_database) == 'База данных не существует.'
    create_base(name_database, name_table)
    assert drop_data_base(name_database) == 'База данных успешно удалена.'
