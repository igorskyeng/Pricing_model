from data.data_pricing_model import LoadPricingModelDatabase


def test_the_entire_output():
    path = 'csv_data.csv'
    assert type(LoadPricingModelDatabase.instantiate_from_csv(path)) is list
    assert len(LoadPricingModelDatabase.instantiate_from_csv(path)) != 0
