use olist;

SELECT  T2.seller_id AS vendedor,
        SUM(T2.price) AS receita_total,
        COUNT( DISTINCT T1.order_id ) AS qtde_pedidos,
        COUNT( T2.product_id ) AS qtde_produtos

FROM tb_ordersas T1  

LEFT JOIN tb_order_items AS T2
ON T1.ORDER_ID = T2.ORDER_ID
WHERE T1.order_approved_at between '2017-06-01' AND '2018-06-01'
;


SELECT 	distinct T2.seller_id AS vendedor,
		SUM(T2.price) AS receita_total
      
FROM tb_orders as T1

LEFT JOIN tb_order_items AS T2
ON T1.order_id = T2.order_id
WHERE T1.order_approved_at between '2017-06-01' AND '2018-06-01';




SELECT * 
FROM tb_orders as t1

left join tb_order_items as t2
ON t1.order_id = t2.order_id;


SELECT DISTINCT tb_sellers.seller_id
FROM tb_orders

LEFT JOIN tb_order_items
ON tb_order_items.order_id = tb_order_items.order_id

LEFT JOIN tb_sellers
ON tb_sellers.seller_id = tb_order_items.seller_id;