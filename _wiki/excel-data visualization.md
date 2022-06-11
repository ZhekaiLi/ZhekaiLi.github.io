---
layout: wiki
title: Data Visualization
cate1: Excel
cate2:
description: 
keywords: Excel
---

# 1 Formatting
## 1.1 Conditional Formatting
用于图形化数据，使其更容易理解

`Home`$\to$`Styles`$\to$`Conditional Formatting`

<img src="/images/2022-06/Snipaste_2022-06-05_19-58-59.png"  width="30%">

### Trend-based
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



### Value-based
**(1) Top/Bottom Rules**

前n个、后n个、前n%、后n%...

<img src="/images/2022-06/Snipaste_2022-06-06_09-12-02.png"  width="50%">

**(2) Highlight Cells Rules**

查重、设定范围或阈值...

<img src="/images/2022-06/Snipaste_2022-06-06_09-14-43.png"  width="50%">



### Interactive Visualization
通过自定义 Rules 可以实现一些很棒的效果。
#### .1 单元格与单元格交互

实现效果: 在左上角 List 框内选中任意一个州的名字，地图中对应的黑点就会亮起来

<img src="/images/2022-06/Snipaste_2022-06-06_09-19-07.png"  width="70%">

首先把地图移开，不难发现实现的原理就在于使包含字符的这些单元格，当检测到自身与左上角的选择框一样时，就变成黄色。点击 `Conditional Formatting`$\to$`New Rule...`，并完成如下设置（注意: 单元格 `O11` 不要固定，因为之后还需要把这个公式应用到其他单元格中）

<img src="/images/2022-06/Snipaste_2022-06-06_09-25-02.png"  width="100%">

首先单击选中刚刚定义 Formula 的单元格 `O11`，再单击下图中的 `Format Painter`，当出现一个刷子一样的光标时，框选整个目标区域。完成

<img src="/images/2022-06/Snipaste_2022-06-06_09-29-23.png"  width="50%">


#### .2 单元格与行列交互

实现效果: 在右上角 List 框内选中任意一个州的名字，表格中对应的行就会被蓝色高亮显示（并且不会覆盖原有的红色高亮）

<img src="/images/2022-06/Snipaste_2022-06-06_10-24-31.png"  width="100%">

首先框选出表格区域，在自定义公式中输入 `$B5`，这里固定列是因为想把这个 Format 应用到所选表格的所有行

<img src="/images/2022-06/Snipaste_2022-06-06_10-22-42.png"  width="100%">

随后在 `Conditional Formatting`$\to$`Manage Rules...` 中通过点击上下箭头，把红色高亮的显示优先级调高

<img src="/images/2022-06/Snipaste_2022-06-06_10-23-40.png"  width="70%">


#### .3 图标与其他元素交互

实现效果，点击代表州的圆形，选择框 `K1` 就会变成对应州的名字，从而进一步地实现对于圆形的黄色高亮（详见 *(1) 单元格与单元格交互*）,以及对于表格区域数据的蓝色高亮（详见 *(2) 单元格与行列交互*）

<img src="/images/2022-06/Snipaste_2022-06-06_10-58-51.png"  width="100%">

这一步需要应用到 `宏(Macro)`

**(1) 首选激活宏选项**
- 另存为文件为 Macro-Enabled
- 打开 `Excel Options`，勾选 `Developer`

<img src="/images/2022-06/Snipaste_2022-06-06_10-34-27.png"  width="70%">

<img src="/images/2022-06/Snipaste_2022-06-06_10-36-06.png"  width="100%">

**(2) 录制宏**
- 点击 `Record Macro`，为宏命名并指定快捷键，然后点击 `OK` 进入录制
- <span style="background-color: yellow; color: black;">这个宏需要实现的效果: 在 `K1`（即选择框）中输入字符 "NT"</span>
- 录制过程: 首先点击 `K1`，再输入 "NT"，最后按下回车键
- 点击菜单栏中的 `Stop Recording` 结束录制

<img src="/images/2022-06/Snipaste_2022-06-06_10-40-00.png"  width="70%">

然后需要把刚刚定义的宏应用到其他所有的州
- 首先打开进入编辑界面（这是一个 VB 编译器）
- 在代码框中可以看到先前定义的 `NT()` 宏，把这个宏复制应用到其他州，这个过程需要一定的适应性修改

<img src="/images/2022-06/Snipaste_2022-06-06_10-48-09.png"  width="70%">
<img src="/images/2022-06/Snipaste_2022-06-06_10-50-40.png"  width="50%">

**(3) 绑定宏**

最后我们需要把宏操作与点击图标的操作绑定
- 选中一个圆形图标，例如选中 "NT" 州对应的圆圈
- 右键单击圆圈$\to$`Assign Macro...`
- 在弹窗中选择需要绑定的名为 "NT" 的宏

完成！之后只要把鼠标移动到圆形的上方，光标就会变成一个手，此时点一下就能够实现最初设想的效果




## 1.2 Sparkline & Shape

**(1) Sparkline**

这是一种缩小化的显示数据图表的方式

- 点击菜单栏 `Insert`$\to$`Sparklines`$\to$`Column`
- 在弹窗中选择数据区域，以及显示 Sparkilines 的区域

<img src="/images/2022-06/Snipaste_2022-06-06_13-08-42.png"  width="70%">

还可以进一步美化显示效果，例如使数值最大的变成红色

<img src="/images/2022-06/Snipaste_2022-06-06_15-03-56.png"  width="50%">

以上展示了柱状图，还能创建线图，方法类似

**(2) Shape**

形状可以使我们的数据可视化更加优雅。

例如，书接上文，在[这里](#3-图标与其他元素交互)我们已经完成了一个非常优雅的效果，即通过点击地图上的表示州的圆圈，就能够使之高亮，并在左侧表格中也高亮显示对应州的数据。这些实现的关键当点击任一圆圈时，选择框内都能显示出该圆圈指向的州

<img src="/images/2022-06/Snipaste_2022-06-06_15-13-30.png"  width="100%">

更进一步的，我们想要在这张图上显示更多的数据: 例如下边这张表中的三列数据

<img src="/images/2022-06/Snipaste_2022-06-06_15-18-25.png"  width="60%">

- 首先使用 `VLOOPUP()` 从上表中提取选择框 `K1` 所显示的州的三个数据
- 然后点击菜单栏 `Insert`$\to$`Illustrations`$\to$`Shapes` 选择一个形状
- 把这个形状复制成三个（对应需要显示的三个数据）
- 全选这三个形状，如下图，点击 `Align Bottom`$\to$`Distribute Horizontally` 

<img src="/images/2022-06/Snipaste_2022-06-06_15-27-05.png"  width="80%">

完美排列！最后在每个形状的 Formula Bar 中输入其对应的单元格，完成

<img src="/images/2022-06/Snipaste_2022-06-06_15-30-14.png"  width="70%">




## 1.3 Custom number format

对于如下列，我们希望正数显示为绿色，负数红色，零则不显示

<img src="/images/2022-06/Snipaste_2022-06-06_15-47-20.png"  width="15%">

- 首先框选目标区域
- 点击如图步骤二所指示的箭头图表
- 在弹窗如图步骤三所指示的框中输入 `格式信息`

<img src="/images/2022-06/Snipaste_2022-06-06_15-54-02.png"  width="100%">

```cs
// 格式信息
Positive;[Negative];[Zero];[Text]

// 例如
// 以下表示正数是绿色，负数红色，零则不显示
[Green]0.00%;[Red]-0.00%;

// 还可以吧数字换成图表，例如用上箭头表示增加，下箭头表示减少
// 还可以指定具体的范围
[>0.01][Green]arrow_up;[<-0.01][Red]arrow_down;[Black]
```



---



# 2 Charting Techniques
## 2.1 Column Chart
下图是一张非常高效的图，清晰地反映了每十年的:
- 排放物的各种来源的比例
- 排放物总量
- 排放物总量的增幅

那么怎么从如下这张数据表中画出这样的图呢?

<img src="/images/2022-06/Snipaste_2022-06-06_19-09-33.png"  width="100%">

那么怎么从如下这张数据表中画出这样的图呢?

<img src="/images/2022-06/Snipaste_2022-06-06_19-15-02.png"  width="100%">

**(1) 创建普通柱状图**
- 框选数据区域，插入一张简单的 `2D Column`

<img src="/images/2022-06/Snipaste_2022-06-06_19-17-20.png"  width="70%">

**(2) 修改为堆叠式柱状图**
- 点击菜单栏`Chart Design`$\to$`Change Chart Type`，选择 `Stacked Column`
- 双击一个色块，然后在右侧窗口减小 `Gap Width` 至 50%

<img src="/images/2022-06/Snipaste_2022-06-06_19-23-34.png"  width="70%">

**(3) 修改横/纵坐标**
- 修改横坐标: 点击`Select Data`$\to$编辑横坐标$\to$框选第一列年份为横坐标
- 修改纵坐标: 点击纵坐标$\to$在右侧窗口中把 `Display units` 改为 Billions

<img src="/images/2022-06/Snipaste_2022-06-06_19-25-38.png"  width="100%">

**(4) 添加表示增幅的数据作为趋势线**
- 框选最后一列数据$\to$`Ctrl+C`$\to$选中图表$\to$`Ctrl+V`。此时虽然数据被添加进来的，但仍然是以 Stack Column 格式，并且因为数据太小根本看不出来了
- 添加 Secondary axis: 打开`Change Chart Type`，按照下图完成操作。完成

<img src="/images/2022-06/Snipaste_2022-06-06_19-35-51.png"  width="70%">




## 2.2 Pie Chart
**(1) 普通的饼图**
- 框选数据区域，插入 `2D Pie`
- 修改 Layout: 菜单栏 `Chart Design`$\to$`Quick Layout`$\to$选择一种显示比例的
- 去掉标题，修改字体
- 插入一张图片放到中心位置: 选中图表$\to$菜单栏 `Insert`$\to$`Illustrations`$\to$`Pictures`

<img src="/images/2022-06/Snipaste_2022-06-07_09-27-57.png"  width="70%">

**(2) Doughnuts: 空心饼图与双圈饼图**

实现效果: 同时包含排放信息与人口信息

<img src="/images/2022-06/Snipaste_2022-06-07_10-00-22.png"  width="50%">

首先创建 Doughnuts:
- 复制 *(1) 普通的饼图* 的结果，并修改图表类型

<img src="/images/2022-06/Snipaste_2022-06-07_09-40-00.png"  width="70%">

随后添加人口数据: 上一步做完后会产生一个双环图，每个环包含一样的数据
- 菜单栏 `Chart Design`$\to$`Select Data`
- 编辑弹窗左侧的数据区域，使得第一环（内环）显示排量，外环显示人口

<img src="/images/2022-06/Snipaste_2022-06-07_09-43-31.png"  width="100%">

最后进行美化:
- 去掉外层的 Legend
- 插入两个文本框，靠近外层的显示 Population，内层则为 Emissions
- 如下图1: 调整中间空白圆形的大小，需要双击一个色块才能打开右侧栏目
- 如下图2: 调整每个外圈色块的透明度


<img src="/images/2022-06/Snipaste_2022-06-07_09-58-41.png"  width="70%">

<img src="/images/2022-06/Snipaste_2022-06-07_09-59-19.png"  width="70%">

**(3) 非常酷炫的饼图**

实现效果: 显示某国家在减排上的进步程度

<img src="/images/2022-06/Snipaste_2022-06-07_10-32-42.png"  width="40%">

首先选择一长列（大概60行）包含相同数字的数据，并创建 Doughnut。在取消 Label 和 Legend、修改颜色以及空心圆的大小后，效果如下:

<img src="/images/2022-06/Snipaste_2022-06-07_10-03-28.png"  width="70%">

随后把国家名及其对应的减排数据添加进去，此时呈现出内外双圈

<img src="/images/2022-06/Snipaste_2022-06-07_10-17-59.png"  width="70%">

最后把外环数据叠放到内环之上，并使表示 %Offset 的那部分圆环透明
- 如下图1: 使用 Secondary Axis 实现叠放
- 如下图2: 使表示 %Offset 的那部分圆环透明

<img src="/images/2022-06/Snipaste_2022-06-07_10-20-44.png"  width="100%">

<img src="/images/2022-06/Snipaste_2022-06-07_10-30-45.png"  width="70%">



## 2.3 Line Chart

实现效果: 根据已知数据（1960-2018）画出CO2浓度变化图，并预测10年后的浓度

<img src="/images/2022-06/Snipaste_2022-06-07_13-22-55.png"  width="100%">

首先选择数据区域（二氧化碳浓度），适当更改一下表格样式

<img src="/images/2022-06/Snipaste_2022-06-07_12-50-30.png"  width="100%">

调整坐标轴
- 横坐标: 选择年份数据列作为横坐标，并改成纵向显示
- 纵坐标: 修改范围，从 300 开始

<img src="/images/2022-06/Snipaste_2022-06-07_12-54-27.png"  width="100%">

显示最新数据的数值: 
- 如下图1: 放大图表，在最后一段绿线的后半部分，有间隔地点击两次
- 如下图2: 完成上一步后曲线的最右端会出现一个小方框，后勾选 `Data Labels`

<img src="/images/2022-06/Snipaste_2022-06-07_13-01-00.png"  width="60%">

<img src="/images/2022-06/Snipaste_2022-06-07_13-03-16.png"  width="70%">

画趋势线:
- 如下图1: 打开右侧关于趋势线的栏目
- 如下图2: 首先勾选显示 `R-square`（该数值越接近1说明拟合越好），然后选择一个 $R^2$ 最接近1的拟合方式，最后勾选显示公式

<img src="/images/2022-06/Snipaste_2022-06-07_13-06-43.png"  width="70%">

<img src="/images/2022-06/Snipaste_2022-06-07_13-09-56.png"  width="70%">

预测十年后的数据:
- 首先在上图右下角的 `Forcast`$\to$`Forward` 输入 10
- 对于趋势线公式 $y=ax^2+bx+c$, $x=1$ 指的是第一年（1960），因此计算十年后（2028）预测值只需把 $x=69$ 带入公式
- 最后取消显示公式，并把通过插入文本框来显示预测值


**修改日期显示**

修改日期间隔

<img src="/images/2022-06/Snipaste_2022-06-08_10-00-43.png"  width="70%">

修改日期显示格式

<img src="/images/2022-06/Snipaste_2022-06-08_10-01-28.png"  width="70%">


## 2.4 Area Chart

**(1) Normal Area Chart**

左侧是一张表示长期二氧化碳浓度的线图，可以很方便地将其转化为面积图

<img src="/images/2022-06/Snipaste_2022-06-07_14-51-00.png"  width="100%">

**(2) Stacked Area Chart**

堆叠面积图能很好地处理那种乱七八糟的线图

<img src="/images/2022-06/Snipaste_2022-06-07_14-55-29.png"  width="100%">

**(3) 100% Stacked Area Chart**

这种图能显示比例的变化，相当于给饼图添加了一个时空维度

<img src="/images/2022-06/Snipaste_2022-06-07_15-00-13.png"  width="100%">

进一步美化: 将 Legend 显示在图中
- 首先勾选 `Data Labels`，会出现像红框2那样好几条密密麻麻的数据
- 然后在右侧栏目勾选 `Series Name`，取消勾选 `Value`

<img src="/images/2022-06/Snipaste_2022-06-07_15-03-43.png"  width="100%">




## 2.5 Scatter & Bubble Chart

**(1) Scatter Chart**

散点图可以显示两列数据，并反映其关系

<img src="/images/2022-06/Snipaste_2022-06-07_15-27-08.png"  width="100%">

**(2) Bubble Chart**

而气泡图可以在散点图的基础上，通过气泡大小再显示一列数据（例如表示人口）
- 首先转换成 `3-D Bubble`，此时所有球都一样大
- 菜单栏 `Chart Design`$\to$`Select Data`$\to$左半边的 `Edit`$\to$在弹窗中将 `Series bubble size` 与 Population 列进行绑定

<img src="/images/2022-06/Snipaste_2022-06-07_15-30-50.png"  width="70%">

<img src="/images/2022-06/Snipaste_2022-06-07_15-34-17.png"  width="70%">

更进一步的，还可以用多种颜色的气泡来表示分类。例如下图中用不同颜色分别代表了五大洲。同时，由于亚洲有中印两个人口大国（大圈圈），因此在左侧数据栏中把 Aisa 移到了最上边（也就是在显示的时候作为最底层）

<img src="/images/2022-06/Snipaste_2022-06-07_15-37-52.png"  width="100%">



## 2.6 Hierarchy Chart

有两种图能够表示层级关系

**(1) Sunburst Chart**

<img src="/images/2022-06/Snipaste_2022-06-08_18-20-48.png"  width="70%">

**(2) Treemap**

<img src="/images/2022-06/Snipaste_2022-06-08_18-22-50.png"  width="70%">



## 2.7 Waterfall & Funnel Chart
**(1) Waterfall Chart**

瀑布图之于普通的柱状图，区别在于它基于的是数据的变化值而不是数据本身，因此能更好地反映 X-Labels 对于数据的影响（例如，下图很好地反映了各个国家对于欧洲人口增长的影响）

<img src="/images/2022-06/Snipaste_2022-06-08_18-33-25.png"  width="100%">

但是，上图存在一个问题: 最左下角表示总体人口增长的数据，在瀑布图中被错误得画成了最高的那一段。因此需要选中那一段$\to$右键单击$\to$`Set as Total`

<img src="/images/2022-06/Snipaste_2022-06-08_18-37-50.png"  width="70%">

<img src="/images/2022-06/Snipaste_2022-06-08_18-39-04.png"  width="70%">

**(2) Funnel Chart**

漏斗图很适合显示一些逐层缩减的关系，比如学生数量从本科到master再到phd逐层减少，再例如塑料数量从最开始的生产到废弃到泄漏再到流入海洋逐渐减少

<img src="/images/2022-06/Snipaste_2022-06-08_18-45-02.png"  width="70%">



## 2.8 Geospatial Chart

非常酷炫，但是国内好像不支持显示地图 `Sorry, map charts aren't supported for your location`

## Custom Chart Techniques

以人口图为例，希望实现如下非常 Amazing 的效果: 展示1996-2019之间英国人口的男女以及年龄比例的变化

<img src="/images/2022-06/GIF_20220608.gif"  width="70%">


首先需要将一个性别的数据变成负数，这样的话两个性别才能一左一右显示
- 在任一单元格中输入 -1$\to$`Ctrl+C`复制这个单元格
- 选中女性数据列 `Ctrl+Shift+Down`
- 点击左上角的 `Paste`$\to$`Paste Special`
- 在弹窗中完成如下点选

<img src="/images/2022-06/Snipaste_2022-06-08_19-24-33.png"  width="100%">

随后点击插入 `2-D Bar`，此时的杆状图存在一个很明显的问题: 表示男性和女性的杆是错开的，没在一条直线上

<img src="/images/2022-06/Snipaste_2022-06-08_19-54-46.png"  width="70%">

修改图的格式:
- 下图1: 将 `Series Overlap` 修改为百分百，并缩小 `Gap Width`
- 下图2: 将纵坐标轴放到图的左侧
- 下图3: 将横坐标轴的负数上的负号去掉（通过设置 `Format Code`）

<img src="/images/2022-06/Snipaste_2022-06-08_20-18-33.png"  width="100%">

<img src="/images/2022-06/Snipaste_2022-06-08_20-34-30.png"  width="100%">

<img src="/images/2022-06/Snipaste_2022-06-08_20-36-35.png"  width="100%">

将图的标题与一个单元格绑定，使其能够随着选择年份的变化而变化

<img src="/images/2022-06/Snipaste_2022-06-08_20-41-18.png"  width="100%">

最后要设置两个按钮:
- 按钮1 "Animate": 从1996-2019逐年显示人口比例的变化
- 按钮2 "Reset": 从2019还原至1996

Macro 设置如下，而后再将这些宏与按钮绑定

<img src="/images/2022-06/Snipaste_2022-06-08_20-43-41.png"  width="70%">

<img src="/images/2022-06/GIF_20220608.gif"  width="70%">

## Creative Chart Techniques

创建一个汽车仪表盘图，用于表示某年海平面上升问题的严重程度

<img src="/images/2022-06/Snipaste_2022-06-09_09-27-13.png"  width="70%">

首先绘制仪表盘: 
- 下图1: 插入 Doughnut 图，并旋转一定角度
- 下图2: 将下面半圈隐去（设为 `No fill`），将上边半圈设置为渐变色，并取消白色的分割线（Border）

<img src="/images/2022-06/Snipaste_2022-06-09_09-05-59.png"  width="70%">

<img src="/images/2022-06/Snipaste_2022-06-09_09-15-14.png"  width="70%">

其次绘制仪表指针:
- 下图1: 红框1表示指针的位置，红框2表示指针的宽度，红框3表示剩下的圆环
- 下图2: 将指针数据插入仪表盘图
- 下图3: 先将除了表示指针之外的圆环隐去，再通过设置 secondary axis 是两个环重合，最后把通过指针图设置为 Pie Chart 以显示整根指针

<img src="/images/2022-06/Snipaste_2022-06-09_09-19-09.png"  width="70%">

<img src="/images/2022-06/Snipaste_2022-06-09_09-22-27.png"  width="70%">

<img src="/images/2022-06/Snipaste_2022-06-09_09-24-31.png"  width="100%">


