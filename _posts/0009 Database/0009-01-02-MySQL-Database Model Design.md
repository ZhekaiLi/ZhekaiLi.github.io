---
layout: post
title: (MySQL) Database Model Design
categories: Database
description: Personal Notes
keywords: Database
mathjax: true
---

Reference: [MySQL 8.0 Reference Manual](https://dev.mysql.com/doc/refman/8.0/en/)

## 1. EER Model
由 database 创建 EER Model，效果如下
<img src="/images/2021-12/Screenshot 2021-12-19 at 11.00.44 AM.png" zoom="100%">

### 1.1 创建方式
<img src="/images/2021-12/Screenshot 2021-12-19 at 11.01.25 AM.png" width="80%">

然后选取目标数据库，其中可以进行一些自定义操作比如只选取部分tables

### 1.2 特点
可视化地展现各表单的内容以及它们之间的关系，尤其是能清晰展现主键和外键

### 1.3 示例
人力资源管理系统
<img src="/images/2021-12/Screenshot 2021-12-19 at 3.12.47 PM.png" width="80%">

## 2. ER模型
Entity Relation(ER)，是一种数据库的概念设计方式

### 2.1 组成部分

<img src="/images/2021-12/Screenshot 2021-12-19 at 7.02.59 PM.png" width="80%">

### 2.2 主要步骤
1. 确定实体(Entity)
2. 设计实体的属性
3. 设计实体之间的联系
4. 确定实体的键
5. 确定关系类型

### 2.3 应用示例

#### 公司员工和部门

1. 确定员工和部门分别为两个实体
2. 给每个实体设计属性
3. 明确实体间的关系：员工 `work in` 部门，且该关系包含一个时间属性 `since`

<img src="/images/2021-12/Screenshot 2021-12-19 at 1.33.17 PM.png" zoom="100%">

<img src="/images/2021-12/Screenshot 2021-12-19 at 1.33.27 PM.png" zoom="100%">

## 3. 设计范式
### 3.1 1NF
不能有多属性的列

### 3.2 2NF & 3NF
主键唯一，且其他列必须依赖于该主键（直接相关）

例如下图中的 `Capacity` 不依赖于主键 `Name`

<img src="/images/2021-12/Screenshot 2021-12-19 at 4.17.17 PM.png" width="70%">

因此需要做如下分割

<img src="/images/2021-12/Screenshot 2021-12-19 at 4.17.27 PM.png" zoom="100%">

## 4. 导入数据

### 4.1 导入 csv
在左侧SCHEMAS栏中，右键单击目标表单，选择 `Table Data Import Wizard`

### 4.2 导入过程中的问题
#### 4.2.1 数据类型不匹配
成功导入的前提是**数据类型能够完全匹配**。例如，在csv文件中某一列存储的时间格式是这样的 `2021.12.21-08:08:08`，但我们在创建表单时为对应列分配的数据类型为 `Datetime`，这将导致整个文件都无法导入

对应的解决方式有:
1. 使用python等工具直接修改csv文件中的时间格式
2. 在MySQL中将对应列的 `datetime` 类型改为 `varchar()`

#### 4.2.2 Foreign key的限制
外键的设置会限制导入数据的顺序，例如当表2的某列通过外键关联了表1的某列，那么表1就必须在表2之前导入，这就不太方便了
```sql
set foreign_key_checks = 0; -- 导入前关闭外键检查
set foreign_key_checks = 1; -- 导入后打开
```


## 5. 数据类型转换
对应 Section 4.1 中提到的 string to datetime 的问题，转化目标：
- 将字符格式 `1987-06-21T04:00:00.000Z (string)`
- 转化为时间 `1987-06-21 04:00:00.000 (datetime)`

查找 [Reference Manual](https://dev.mysql.com/doc/refman/8.0/en/) 是否存在相关函数：
<img src="/images/2021-12/Screenshot 2021-12-21 at 11.25.32 AM.png" width="80%">

找到函数：`STR_TO_DATE(str, fomat)`
```sql
select str_to_date('01,05,2013', '%d,%m,%Y');
```
完整示例：修改数据类型
```sql
create table employees(
    employee_id int not null,
    hire_date datetime
);
-- 为了能成功导入数据，先修改对应列的数据类型为 varchar()
alter table employees modify column hire_date varchar(255);

-- 使用 table import wizard 导入 csv

-- 数据类型转换
update employees set hire_date = str_to_date(hire_date, '格式');
-- 最后把对应列的数据类型改回 datetime
alter table employees modify column hire_date datetime;
```
