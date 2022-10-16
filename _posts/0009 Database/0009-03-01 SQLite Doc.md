---
layout: post
title: SQLite Doc
categories: Database
description: Personal Notes
keywords: Database
mathjax: true
---

# Table
## .1 Create Table
在对数据库或表单的创建、删除操作中，可在对象名前加上 `if exists`/`if not exists`，以避免由重复操作导致的报错。
```sql
-- 创建
create table if not exists 表单名(
    列1名 数据类型 [修饰1],
    列2名 数据类型 [修饰2]
);

-- 删除
drop table if exists 表单名;

-- 描述：输出各列的定义信息（包括列名、数据类型、是否允许空值、默认值等）
describe 表单名;
```

**(1) 数据类型**:（示例中有详细说明）

||||
|---|---|---|
|`int(size)`| 整形| size 仅有显示意义，需与 `zerofill` 等修饰配合使用
|`decimal(s1, s2)`| 浮点数| 准确值；s1 表最大总位数，s2 表小数点后的位数，必填; 对于超出位数进行四舍五入，例如 decimal(5, 2) 34.439$\to$34.44
|`char(size)`| 字符| 存储空间固定 = size
|`varchar(size)`| 字符| 存储空间不固定，size 仅规定其上限

**(2) 修饰**:

|||
|-|-|
|`primary key`| 设置为<span style="background-color: yellow; color: black;">主键</span>，每个表的主键<u>唯一</u>(主键值必须唯一标识表中的每一行，且不能为 NULL)
|`NULL`| 表明任意行数据在该列的值可以为空
|`not NULL`| 表明任意行数据在该列的值都不能为空

示例：
```sql
create table if not exists T1(
    Id     char(10)     primary key,
    Brand  char(10)     not NULL,
    Price  decimal(8,2) not NULL,
    "Desc" Varchar(750) NULL
)
```


## .2 Insert Record

```sql
-- 插入一条有两列的record
insert into table1 values (a11, a12);

-- 插入多条数据
insert into table1 values
(a21, a22),
(a31, a32);

-- 插入一条仅为指定列赋值的record
insert into table1(col2, col2) values (a42, a41);
```

## .3 Create Temporary Table

Temporary table will be deleted when current session is terminated. Why use?
- Faster than creating a real table
- Useful for complex queries using subsets and joins

```sql
create temporary table TT1 as (
    select ...
    from ...
    (where)
)
```


## .4 Add Comments

```sql
SELECT Id
--, Brand (One line comment)
,Price
FROM PRODUCTS

SELECT Id
/*, Brand (Section comments)
,Price*/
FROM PRODUCTS
```

# Query
## 4.1 总体结构
```sql
select col1
from table1
(where) condition
(group by) col2
(having) condition
(order by) sorting
(limit)
```



## 4.2 各组成部分
### (1) 选取数据 select (into) from
```sql
-- 从表单中选取所有数据
select * from table1;
-- 根据选取的内容创建一张新表单
select * into table2 from table1;

-- 选取用户id和姓
select user_id, last_name from users;
-- 输出用户的全名
select concat(first_name,' ',last_name) as full_name
from users;

-- 统计每个位置有多少用户
select location, count(loaction) from users
group by location;

-- 查看该列有哪些不一样的数值（非重复值）
select distinct col1 from table1;
```
**correlation name**

```sql
select O.order_id, U.user_name
from orders O, users U
where O.user_id = U.user_id;
```

### (2) 限制条件 where 
```sql
select col from table1 where (限制条件);
```
多个条件之间可以用 `or`/`and` 并列，用 `not` 表否定

表示大小关系（时间也可以用符号比较）：
- `col = 10`
- `col <> 10` 不等于
- `col between 10 and 20` 限定范围
- `col is NULL`
- `col is not NULL`

表示从属关系：
- `col in (9, 10, 11)` 
- `col in (select col2 from table2)`

比较字符串：
- `col like '%soft%'` 选取包含 `soft` 字段的元素，例如 `banksoft.`
- `col like 'soft%'` 选取以 `soft` 字段开头的元素
- `col like 's%t'` 选取以 `s` 开头 `t` 结尾的元素
- `col_name like 's_ft%'` 下划线表示任意字符 (可以使用多个)

**AND vs. OR**:
AND 优先级大于 OR，也就意味着
```sql
Id=9 OR Id=10 AND Price>15
-- 等同于
Id=9 OR (Id=10 AND Price>15)
```
因此需要使用括号 `()` 来提升可读性


### (3) 聚合与分组 group by
根据商品状态分组，统计各不同状态的数据条目的数量及其均价
```sql
select
    prod_status, count(*), avg(prod_price)
from products
group by prod_status

-- 修改: 同时能够显示出各组内数据的商品名
select
    GROUP_CONCAT(distinct prod_name), -- distinct 去重
    count(*), avg(prod_price)
from products
group by prod_status
```

### (4) 后置条件 having
用于对已经经过选取、条件限制、分组之后的数据添加进一步的限制要求
```sql
select prod_status, sum(v1) as v1_sum, sum(v2) as v2_sum
from table1 
where v3 >= 0 
group by prod_status
having v1_sum + v2_sum >= 100;
```



### (5) 排序 order by
```sql
-- 升序排列（默认）
select * from table1 order by col1 (asc);
-- 降序排列，并取前三个最大的
select * from table1 order by col1 desc limit 3;
-- 符合排列，先根据col1升序，在其排序结果内再根据col2降序
select * from table1 order by col1 asc, col2 desc;
```

复合示例：
```sql
-- 取出table1中，生产日期大于2014年的物品中，价格前三贵的物品的名字
select col_name from table1 
where 
    col_date > '2015-1-1' 
order by col_price desc limit 3;
```


### (6) 切片 limit
```sql
-- 取前n条数据
select col1 from table1 limit n;

-- 取第n+1-n+m+1条数据
select col1 from table1 limit n, m;
```
`limit` 后的 `n`/`m` 都只能为常量/输入或自定义变量，不能为表达式

## 4.3 子查询 Subquery
嵌套在 `FROM`, `WHERE` or `HAVING` 中，以解决 query 依赖问题
值判断: =, >, <, <>(不等号), ...
集合判断: in, any, all, exists

```sql
-- 查看名字以“A”开头且电话号码以“5”结尾的顾客的信息
select * from (
    select * from Customer 
    where name like 'A%'
) as tem_C
where temp_C.phone like '%5';
```

**(1) IN**
```sql
-- 查看状态为新上架的商品订单
select * from orders
where product_id in (
    select product_id from products
    where sale_status = 'New'
);
```

**(2) EXISTS**
From `Drinks(name, manufacturer)`, `Sells(café, drink, price) `
```sql
-- 查看售价高于5元的drink信息
select * from Drinks D
where exists (
    select * from Sells
    where drink = D.name and price > 5
);
```
执行顺序：
(1) 首先执行一次外部查询，并缓存结果集，如 `select * from Drinks D`
(2) 遍历外部查询结果集的每一行记录，代入子查询中作为条件进行查询
(3) 如果子查询有返回结果，则EXISTS子句返回TRUE，这一行记录可作为外部查询的结果行，否则不能作为结果行



**(3) 嵌套子查询**
通过 `Customers`$\to$(customer_ID)$\to$`Orders`$\to$order_number$\to$`OrderItems` 来查找购买了牙刷的顾客

```sql
select Customer_name from Customers
where CustID in (
    select Customer_ID from Orders
    where Order_number in (
        select order_num from OrderItems
        where prod_name = "Toothbrush"
    )
)
```




# 5. Function
MySQL有丰富的函数支持，例如仅对于字符串的处理，就有[mysql.doc](https://dev.mysql.com/doc/refman/8.0/en/string-functions.html)



## 5.1 Case 分组

两种方式:
(1) 类似于 C# 中的 switch case
```sql
CASE input_expr
    WHEN when_expr THEN result_expr
    [...]
    [ELSE else_result_expr]
END
```

(2) 与 MySQL 略有不同（上一种方式不知道能不能在 MySQL 中使用）
```sql
SELECT
    col_name,
    price,
    CASE
        WHEN col_price < 20 THEN '0-20'
        WHEN col_price >= 20 AND col_price < 40 THEN '20-40'
        ELSE 'too expensive'
    END price_group
FROM
    table1;
``` 




## 5.3 Aggregation
`SUM()` `AVG()` `COUNT()` `MIN()` `MAX()` `GROUP_CONCAT()`

**AVG**
在 Aggregation 中使用 `CASE WHEN ELSE`

例如：统计好评在所有有效评价中的占比
- `comm=ENUM(‘Good’,'Bad','None')`，有效评价不包括 `'None'`
- 如果没有评价，则返回 `NULL`
```sql
select avg(case
        when comm='Good' then 1
        when comm='Bad' then 0
        else null 
end) as good_rate from Comments
```

**SUM**
```sql
select sum(c1) as sum1, sum(c2) as sum2
from table1;
```

`SUM()` 可用于统计某一条件的成立次数（Leetcode 1173）
```sql
-- 统计 col1,col2 值相等的数据的数量
select sum(col1 = col2) from table1;
```

同理，`AVG()` 等亦可，<span style="background-color: yellow; color: black;">但是 `COUNT()` 依旧会统计 False，因此需要利用其不会统计 NULL 的特性</span>（详见下个代码框中的第三行）

**COUNT**

```sql
select count(*) from table1;     -- 数据总个数
select count(col1) from table1;  -- 特定列的非空数据个数
select count(distinct col1) from table1;     -- 特定列去除重复值后的数据个数
select count(col1 > 0 or null) from table1;  -- 特定列数值大于0的数据个数
```
可以用于去重

```sql
-- 查看5号商品有几种不同的售价
select count(distinct product_price) from products
where product_id = "005"; 
```
**GROUP_CONCAT 文字聚合**

```sql
-- 查看每个买家购买的商品种类（根据字符排序）
select user_id, group_concat(distinct product_name order by product_name) 
from orders
group by user_id
```
**其他注意事项**:
- `NULL` 不会参与aggregation，除非当所选值均为 `NULL` 时则会返回 `NULL`。

## 5.5 String

**(1) Concatenation 连接字符串** (额外添加的字符需要用引号引起来)
```sql
str1 || str2
```

```sql
select 
FirstName || LastName as FullName,
City || '-' || State '-' Country as Location 
from table2
```

**(2) Trimming 消除字符串的首尾空格**
```sql
TRIM(str) --首尾
LTRIM(str) --首
RTRIM(str) --尾
```

**(3) Substring 字符串切片**
```sql
SUBSTR(str, 切片位置, 切片长度)
SUBSTR(str, 切片位置) --切到末尾
```

```sql
SUBSTR(Bruce, 2, 3) >>> ruc
SUBSTR(Bruce, 2) >>> ruce
```

**(4) 大小写**
```sql
UPPER(str)
LOWER(str)
```

## 5.6 Time/ Date
Date Formats

```sql
YYYY-MM-DD --DATE
YYYY-MM-DD HH:MI:SS --DATETIME
YYYY-MM-DD HH:MI:SS --TIMESTAMP
```
Functions

```sql
DATE('now') --当前日期
STRFTIME(format, date) --提取某个时间元素（年月日时分秒）
```
Example
获取当前的日期和时刻

```sql
STRFTIME('%Y %m %d', 'now')
STRFTIME('%H %M %S', 'now')
```
获取出生的年月日和当前年龄
<img src="/images/2022-07/Snipaste_2022-07-18_16-29-18.png"  width="70%">



## 5.7 NULL

```sql
coalesce(value_1, value_2, ...value_n) --返回输入列表中的第一个非 NULL 值
```

<img src="/images/2022-07/.png"  width="100%">
<img src="/images/2022-07/.png"  width="100%">
<img src="/images/2022-07/.png"  width="100%">





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


