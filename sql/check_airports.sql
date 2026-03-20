WITH ranked AS (
    SELECT
        country_name,
        airport_count,
        ROW_NUMBER() OVER (ORDER BY airport_count DESC, country_name) AS top_rank,
        ROW_NUMBER() OVER (ORDER BY airport_count ASC, country_name) AS bottom_rank
    FROM gold_airport_statistics
)
SELECT 'top_3' AS segment, country_name, airport_count
FROM ranked
WHERE top_rank <= 3

UNION ALL

SELECT 'bottom_10' AS segment, country_name, airport_count
FROM ranked
WHERE bottom_rank <= 10