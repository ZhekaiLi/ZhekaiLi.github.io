---
layout: post
title: Grasshopper Development-GhNote-02 Geometry
categories: Grasshopper-Development
description: Personal Notes
keywords: Grasshopper-Development, Grasshopper, C#
---

【缩略词】：
1. Brep: Boundary representation 边界表示


# 1 基本几何体
**（1）平面：** Plane Surface (plane, x, y)
**（2）球壳：** Sphere (plane/ point, r)
1. 第一个输入若为 plane，则球心位于改平面的左上角顶点

**（3）长方体：** Center box (plane/ point, x, y, z)

# 2 相关操作
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

# 3 自由曲面
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












