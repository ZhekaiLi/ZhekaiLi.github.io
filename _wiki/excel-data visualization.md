---
layout: wiki
title: Data Visualization
cate1: Excel
cate2:
description: 
keywords: Excel
---

## Conditional Formatting
用于图形化数据，使其更容易理解

`Home`$\to$`Styles`$\to$`Conditional Formatting`

<img src="/images/2022-06/Snipaste_2022-06-05_19-58-59.png"  width="30%">

### Bar & Color & Icon
**(1) Data Bars**

<img src="/images/2022-06/Snipaste_2022-06-05_20-00-53.png"  width="70%">

**(2) Color Scales**

<span style="background-color: yellow; color: black;">除了默认选项，这两种 Formatting 均可定制化，方法类似 *(3) Icon Sets* 中介绍的</span>
从蓝至红表示数据由大至小

<img src="/images/2022-06/Snipaste_2022-06-05_20-02-06.png"  width="70%">

**Icon Sets**

首先将表格最右侧一列表示变化幅度的数据复制一遍 ()

<img src="/images/2022-06/Snipaste_2022-06-05_20-05-12.png"  width="70%">

再选中该列并点击 `Icon Sets`，之后我们发现 -0.2% 与 0.4% 这两个数据也被赋予黄色箭头，这与我们所预想的红表示下降、绿色表示上升以及黄色表示不变不符合

<img src="/images/2022-06/Snipaste_2022-06-05_20-06-13.png"  width="70%">

因此需要修改图标的规则。点击 `Conditional Formatting`$\to$`Manage Rules`，在红框中选择 `This Worksheet`，随后点击编辑刚刚创建的 Icon Set

<img src="/images/2022-06/Snipaste_2022-06-05_20-10-44.png"  width="70%">

在弹窗中如图进行修改

<img src="/images/2022-06/Snipaste_2022-06-05_20-12-32.png"  width="70%">

完成后效果 Perfect!

<img src="/images/2022-06/Snipaste_2022-06-05_20-13-19.png"  width="70%">


<img src="/images/2022-06/.png"  width="70%">
<img src="/images/2022-06/.png"  width="70%">
<img src="/images/2022-06/.png"  width="70%">
<img src="/images/2022-06/.png"  width="70%">
<img src="/images/2022-06/.png"  width="70%">
<img src="/images/2022-06/.png"  width="70%">
<img src="/images/2022-06/.png"  width="70%">
<img src="/images/2022-06/.png"  width="70%">



选中 ys,xs 数据后，创建 scatter plot
<img src="/images/2022-04/Snipaste_2022-04-30_09-49-15.png"  width="100%">

Add trendline, choose linear and click to show equation and R-squared
<img src="/images/2022-04/Snipaste_2022-04-30_09-55-07.png"  width="50%">
<img src="/images/2022-04/Snipaste_2022-04-30_09-56-09.png"  width="100%">

排序 sort
<img src="/images/2022-04/Snipaste_2022-04-30_10-12-08.png"  width="100%">

Solver
1000本金7%年化，几年后会增值到5000？
<img src="/images/2022-04/Snipaste_2022-04-30_10-57-59.png"  width="100%">


