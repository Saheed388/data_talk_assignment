import os
from pandas import DataFrame
import gcsfs
import pyarrow as pa
import pyarrow.parquet as pq

if 'data_exporter' not in globals():
    from mage_ai.data_preparation.decorators import data_exporter

os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = "/home/src/magic-zoomcamp/gcp_json/my-credentials.json"

bucket_name = 'data_tlk_388'
project_id = 'latest-project-410306'

table_name = "nyc_taxi_data_home_work"

root_path = f'gs://{bucket_name}/{table_name}'

@data_exporter
def export_data_to_gcs(data: DataFrame, **kwargs) -> None:
    data['lpep_pickup_datetime'] = data['lpep_pickup_datetime'].dt.date

    # Use GCSFileSystem from gcsfs
    gcs = gcsfs.GCSFileSystem(project=project_id)

    # Write Parquet file to Google Cloud Storage
    table = pa.Table.from_pandas(data)
    pq.write_to_dataset(
        table,
        partition_cols=['lpep_pickup_datetime'],
        filesystem=gcs,
        root_path=root_path
    )
