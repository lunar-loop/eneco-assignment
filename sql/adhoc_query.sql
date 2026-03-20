-- Flag 2 API data
-- SELECT * FROM bronze_countries_v2 WHERE json_data LIKE '%FLAG%'

-- Flag 3 in Postgres
-- SELECT name FROM track WHERE name like '%FLAG%'

-- Flag 4 in CSV data
SELECT keywords FROM silver_countries WHERE keywords LIKE '%FLAG%'