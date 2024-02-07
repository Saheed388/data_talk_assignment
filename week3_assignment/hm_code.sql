CREATE OR REPLACE TABLE `latest-project-410306.ny_taxi.grren_taxi_trip_2022`
PARTITION BY
  DATE(tpep_pickup_datetime) AS
SELECT * FROM `latest-project-410306.ny_taxi.grren_taxi_trip_2022`;


CREATE OR REPLACE EXTERNAL TABLE `latest-project-410306.ny_taxi.grren_taxi_trip_2022`
OPTIONS (
  format = 'CSV',
  uris = ['gs://data_tlk_388/module3/m3parquet_green_tripdata_2022']
);

SELECT COUNT(1) 
FROM `latest-project-410306.ny_taxi.grren_taxi_trip_2022`
WHERE fare_amount = 0;
