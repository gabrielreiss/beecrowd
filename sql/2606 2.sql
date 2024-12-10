/* Seu chefe precisa que você exiba o código e
 o nome dos produtos, cuja categoria inicie com 'super' */ 

/* tentativa
SELECT id, name FROM products;
SELECT id FROM categories
WHERE name LIKE 'super%'; */

/* query certa */
SELECT P.ID, P.NAME FROM PRODUCTS P 
INNER JOIN CATEGORIES C ON C.ID = P.ID_CATEGORIES 
WHERE C.NAME LIKE 'super%';