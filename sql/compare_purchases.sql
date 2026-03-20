WITH invoice_rows AS (
    SELECT
        inv.customer_id,
        inv_line.unit_price * inv_line.quantity AS row_price,
        gnr.name AS genre_name
    FROM invoice AS inv
    LEFT JOIN invoice_line AS inv_line
        ON inv.invoice_id = inv_line.invoice_id
    LEFT JOIN track AS trk
        ON inv_line.track_id = trk.track_id
    LEFT JOIN genre AS gnr
        ON trk.genre_id = gnr.genre_id
    -- WHERE inv.invoice_date > '2000-01-01'
),
customer_genre_counts AS (
    SELECT
        customer_id,
        SUM(row_price) AS customer_total_purchase_amount,
        COUNT(*) FILTER (WHERE genre_name = 'Jazz') AS jazz_count
    FROM invoice_rows
    GROUP BY customer_id
),
customer_labels AS (
    SELECT
        customer_id,
        customer_total_purchase_amount,
        CASE
            WHEN jazz_count = 0 THEN 'Not Jazz Customer'
            ELSE 'Jazz Customer'
        END AS customer_type
    FROM customer_genre_counts
)
SELECT
    customer_type,
    AVG(customer_total_purchase_amount) AS avg_customer_total_purchase_amount
FROM customer_labels
GROUP BY customer_type