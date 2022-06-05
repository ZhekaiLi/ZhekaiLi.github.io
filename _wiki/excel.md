---
layout: wiki
title: Basis
cate1: Excel
cate2:
description: 
keywords: Excel
---



## Basic
**(1) 同时选择多个 cell**: 按住 `command`

**(2) 显示公式**: 在等号前加一个单引号

<img src="/images/2022-06/Snipaste_2022-06-02_15-32-08.png"  width="40%">

**(3) 将公式自动应用到整列**: 双击单元格右下角

**(4) 选取整列**: 例如当我们想要对整列 Amount 求和，可以先点击 Q2(不能是打字输入)，再点击 `Shift`+`Control`+`Down`

<img src="/images/2022-06/Snipaste_2022-06-03_09-28-52.png"  width="30%">

**(5) 插入新列**: 选中一列，然后 `Ctrl/Cmd`+`Shift`+`+`

**(6) 函数补全**: `TAB`

<img src="/images/2022-06/Snipaste_2022-06-03_14-57-49.png"  width="30%">



### Named Ranges
#### .1 Define `Name`

用于定位一些重要数据或是定值，同时方便其调用。三种创建方式:
**(1) 修改 Name Box**
例如，把红框内的 "N2" 改名为 "Penalty_Rate"

<img src="/images/2022-06/Snipaste_2022-06-03_20-18-05.png"  width="70%">
- 可以通过点击红框右侧的箭头快速定位
- 之后在调用 N2 的时候可以直接输入 Penalty_Rate

<img src="/images/2022-06/Snipaste_2022-06-03_20-21-13.png"  width="70%">

**(2) Define Name**
`Ctrl+Shift+Down` 选中一整列，点击 `Define Names` 然后可以在弹窗中改名或者修改这个名字应用的范围（Sheet or Workbook）
<img src="/images/2022-06/Snipaste_2022-06-03_21-20-04.png"  width="70%">

**(3) Create from Selection**
先选中所有目标 headers，全选这些列之后点击 `Create from Selection` 然后在弹窗中选择以首行内容作为名字
<img src="/images/2022-06/Snipaste_2022-06-03_21-24-54.png"  width="70%">


#### .2 Manage
方便地新建、编辑、删除 `Name`
<img src="/images/2022-06/Snipaste_2022-06-03_21-33-35.png"  width="70%">


#### .3 Calculations
可以通过 `Name Manager` 创建常量

```cs
COUNTIFS(Country, "China")       // 查看名为 Location 的组里有多少个为 China
SUMIFS(Salary, Country, "China") // 查看住在中国的人的总薪水
AVERAGEIFS() MINIFS() MAXIFS()   // 同理
```


#### .4 Data Validation
为了实现如下效果

<img src="/images/2022-06/Snipaste_2022-06-04_09-06-45.png"  width="70%">

需要如下步骤
1. 把这两个地名设置为一个名为 `Locations` 的 Named Range
2. 选中 cell K2, 点击 `Data`$\to$`Data Validation`
3. 在弹窗中修改 `Allow` 为 List, 点击 `Source` 框
4. 点击 `Formulas`$\to$`Use in Formula`$\to$`Locations`

<img src="/images/2022-06/Snipaste_2022-06-04_09-04-33.png"  width="70%">

<img src="/images/2022-06/Snipaste_2022-06-04_09-07-39.png"  width="50%">

*Problem*: 上述方案存在一个问题，即在第一步设置的 `Locations` 是<span style="background-color: yellow; color: black;">指定的，只包含两个城市</span>。而我们希望，当继续在下方单元格填入城市名时，也能被自动纳入

<img src="/images/2022-06/Snipaste_2022-06-04_09-19-52.png"  width="50%">

步骤如下:
1. 在 `Name Manager` 中选择编辑 `Locations`
2. 在弹窗中输入以下表达式：

```cs
// COUNTA: 统计指定范围内非空单元格的个数
// OFFSET: 返回一个 range，范围是以 A8 为 reference_cell, 
//         横向纵向偏移0格（也就是还是自身），
//         从偏移后的单元格开始往下公 COUNTA(...) 个
=OFFSET('Recon Analysis'!$A$8, 0, 0, 
    COUNTA('Recon Analysis'!$A$8:$A$18)
)
```



---



## Functions
### Text
> **Combine**

`CONCAT()` `&` `TEXTJOIN()`

<img src="/images/2022-06/Snipaste_2022-06-02_16-01-03.png"  width="35%">

> **Split**

`LEFT()` `RIGHT()` `MID()`

<img src="/images/2022-06/Snipaste_2022-06-02_16-07-57.png"  width="60%">

*Problem*: 如果想要提取多个时间的完整的月份，由于不同月份的单词长度可能不同，因此无法直接用以上简单形式实现
- `FIND()`

例如对于以下情况，`FIND("-",B15,6)` 指的是从目标 cell 的第 `6` 个字符开始，寻找下一个 `"-"` 的位置。因此只要再减去六，就可以得到两个横杠之间的单词长度

<img src="/images/2022-06/Snipaste_2022-06-02_16-18-35.png"  width="60%">

- `LEN()`

思路类似，因为所有时间的月份的前后长度都一样

<img src="/images/2022-06/Snipaste_2022-06-02_16-26-57.png"  width="45%">

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

```cs
SUBSTITUTE(cell, old_txt, new_txt, [order])`
```
例如 `SUBSTITUTE(cell,"|"," ",2)` 表示把单元格内的第二个 "|" 替换成 “ ”

*Problem*: 想要完成如下转换，注意字符 "S" 与 "7" 之间存在一个奇怪的符号（不是空格，无法用 `TRIM()`） 
|Init|After|
|-|-|
|S 7|7|

此时需要通过两层替换, 内层替换掉"S", 外层替换掉那个奇怪符号

```cs
SUBSTITUTE(SUBSTITUTE(cell,"S",""), MID(cell,2,1), "")
```



### Date & Time
> **Get time**

```cs
/*** Generate date ***/
DATE(2022,6,3)

/*** Current time ***/
NOW()   // 2022/6/3 10:19
TODAY() // 2022/6/3

/*** Get time ***/
// Assume date_cell = 2022-06-03
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
YEARFRAC(start_date, end_date)    // 两个日期之间差了几年（会有小数）
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



### Math

```cs
ROUNDDOWN(value_cell, 0) // 向下取整，如果是 1 就表示取一位小数
```



### Statistical

```cs
COUNTA(range)  // 统计非空单元格个数
RAND()         // 0-1 随机数
LOG(n,i)       // $\log_in$
AVERAGE(A1:A5) // 均值

/*** 线性回归 ***/
SLOPE(ys, xs)          // 斜率
INTERCEPT(ys, xs)      // 截距
CORREL(array1, array2) // 协方差系数
RSQ(ys, xs)            // R-squared
```



### Logic
> **IF**

```cs
IF(logic_expr, [value_if_true], [value_if_flase])
```
- `logic_expr` 为逻辑表达式，包含 `>,>=.=,<,<=,<>`

例如: 
- 想要显示付款日期是否超过了截止日期，可以新建一列并填入以下第一行公式
- 想要进一步显示过期了几天，可以再新建一列并填入以下第二行公式

```cs
=IF([@[Payment Date]]>[@[Due Date]],"Yes","")
=IF([@[Over Due]]="",0,NETWORKDAYS([@[Due Date]],[@[Payment Date]],Holidays))
```
> **AND & OR**

```cs
AND(logic_expr1, logic_expr2, [...])
OR(logic_expr1, logic_expr2, [...])
```
与或函数只能返回 TRUE/FLASE，如果想要返回其他值，只需在外边套一个 `IF(AND(...),"Yes","No")`



### Lookup
**(1) VLOOKUP**

```cs
VLOOKUP(value, table/array, col_index, [approximate_match])
// 要查找的值, 查找区域, 要返回的结果在查找区域的第几列, 精确匹配或近似匹配
```
- <span style="background-color: yellow; color: black;">要查找的值必须包含于查找区域的首列，首列必须升序排列</span>
- 精确匹配 0/FALSE; 近似匹配 1/TRUE
- 近似匹配是向下近似，例如下图中 9 匹配 5

例如根据表格查找对应的罚款金额:
<img src="/images/2022-06/Snipaste_2022-06-04_22-12-10.png"  width="70%">

*Application*: 使用 `VLOOPUP()` 检查两张表中的数据是否匹配

例如，要检查以下两表中同一个 Payment Ref 是否都对应一样的 Amount
- `表1 = [Doc No., Payment Ref, Amount]`
- `表2 = [Payment Ref, Amount]`

```cs
// 在表1的右侧新建一列
=[@[$ Amount]] - VLOOKUP([@[Payment Ref]], tbl_2, 2, 0)

// 在表2的右侧新建一列
// 首先需要把表1的两列设为 Named Ranges
=[@[$ Amount]] - XLOOKUP([@[Payment Ref]], Payment_Ref, Amount, 0)
```
**(2) XLOOKUP**

```cs
XLOOKUP(lookup_value, lookup_array, return_array, [if_not_found], [match_mode], [search_mode])
```
`XLOOKUP()` 的优点
- 更灵活，`VLOOKUP()` 中的 table/array 以及 col_index 相当于限定死了 lookup_array 只能是指定表格的第一列，并且 return_array 只能是在同一个表格中。而 `XLOOKUP()` 没有限制，可以指定任意 Named Range 为 lookup/return_array
- 可以指定 if_not_found 的值
- 甚至可以指定搜索方式（顺序查找、二分查找）

**(3) INDEX & MATCH**
> 单维度匹配 

例如，想要实现以下效果：在红框1中选择国家，红框2能够自动显示其人口
<img src="/images/2022-06/Snipaste_2022-06-05_09-47-09.png"  width="`00%">

```cs
INDEX(array, row_num, [col_num])
// INDEX(Population, 2) 返回 Albania 的人口 2,880,917

MATCH(lookup_value, lookup_array, [approximate_match])
// MATCH(A2, Country, 0) 返回 3 (Algeria 在 Country(Named Range) 中的排序)
```
因此最终，在红框2中输入以下公式

```cs
=INDEX(Population, MATCH(A2, Country, 0))
```
> 双维度匹配

更进一步的，想要实现以下效果：在红框1中选择国家，红框2中选择属性 Capital/Currency/...，红框3能自动显示其属性值
<img src="/images/2022-06/Snipaste_2022-06-05_09-59-31.png"  width="100%">

<img src="/images/2022-06/Snipaste_2022-06-05_10-06-23.png"  width="100%">



---



## Table
### .1 Create
菜单栏 `Insert`$\to$`Tables`$\to$`Table` (<span style="background-color: yellow; color: black;">Shortcut `Ctrl+T`</span>)

创建完后一般先 Rename
<img src="/images/2022-06/Snipaste_2022-06-04_11-18-20.png"  width="100%">

如果要取消创建，首先将 `Style` 修改为 Light空，再点击 `Convert to Range`
<img src="/images/2022-06/Snipaste_2022-06-04_11-22-33.png"  width="100%">



### .2 Customise
勾选 `Total Rows`，表格的底部就会自动增加一行 Total 行，接着可以选择统计方式
<img src="/images/2022-06/Snipaste_2022-06-04_11-50-23.png"  width="70%">

调整列位置: 将鼠标悬浮于 Header 的上方横线，此时会出现一个黑色的向下箭头。点一下选中整行数据，再点一下就会包括 Header，此时即可拖动来调整该列的位置。行同理



### .3 Sort & Filter
**(1) Simple sort** 直接点击 Header 右侧的箭头                       

**(2) Complex sort** 实现嵌套排序，例如

<img src="/images/2022-06/Snipaste_2022-06-04_14-50-54.png"  width="70%">

**(3) Filter** 点击 Header 右侧的箭头
- 可以直接通过勾选进行筛选
- 如果是数字类型的数据，还可以点击 `Number Filters` 进行筛选（限定范围，top10，高于或低于平均，>/=/<）

清除所有的 Filter: 菜单栏 `Data`$\to$`Sort & Filter`$\to$`Clear`

**(4) Slicer**: 图形化显示 Filter，非常简洁高效

在弹窗中勾选想要插入的 Filter
<img src="/images/2022-06/Snipaste_2022-06-04_15-03-37.png"  width="70%">

然后就会出现两个非常酷的小窗口，直接点击其中的元素便能实现筛选
<img src="/images/2022-06/Snipaste_2022-06-04_15-05-32.png"  width="70%">



### .4 Calculations (& Structured References)
**(1) 表格运算**

```cs
ROWS(table_name)                               // 表格包含的数据行数
AVERAGEIFS(table_name[Salary],Country,"China") // 统计某个国家的平均收入
```
**(2) 列求和** 先将鼠标悬浮于 Amount 的上方横线，再点击出现的一个黑色的向下箭头。此时 `SUM()` 中出现的字段称为 **Structured Reference**

<img src="/images/2022-06/Snipaste_2022-06-04_15-20-55.png"  width="70%">

**(3) 列之间的运算** 计算两个日期之间的差值: 直接如下图点两下，按回车之后便会自动生成一整列，再给新生成的列改个名即可

<img src="/images/2022-06/Snipaste_2022-06-04_15-30-04.png"  width="70%">

<img src="/images/2022-06/Snipaste_2022-06-04_15-31-32.png"  width="50%">



### .5 Automation
使用 Table 的优点:
- 即使把当前所有数据都删除了（Headers 还在），各个列之间的关系仍然存在（包括 Named Ranges），只要填入新数据就可以自动完成所有的计算与统计
- 更新 Table 的同时会更新其包含的 Named Ranges, Data Validation



