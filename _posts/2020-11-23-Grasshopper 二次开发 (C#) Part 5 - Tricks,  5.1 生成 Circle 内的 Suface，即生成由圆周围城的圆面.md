---
layout: post
title: Grasshopper 二次开发 (C#) Part 5 - Tricks, 5.1 生成 Circle 内的 Suface，即生成由圆周围城的圆面
categories: Grasshopper-Development
description: Personal Notes
keywords: Grasshopper-Development, Grasshopper, C#
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
为了创建一个圆面，作者希望能够通过某种方法，凭借 new Circle(plane, center, radius) 所创建的圆周曲线，直接生成圆面。

这个操作在 GH 的可视化编程中非常容易实现，例如 Boundary Surface & Patch，但在 C# 编程实现的过程中，作者查阅了整个 Surface Class & Circle Class，都没能找到实现方案。

# Solvement
最后通过在 GH 论坛上的搜索，该问题得以较好地解决，[这是论坛帖子的链接](https://www.grasshopper3d.com/forum/topics/circle-curve-to-surface)，具体代码如下

```csharp
Circle circle = new Circle(Plane.WorldXY, new Point3d(0, 0, 0), 1);
Brep brep = Brep.CreatePlanarBreps(circle.ToNurbsCurve())[0];
```
`brep` 即为我们所需要的的圆面

![在这里插入图片描述](https://img-blog.csdnimg.cn/20200816201901185.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L3dlaXhpbl80MzcyODEzOA==,size_16,color_FFFFFF,t_70#pic_center)


