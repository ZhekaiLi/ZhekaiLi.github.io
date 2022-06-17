---
layout: wiki
title: PivotTable
cate1: Excel
cate2: 
description: 
keywords:
---

# 1. Create
**由 Table 创建 PivotTable**
- 首先回顾一下快速创建 Table 的方式: 选中目标区域的第一个单元格（第一个 Header）$\to$`Ctrl+Shift+Right` 全选所有的 Headers$\to$`Ctrl+Shift+Down` 全选所有的数据$\to$`Ctrl+T` 创建 Table，然后改名
- 菜单栏 `Insert`$\to$`PviotTable`$\to$输入 Table 名
- 在右侧栏目根据需求定义 Fields

创建完成后，根据需要把不同的 Fields 拖入右下角的四个象限框中。例如，显示各大洲在各个年份的再生能源和化石能源发电量
- `Columns`: 年份
- `Rows`: 大洲$\to$再生能源/ 化石能源
- `Values`: 发电量

<img src="/images/2022-06/Snipaste_2022-06-10_15-31-41.png"  width="100%">

如果不小心关闭了 `Field List`，可以点击下图红框打开

<img src="/images/2022-06/Snipaste_2022-06-10_15-33-09.png"  width="70%">






# 2. Modify
**更改统计方式**: Sum Count Average Max...

<img src="/images/2022-06/Snipaste_2022-06-10_20-42-11.png"  width="70%">

**更改统计值的显示方式**: 
- 下图1: 查看各洲再生能源占总发电量的比例
- 下图2: 看看哪个洲使用了最多的再生能源

<img src="/images/2022-06/Snipaste_2022-06-10_20-48-17.png"  width="70%">

<img src="/images/2022-06/Snipaste_2022-06-10_20-47-33.png"  width="70%">

**为空白单元格赋初值**: 菜单栏 `PivotTable Analyze`$\to$`PivotTable`$\to$`Options`$\to$在弹窗中完成如下修改

<img src="/images/2022-06/Snipaste_2022-06-10_21-12-34.png"  width="70%">






# 3. Design & Layout
菜单栏 `Design`
- `Subtotals` (红框): 是否显示子类的统计和（及其显示位置）
- `Grand Totals` (蓝框): 是否在表格底部和右侧显示列、行的统计和
- `Report Layout` (绿框): 修改排版格式

<img src="/images/2022-06/Snipaste_2022-06-10_20-54-03.png"  width="100%">

**More about Subtotals**

如果有两层及以上的 Subtitle，但是只想让第一层不显示其 Subtotal，此时可以选中第一层的 Header 并右键单击$\to$取消勾选 `Subtotal "..."`

<img src="/images/2022-06/Snipaste_2022-06-10_20-59-52.png"  width="100%">

可以定义多种 Subtotal 方式，例如想要让第二层的 Subtotal 同时显示均值以及求和:
- 选中第二层的 Header 并右键单击$\to$`Fielding Settings`
- 在弹窗中完成如下操作，可以看到显示出了两种统计值

<img src="/images/2022-06/Snipaste_2022-06-10_21-06-21.png"  width="100%">






# 4. Data Processing
## 4.1 Group
当选择日期作为 Rows 的时候，Excel 可能会自动按照年、季度对日期进行分组，点击下图中的红框来取消该自动分组

<img src="/images/2022-06/Snipaste_2022-06-10_21-22-10.png"  width="100%">

然后自定义具体的分组方式，例如下图按照年、月对日期进行分组

<img src="/images/2022-06/Snipaste_2022-06-10_21-24-55.png"  width="70%">

**创建 Group**

- 下图1: 按住 `Ctrl` 选中想要分类的三个对象$\to$点击菜单栏 `Group`
- 下图2: 新创建的 Group

<img src="/images/2022-06/Snipaste_2022-06-11_19-54-10.png"  width="100%">

<img src="/images/2022-06/Snipaste_2022-06-11_20-11-39.png"  width="100%">



## 4.2 Sort
**Simple Sort**: 根据选中列排序

<img src="/images/2022-06/Snipaste_2022-06-11_20-15-47.png"  width="100%">

**Sort with Custom List**: 使用 `Custom List`，我们可以添加/修改一些默认的排序方式（例如当对一周7天排序时，可以让 Tuesday 排在第一个）

Excel 已经默认定义了一些，查看方式
- 下图1: 点击 `Edit Custom Lists...`
- 下图2: 可以看到默认对于一周7天的排序是从 Sunday 开始的
- 下图3: 通过三步操作，添加一个从 Wednesday 开始的排序方式


<img src="/images/2022-06/Snipaste_2022-06-11_20-24-40.png"  width="100%">

<img src="/images/2022-06/Snipaste_2022-06-11_20-27-18.png"  width="70%">

<img src="/images/2022-06/Snipaste_2022-06-11_20-35-45.png"  width="100%">


## 4.3 Filter
**Simple Filter**

<img src="/images/2022-06/Snipaste_2022-06-11_21-00-00.png"  width="50%">

对于日期、文本、数字类型数据的简单排序，都能在点击上图箭头所打开的窗口内实现，详见[我的另一篇 Wiki: Excel Basis #4.3](./excel.md#43-sort--filter)

**Clear Filters** 三种方式
- M1: 点击上图红框$\to$`Clear Filter From "..."`
- M2: 菜单栏 `PivotTable Analyze`$\to$`Actions`$\to$`Clear`
- M2: 菜单栏 `Data`$\to$`Sort & Filter`$\to$`Clear`

**Filter in Fields**

To filter by a field that we do not want to show in the PivotTable itself

<img src="/images/2022-06/Snipaste_2022-06-11_21-26-06.png"  width="100%">

需要注意的是，当在 Filter 里选取了多个对象，PivotTable 会以求和的形式把它们合并后显示。此时如果需要分别展示这些对象，需点击下图2中红框，然后便能为每个对象单独生成一张 Sheet

<img src="/images/2022-06/Snipaste_2022-06-11_21-27-27.png"  width="50%">

<img src="/images/2022-06/Snipaste_2022-06-11_21-31-18.png"  width="100%">

# 5. Calculations
Calculated Fields 类似于创建列，Calculated Items 类似于创建行
## 5.1 Calculated Fields
Formulas refer to other fields in a PivotTable

**创建**
- 下图1: 打开编辑窗口
- 下图2: 在弹窗中完成如下四步操作（创建一个新的 Field，储存对应的人民币金额）
- 下图3: 创建完成后该 Field 会出现在 Fields List 中随时调用

<img src="/images/2022-06/Snipaste_2022-06-12_10-52-46.png"  width="70%">

<img src="/images/2022-06/Snipaste_2022-06-12_10-57-18.png"  width="70%">

<img src="/images/2022-06/Snipaste_2022-06-12_11-00-24.png"  width="80%">

**修改/删除**: 在上2图弹窗中直接操作



## 5.2 Calculated Items
Formulas refer to other items within a specific PivotTable

<span style="background-color: yellow; color: black;">Calculated Item 不能创建于已经存在 Groups 的 PivotTable</span>。一般情况下，Table 和它所有的 PivotTable 都是相互联系的的，因此如果在一个 Table$\to$PivotTable_1 中创建过 Groups，那么即使重新 insert Table$\to$PivotTable_2，这张新建的表也会带有 Groups 信息。面对这种情况，我们需要的是基于 Table <span style="background-color: yellow; color: black;">彻底创建一张新的 PivotTable</spane>:
- 下图1: `Alt + D + P`$\to$点击 `Next`
- 在下个窗口输入 Table 名$\to$点击 `Next`
- 下图2: 点击 `No`（表示彻底新建）

<img src="/images/2022-06/Snipaste_2022-06-12_16-35-19.png"  width="50%">

<img src="/images/2022-06/Snipaste_2022-06-12_16-36-45.png"  width="100%">


**创建 Calculated Items**:
- 下图1: 打开编辑窗口
- 下图2: 在弹窗中定义 Calculated Items
- 下图3: 成功显示

<img src="/images/2022-06/Snipaste_2022-06-12_10-52-46.png"  width="70%">

<img src="/images/2022-06/Snipaste_2022-06-12_11-26-05.png"  width="70%">

<img src="/images/2022-06/Snipaste_2022-06-12_11-28-45.png"  width="80%">






# 6. PivotChart
PivotChart 近似于 Chart，其不支持创建部分类型的图表（下图的红框部分）

而大部分对 Chart 的修改/美化都能同样应用于 PivotChat，详见我的另一篇 [WIKI: Excel Data Visualization](./excel-data%20visualization.md#2-charting-techniques)

<img src="/images/2022-06/Snipaste_2022-06-12_12-46-48.png"  width="70%">

插入 PivotChart 后的界面大致如下:
- 右侧栏目的名字，变成了 `PivotChart Fields`
- 右侧栏目下方的变化: `Column`$\to$`Lengend`, `Row`$\to$`Axis`
- 左侧图表中的灰色窗口: 调整 Legend/Axis 显示的信息
- 左侧图表右下角的加减符号: 调整分类信息的细节程度（`+`意味着更细节的分类，`-`更粗略的分类）

<img src="/images/2022-06/Snipaste_2022-06-12_12-50-21.png"  width="100%">

**添加 Filter**: 把上图右下角 `Axis` 框中的第一项拖进上方的 `Filter` 框中后，左侧图表左上角就会出现一个 Filter

<img src="/images/2022-06/Snipaste_2022-06-12_12-58-48.png"  width="100%">

**取消显示图表中所有的灰色框**: 菜单栏 `PivotChart Analyze`$\to$`Show/Hide`$\to$`Field Buttons`
