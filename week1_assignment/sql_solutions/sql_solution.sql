select * from taxi_zone_lookup
select * from green_tripdata_2019_09

SELECT COUNT(*)
FROM green_tripdata_2019_09
WHERE DATE(pickup_date) = '2019-09-18' AND DATE(dropoff_datet) = '2019-09-18'


SELECT pickup_date, MAX(trip_distance) AS max_trip_distance
FROM green_tripdata_2019_09
GROUP BY pickup_date
ORDER BY max_trip_distance DESC
LIMIT 1;



SELECT "Borough", SUM(total_amount) AS total_amount_sum
FROM green_tripdata_2019_09 gt
join taxi_zone_lookup tz on tz."LocationID" = gt."PULocationID"
WHERE DATE(pickup_date) = '2019-09-18' AND "Borough" != 'Unknown'
GROUP BY "Borough"
HAVING SUM(total_amount) > 50000
ORDER BY total_amount_sum DESC
LIMIT 3;



SELECT 
    tz_dropoff."Zone" AS dropoff_zone, 
    tz_dropoff."service_zone",
    SUM(gt.tip_amount) AS total_tip_amount
FROM 
    green_tripdata_2019_09 gt
JOIN 
    taxi_zone_lookup tz_pickup ON tz_pickup."LocationID" = gt."PULocationID"
JOIN 
    taxi_zone_lookup tz_dropoff ON tz_dropoff."LocationID" = gt."DOLocationID"
WHERE 
    DATE(gt.pickup_date) = '2019-09-18' AND tz_pickup."Zone" = 'Astoria'
GROUP BY 
    tz_dropoff."Zone", tz_dropoff."service_zone"
ORDER BY 
    total_tip_amount DESC;