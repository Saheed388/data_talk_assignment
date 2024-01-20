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