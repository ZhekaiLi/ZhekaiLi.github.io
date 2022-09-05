---
layout: wiki
title: Power Query
cate1: Excel
cate2:
description: 
keywords: Excel
---

LINKs Back:
[WIKI: Power BI](/_wiki/power%20bi.md)


# 1. Get Data 导入数据
**(1) 从当前 Workbook**
<img src="/images/2022-05/Snipaste_2022-05-01_14-54-27.png"  width="80%">

**(2) 从外部 Workbook**
<img src="/images/2022-05/Snipaste_2022-05-01_15-27-33.png"  width="80%">
在弹窗左侧选择需要导入的 sheet，后点击右下角 `Transform Data/Edit`

**(3) 从外部 Database**
`Get Data` $\to$ `From Database` $\to$ `具体的数据库种类`

**(4) 从外部 Folder**
`Get Data` $\to$ `From File` $\to$ `From Folder`

弹窗显示 Folder 中所包含的文件信息
<img src="/images/2022-05/Snipaste_2022-05-02_09-57-29.png"  width="100%">

方法1：点击右下角的 `Combine` $\to$ `Combine & Transform Data`
弹窗显示只包含第一个文件信息的预览视图，点击 `OK`
<img src="/images/2022-05/Snipaste_2022-05-02_10-00-25.png"  width="100%">

方法2：点击右下角的 `Transform Data`
在弹窗中点击 `Content` 列右侧的按钮，即可弹出与*方法1*一样的窗口
<img src="/images/2022-05/Snipaste_2022-05-02_10-06-20.png"  width="100%">

**(5) 从外部 PDF**
能够自动识别 pdf 文件中的表格










# 2. User Interface
当完成步骤 `Get Data` 后，会显示出 Power Query 的界面
<img src="/images/2022-05/Snipaste_2022-05-01_14-57-23.png"  width="100%">

在 Power Query 中执行的每一步操作都会在右侧 Applied Steps 栏目显示，可以通过点击叉叉以实现撤回操作
<img src="/images/2022-05/Snipaste_2022-05-01_15-06-29.png"  width="100%">


**将 Query 导入 worksheet**
点击左上角的 `Close & Load`
- 选择 `Close & Load` 导入一个新的 sheet
- 选择 `Close & Load To...` 导入当前 sheet，或选择以其他方式导入
<img src="/images/2022-05/Snipaste_2022-05-01_15-40-18.png"  width="50%">





# 3. Query Edit 
## 3.1 Refresh (Update)
当把字符串 "MC" 填入<span style="background-color: yellow; color: black;">原表格</span>中的一个空缺 cell 时，其对应的 Query 表不会自动同步，需要右键单击 $\to$ `Refresh`
<img src="/images/2022-05/Snipaste_2022-05-01_15-18-36.png"  width="100%">
<img src="/images/2022-05/Snipaste_2022-05-01_15-21-11.png"  width="80%">
<img src="/images/2022-05/Snipaste_2022-05-01_15-22-15.png"  width="100%">

同理，对于其他导入方式，数据源发生改变后，点击 `Refresh` 即可同步数据源的改变
- 对于 Folder 类型的数据源，“改变”一般指的是文件的添加/删除







## 3.2 Add Column 添加列
### Custom Column
菜单栏 `Add Column` $\to$ `General` `Custom Column`

例如，添加一列来统计各类商品的总价
<img src="/images/2022-05/Snipaste_2022-05-03_09-53-46.png"  width="100%">

### Conditional Column
菜单栏 `Add Column` $\to$ `General` `Conditional Column`

例如，添加一列来查看支出是否超过了预算
<img src="/images/2022-05/Snipaste_2022-05-06_09-35-21.png"  width="100%">










## 3.3 Split Column 分隔列 (用以提取数据)
### Split Columns
例如，目标是把下图中的第一列分隔成两列 (课程代码 + 课程名)
<img src="/images/2022-05/Snipaste_2022-05-01_14-57-23.png"  width="100%">

点击菜单栏中部的 `Split Columns` $\to$ `By Delimiter`
在弹窗中点选 Split at `Left-most delimiter`

将两个分隔列都改名之后效果如下
<img src="/images/2022-05/Snipaste_2022-05-01_15-04-37.png"  width="100%">

<span style="background-color: yellow; color: black;">除此之外，还有非常多分隔的方式</span>，以满足不同需求
<img src="/images/2022-05/Snipaste_2022-05-06_09-03-02.png"  width="50%">

### Other Methods

> **M1: 根据输入智能调整分隔**

菜单栏 `Add Column` $\to$ 第一个图标 `Column From Examples`

例如，我们想从第一列提取出 Sydney, Brisbane and Melbourne
- 首先在右侧的第一行输入 Sydney $\to$ 按下回车
<img src="/images/2022-05/Snipaste_2022-05-06_09-09-01.png"  width="100%">
- 此时发现 Sydney and Melbourne 已经被成功提取，但是 Brisbane 被错误提取成了 Bri。因此接下来在下图红框内输入 Brisbane $\to$ 回车
<img src="/images/2022-05/Snipaste_2022-05-06_09-12-05.png"  width="100%">
- 最后点击 `OK` 完成提取
<img src="/images/2022-05/Snipaste_2022-05-06_09-14-22.png"  width="100%">

> **M2: 提取前/后任意长度的字符串**

菜单栏 `Add Column` $\to$ `Extract`







## 3.4 Append Queries 纵向合并
### 合并两个 Query
目标：为下图的两张表分别创建 Query，并将它们纵向合并
<img src="/images/2022-05/Snipaste_2022-05-02_16-32-26.png"  width="100%">

(1) 首先，为表 `Sydney` 创建 Query。为了使 `Sydney` 的列数与 `Other Instructors` 匹配<span style="background-color: yellow; color: black;">需添加 Location 列</span>
- Get Data: 点击 `From Table/Rage`
<img src="/images/2022-05/Snipaste_2022-05-02_16-37-28.png"  width="80%">

- 添加 Location 列
<img src="/images/2022-05/Snipaste_2022-05-02_16-39-48.png"  width="100%">
效果如下
<img src="/images/2022-05/Snipaste_2022-05-02_16-41-53.png"  width="80%">

- 导出 Query:
命名为 "Instructors_Sydney" $\to$ 点击 `Close & Load To...` $\to$ 点选 `Only Create Connection`

(2) 然后为表 `Other Instructors` 创建 Query
- 命名为 "Instructors_Other" $\to$ 点击 `Close & Load To...` $\to$ 点选 `Only Create Connection`
- 创建效果如下:
<img src="/images/2022-05/Snipaste_2022-05-02_16-53-29.png"  width="50%">

(3) 最后，Append Queries 实现纵向合并
- 点击 `Get Data` $\to$ `Combine Queries` $\to$ `Append`，在弹窗中选择刚刚创建的两个 Query Connections
<img src="/images/2022-05/Snipaste_2022-05-02_16-56-52.png"  width="100%">

- 纵向合并结果如下，可以将这个新的 Query 命名为 "Instructors_All"
<img src="/images/2022-05/Snipaste_2022-05-02_16-58-32.png"  width="100%">

### 合并多个 Query
目标: 将一个 Workbook 中三个 Sheet 纵向合并为一个 Sheet

(1) 首先，将这三个 Sheet 都创建为 Query
<img src="/images/2022-05/Snipaste_2022-05-02_21-03-28.png"  width="100%">

- 选择 `Append Queries as New`
<img src="/images/2022-05/Snipaste_2022-05-02_21-05-34.png"  width="100%">
<img src="/images/2022-05/Snipaste_2022-05-02_21-06-26.png"  width="100%">

- 通过改名解决 Append 异常
- - 下图显示多出来了三列，这是因为除了 Table1 有正常的 Header 以外，Table2 & Table3 均没有
<img src="/images/2022-05/Snipaste_2022-05-02_21-09-00.png"  width="100%">

- - 修改 Table2 中的 Header，并将下图红框中的代码复制进 Table3，从而完成对 Table3 的快速更改
<img src="/images/2022-05/Snipaste_2022-05-02_21-12-39.png"  width="100%">

- - 完成修改后，新的 Query 显示 Append 正常，完成合并








## 3.5 Merge Queries 横向合并
Append vs. Merge
<img src="/images/2022-05/Snipaste_2022-05-02_21-19-33.png"  width="100%">

非常类似 MySQL 中的 JOIN，主要包含
<img src="/images/2022-05/Snipaste_2022-05-02_21-26-41.png"  width="70%">
- Left/Right Outer Join
```sql
select * from A left join B on A.keyA = B.keyB
```
- Left/Right Anti Join
```sql
select * from A left join B on A.keyA = B.keyB
where B.keyB is NULL
```
- Inner Join
```sql
select * from A (inner) join B on A.keyA = B.keyB
```
- Full Outer Join
```sql
select * from A full outer join B on A.keyA = B.keyB
```

例如，想要在下一图的表中根据 Instructor ID，添加 Instructor Name 信息(储存在另一张表中(下二图))
<img src="/images/2022-05/Snipaste_2022-05-02_21-31-13.png"  width="100%">
<img src="/images/2022-05/Snipaste_2022-05-02_21-33-13.png"  width="70%">

点击 `Merge Queries`，在弹窗中除了指定两张表以及 Merge 类型，还需在每张表都选一列用于匹配，类似于
```sql
on A.keyA = B.keyB
```
<img src="/images/2022-05/Snipaste_2022-05-02_21-53-20.png"  width="80%">

再选择显示需要添加的列
<img src="/images/2022-05/Snipaste_2022-05-02_22-01-04.png"  width="80%">

最后点击 `Close & Load` 完成 Merge






## 3.6 Unpivot
对于下图这样 pivoted 的五列，会让我们难以分析其统计值。因此需要把它们聚合为一列 (unpivot)，用以直接储存分数 (1-5)
<img src="/images/2022-05/Snipaste_2022-05-04_08-56-49.png"  width="60%">

首先打开 Power Query 界面 $\to$ 选中这五列数据 (按住Shift) $\to$ 菜单栏 `Transform` $\to$ `Unpivot Columns` (或者选中其他所有的数据，然后点击 `Unpivot Other Columns`)

将生成的第一列改名为 "Rating"，<span style="background-color: yellow; color: black;">并将其数据类型修改为 Number</span>。再删除第二列，即可完成 unpivoting
<img src="/images/2022-05/Snipaste_2022-05-04_09-07-36.png"  width="60%">







## 3.7 Pivot
目标: 把每个 Room 的所有 Facility 信息都显示在一行数据中
<img src="/images/2022-05/Snipaste_2022-05-04_09-59-14.png"  width="100%">

菜单栏 `Transform` $\to$ `Pivot Column`
<img src="/images/2022-05/Snipaste_2022-05-04_10-01-51.png"  width="100%">

完成
<img src="/images/2022-05/Snipaste_2022-05-04_10-02-55.png"  width="100%">






## 3.8 Group
例如，统计每个 Brach 的每个 Department 的所有课程的天数和
<img src="/images/2022-05/Snipaste_2022-05-04_22-35-06.png"  width="100%">
```sql
select Branch, Department, sum(Days)
from Table
group by Branch, Department
```

在 Power Query 界面菜单栏 `Home` $\to$ `Group By`
<img src="/images/2022-05/Snipaste_2022-05-04_22-39-52.png"  width="100%">

初步完成分组，但同时也发<span style="background-color: yellow; color: black;">异常: Sydney 下有两个 Sales</span>
<img src="/images/2022-05/Snipaste_2022-05-04_22-41-04.png"  width="80%">

合理怀疑是其中的一个 Sales 字符串后面跟了一些空格，从而被识别为不同的两组。为了解决这个问题:
- 首先点击右侧 `Applied Steps` 窗口中分组操作 (`Grouped Rows`) 的上一步 (`Changed Types`) 从而返回到分组之前
- 再选中 `Department` 列，并点击 `Replace Values`

<img src="/images/2022-05/Snipaste_2022-05-04_22-44-13.png"  width="100%">

在尝试将 " " 替换为 "" 无果后，猜测这个空格是不是 `Non-break Space`，尝试将其替换为 "" 后，问题解决
<img src="/images/2022-05/Snipaste_2022-05-04_22-46-54.png"  width="100%">

最后点击右侧 `Applied Steps` 窗口的中分组操作 (`Grouped Rows`)，发现异常消失





## 其他常用功能
> **Merge columns 聚合数据**

按住 Shift, 同时选择两个目标列 $\to$ 右键单击任一列名 $\to$ 选择 `Merge Columns`
<img src="/images/2022-05/Snipaste_2022-05-02_09-36-24.png"  width="100%">

> **将第一行设置为 Headers**

<img src="/images/2022-05/Snipaste_2022-05-02_10-12-16.png"  width="100%">

> **Format 修改格式** 

菜单栏 `Transform` $\to$ `Text Column` `Format`

### About null
> **Fill 填充 null**

<img src="/images/2022-05/Snipaste_2022-05-01_15-38-35.png"  width="100%">

> **Replace Values 更改 null**

菜单栏 `Transform` $\to$ `Any Column` `Replace Values`








# 4. Ex: Clean Data 数据清洗

例如对于这样一张表，由上至下储存了多个人的 Course Evaluation，每个 Evaluation 包含七个小问题以及对应的打分

而我们需要从中提取出每个 Qustion 的 **average score**

<img src="/images/2022-05/Snipaste_2022-05-03_10-51-21.png"  width="100%">

**Step1: 去除错误的自动操作**
将其导入 Power Query 之后，软件会自动执行一些它认为可能正确的操作，例如修改某些列的数据类型、自动将第一行转为 Headers 等。因此第一步就是去除那些错误的自动操作
<img src="/images/2022-05/Snipaste_2022-05-03_10-56-34.png"  width="100%">

**Step2: 重新设置 Headers**
观察上图，发现目标 Headers 位于第七行。
- 因此首先需要删除前六行: 菜单栏 `Home` $\to$ `Remove Rows` $\to$ `Remove Top Rows`
- 再将当前的第一行设置为 Headers: 菜单栏 `Home` $\to$ `Use First Row as Headers`

**Step3: 填充 null**
第一列向下填充，第二列向上。菜单栏 `Transform` $\to$ `Fill` $\to$ `Down/Up`
<img src="/images/2022-05/Snipaste_2022-05-03_11-09-29.png"  width="100%">

**Step4: 去除无用数据**
例如在上图中的 Questions 列，可以发现除了 Q1-Q8，还参杂一些无用的数据，例如 9-16 行的 null，以及 17 行的 "Questions"。点击列名右侧的 Filter 图标从而去除它们

**Step5: 去除重复数据**
我们将"重复数据"定义为所有属性值都完全相同的数据
- 首先按住 `Shift` 键 $\to$ 点击第一列的 Header 和最后一列的 Header 从而实现全选
- 再点击菜单栏 `Home` $\to$ `Remove Rows` $\to$ `Remove Duplicates`

**Step6: 根据需要进行排序**
需求
```sql
order by "Questions", "Eval No."
```
<img src="/images/2022-05/Snipaste_2022-05-03_12-43-17.png"  width="60%">

**Step7: Unpivoting Data**
[详见](#unpivot-data)

**Step8: 创建 Pivot Table**
<img src="/images/2022-05/Snipaste_2022-05-04_09-15-53.png"  width="100%">

新建一张 Worksheet 存放 Pivot Table

Excel 主界面菜单栏 `Insert` $\to$ `Tables` $\to$ `Pivot Table`

在弹窗中输入 Table Name: Evals
<img src="/images/2022-05/Snipaste_2022-05-04_09-19-20.png"  width="50%">

然后经过一通操作，得到下图
<img src="/images/2022-05/Snipaste_2022-05-04_09-43-25.png"  width="100%">

