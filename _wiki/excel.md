---
layout: wiki
title: Basis
cate1: Excel
cate2:
description: 
keywords: Excel
---

## Basic
(1) 同时选择多个 cell: 按住 `command`

(2) 显示公式: 在等号前加一个单引号
<img src="/images/2022-06/Snipaste_2022-06-02_15-32-08.png"  width="50%">


`rand()` 0-1 随机数
`log(n,i)` $\log_in$
`average(A1:A5)` 均值

线性回归
`slope(ys, xs)` 斜率
`intercept(ys, xs)` 截距
`correl(array1, array2)` 协方差系数
`rsq(ys, xs)` R-squared

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

逻辑表达式
`IF(logical expr, value_ifTrue, value_ifFalse)`
<img src="/images/2022-04/Snipaste_2022-04-30_11-14-46.png"  width="40%">
红框中之所以能够显示以等号开头的字符串，是因为其实输入的是 `'=IF(...)`，开头添加的引号声明该输入为字符串格式，因此不会被识别为计算式


## Functions
**Combine text values**
`CONCAT()`, `&`, `TEXTJOIN()`
<img src="/images/2022-06/Snipaste_2022-06-02_16-01-03.png"  width="40%">

**Split text data**
`LEFT()`, `RIGHT()`, `MID()`
<img src="/images/2022-06/Snipaste_2022-06-02_16-07-57.png"  width="70%">

使用 `FIND()` 优化 `MID()`

例如对于以下情况，`FIND("-",B15,6)` 指的是从目标 cell 的第 `6` 个字符开始，寻找下一个 `"-"` 的位置。因此只要再减去六，就可以得到两个横杠之间的单词长度
<img src="/images/2022-06/Snipaste_2022-06-02_16-18-35.png"  width="70%">



