---
layout: wiki
title: PivotTable
cate1: Excel
cate2: 
description: 
keywords:
---

# Create
**由 Table 创建 PivotTable**
- 首先回顾一下快速创建 Table 的方式: 选中目标区域的第一个单元格（第一个 Header）$\to$`Ctrl+Shift+Right` 全选所有的 Headers$\to$`Ctrl+Shift+Down` 全选所有的数据$\to$`Ctrl+T` 创建 Table，然后改名
- 菜单栏 `Insert`$\to$`PviotTable`$\to$输入 Table 名
- 在右侧栏目根据需求定义 Fields

例如，显示各大洲在各个年份的再生能源和化石能源发电量
- `Columns`: 年份
- `Rows`: 大洲$\to$再生能源/ 化石能源
- `Values`: 发电量

<img src="/images/2022-06/Snipaste_2022-06-10_15-31-41.png"  width="100%">

如果不小心关闭了 `Field List`，可以点击下图红框打开

<img src="/images/2022-06/Snipaste_2022-06-10_15-33-09.png"  width="70%">



---



# Modify
**更改统计方式**: Sum Count Average Max...

<img src="/images/2022-06/Snipaste_2022-06-10_20-42-11.png"  width="70%">

**更改统计值的显示方式**: 
- 下图1: 查看各洲再生能源占总发电量的比例
- 下图2: 看看哪个洲使用了最多的再生能源

<img src="/images/2022-06/Snipaste_2022-06-10_20-48-17.png"  width="70%">

<img src="/images/2022-06/Snipaste_2022-06-10_20-47-33.png"  width="70%">

**为空白单元格赋初值**: 菜单栏 `PivotTable Analyze`$\to$`PivotTable`$\to$`Options`$\to$在弹窗中完成如下修改

<img src="/images/2022-06/Snipaste_2022-06-10_21-12-34.png"  width="70%">


---



# Design & Layout
菜单栏 `Design`
- `Subtotals` (红框): 是否显示子类的统计和（及其显示位置）
- `Grand Totals` (蓝框): 是否在表格底部和右侧显示列、行的统计和
- `Report Layout` (绿框): 修改排版格式

<img src="/images/2022-06/Snipaste_2022-06-10_20-54-03.png"  width="100%">

**More about Subtotals**

如果有两层及以上的 Subtitle，但是只想让第一层不显示其 Subtotal，此时可以选中第一层的 Header 并右键单击$\to$取消勾选 `Subtotal "..."`

<img src="/images/2022-06/Snipaste_2022-06-10_20-59-52.png"  width="100%">

可以定义多种 Subtotal 的方式，例如想要让第二层的 Subtotal 同时显示均值以及统计和:
- 选中第二层的 Header 并右键单击$\to$`Fielding Settings`
- 在弹窗中完成如下操作，可以看到显示出了两种统计值

<img src="/images/2022-06/Snipaste_2022-06-10_21-06-21.png"  width="100%">



---



# Group & Sort

当选择日期作为 Rows 的时候，Excel 可能会自动按照年、季度对日期进行分组，点击下图中的红框来取消该自动分组

<img src="/images/2022-06/Snipaste_2022-06-10_21-22-10.png"  width="100%">

然后自定义具体的分组方式，例如下图按照年、月对日期进行分组

<img src="/images/2022-06/Snipaste_2022-06-10_21-24-55.png"  width="70%">

<img src="/images/2022-06/.png"  width="70%">
<img src="/images/2022-06/.png"  width="70%">
<img src="/images/2022-06/.png"  width="70%">
<img src="/images/2022-06/.png"  width="70%">

<img src="/images/2022-06/.png"  width="70%">
<img src="/images/2022-06/.png"  width="70%">
<img src="/images/2022-06/.png"  width="70%">


