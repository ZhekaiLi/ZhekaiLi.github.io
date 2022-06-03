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

(3) 将公式自动应用到整列: 双击单元格右下角

(4) 选取整列: 例如当我们想要对整列 Amount 求和，可以先点击 Q2(不能是打字输入)，再点击 `Shift`+`Control`+`Down`
<img src="/images/2022-06/Snipaste_2022-06-03_09-28-52.png"  width="40%">

(5) 在选中列之前插入新列: `Ctrl/Cmd`+`Shift`+`+`



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
### Text
> **Combine**

`CONCAT()`, `&`, `TEXTJOIN()`
<img src="/images/2022-06/Snipaste_2022-06-02_16-01-03.png"  width="40%">

> **Split**

`LEFT()`, `RIGHT()`, `MID()`
<img src="/images/2022-06/Snipaste_2022-06-02_16-07-57.png"  width="70%">

Problem: 如果想要提取多个时间的完整的月份，由于不同月份的单词长度可能不同，因此无法直接用以上简单形式来实现

- `FIND()`

例如对于以下情况，`FIND("-",B15,6)` 指的是从目标 cell 的第 `6` 个字符开始，寻找下一个 `"-"` 的位置。因此只要再减去六，就可以得到两个横杠之间的单词长度
<img src="/images/2022-06/Snipaste_2022-06-02_16-18-35.png"  width="70%">

- `LEN()`

思路类似，因为所有时间的月份的前后长度都一样
<img src="/images/2022-06/Snipaste_2022-06-02_16-26-57.png"  width="50%">

> **Convert**
```cs
VALUE(cell) // convert text to value
```

> **Clean**

```cs
CLEAN(cell) // 清除单元格内的一些非ascii字符
TRIM(cell)  // 清除前后空格，以及中间多余的空格（例如单词之间空了多个空格）
```
> **Change case 大小写**

```cs
UPPER(cell)
LOWER(cell)
PROPER(cell)  // 首字母大写
```
> **Replace characters**

`SUBSTITUTE(cell, old_txt, new_txt, [order])`
例如 `(cell,"|"," ",2)` 表示把单元格内的第二个 "|" 替换成 “ ”

Problem: 想要完成如下转换，注意字符 "S" 与 "7" 之间存在一个奇怪的符号（不是空格，无法用 `TRIM()`） 
|Init|After|
|-|-|
|S 7|7|

因此需要通过两层replace, 内层替换掉"S", 外层替换掉那个奇怪符号

```cs
SUBSTITUTE(SUBSTITUTE(cell,"S",""), MID(cell,2,1), "")
```

### Date & Time
> **Get time**

Generate date

```cs
DATE(2022,6,3)
```
Current time

```cs
NOW()   // 2022/6/3 10:19
TODAY() // 2022/6/3
```

Get day/month/year from datetime (assume `date_cell = 2022-06-03`)

```cs
DAY(date_cell)   // 3
MONTH(date_cell) // 6
YEAR(date_cell)  // 2022

TEXT(date_cell, [format_text]) // datetime to year/month/day
```
|format_text|result|
|-|-|
|"D" "DD" "DDD" "DDDD"|3, 03, Fri, Friday|
|"M" "MM" "MMM" "MMMM"|6, 06, Jun, June|
|"YY" "YYYY"| 22, 2022|
|"DDD/M/YYYY"| Fri/6/2022|


> **Calculations**

日期可以和数字相互转换，日期+1就代表经过了一天，数字1表示时间1900-01-01

```cs
DAYS(end_date, start_date)        // = end_date - start_date
WORKDAY(start_date, num)          // 返回 start_date 后第 num 个工作日的日期
    WORKDAY.INTL(start_date, num, [weekend], [holidays])
    // 自定义休息日，例如 "0100000" 表示一周只在周二休息一天
    // 自定义假期，可以写 DATE(y,m,d)，也可以框选一堆日期
NETWORKDAYS(start_date, end_date) // 返回期间的工作日天数（左右都包括）
    NETWORKDAYS.INTL(...)
```

```cs
// 返回这个月的最后一天（如果是-1就是上个月，1下个月，其他同理）
EOMONTH("03/06/2022", 0) // 30/06/2022
// 增减月份
EODATE("03/06/2022", 1)  // 03/07/2022
```


