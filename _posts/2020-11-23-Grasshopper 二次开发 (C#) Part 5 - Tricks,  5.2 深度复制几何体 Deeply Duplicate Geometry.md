---
layout: post
title: Grasshopper 二次开发 (C#) Part 5 - Tricks, 5.2 深度复制几何体 Deeply Duplicate Geometry
categories: Grasshopper Development
description: Personal Notes
keywords: Grasshopper Development, Grasshopper, C#
---

本博客内容正在持续更新，最后一次更新时间：2020.09.04
**【说明】
1.本专栏的 Part 5 主要介绍作者在学习和实践中所遇到的一些问题的解决方案，如有差错或更优解，欢迎指正
2.您如果碰到有关 GH 二开的任何问题，欢迎在本专栏的任意一篇博文下留言交流**

**【本文重点】**
1.查文档：(1) [RhinoCommon SDK](https://developer.rhino3d.com/5/api/RhinoCommon/html/N_Rhino.htm#!) (2) [Grasshopper API](https://developer.rhino3d.com/api/grasshopper/html/T_Grasshopper_DataTree_1.htm#!)
2.专栏地址：[专栏：Rhino (Grasshopper) 二次开发 (C#)](https://blog.csdn.net/weixin_43728138/category_10266504.html)

**【推荐阅读】**
1.有关 Grasshopper 部分知识点和操作欢迎参考 [Grasshopper 学习笔记](https://blog.csdn.net/weixin_43728138/article/details/107815978)
2.视频教程：本文部分内容来自油管教程 [C# Scripting and Plugin Development for Grasshopper](https://www.youtube.com/watch?v=urWRRpy1fCw&t=5224s)

# Problem
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
# Solvement
通过查阅文档，作者发现了 GeometryBase 类有一个叫 Duplicate() 的方法，介绍中写着 "Construct a deep copy"
![在这里插入图片描述](https://img-blog.csdnimg.cn/20200829113254797.png#pic_center)
一试就成，于是问题解决了（惭愧）
其他很多类似的引用类型都有类似名称与功能的方法

