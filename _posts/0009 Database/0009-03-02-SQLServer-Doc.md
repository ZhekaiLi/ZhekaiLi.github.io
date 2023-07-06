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

# SQL Server Doc
</center>

<span style="background-color: yellow; color: black;">以下内容仅包括 SQL Server 与 MySQL 不同之处，其余请参考 MySQL Doc</span>

<!----------------------------------------------------------->
## 2. Table
### 2.2 修改
修改表名

```sql
exec sp_rename 'OldTableName', 'NewTableName'
```
