/* 
O setor financeiro encontrou alguns problemas na entrega de um dos nossos fornecedores, 
a entrega dos produtos não condiz com a nota fiscal.

Seu trabalho é exibir o nome dos produtos e o nome do fornecedor, 
para os produtos fornecidos pelo fornecedor ‘Ajax SA’.
*/

SELECT products.name, providers.name
FROM products
INNER JOIN providers
ON products.id_providers = providers.id
WHERE providers.name = 'Ajax SA';