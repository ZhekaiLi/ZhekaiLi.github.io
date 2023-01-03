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


# 2. Table
Check information of all the columns in a table

`PRAGMA table_info(tb)`

For example, for a table called 'Pets'
|PetId|PetName|TypeId|
|-|-|-|-|
|1|Bob|1|
|2|Sam|1|
|3|Tom|2|

```py
PRAGMA table_info(Pets)
>>>
cid         name        type        notnull     dflt_value  pk        
----------  ----------  ----------  ----------  ----------  ----------
0           PetId       INTEGER     0                       1         
1           PetName                 0                       0         
2           TypeId                  0                       0 
```




# 5. Function
## 5.1 Case

## 5.3 Aggregation

## 5.5 String
**(1) Length**

```sql
length(str)
```


# 10. C.R.U.D Methods
- Create - INSERT
- Read - SELECT
- Update - UPDATE
- Delete - DELETE





<img src="/images/2022-07/.png"  width="100%">
<img src="/images/2022-07/.png"  width="100%">
<img src="/images/2022-07/.png"  width="100%">
<img src="/images/2022-07/.png"  width="100%">
<img src="/images/2022-07/.png"  width="100%">
<img src="/images/2022-07/.png"  width="100%">
<img src="/images/2022-07/.png"  width="100%">


