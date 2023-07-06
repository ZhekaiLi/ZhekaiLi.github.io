---
layout: post
title: MySQL Doc
categories: Database
description: Personal Notes
keywords: Database
mathjax: true
topmost: true
---

<center>

# Oracle SQL Doc
</center>

<span style="background-color: yellow; color: black;">以下内容仅包括 Oracle SQL 与 MySQL 不同之处，其余请参考 MySQL Doc</span>

<!----------------------------------------------------------->
## 4. Query (Select)
### 4.1 Overall
```sql
select col1
from table1
(where) condition
(group by) col2
(having) condition
(order by) sorting
```


### 4.2 Components
#### (6) Limit
不同于 MySQL，Oracle SQL 并不使用 `limit` 关键字，而是使用 `rownum` + `where` 来实现类似功能

```sql
-- MySQL
select col1 from table1 limit n;

-- Oracle SQL
select col1 from table1 where rownum <= n;
```


