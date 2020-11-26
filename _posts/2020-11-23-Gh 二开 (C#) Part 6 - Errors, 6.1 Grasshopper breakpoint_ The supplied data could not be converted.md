---
layout: post
title: Gh 二开 (C#) Part 6 - Errors, 6.1 Grasshopper breakpoint. The supplied data could not be converted
categories: Grasshopper-Development
description: Personal Notes
keywords: Grasshopper-Development, Grasshopper, C#
---
**ATTENSION - If some LeTeX equations could not show well, pleae try to refresh this page.**

**【说明】**
1. 本专栏的 Part 6 主要介绍作者在学习和实践中所遇到的一些程序运行问题的解决方案，如有差错或更优解，欢迎指正
2. 您如果碰到有关 GH 二开的任何问题，欢迎在本专栏的任意一篇博文下留言交流

**【推荐阅读】**
1. 查文档：(1) [RhinoCommon SDK](https://developer.rhino3d.com/5/api/RhinoCommon/html/N_Rhino.htm#!) (2) [Grasshopper API](https://developer.rhino3d.com/api/grasshopper/html/T_Grasshopper_DataTree_1.htm#!)
2. CSDN专栏地址：[专栏：Rhino (Grasshopper) 二次开发 (C#)](https://blog.csdn.net/weixin_43728138/category_10266504.html)

**【参考资料】**
1. Youtube: [C# Scripting and Plugin Development for Grasshopper](https://www.youtube.com/watch?v=urWRRpy1fCw&t=5224s)

# 1 Error
Grasshopper breakpoint: The supplied data could not be converted，如图
![在这里插入图片描述](https://img-blog.csdnimg.cn/20200828235041634.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L3dlaXhpbl80MzcyODEzOA==,size_16,color_FFFFFF,t_70#pic_center)
# 2 Solvement
这种报错产生的原因在于，输入或输出数据的声明类型与实际类型不匹配，如下
```csharp
DA.SetData("Geometry", gb);
```
若 gb 的数据类型为 List，那么该行语句将会报错，改为
```csharp
DA.SetDataList("Geometry", gb);
```
后便可正常运行
