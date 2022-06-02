---
layout: wiki
title: Basis
cate1: Tableau
cate2: 
description: 
keywords:
---

## Step 01: 划分数据区域
从 Excel 导入数据后，

<img src="/images/2022-04/Snipaste_2022-04-25_19-21-45.png"  width="100%">

所有的数据列被自动划分为两个区域
- **蓝色区域(Dimention)**: 一般用于储存<span style="background-color: yellow; color: black;">非</span>数值类型，或是表示分类信息的数据。例如，姓名，编号，职业，性别
- **绿色区域(Measure)**: 一般用于储存数值类型。例如，工资，年龄

当然自动分类不一定符合要求和需求，此时需要转换一些数据列的所在区域。例如把 wage 从 `Dimention` convert to `Meausre`


<img src="/images/2022-04/Snipaste_2022-04-25_19-38-17.png"  width="60%">

### Marks Card
<img src="/images/2022-04/Snipaste_2022-04-26_21-27-30.png"  width="40%">

- `Color`: 更改图表颜色
- `Size`: 更改点、线、柱的宽度
- `Detail`: 为图标添加更多交互信息
例如: [柱状图](#15-显示更多交互信息)

### Filter Card

## 画图
### 1 柱状图
例如，想要比较各个行业的收入中位数
- 把 `Measure` 类型的 wage 拖入右上方的 Rows 框
- 把 `Dimention` 类型的 job tile 拖入 Columns 框

<img src="/images/2022-04/Snipaste_2022-04-25_20-19-21.png"  width="100%">

在 Rows 框内，可以选择数据的统计值: sum, avg, std, max... 

<img src="/images/2022-04/Snipaste_2022-04-25_20-23-26.png"  width="40%">

#### 1.1 排序
点击左侧图标实现排序
<img src="/images/2022-04/Snipaste_2022-04-25_20-31-34.png"  width="40%">

#### 1.2 行列置换
<img src="/images/2022-04/Snipaste_2022-04-25_20-38-38.png"  width="60%">

#### 1.3 二次分组
<img src="/images/2022-04/Snipaste_2022-04-25_21-11-29.png"  width="80%">

#### 1.4 上下子图
划分成上下两张图表，分别统计两列数据，或者一列数据的两种统计值（例如上表显示avg，下表显示std）
<img src="/images/2022-04/Snipaste_2022-04-26_21-01-05.png"  width="80%">

#### 1.5 显示更多交互信息
将 `Measure` 类型的数据拖入左侧的 Detail 框中
<img src="/images/2022-04/Snipaste_2022-04-26_21-03-14.png"  width="80%">

### 2 气泡图
相较于创建柱状图时需要把数据拖入 Columns & Rows 栏，创建气泡图时需要把数据拖入 Marks Card 中的 Color & Size & Lable

有好几种形式
#### 形式1: 单分类(Color = Label)
- Color: 职业
- Size: 平均工资
- Label: 职业
<img src="/images/2022-04/Snipaste_2022-04-26_21-39-58.png"  width="100%">

#### 形式2: 双分类(Color != Label)
- Color: Visa
- Size: 平均工资
- Label: 职业
<img src="/images/2022-04/Snipaste_2022-04-26_22-37-00.png"  width="100%">

#### 形式3: 双分类(Color = Label)
在形式1的基础上，<span style="background-color: yellow; color: black;">按住 Shift 后</span>把 Visa 拖到 Color 栏
- Color: 色系表示不同的职业，深浅表示不同的 Visa
- Size: 平均工资
- Label: 职业
<img src="/images/2022-04/Snipaste_2022-04-26_22-47-18.png"  width="100%">

#### 多个气泡图
首先依据 Visa 数据分类，再创建多个基础形式的气泡图
<img src="/images/2022-04/Snipaste_2022-04-26_22-33-55.png"  width="100%">

### 3 折线图
以下情况应当选择折线图 instead of 柱状图
- 值随时间变化，需要观察变化的幅度和趋势
- 连续变量1随连续变量2的变化而变化

#### 示例: 分析年薪涨跌

**(1) 画出年薪中位数随年份变化的涨跌，发现总体趋势平稳**
<img src="/images/2022-04/Snipaste_2022-04-29_09-27-51.png"  width="100%">

**(2) 画出年薪中位数随季度变化的涨跌**
操作: 点击 YEAR 左侧的加号(就会变成下图中的减号)。这里折线的==不连续==，是因为 Case Receive Date 为 Dimention 类的数据
<img src="/images/2022-04/Snipaste_2022-04-29_09-31-54.png"  width="100%">

而将其转换为 Measure 类型后，再点击加号(由 YEAR 变为 QUARTER)，即可显示出连续折线
<img src="/images/2022-04/Snipaste_2022-04-29_09-36-37.png"  width="80%">

<img src="/images/2022-04/Snipaste_2022-04-29_09-38-25.png"  width="100%">

相较于时间跨度为年的折线图的平稳趋势，跨度为季度的折线图==有明显的先降后升的趋势，能反映出更多细节==

**(3) 画出不同职业年薪中位数的涨跌**
把 Job Title 拖入 Colors 框中，不难发现大部分数据都在 2019 年之后
<img src="/images/2022-04/Snipaste_2022-04-29_09-52-47.png"  width="100%">

因此可以添加一个关于日期 Filter
<img src="/images/2022-04/Snipaste_2022-04-29_09-55-56.png"  width="100%">

**(4) 比较年薪中位数/最大值/最小值的涨跌**
总体趋势为高薪的人挣得更多，低薪的挣得更少
<img src="/images/2022-04/Snipaste_2022-04-29_10-20-49.png"  width="100%">

添加并查看 Trend Lines(线性回归)。通过将鼠标悬停在趋势线上，可以查看如趋势线公式、R-squared、P-value等具体数值
<img src="/images/2022-04/Snipaste_2022-04-29_10-26-57.png"  width="100%">

分别查看各个职业
<img src="/images/2022-04/Snipaste_2022-04-29_10-46-15.png"  width="100%">

设置趋势线
- 更改趋势线类型(linear, ploy, exponential)
- 将趋势线从多条线显示多种职业，改回一条线现实总体情况

<img src="/images/2022-04/Snipaste_2022-04-29_10-52-56.png"  width="70%">

<img src="/images/2022-04/Snipaste_2022-04-29_10-53-45.png"  width="100%">

### 4 箱形图
<img src="/images/2022-04/Snipaste_2022-04-29_10-57-39.png"  width="100%">

绘制每年年薪的 boxplot(需要在 Analysis 菜单中取消选择 Aggregate Measures)，==可以看到有很多 outliers==
<img src="/images/2022-04/Snipaste_2022-04-29_11-22-37.png"  width="100%">

通过限制 y 轴范围来不显示 >= 1000K 的 outliers
<img src="/images/2022-04/Snipaste_2022-04-29_11-32-20.png"  width="100%">

通过添加 Filter，查看各职业每年年薪的 boxplot
<img src="/images/2022-04/Snipaste_2022-04-29_11-26-25.png"  width="100%">






## Outliers, Filtering and Groups
<img src="/images/2022-04/Snipaste_2022-04-27_11-18-56.png"  width="80%">

通过比较发现，attorney 类有较大的标准差，合理怀疑其中是否存在异常值(过大/过小)

取消勾选 Aggreate，使每个数据都以点的形式显示出来(需调整 Size)。可以发现确实有 attorney 类的确存在几个异常数据

<img src="/images/2022-04/Snipaste_2022-04-27_14-03-32.png"  width="100%">

### 1 查看异常值
框选异常数据后右键单击，选择 View Data
<img src="/images/2022-04/Snipaste_2022-04-27_11-31-36.png"  width="30%">

可以查看到异常值对应的信息
<img src="/images/2022-04/Snipaste_2022-04-27_11-33-34.png"  width="80%">

### 2 去除异常值
两种方法通过 Filter 去除异常值

> **M1: 限制数据范围，去除过大的数据**
- 将数据拖入 Filter 框，并在弹出的窗口中设置范围
<img src="/images/2022-04/Snipaste_2022-04-27_14-05-31.png"  width="80%">

- 限定范围后数据变得好看很多，可以通过右键单击左侧红框，并选择 Show Filter 从而调出右侧红框，实现快速调节范围
<img src="/images/2022-04/Snipaste_2022-04-27_14-09-26.png"  width="80%">

> **M2: 将异常数据与其他数据划分为两组**
- 首先将一个类似主键的属性(e.g. Case Number)拖到 Detail 框
- 再框选异常数据，右键单击并在 Group 中选择 Case Number
<img src="/images/2022-04/Snipaste_2022-04-27_14-45-17.png"  width="80%">
- 可以看到在左侧属性栏以及 Marks Card 中新增了分类信息
<img src="/images/2022-04/Snipaste_2022-04-27_15-37-50.png"  width="100%">
- 将分类信息拖入 Filter Card，并右键单击打开 Show Filter，勾选 Other 类从而实现去除异常值
<img src="/images/2022-04/Snipaste_2022-04-27_15-41-16.png"  width="100%">

### 3 分析异常值
前提：已将异常值与其他值分成两类（使用上述的第二种去除异常值的方法）

> **比较异常值与其他值的统计值**
- 首先筛选出异常值所在的 attorny 类
- 再将 Case Number (group) 拖入 Columns 栏
<img src="/images/2022-04/Snipaste_2022-04-27_15-50-01.png"  width="80%">

### 4 筛选和分组
例如想要查看某几个州 data 相关工作的平均薪资
(1) 创建分组
<img src="/images/2022-04/Snipaste_2022-04-27_17-49-13.png"  width="80%">

(2) 发现同一个州有两种命名方式，首先选择其中一个，点击 Group 并命名
<img src="/images/2022-04/Snipaste_2022-04-27_17-57-30.png"  width="50%"><img src="/images/2022-04/Snipaste_2022-04-27_17-51-50.png"  width="50%">

(3) 再将另一个拖进去，从而完成分组
<img src="/images/2022-04/Snipaste_2022-04-27_17-53-53.png"  width="50%"><img src="/images/2022-04/Snipaste_2022-04-27_17-54-52.png"  width="50%">

(4) 同理，完成其他目标州的分组。通过勾选 Include 'Other' 把其他未分组的数据都归入 Other 组
<img src="/images/2022-04/Snipaste_2022-04-27_18-04-38.png"  width="50%">

(5) 再通过一通操作
- 使用 Filter 筛选出目标州的数据
- 将需要绘制的信息拖入 Columns & Rows
- 将 Job Title 拖入 Color 框以区分颜色
- 在左下角框内，把与 Data 相关的工作拖到上边

<img src="/images/2022-04/Snipaste_2022-04-27_20-06-51.png"  width="80%">
