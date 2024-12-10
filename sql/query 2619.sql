/*
A nossa empresa está querendo fazer um novo contrato para o fornecimento de novos produtos superluxuosos, 
e para isso precisamos de alguns dados dos nossos produtos.

Seu trabalho é exibir o nome dos produtos, nome dos fornecedores e o preço, 
para os produtos cujo preço seja maior que 1000 e sua categoria seja ‘Super Luxury.
*/

SELECT pd.name, pv.name, pd.price
FROM products pd
INNER JOIN providers pv
ON pd.id_providers = pv.id
INNER JOIN categories c
ON c.id = pd.id_categories
WHERE c.name = 'Super Luxury'
AND pd.price >= 1000;