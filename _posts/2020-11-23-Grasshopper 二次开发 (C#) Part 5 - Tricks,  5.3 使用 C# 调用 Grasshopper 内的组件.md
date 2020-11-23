---
layout: post
title: Grasshopper 二次开发 (C#) Part 5 - Tricks, 5.3 使用 C# 调用 Grasshopper 内的组件
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

# Backgroud
在用 C# 编写 GH 的 plug-in 时，通常需要借助一些外部组件以方便快捷地实现某种功能（吐槽一下，GH 的 C# 库中对于几何体的相关操作实在是少得可怜）
# Solvement
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


