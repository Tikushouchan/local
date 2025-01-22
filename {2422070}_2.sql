SELECT block, COUNT(*) as other_business_count
FROM minato_restaurant
WHERE business_type <> '飲食店営業'
GROUP BY block;