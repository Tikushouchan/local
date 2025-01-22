SELECT customer_name, SUM(p.price * quantity) AS total_purchase
FROM products AS p
INNER JOIN orders AS o ON p.product_id = o.product_id
INNER JOIN customers AS c ON o.customer_id = c.customer_id
WHERE order_date BETWEEN '2025-01-01' AND '2025-06-30'
GROUP BY customer_name
ORDER BY total_purchase DESC
LIMIT 3;