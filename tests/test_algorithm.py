from data.config import create_base, drop_data_base
from src.db_manager import DBManager
from src.algorithm import Algorithm
from io import StringIO


name_database = 'test_pricing_model'
name_table = 'test_company_prices'
company = 'self'
product = 'self'


def test_algorithm2():
    create_base(name_database, name_table)
    DBManager.checking_completeness_database(StringIO("""2"""), name_database, name_table)
    list_pricing_model = DBManager.the_entire_output(name_database, name_table)
    algorithm = Algorithm.algorithm2(list_pricing_model)

    for item in range(0, len(algorithm)):
        assert algorithm[item] is not None

    drop_data_base(name_database)


def test_algorithm3():
    create_base(name_database, name_table)
    DBManager.checking_completeness_database(StringIO("""2"""), name_database, name_table)
    list_pricing_model = DBManager.the_entire_output(name_database, name_table)
    algorithm = Algorithm.algorithm3(list_pricing_model)

    for item in range(0, len(algorithm)):
        assert algorithm[item] is not None

    drop_data_base(name_database)


def test_algorithm4():
    create_base(name_database, name_table)
    DBManager.checking_completeness_database(StringIO("""2"""), name_database, name_table)
    list_pricing_model = DBManager.the_entire_output(name_database, name_table)
    algorithm = Algorithm.algorithm4(list_pricing_model)

    for item in range(0, len(algorithm)):
        assert algorithm[item] is not None

    drop_data_base(name_database)


def test_algorithm5():
    create_base(name_database, name_table)
    DBManager.checking_completeness_database(StringIO("""2"""), name_database, name_table)
    list_pricing_model = DBManager.the_entire_output(name_database, name_table)
    algorithm = Algorithm.algorithm5(list_pricing_model)

    for item in range(0, len(algorithm)):
        assert algorithm[item] is not None

    drop_data_base(name_database)
