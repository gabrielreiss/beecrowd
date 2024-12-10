SELECT name, customers_number FROM lawyers
WHERE customers_number = ( SELECT max(customers_number) FROM lawyers )
UNION ALL
SELECT name, customers_number FROM lawyers
WHERE customers_number = ( SELECT MIN(customers_number) FROM lawyers )
UNION ALL
SELECT 'Average', CAST(AVG(customers_number) AS INT) FROM lawyers;





/*
SELECT lawyers.name,ROUND(lawyers.customers_number) FROM lawyers
WHERE lawyers.customers_number = 
(SELECT max(lawyers.customers_number) FROM lawyers)
UNION
SELECT lawyers.name,ROUND(lawyers.customers_number) FROM lawyers
WHERE lawyers.customers_number = 
(SELECT MIN(lawyers.customers_number) FROM lawyers)
UNION
SELECT 'Average',ROUND(AVG(lawyers.customers_number)) FROM lawyers;
*/