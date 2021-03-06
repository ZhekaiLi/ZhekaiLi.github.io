﻿---
layout: post
title: Grasshopper-Development C# Part 5 - Tricks
categories: Grasshopper-Development
description: Personal Notes
keywords: Grasshopper-Development, Grasshopper, C#
---
**ATTENSION - If some LeTeX equations could not show well, pleae try to refresh this page.**

**【说明】**
1. 本专栏的 Part 5 主要介绍作者在学习和实践中所遇到的一些问题的解决方案，如有差错或更优解，欢迎指正
2. 您如果碰到有关 GH 二开的任何问题，欢迎在本专栏的任意一篇博文下留言交流

**【推荐阅读】**
1. 查文档：(1) [RhinoCommon SDK](https://developer.rhino3d.com/5/api/RhinoCommon/html/N_Rhino.htm#!) (2) [Grasshopper API](https://developer.rhino3d.com/api/grasshopper/html/T_Grasshopper_DataTree_1.htm#!)
2. CSDN专栏地址：[专栏：Rhino (Grasshopper) 二次开发 (C#)](https://blog.csdn.net/weixin_43728138/category_10266504.html)

**【参考资料】**
1. Youtube: [C# Scripting and Plugin Development for Grasshopper](https://www.youtube.com/watch?v=urWRRpy1fCw&t=5224s)

# 5.1 
#### 生成 Circle 内的 Suface，即生成由圆周围城的圆面
## Problem
为了创建一个圆面，作者希望能够通过某种方法，凭借 new Circle(plane, center, radius) 所创建的圆周曲线，直接生成圆面。

这个操作在 GH 的可视化编程中非常容易实现，例如 Boundary Surface & Patch，但在 C# 编程实现的过程中，作者查阅了整个 Surface Class & Circle Class，都没能找到实现方案。

## Solvement
最后通过在 GH 论坛上的搜索，该问题得以较好地解决，[这是论坛帖子的链接](https://www.grasshopper3d.com/forum/topics/circle-curve-to-surface)，具体代码如下

```csharp
Circle circle = new Circle(Plane.WorldXY, new Point3d(0, 0, 0), 1);
Brep brep = Brep.CreatePlanarBreps(circle.ToNurbsCurve())[0];
```
`brep` 即为我们所需要的的圆面

![在这里插入图片描述](https://img-blog.csdnimg.cn/20200816201901185.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L3dlaXhpbl80MzcyODEzOA==,size_16,color_FFFFFF,t_70#pic_center)

# 5.2
#### 深度复制几何体 Deeply Duplicate Geometry

## Problem
在复制 GeometryBase 类型的对象的过程中（如 surface, box），因为它们是引用类型的对象（不同于 point, line），有很多种方法都不能实现它们的深度复制，以至于在进行一些变换操作如旋转变换时，始终无法实现需求

以下是典型的失败案例集合：
（1）构建一对以 XY 平面为对称轴的圆面

```csharp
// wrong method 1
/// 封闭圆环c形成圆面b
Brep b = Brep.CreatePlanarBreps(c.ToNurbsCurve())[0];
geometryList.Add(b);
/// 镜像
b.Transform(Transform.Mirror(Plane.WorldXY));
geometryList.Add(b);

// wrong method 2
/// 封闭圆环c形成圆面b
Brep b = Brep.CreatePlanarBreps(c.ToNurbsCurve())[0];
geometryList.Add(b);
/// 镜像
Brep bn = b;
bn.Transform(Transform.Mirror(Plane.WorldXY));
geometryList.Add(bn);
```
但实际上，只能构建出两个一样的圆面，也就意味着，第一个被添加进 geometryList 的圆面 b，依旧会被其后的 b.Transform() 所改变

（2）根据列表中的现有几何体构建他们以 XY 平面为对称轴的镜像，同时保留原本的几何体

```csharp
// wrong method 1
List<GeometryBase> gbln = gbl;
for (int i = 0; i < gbln.Count; i++)
{
	gbln[i].Transform(Transform.Mirror(Plane.WorldXY));
	gbl.Add(gbln[i])
}


// wrong method 2
List<GeometryBase> gbln = new List<GeometryBase>(gbln.ToArray());
for (int i = 0; i < gbln.Count; i++)
{
	gbln[i].Transform(Transform.Mirror(Plane.WorldXY));
	gbl.Add(gbln[i])
}


// wrong method 3
int length = gbl.Count;
for (int i = 0; i < length; i++)
{
	gbl.Add(gbln[i])
	gbl[gbl.Count - 1].Transform(Transform.Mirror(Plane.WorldXY));
}
```
哈哈哈哈，看到这里你是不是会觉得作者好傻，的确！！！因为是了这么多错误的方法，其实都没有办法更正最本质的错误，即**对象本身就是引用类型的**（和 point, line 等有很大的不同）
## Solvement
通过查阅文档，作者发现了 GeometryBase 类有一个叫 Duplicate() 的方法，介绍中写着 "Construct a deep copy"
![在这里插入图片描述](https://img-blog.csdnimg.cn/20200829113254797.png#pic_center)
一试就成，于是问题解决了（惭愧）
其他很多类似的引用类型都有类似名称与功能的方法

# 5.3
#### 使用 C# 调用 Grasshopper 内的组件
## Backgroud
在用 C# 编写 GH 的 plug-in 时，通常需要借助一些外部组件以方便快捷地实现某种功能（吐槽一下，GH 的 C# 库中对于几何体的相关操作实在是少得可怜）
## Solvement
先上代码
```csharp
Point3d p1 = new Point3d(0, 0, 0);
Point3d p2 = new Point3d(0, 2, 0);
Point3d p3 = new Point3d(2, 1, 0);

var func_info1 = Rhino.NodeInCode.Components.FindComponent("Rectangle3Pt");
var func = func_info1.Delegate as dynamic;
var rectangle = func(p1, p2, p3)[0];

A = rectangle;
```
该代码的实现的功能：
（1）创建三个点 `p1, p2, p3`
（2）找到 GH 中名为 "Rectangle3Pt" 的组件，并将其赋值给 `func`
（3）将这些点作为 function 的输入
（4）读取输出列表中中的第一个值，并将其赋值给 `rectangle`

其中 "Rectangle3Pt" 组件的功能是根据输入的三个点，创建一个矩形线框。以下两图说明含有上述代码 C# 组件能够实现与之相同的功能

![在这里插入图片描述](https://img-blog.csdnimg.cn/20200904191953562.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L3dlaXhpbl80MzcyODEzOA==,size_16,color_FFFFFF,t_70#pic_center)
![在这里插入图片描述](https://img-blog.csdnimg.cn/20200904192334523.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L3dlaXhpbl80MzcyODEzOA==,size_16,color_FFFFFF,t_70#pic_center)
【注意事项】
代码 `Rhino.NodeInCode.Components.FindComponent("XXX")` 中的 XXX 必须是目标组件的全称（空格忽略），否则就会找不到

例如对于下图组件，`XXX = ControlPointLoft` 

![在这里插入图片描述](https://img-blog.csdnimg.cn/20200904193645317.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L3dlaXhpbl80MzcyODEzOA==,size_16,color_FFFFFF,t_70#pic_center)


