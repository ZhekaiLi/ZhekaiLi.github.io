---
layout: post
title: Grasshopper Basis
categories: Grasshopper-Development
description: Personal Notes
keywords: Grasshopper-Development, Grasshopper, C#
---


<center>

# Grasshopper Basis
</center>

【缩略词】：
1. Brep: Boundary representation 边界表示

# 1. Grasshopper Window

**(1) 切换不同项目**
- 点击右上角文件名即可查看

<img src="https://img-blog.csdnimg.cn/20200805212310217.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L3dlaXhpbl80MzcyODEzOA==,size_16,color_FFFFFF,t_70" width="80%" alt="">

# 2. Panel Textbox
文本框是一个基础组件，主要用于显示电池的输出以及作为数据的输入。

需要注意的是当作为输入时，panel 的内容默认为 text 类型，但是可以根据电池输入端的要求进行变更。如图，在 panel 内输入字符 3 后，text 电池与 number 电池都没有报错（这两个电池的功能在于检查输入的数据类型）
<img src="https://img-blog.csdnimg.cn/202008071349282.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L3dlaXhpbl80MzcyODEzOA==,size_16,color_FFFFFF,t_70" width="30%" alt="">

此外，输完数字后要通过点击外部区域来确认输入，不能敲回车键。因为敲回车键会使得 Panel 的内容变成 3\n，此时就不能变更为 number 了，敲回车键后的效果如下图
<img src="https://img-blog.csdnimg.cn/20200807135232614.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L3dlaXhpbl80MzcyODEzOA==,size_16,color_FFFFFF,t_70" width="30%" alt="">

# 3. Bettery
## 3.1 将在 Rhino 中创建的 geometry 赋值给电池
以 Curve 为例，具体步骤：
1. 右键单击组件，选择 Set one Curve
2. 返回 Rhino 图形界面选择已经绘制完成的曲线
<img src="https://img-blog.csdnimg.cn/20200805152340882.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L3dlaXhpbl80MzcyODEzOA==,size_16,color_FFFFFF,t_70" width="50%" alt="">
## 3.2 删除电池间的连线
按住 Crtl 键，点击一段连线的尾部（此时会出现一个红色的箭头图标），再把连线从尾部拖回头部即可完成删除
## 3.3 Bake：将 Rhino 与 GH 分离
将 GH 中的虚拟模型导入至 Rhino 中变为实体（即可在 Rhino 中做进一步的建模分析导出扥操作）
以 Point 为例
1. 在 GH 中绘制一个点
<img src="https://img-blog.csdnimg.cn/20200813133220124.png" width="50%" alt="">
2. 右键单击电池，选择 Bake
<img src="https://img-blog.csdnimg.cn/20200813133240666.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L3dlaXhpbl80MzcyODEzOA==,size_16,color_FFFFFF,t_70" width="50%" alt="">
4. 可以看到不管是"取消 Preview", "选择 Enable" 还是 "删除电池"，Rhino 中创建的点都不会消失
<img src="https://img-blog.csdnimg.cn/20200813133337437.png" width="50%" alt="">

##  3.4 Internalise data：将 GH 与 Rhino 分离
将 Rhino 中的模型参数固化于电池（即可在 Rhino 中做的改变将不会影响电池中储存的模型）
以 Point 为例
1. 同 Section 3.1 赋值完成后，右键单击电池，选择 Internalise data
<img src="https://img-blog.csdnimg.cn/20200813133934963.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L3dlaXhpbl80MzcyODEzOA==,size_16,color_FFFFFF,t_70" width="50%" alt="">
2. 可以看到在 Rhino 中点的移动不会影响电池储存的点
<img src="https://img-blog.csdnimg.cn/20200813134340931.png" width="50%" alt="">

## 3.5 Ctrl + Alt + 左键：电池在菜单内的位置
...

# 4. Basic Geometry
**（1）平面：** Plane Surface (plane, x, y)
**（2）球壳：** Sphere (plane/ point, r)
1. 第一个输入若为 plane，则球心位于改平面的左上角顶点

**（3）长方体：** Center box (plane/ point, x, y, z)

## 4.1 Functions
**（1）放大/ 缩小几何体：**
1. 各方向等比例缩放：Scale (geometry, center, factor)
2. 个方向自定义比例缩放：Scale NU (geometry, center, x, y, z)

**（2）拆分几何体为面、边线、顶点：** 
`Deconstruct Brep (geometry) >> (planes, edges, vetexes)`

如果输入的几何体为球体，则三个输出分别为已下形式：

<img src="https://img-blog.csdnimg.cn/20200815132005801.png" width="60%" alt=""><br>

<img src="https://img-blog.csdnimg.cn/20200815132027783.png" width="60%" alt=""><br>

<img src="https://img-blog.csdnimg.cn/20200815132050786.png" width="60%" alt="">

**（3）拉伸几何体，拉线成面，拉面成体：** 
`Extrude (geometry, vector)`

**（4）几何体 A 与 几何体 B 的交集 and 并集：** 
`Solid Union(), Solid Intersection()`

**（5）几何体 A 减去自身与几何体 B 的重叠部分后剩下的几何体：** 
`Solid Difference (geometry A, geometry B)`

## 4.2 Curved Surface (自由曲面)
**（1）在两段 curves 之间生成曲面：** 
`Loft (curves, )`

<img src="https://img-blog.csdnimg.cn/20200815134049321.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L3dlaXhpbl80MzcyODEzOA==,size_16,color_FFFFFF,t_70" width="70%" alt="">

**（2）curve 沿轨迹 rail生成曲面：** 
`Sweep (rail(curve, line...) , curve)`

<img src="https://img-blog.csdnimg.cn/20200815135401979.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L3dlaXhpbl80MzcyODEzOA==,size_16,color_FFFFFF,t_70" width="70%" alt="">

**（3）沿轨迹 rail，生成通过 curves 的曲面：** 
`Sweep(rail(line, curve...), curves)`

<img src="https://img-blog.csdnimg.cn/20200815135812460.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L3dlaXhpbl80MzcyODEzOA==,size_16,color_FFFFFF,t_70" width="70%" alt="">

**（4）curve 围绕 axis 旋转一定角度生成曲面：** 
`Revolution (curve, axis(line), degree)`

以生成圆台的侧边（灯罩形）为例：
图中的 Line SDL(point, vector, length) 电池的功能为，从 point 出发沿着 vector 生成长度为 length 的直线
<img src="https://img-blog.csdnimg.cn/20200815153659781.png" width="50%" alt="">

**（5）curve 沿轨迹 rail 围绕 axis 旋转生成曲面：** 
`Rail Revolution (curve, rail(curve, line...), axis(line))`

<img src="https://img-blog.csdnimg.cn/2020081515531299.gif" width="60%" alt="">

**（6）生成由闭合曲线围城的面：** 
1. 曲线在一个平面内，即为平面曲线：`Boundary Surface (curve)`
2. 曲线为空间曲线：`Patch (curve)`（Patch 是一个很有意思的电池，输入可以有很多，能够生成在多个点、线的限制下的曲面）



 




