---
layout: post
title: Data Cleaning 数据清洗
categories: Database
description: Personal Notes
keywords: Database
mathjax: true
---

Reference: [MySQL 8.0 Reference Manual](https://dev.mysql.com/doc/refman/8.0/en/)


# 1. Import Data (导入数据)
## 1.1 MySQL
### 1.1.1 Import from .csv
在左侧SCHEMAS栏中，右键单击目标表单，选择 `Table Data Import Wizard`
<img src="/images/2022-10/Snipaste_2022-10-07_12-33-26.png" width="50%">

#### (a) Poblems 
**(1) 数据类型不匹配**
成功导入的前提是**数据类型能够完全匹配**。例如，在csv文件中某一列存储的时间格式是这样的 `2021.12.21-08:08:08`，但我们在创建表单时为对应列分配的数据类型为 `Datetime`，<span style="background-color: yellow; color: black;">这将导致整个文件都无法导入</span>

对应的解决方式有:
1. 使用python等工具直接修改csv文件中的时间格式
2. 在MySQL中将对应列的 `datetime` 类型改为 `varchar()`

**(2) Foreign key的限制**
外键的设置会限制导入数据的顺序，例如当表2的某列通过外键关联了表1的某列，那么表1就必须在表2之前导入，这就不太方便了
```sql
set foreign_key_checks = 0; -- 导入前关闭外键检查
set foreign_key_checks = 1; -- 导入后打开
```


#### (b) Solution
应对数据类型不匹配所导致的数据大量丢失的问题，可行的办法之一就是先在 excel 中将所有单元格均设置为 TEXT。然后在 `Import Wizard` 中将所有列的数据类型也设置为 TEXT，这样能够保证数据导入的完整性

使用下个 section 中的方式重新设置各列的数据类型






# 2. Data Cleaning
## 2.1 Define data type (判断数据类型)
判断字符串是否只包含数字
```sql
-- 统计 col1 中无法被转换成数字的字符串的个数
-- col1 regexp '[^0-9.]' 对于只包含数字和小数点的字符串返回 0
select sum(col1 regexp '[^0-9.]') from table1;
```

## 2.2 Supstitue data
```sql
update table1 set col1 = 'value' where 'condition';
```

例如，把 col1 中不只包含数字的字符串设置为 NULL
```sql
update table1 set col1 = NULL where col1 REGEXP '[^0-9.]';
```

<span style="background-color: yellow; color: black;">注意！当sql_safe_updates = true时将无法进行删除/修改操作，需将其设置为false</span>
```sql
set sql_safe_updates = false;
```


## 2.3 Change data type
把 col1 转换为 INT 类型的数据列
```sql
ALTER TABLE table1.col1
CHANGE COLUMN col1 col1 INT NULL DEFAULT NULL ;
```
