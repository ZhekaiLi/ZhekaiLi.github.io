---
layout: wiki
title: Power Pivot
cate1: Excel
cate2: 
description: 
keywords:
---

LINKs Back:
[WIKI: Power BI](/_wiki/power%20bi.md)


Power Pivot 能够帮助我们管理百万级的数据

# 1. Power Pivot UI
## 1.1 Open Power Pivot
**(1) 添加 Power Pivot 选项至菜单栏**
- 菜单栏点击 `File` $\to$ 左侧栏最下面点击 `Options` 
- 在弹窗中进行如下选择 $\to$ 点击右边的 `Go...`
<img src="/images/2022-05/Snipaste_2022-05-30_15-45-19.png"  width="100%">
- 在弹窗中勾选 `Microsoft Power Pivot for Excel`

**(2) 打开界面**
- 菜单栏点击 `Power Pivot`$\to$`Manage`
- 界面如下，长的类似于 Power Query
<img src="/images/2022-07/Snipaste_2022-07-08_19-25-07.png"  width="100%">






# 2. Data Model
Data Model 可以看作是 Power Pivot 里的一张张表，是一种用于分析的数据储存形式

<img src="/images/2022-07/Snipaste_2022-07-08_19-42-01.png"  width="100%">



## 2.1 Add Data Model
LINKs Back:
[WIKI: Power BI - 3. Add Calender Model with DAX](/_wiki/power%20bi.md#3-add-calender-model-with-dax)

在添加 Data Model 的同时会创建对应的 Connection

<img src="/images/2022-07/Snipaste_2022-07-08_19-50-05.png"  width="40%">

**M1: Use Power Query**
- 需要勾选 `Add this data to the Data Model`
<img src="/images/2022-07/Snipaste_2022-07-08_19-35-08.png"  width="40%">

**M2: Use Power Pivot**
- 菜单栏点击 `Power Pivot`$\to$`Add to Data Model`

**M3: Directly From Database**
- Power Pivot 的菜单栏 `Home`$\to$`Get External Data`$\to$`From Database`

**Create Calender Table**
创建一个用于储存日期数据的 Data Model(包含日期的各种形式，对应的星期几、年月日等)，用于和日期相关的查找、Merge等操作

<img src="/images/2022-07/Snipaste_2022-07-08_19-48-15.png"  width="100%">






# 3. Relationship Among Data Model

Relationship has three normal types: `one-to-one`, `one-to-many`, `many-to-many`

而 Data Model 主要分为两种类型:
- Look-up Table 存放更新频率低的数据，一般作为 Data Table 的查找匹配对象
- Data Table 存放更新频率高的数据

例如: Customers, Products and Salespeople 作为 Look-up Table, Orders 作为 Data Table

<img src="/images/2022-07/Snipaste_2022-07-11_20-45-20.png"  width="100%">

通常情况下，Look-up Table 与 Data Table 之间存在 `one-to-many` 关系，这种关系是合理的、不会出现异议。例如上图每个订单都只对应一个顾客和一个销售者

然而，它们之间有时候会出现 `many-to-many` 关系，例如上图的 Products Table-to-Orders Table, 因为一个订单可以包含多种商品，而一种商品可能出现在多个订单内，<span style="background-color: yellow; color: black;">这就会导致查找的不确定性</span>

解决方式是再添加一个 Orders Item Table, 因为每个订单商品只对应一个订单与一种商品，从而消除了 `many-to-many`


<img src="/images/2022-07/Snipaste_2022-07-11_20-50-59.png"  width="100%">


<img src="/images/2022-07/.png"  width="100%">

## 3.1 View Relationship
打开 Power Pivot 界面$\to$点击`Diagram View`$\to$将光标悬停在连线上

例如，下图显示的是在 Chapter 4.3.2 中创建的 relationship

<img src="/images/2022-07/Snipaste_2022-07-09_10-12-10.png"  width="100%">



## 3.2 Reorganize Relationship
默认情况下各个 Data Model 的排版是混乱的

推荐的排版方式如下:
- Look-up table 放在最上排
- Data table 放在下排

这是因为 look-up table 一般用于查找匹配，因此适合放在最方便查看的位置

<img src="/images/2022-07/Snipaste_2022-07-09_10-39-19.png"  width="100%">




## 3.3 Create Relationship
### 3.3.1 In Relationship Viewer
例如下图，左键按住 lkp_Customer 中的 ID，然后拖动至 Orders 中的 CustomerID 

<img src="/images/2022-07/Snipaste_2022-07-09_10-48-22.png"  width="100%">


### 3.3.2 From PivotTable
了来自两个分别来自不同 Data Model 的 fields 后，需要为这两个 Data Model 创建 relationship。一般直接点击 `Auto-Detect...` 即可

<img src="/images/2022-07/Snipaste_2022-07-09_10-02-14.png"  width="50%">

当然也可以点击 `CREATE...` 手动创建 relationship

<img src="/images/2022-07/Snipaste_2022-07-09_10-05-50.png"  width="100%">



## 3.4 Edit/ Remove Relationship
右键单击任一关系线后可以在弹出的小窗中选择删除或编辑 relationship，编辑界面如下:

<img src="/images/2022-07/Snipaste_2022-07-09_10-17-01.png"  width="80%">






# 4. PivotTable From Data Model
PivotTable 可以基于多个 Data Model 创建
## 4.1 Create
**Prerequisite**
基于多个 Data Model 创建 PivotTable 的前提是这些 Data Model 之间需要存在完整的 relationships (例如下图)。Relationship 的查看/创建方式详见 Chapter 4

<img src="/images/2022-07/Snipaste_2022-07-09_10-58-33.png"  width="80%">

**Create Steps:**
- 点击菜单栏 `Insert`$\to$`PivotTable`$\to$`From Data Model`
- 点击设置符号可以修改排版方式，以更完整地显示各个表单

<img src="/images/2022-07/Snipaste_2022-07-08_20-25-58.png"  width="60%">





# 5. Data Analysis in Power Pivot
> **Formatting**

<img src="/images/2022-07/Snipaste_2022-07-09_19-36-22.png"  width="70%">

> **Add Column Through DAX Function**

DAX(Data Analysis eXpression) 类似于普通 Excel 函数，区别在于其作用的对象是列而不是单元格

例如下图，在最右侧单元格内输入 `=FUNC(表名[列名])`

<img src="/images/2022-07/Snipaste_2022-07-09_19-40-09.png"  width="100%">

> **Add Hierarchy**

在 Data Model 中添加 Hierarchy 可以为在 PivotTable 中的数据处理带来很大的便利性。例如下图的 Hierarchy 来自系统快捷创建的    `Calender` Model (详见 Chapter 3.1 最后)

<img src="/images/2022-07/Snipaste_2022-07-09_19-44-04.png"  width="60%">

自主添加 Hierarchy: 例如为 `Customer` Model 的地理位置信息添加 Hierarchy (County > State > City)
- 首先打开 `Diagram View` 界面，并将目标 Data Model 最大化显示
<img src="/images/2022-07/Snipaste_2022-07-09_19-53-35.png"  width="100%">

- 然后点击右上角的小黄标新建一个 Hierarchy，并由大到小把层级对象依次拖进去
<img src="/images/2022-07/Snipaste_2022-07-09_19-55-52.png"  width="80%">

效果如下。展开 Hierarchy: 直接点击地名单元格左边的加号，或是点击红框内的 `Drill Down/Up` 访问层级，以及点击加减号展开层级

<img src="/images/2022-07/Snipaste_2022-07-09_21-46-06.png"  width="40%">

> **Distinct Count**

这是 PivotTable based on Power Pivot 独有的属性

例如下图想通过订单数据来统计每个地区的消费者个数

<img src="/images/2022-07/Snipaste_2022-07-09_21-56-19.png"  width="80%">









# 6. Data Visualization with Power Pivot

PivotTable 不支持很多类型的图(Treemap, Histogram, Sunburst...)，因此我们需要把 PivotTable 中的数据转化为普通 Excel 单元格，再基于这些普通单元格构建图

<img src="/images/2022-07/Snipaste_2022-07-10_08-55-13.png"  width="80%">

以下图为例，目标是构建一张能够表示层级关系的 Sunburst 图(Slicer 的添加方式: 菜单栏 `PivotTable Analyze`$\to$`Filter`$\to$`Insert Slicer`)

<img src="/images/2022-07/Snipaste_2022-07-10_09-04-09.png"  width="100%">

**(1) 展开 Hierarchy，使其看起来像普通单元格**
- 选中 PivotTable, 菜单栏 `Design`$\to$`Layout`$\to$`Reprot Layout`$\to$`Show in Tabular Form`
- ...$\to$`Layout`$\to$`Grand Totals`$\to$`Off for Rows and Columns`

<img src="/images/2022-07/Snipaste_2022-07-10_09-08-42.png"  width="80%">

**(2) Convert PivotTable to Formulas**
- 选中 PivotTable, 菜单栏 `PivotTable Analyze`$\to$`Calculations`$\to$`OLAP Tools`$\to$`Convert to Formulas`
- 完美! 这样我们就可以插入表示 Hierarchy 的 Sunburst 图了

<img src="/images/2022-07/Snipaste_2022-07-10_09-13-30.png"  width="100%">





# 7. DAX Measures
在 Chapter 6 的第二小节，我们使用 DAX Function 在 Power Pivot 中创建了一列数据。更进一步的 DAX 还能应用于创建 DAX Measures

**Measures** is a dynamic calculaiton where the results change contextually (filter...). 例如下一图的最后一列是直接通过下二图这样的方式创建的，因此存在不少问题:
- 列名 `Sum of SubTotal2` 不好，虽说可以修改，但是每次这么创建都得改名
- 数据格式不对，同样的也需要在每次创建时修改

<img src="/images/2022-07/Snipaste_2022-07-10_10-03-35.png"  width="100%">

<img src="/images/2022-07/Snipaste_2022-07-10_10-04-37.png"  width="50%">

That's why we need DAX Measures. 两种创建方式: 

**(1) Method 1: In Power Pivot Data View**
在灰色粗横线下的单元格内输入 `Measure名:=FUNC(表名[列名])`，注意等号前面还有一个冒号，然后在菜单栏修改 `Formatting` 为目标格式

<img src="/images/2022-07/Snipaste_2022-07-10_10-11-11.png"  width="100%">

**(2) Mehotd 2: Through PivotTable Fields Window**
- 右键单击 Data Model 名$\to$打开 `Add Measure`
<img src="/images/2022-07/Snipaste_2022-07-10_10-15-35.png"  width="60%">

- 在弹窗中完成如下三处修改 
<img src="/images/2022-07/Snipaste_2022-07-10_10-27-14.png"  width="100%">

效果如下, Perfect:

<img src="/images/2022-07/Snipaste_2022-07-10_10-28-36.png"  width="100%">






# 8. DAX Function

**(1) 添加筛选条件** `CALCULATE(Expression, [Filter1], ...)`

例如，筛选出自行车的销售数据

<img src="/images/2022-07/Snipaste_2022-07-10_19-59-31.png"  width="100%">

根据 Slicer 的筛选显示去年同期的数据

<img src="/images/2022-07/Snipaste_2022-07-10_22-14-33.png"  width="80%">
