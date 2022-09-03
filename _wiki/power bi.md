---
layout: wiki
title: Power BI
cate1: Others
cate2: 
description: 
keywords:
---

Power BI 是一个数据可视化工具

# 1. Import Data

Power BI 支持非常丰富的数据源

<img src="/images/2022-07/Snipaste_2022-07-11_21-41-28.png"  width="100%">

## 1.1 Import From Excel
如果选择 From Excel Workbook, 则会使用 Power Query 导入数据([WIKI: Excel Power Query](excel/excel-power%20query.md)), 导入完成后界面如下，其中每张导入的数据表都是一个 Data Model([WIKI: Excel Power Pivot](excel/excel-power%20pivot.md))

<img src="/images/2022-07/Snipaste_2022-07-11_21-45-42.png"  width="100%">



## 1.2 View Data
如上图，在导入数据后发现看不到数据，这是因为我们的 Work Place 仍停留在 `Report` 页面，因此需切换到 `Data` 页面

<img src="/images/2022-07/Snipaste_2022-07-11_21-48-31.png"  width="100%">



## 1.3 Relationship Among Data Models
类似于 Power Pivot([WIKI: Excel Power Pivot](excel/excel-power%20pivot.md)), Power BI 在处理由 Excel 导入的数据时也是基于 Data Model, 因此需要设置 Relationships

<img src="/images/2022-07/Snipaste_2022-07-11_21-58-03.png"  width="100%">



## 1.4 Add Measure

在右侧 Fields 窗口中右键单击目标 Data Model$\to$选择 `New Measure`$\to$在上方 formula bar 中输入 `Measure_Name=FUNC(...)`

**Group Non-Measures**: 我们创建的 Measures 一般使用频率较高，然而由于默认状态下 Measures 和 Non-Measures 都是按照首字母排序放一起的，因此会如下左图显得比较乱，我们希望实现下右图的效果

<center>
<img src="/images/2022-07/Snipaste_2022-07-12_19-53-21.png"  width="25%">&emsp;&emsp;&emsp;    
<img src="/images/2022-07/Snipaste_2022-07-12_20-06-02.png"  width="33.5%">
</center>

- 首先切换到 `Model` 页面$\to$右键单击目标 Model$\to$选择 `Select columns`
  
<img src="/images/2022-07/Snipaste_2022-07-12_20-03-06.png"  width="100%">

- 其次在右侧 `Properties` 栏目中完成如下命名

<img src="/images/2022-07/Snipaste_2022-07-12_20-05-12.png"  width="100%">



## 1.5 Add Hierarchy
例如，创建一个关于时间的 Hierarchy:
- 点击最大单位 Fiscal Year 右侧的省略号$\to$选择 `Create hierarchy`$\to$改名为 Fiscal Date
<img src="/images/2022-07/Snipaste_2022-07-14_10-26-17.png"  width="40%">
- 由大到小依次加入其他层级 Fiscal Quater > Fiscal Month > Day
<img src="/images/2022-07/Snipaste_2022-07-14_10-30-18.png"  width="60%">







# 2. Visualization

已知如下五个 Data Models 的 Relationships

<img src="/images/2022-07/Snipaste_2022-07-11_22-05-35.png"  width="100%">

## 2.1 Bubble Chart in GeoMap
需求: 查看各个每个国家的每个州的总顾客消费能力

(1) 把州数据 `Customer[State]` 拖入 `Report` 页面，Power BI 会将其自动识别为地理位置信息，并通过地图显示

<img src="/images/2022-07/Snipaste_2022-07-11_22-10-41.png"  width="100%">

(2) 把消费能力定义为购买商品的总价值，因此需在 `Order_Items` Model 中创建一个 Measure `Consumption`
- 在右侧 Fields 窗口中右键单击 `Order_Items`$\to$选择 `New Measure`$\to$在上方 formula bar 中完成如下输入
<img src="/images/2022-07/Snipaste_2022-07-11_22-15-47.png"  width="100%">
- 把新建的 Measure 拖入 `Bubble Size` 栏，可以看到地图中气泡的大小有了区分
<img src="/images/2022-07/Snipaste_2022-07-11_22-16-49.png"  width="100%">

(3) 最后给不同的国家上色以区分: 把 `Customer[Country]` 拖入 `Legend` 栏

<img src="/images/2022-07/Snipaste_2022-07-11_22-19-42.png"  width="100%">

### 2.1.1 Avoid confused GeoPosition
观察上图右下方，发现非洲有一个表示法国的橙色点，并且美东海岸也有一个表示加拿大的蓝色点，出现这种情况是因为这些国家存在同名的 state

**Solution**: 在 Data Model 中新建一个 Column `Region`
- 右键单击目标 Model$\to$点击 `Edit query` 打开 Power Query 界面
<img src="/images/2022-07/Snipaste_2022-07-14_10-01-50.png"  width="50%">

- 完成如下创建后，将 Location 栏原本的 `State` 替换为 `Region`
<img src="/images/2022-07/Snipaste_2022-07-14_10-08-11.png"  width="100%">





## 2.2 TreeMap

需求: 查看不同国家的总消费能力

有了 Chapter 2.1 的经验，创建 TreeMap 非常简单

<img src="/images/2022-07/Snipaste_2022-07-11_22-23-20.png"  width="100%">

<span style="background-color: yellow; color: black;">Power BI 牛逼的一点是图表之间能够互动</span>，例如如果我点击上图最大的表示 US 的紫色色块，那么在 TreeMap 中其他色块颜色变浅的同时，左侧 GeoMap 也会切换到美国

<img src="/images/2022-07/Snipaste_2022-07-11_22-26-04.png"  width="70%">

同样的，如果我点击 GeoMap 中表示加州的大紫圈，右侧 TreeMap 也会有变化

<img src="/images/2022-07/Snipaste_2022-07-11_22-27-15.png"  width="70%">



## 2.3 Matrix
<img src="/images/2022-07/Snipaste_2022-07-12_10-18-16.png"  width="100%">



## 2.4 Card
用于直接显示一些重要的数据
<img src="/images/2022-07/Snipaste_2022-07-12_20-08-28.png"  width="100%">

修改 Value 和 Label 的颜色 & 设置背景为透明（关闭背景）
<img src="/images/2022-07/Snipaste_2022-07-12_20-15-45.png"  width="48%">&emsp; <img src="/images/2022-07/Snipaste_2022-07-12_20-17-04.png"  width="46%">




## 2.4 Area Chart
创建方式非常简单。有一个特点在于它可以联动 Hierarchy ([Section 1.5](#15-add-hierarchy))，以实现如下效果，即在图中改变显示的层级:

<img src="/images/2022-07/Snipaste_2022-07-14_10-34-19.png"  width="100%">

这种 x-y 图还可以为其添加各种表示统计变量的线

<img src="/images/2022-07/Snipaste_2022-07-15_09-56-17.png"  width="80%">


## 2.n More Visuals
Power BI 有着非常丰富的外部图表资源，登陆后界面如右图

<img src="/images/2022-07/Snipaste_2022-07-12_20-23-45.png"  width="34%"> <img src="/images/2022-07/Snipaste_2022-07-12_21-01-46.png"  width="63%">

例如，在上右图内搜索并添加 Violin Plot:
效果如下，当把鼠标移动到任一 violin 上时，会显示出该 category 的统计信息（max, mean, median...）

<img src="/images/2022-07/Snipaste_2022-07-12_21-07-48.png"  width="100%">









# 3. Add Calendar Model with DAX

需求: 创建一个类似于 Power Pivot 中的 Date Table([WIKI: Excel Power Pivot](./excel/excel-power%20pivot.md#21-add-data-model)) 那样储存时间信息的 Data Model

**(1) 创建空白表**

<img src="/images/2022-07/Snipaste_2022-07-12_09-49-46.png"  width="80%">

**(2) 在 formula bar 中定义表名及其第一列数据**

```python
表名 = CALENDEAR(Start_date, End_date)
```

<img src="/images/2022-07/Snipaste_2022-07-12_09-58-16.png"  width="100%">

**(3) Mark as date table**
将新表设置为 Hierarchy 和 Time Intelligence 的对象，方便之后的分析
- 菜单栏 `Table tools`$\to$`Mark as date table`$\to$在弹窗中选择第一列

<img src="/images/2022-07/Snipaste_2022-07-12_10-01-33.png"  width="100%">

**(4) 添加年份、月份数据**

```python
Year = YEAR(Calendar[Date])
Month Number = MONTH(Calendar[Date])
Month = FORMAT(Calendar[Date], "mmm")
```

<img src="/images/2022-07/Snipaste_2022-07-12_10-07-57.png"  width="100%">

**(5) Add Relationship**
参考 [Section 1.3](#13-relationship-among-data-models) 中的内容，将 `Calendar` 与其他 Model 关联

**(6) Sort by Month**
选中 `Month` 列，将其 Sort by `Month Number`

<img src="/images/2022-07/Snipaste_2022-07-12_10-27-13.png"  width="100%">

**为什么要 sort month？** 因为如果不带排序而直接应用 `Calendar` 中的月份数据，就会出现按照月份首字母排序的情况（April 打头），这不是我们乐见的

<img src="/images/2022-07/Snipaste_2022-07-12_10-21-51.png"  width="100%">

**(7) 添加财年数据 Fisical Year**
观察下图，发现 2017 和 2020 年只有半年的数据，因而导致了 Area Chart 中出现两头小的情况。这是因为数据是按照公司的财年统计的，2018财年 = 2017.7-2018.6

<img src="/images/2022-07/Snipaste_2022-07-12_10-30-08.png"  width="100%">

向 `Calendar` Model 添加三列数据，再将 `Fiscal Month` sort by `Fiscal Month Num`

```python
Fiscal Year = IF(Calendar[Month Number]>6, Calendar[Year]+1, Calendar[Year])
Fiscal Month Num = IF(Calendar[Month Number]>6, Calendar[Month Number]-6, Calendar[Month Number]+6)
Fiscal Month = Calendar[Month]
```

<img src="/images/2022-07/Snipaste_2022-07-12_11-07-02.png"  width="100%"> 

**(8) 将时间数据替换为 Fiscal Time**
将 Area Chart 与 Matrix 的时间数据都替换为 Fiscal Time 后的效果如下

<img src="/images/2022-07/Snipaste_2022-07-12_11-08-04.png"  width="100%">







# 4. Power BI Report

实现如下效果:
<img src="/images/2022-07/Snipaste_2022-07-14_08-36-34.png"  width="100%">


**(1) 插入公司图片并将其放在顶端**
菜单栏 `Insert`$\to$`Elements`$\to$`Image`

**(2) 将三个重要数据以 Card 形式显示在右上区域**
详见 [Section 2.4](#24-card)

**(3) 插入图表**
- 使用 GeoMap + Bubble Chart 显示各地收入 ([Section 2.1](#21-bubble-chart-in-geomap))
- 使用 TreeMap 图形化各地收入占比 ([Section 2.2](#22-treemap))
- 使用 Matrix 显示各财年各月收入数据 ([Section 2.3](#23-matrix) + [Section 3](#3-add-calendar-model-with-dax))
- 使用 Violin Chart 显示不同种类商品的销售数据 ([Section 2.n](#2n-more-visuals))
- 使用 Area Chart 显示销售额随时间的变化 ([Section 2.4](#24-area-chart))


## 4.1 Focus & Spotlight

以下三个红框分别表示: `最大化显示 Chart`, `最大化显示 Chart+Table`, `高亮`

<img src="/images/2022-07/Snipaste_2022-07-14_09-51-33.png"  width="80%">


## 4.2 Filter & Slicer

**创建 Slicer:**

<img src="/images/2022-07/Snipaste_2022-07-15_09-29-21.png"  width="32%">
<img src="/images/2022-07/Snipaste_2022-07-15_09-28-58.png"  width="50%">

**使 Slicer 能够联动当前页面中的所有 Chart:**
- 选中 Slicer$\to$菜单栏 `Format`$\to$`Edit interactions`
- 确保所有 Chart 右上角的禁止符都是灰色的（如果显示黑色则只要点击其左侧的 Filter 图标即可）
<img src="/images/2022-07/Snipaste_2022-07-15_09-35-39.png"  width="60%">

同样，如果想要某些 Chart 不随 Slicer 变化而变化，则需要激活禁止符

**为多个页面创建同步的 Slicer:** 
需求是使得一个 Slicer 能够控制所有页面的 Chart
- 选中 Slicer$\to$菜单栏 `View`$\to$`Show panes`$\to$`Sync slicers`
- 完成如下图所示勾选后，当前 Slicer 就会出现在这两个页面的相同位置，且能同时控制这两个页面中的所有 Chart
<img src="/images/2022-07/Snipaste_2022-07-15_09-43-19.png"  width="50%">







# 5. Add Time Intelligence
## 5.1 通过 Waterfall Chart 显示每月收入的涨跌
<img src="/images/2022-07/Snipaste_2022-07-15_10-02-33.png"  width="80%">

只需要创建两个Measure: 其一表示上个月的收入，其二表示收入差

```py
Revenue Previous Month = CALCULATE([Revenue],PREVIOUSMONTH('Calendar'[Date]))
MoM Change = [Revenue]-[Revenue Previous Month]
```

## 5.2 通过百分比来图形化显示收入涨跌幅度
回忆 [WIKI: Excel Visualization](./excel/excel-data%20visualization.md#111-trend-based) Chapter 1.1.1 Trend-based (3) Icon Set

<img src="/images/2022-07/Snipaste_2022-07-15_10-18-06.png"  width="70%">

(1) 首先需要 Section 5.1 的基础上再添加一个 Measure

```py
MoM % Change = DIVIDE([MoM Change],[Revenue Previous Month],0)
```

(2) 创建一个 Table 并填入 Column 数据

<img src="/images/2022-07/Snipaste_2022-07-15_10-49-21.png"  width="40%">

(3) 添加 Conditioanl Formatting

<img src="/images/2022-07/Snipaste_2022-07-15_10-55-35.png"  width="100%">