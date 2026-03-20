SELECT
    country_name, longest_runway_airport_name, longest_runway_length_ft, longest_runway_width_ft
FROM gold_airport_statistics
WHERE airport_count > 0 AND longest_runway_length_ft IS NOT NULL
ORDER BY longest_runway_length_ft DESC