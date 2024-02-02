import io
import pandas as pd
import requests

# Importing from a module if not defined in the current scope
if 'data_loader' not in globals():
    from mage_ai.data_preparation.decorators import data_loader
if 'test' not in globals():
    from mage_ai.data_preparation.decorators import test

# Data loading function decorated with @data_loader
@data_loader
def load_data_from_api(*args, **kwargs):
    """
    Template for loading data from API
    """
    # URLs for the final three months
    urls = [
        'https://github.com/DataTalksClub/nyc-tlc-data/releases/download/green/green_tripdata_2020-10.csv.gz',
        'https://github.com/DataTalksClub/nyc-tlc-data/releases/download/green/green_tripdata_2020-11.csv.gz',
        'https://github.com/DataTalksClub/nyc-tlc-data/releases/download/green/green_tripdata_2020-12.csv.gz'
    ]

    # List to store DataFrames for each month
    dfs = []

    # Iterate over the URLs and load the data
    for url in urls:
        response = requests.get(url)
        df = pd.read_csv(io.BytesIO(response.content), compression='gzip', sep=',')

        # Apply data types to columns
        taxi_dtypes = {
            'VendorID': pd.Int64Dtype(),
            'store_and_fwd_flag': 'string',
            'RatecodeID': float,
            'PULocationID': float,
            'DOLocationID': float,
            'passenger_count': float,
            'trip_distance': float,
            'fare_amount': float,
            'extra': float,
            'mta_tax': float,
            'tip_amount': float,
            'tolls_amount': float,
            'ehail_fee': float,
            'improvement_surcharge': float,
            'total_amount': float,
            'payment_type': float,
            'trip_type': float,
            'congestion_surcharge': float
        }

        parse_dates = ['lpep_pickup_datetime', 'lpep_dropoff_datetime']

        df = df.astype(taxi_dtypes)
        df[parse_dates] = df[parse_dates].apply(pd.to_datetime)

        # Append the DataFrame to the list
        dfs.append(df)

    # Concatenate DataFrames for each month
    final_df = pd.concat(dfs, ignore_index=True)

    return final_df

# Test function decorated with @test
@test
def test_output(output, *args) -> None:
    """
    Template code for testing the output of the block.
    """
    assert output is not None, 'The output is undefined'
