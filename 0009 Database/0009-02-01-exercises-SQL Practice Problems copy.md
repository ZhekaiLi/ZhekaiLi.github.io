---
layout: post
title: Practice
categories: Z-attach
description: Personal Notes
keywords: Z-attach
mathjax: false
---

对于如下三张表单：
`orders`
<img src="/images/2021-12/Screenshot 2021-12-17 at 11.16.29 AM.png" zoom="100%">
`users`
<img src="/images/2021-12/Screenshot 2021-12-17 at 11.16.54 AM.png" zoom="100%">
`products`
<img src="/images/2021-12/Screenshot 2021-12-17 at 11.17.08 AM.png" zoom="100%">

### 1. 计算每种产品的销售价格
```sql
-- id + 总价格
SELECT 
    product_id, SUM(unit_price * quantity) AS sales_amount
FROM
    orders
GROUP BY product_id;

-- name + 总价格
SELECT 
    product_name, SUM(unit_price * quantity) AS sales_amount
FROM
    products
        LEFT JOIN
    orders USING (product_id)
GROUP BY product_id;
```

### 2. 统计每个客户买了多少商品
```sql
SELECT 
    user_name, SUM(unit_price * quantity) AS sales_amount
FROM
    users
        LEFT JOIN
    orders USING (user_id)
GROUP BY user_id;
```

### 3. 查看销量最大的两个商品
```sql
SELECT 
    product_name, SUM(quantity) AS sale_number
FROM
    products
        LEFT JOIN
    orders USING (product_id)
GROUP BY product_name
ORDER BY sale_number DESC
LIMIT 2;
```

### 4. 每个客户的消费次数
```sql
SELECT 
    user_name, COUNT(user_id) AS buy_number
FROM
    users
        LEFT JOIN
    orders USING (user_id)
GROUP BY user_name;
```

### 5. 各个价格区间内的商品的总销售额
```sql
SELECT 
    product_group.price_group, SUM(orders.sale_amount)
FROM
    (SELECT 
        product_id,
            product_name,
            (CASE
                WHEN price < 20 THEN '0-20'
                WHEN price >= 20 AND price < 30 THEN '20-30'
                WHEN price >= 30 AND price < 40 THEN '30-40'
                ELSE '>=40'
            END) AS price_group
    FROM
        products) AS product_group
        LEFT JOIN
    orders USING (product_id)
GROUP BY product_group.price_group;
```