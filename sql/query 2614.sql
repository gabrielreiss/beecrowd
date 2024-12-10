/*
A vídeo locadora está fazendo seu relatório semestral e precisa da sua ajuda. 
Basta você selecionar o nome dos clientes e a data de locação, 
das locações realizadas no mês de setembro de 2016.
*/

SELECT c.name, r.rentals_date
FROM customers c
INNER JOIN rentals r
ON c.id = r.id_customers 
WHERE r.rentals_date BETWEEN '2016-09-01 00:00:00' AND '2016-09-30 23:59:59';