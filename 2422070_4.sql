SELECT SUM(products.price * orders.quantity) AS total_sales
FROM products 
  INNER JOIN orders ON order_id = orders.order_id
  INNER JOIN customers ON orders.customer_id =customers.customer_id
WHERE customers.gender = 'Female'
  AND customers.age >=20
  AND order_date BETWEEN '2024-01-01' AND '2024-03-31';