if 'transformer' not in globals():
    from mage_ai.data_preparation.decorators import transformer
if 'test' not in globals():
    from mage_ai.data_preparation.decorators import test

@transformer
def transform(data, *args, **kwargs):
    """
    Template for data transformation
    """
    # Replace spaces with underscores and convert to lowercase for column names
    data.columns = data.columns.str.replace(' ', '_').str.lower()

    # Remove rows where passenger_count or trip_distance is equal to 0
    data = data[(data['passenger_count'] > 0) & (data['trip_distance'] > 0)]

    # Specify your additional transformation logic here

    return data

@test
def test_output(output, *args) -> None:
    """
    Template code for testing the output of the block.
    """
    assert output is not None, 'The output is undefined'
