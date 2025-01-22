SELECT 
    EXTRACT(MONTH FROM init_license_dt) AS month, 
    business_type, 
    COUNT(*) AS store_count
FROM minato_restaurant
WHERE init_license_dt >= '2022-01-01' 
AND init_license_dt < '2023-01-01'
GROUP BY month, business_type
ORDER BY month, business_type;