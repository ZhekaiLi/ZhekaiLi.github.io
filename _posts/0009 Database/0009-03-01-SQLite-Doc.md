<!-- ---
完善中，暂不发布
layout: post
title: SQLite Doc
categories: Database
description: Personal Notes
keywords: Database
mathjax: true
--- -->


SQLite 是一种小型化易部署的数据库，其大部分语法都能和 MySQL 通用

# 4. Query



# 5. Function
## 5.1 Case
## 5.3 Aggregation

## 5.5 String
**(1) Length**

```sql
length(str)
```
## 5.6 Time/ Date
## 5.7 NULL




<!----------------------------------------------------------->
# 7. JOINS
<span style="background-color: yellow; color: black;">顺序位置</span>：列表的 JOINS 用 `on` 来表示条件，其后可以再跟条件 `where`（亦可不跟）

<img src="/images/2021-12/Screenshot 2021-12-12 at 9.50.50 AM.png" zoom="0%">

目标：生成新表单 user_name \| product_name \| unit_price \| quantity
- `users`: user_id \| user_name
- `products`: prodcut_id \| product_name
- `orders`: order_id \| user_id \| product_id \| unit_price \| quantity



## 7.1 INNER JOIN (or JOIN)
```sql
select
    user_name, product_name, unit_price, quantity
from 
    orders inner join (users, products)
on
    orders.user_id = users.user_id and orders.product_id = products.product_id;
```
或者
```sql
-- or
select user_name, product_name, unit_price, quantity
from orders 
inner join users on orders.user_id = users.user_id
inner join products on orders.product_id = products.product_id;
```



## 7.3 LFTT/ RIGHT JOIN
= LEFT/ RIGHT OUTER JOIN

保留左/ 右表单的全部内容，并取另一张表单中满足对应条件的数据。

以下面这段代码为例，
1. `products` 包含2个商品(A,B)的名称和价格，`orders` 包含4条订单信息(数量：A1,B2,C1)。LEFT JOIN的结果为一个包含3行数据的表单：左半边相当于在 `products` 的基础上添加了一条重复的商品B的名称和价格
2. `products` 包含4个商品(A,B,C,D)的名称和价格，`orders` 包3条订单信息(数量：A1,B1,D1)。LEFT JOIN的结果为一个包含4行数据的表单：左半边等同于 `products`；右半边相当于在 `orderss` 的基础上添加了一条null行

```sql
select * from products left join orders
on products.product_id = orders.product_id;

-- or
select * from products left join orders
using (product_id);
```



## 7.4 FULL OUTER JOIN
保留两个表单的全部内容，为无法匹配的内容填入 `NULL`


## 7.5 UNION (ALL)
相比于 JOIN 的横向匹配
- UNION ALL 为纵向数据堆叠，前提是需要堆叠的表单需要由相同的列
- UNION 则会去除重复行数据

```sql
select City, Country from Customers
where Country = "Germany"
UNION
select City, Country from Suppliers
where Country = "Germany"
```


select count(*), C.CustomerId, C.FirstName, C.LastName, C.Email
from Customers C
left join Invoices I 
on C.CustomerId = I.CustomerId
group by C.CustomerId





# 9. View
View (视图) 是一种虚拟表，其内容由查询定义，本身并不包含数据。视图看起来和真实的表完全相同，但其中的数据来自定义视图时用到的基本表，并且在打开时动态生成。与直接操作基本表相比，视图具备以下优点：
- 提高数据安全性：在设计数据库时可以针对不同的用户定义不同的视图，使用视图的用户只能访问他们被允许查询的结果集
- 数据独立：视图的结构定义好之后，如果增加新的关系或对原有的关系增加新的字段对用户访问的数据都不会造成影响

例如对以下数据表：
Frequents (customer, cafe), Sells (cafe, drink, price)
创建视图 CanDrink (customer, drink) 以查看顾客可能喝的饮料
```sql
CREATE VIEW CanDrink AS
SELECT customer, drink
FROM Frequents, Sells
WHERE Frequents.cafe = Sells.cafe;
```

**Table vs. View**
**联系（修改）：**
1. 对基本表的修改会直接影响视图中对应的内容
2. 无法修改基于多个基本表的视图
3. 对基于单一基本表的视图的修改会影响基本表中对应的内容

**区别：**
1. 视图是已经编译好的sql语句，没有实际的物理记录；表有
2. 表是内容，视图是窗口 
3. 视图的建立和删除只影响视图本身，不影响对应的基本表



<!----------------------------------------------------------->


# 10. Data for Unknown Quality
## Pivot Data

需求: 依据下一图中的 `parameter_name` 将占两行的数据压缩成占一行(如下一图)

<img src="/images/2022-07/Snipaste_2022-07-20_10-54-21.png"  width="100%">

<img src="/images/2022-07/Snipaste_2022-07-20_11-02-27.png"  width="100%">

使用了两个 `CASE` 之后，还需使用 `MAX()` 函数来去掉 NULL 值并实现两行合并成一行
<img src="/images/2022-07/Snipaste_2022-07-20_10-58-36.png"  width="100%">
<img src="/images/2022-07/Snipaste_2022-07-20_11-02-02.png"  width="100%">


## Identify Unreliable Data (include NULLs)

JOIN 时添加一行 `AND ...`(下左图)，以防止 NULL 值的相互匹配(下右图)

<img src="/images/2022-07/Snipaste_2022-07-20_10-42-06.png"  width="35%">
<img src="/images/2022-07/Snipaste_2022-07-20_10-42-32.png"  width="62.5%">




<img src="/images/2022-07/.png"  width="100%">
<img src="/images/2022-07/.png"  width="100%">
<img src="/images/2022-07/.png"  width="100%">
<img src="/images/2022-07/.png"  width="100%">
<img src="/images/2022-07/.png"  width="100%">
<img src="/images/2022-07/.png"  width="100%">
<img src="/images/2022-07/.png"  width="100%">


