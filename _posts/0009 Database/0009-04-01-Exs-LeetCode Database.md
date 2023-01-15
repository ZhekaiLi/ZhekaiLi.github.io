---
layout: post
title: LeetCode Database Practice
categories: Database
description: Personal Notes
keywords: 
mathjax: false
---

## Methods

可以使用 `with` 语句来创建临时表单。这样会清楚明白很多
```sql
with T1 as (
    select ...
)
select ... from T1
...
```

创建多个临时表单
```sql
with T1 as (
    select ...
), T2 as (
    select ...
)
```


## 176. Second Highest Salary
如果遇到以下需求：若查询不到匹配选项，则返回 `NULL`。可以使用嵌套 select 的方式：
```sql
select (select ...) as num;
```

```sql
SELECT
    (SELECT DISTINCT
            Salary
        FROM
            Employee
        ORDER BY Salary DESC
        LIMIT 1 OFFSET 1) AS SecondHighestSalary
;
```

## 193. Delete Duplicate Emails
```sql
-- 1
delete p1 from Person p1, Person p2
where p1.Email = p2.Email and p1.Id > p2.Id;

-- 2
delete from Person
where Id in (
    select p.Id from(
        select p1.Id from Person p1, Person p2
        where p1.Email = p2.Email and p1.Id > p2.Id
    ) as p
);
```

## 1082.

`AVG,SUM,COUNT,MIN,MAX` 为 aggregation，只能应用于列数据上：
```sql
-- 选取各商品的均价
select AVG(price) from Products
group by prod_id;
```

`ALL,ANY` 则只能应用于一组被 Select 语句筛选出来的数据组：
```sql
-- 查找表1中商品，其价格需要高于表2中的所有商品
select prod_id from Products_1
where price > ALL(select price from Products_2)`
```
## 1435.

通过 select 实现创建数据（类似插入的效果）。例如创建一个包含一条数据的 id + name 表，007 和 'Bonder' 都不在原表 People 中
```sql
select 007 as 'id', 'Bonder' as 'name' from People;
```
|id|name|
|-|-|
|07|Bonder|

## 1511. Customer Order Frequency
在 aggregation 中使用 if 语句
```sql
-- 筛选出在六月和七月消费均超过100的用户
select user_id from Orders
group by user_id
having SUM(IF(MONTH(date) = 6, qauntity, 0) * price) > 100
    and SUM(IF(MONTH(date) = 7, qauntity, 0) * price) > 100
```

## 查询各个部门里薪资最高的员工

Employees:
|employee_id|salary|department_id|
|-|-|-|
- 首先查找出各个部门的最高薪资
- 再查找所有满足 `(department_id, salary) in (以上查找结果)` 的员工
```sql
select department_id, employee_id, salary
from Employees
where (department_id, salary) in (
    select department_id, max(salary)
    from Employees
    group by department_id
)
```

## 挑选出某个属性连续多次的对象
例如，挑选出连续四天有购买记录的买家id

Orders:
|id|order_date|
|-|-|

```sql
select distinct id
from Orders O1
join Orders O2
on O1.id = O2.id 
    and DATEDIFF(O2.order_date, O1.order_date) between 1 and 3
group by O1.id, O1.order_date
having count(distinct O2.order_date) = 3
```
这里的关键是最后两行：在进行二次分组之后，`count(distinct O2.order_date)=3` 表示该 `O1.order_date` 之后有三个连续的日期，算上自身一共四个

## 统计所有区间内的对象数量
例如，统计每辆车的上车人数

Buses
|bus_id|arr_time|
|-|-|
|1|1|
|2|5|
|3|9|

Passengers
|p_id|arr_time|
|-|-|
|1|1|
|2|6|
|3|7|

**Output**
|bus_id|count(passengers)|
|-|-|
|1|1|
|2|0|
|3|2|

这道题的关键思路是，首先建立一张表格，能够同时显示第 i 辆车的 arrival_time 及其上一辆车的 arrival_time
|bus_id|$t_i$|$t_{i-1}$|
|-|-|-|
|1|1|-1|
|2|5|1|
|3|9|5|

这样以来，可以很方便的通过 `left join Passengers` 来统计各个区间内上车的人数

```sql
with T as (
    select B1.bus_id, B1.arrival_time as t1,
        ifnull(max(B2.arrival_time),-1) as t2
    from Buses B1
    left join Buses B2
    on B1.arrival_time > B2.arrival_time
    group by B1.bus_id
)

select T.bus_id, 
    sum(P.arrival_time is not null) as passengers_cnt
from T
left join Passengers P
on T.t1 >= P.arrival_time and T.t2 < P.arrival_time
group by T.bus_id
order by T.bus_id
```

## 用滑动窗口统计属性
例如，想要用滑动窗口，统计三天内(current day + 2 days before) 的 moving average & sum 

Customer
| customer_id | name         | visited_on   | amount      |
|-------------|--------------|--------------|-------------|
| 1           | Jhon         | 2019-01-01   | 100         |
| 2           | Daniel       | 2019-01-02   | 110         |
| 3           | Jade         | 2019-01-03   | 120         |
| 4           | Khaled       | 2019-01-04   | 130         |
| 5           | Winston      | 2019-01-04   | 110         | 
| 6           | Elvis        | 2019-01-05   | 140         | 

**Output**
| visited_on   | sum(amount) | avg(amount) |
|--------------|-------------|-------------|
| 2019-01-03   | 330         | 110         |
| 2019-01-04   | 470         | 156.67      |
| 2019-01-05   | 500         | 166.67      |

```sql
with T as (
    select visited_on, sum(amount) as amount
    from Customer
    group by visited_on
    order by visited_on
)

select T1.visited_on, sum(T2.amount), avg(T2.amount),2)
from T T1 left join T T2
on datediff(T1.visited_on, T2.visited_on) between 0 and 2
group by T1.visited_on
having count(*) >= 3
```
