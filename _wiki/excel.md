---
layout: wiki
title: Basis
cate1: Excel
cate2:
description: 
keywords: Excel
---

同时选择多个 cell: 按住 `command`

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