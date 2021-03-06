﻿---
layout: post
title: Grasshopper-Development C# Part 6 - Errors
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

# 6.1
#### , 6.1 Grasshopper breakpoint. The supplied data could not be converted
## 1 Error
Grasshopper breakpoint: The supplied data could not be converted，如图
![在这里插入图片描述](https://img-blog.csdnimg.cn/20200828235041634.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L3dlaXhpbl80MzcyODEzOA==,size_16,color_FFFFFF,t_70#pic_center)
## 2 Solvement
这种报错产生的原因在于，输入或输出数据的声明类型与实际类型不匹配，如下
```csharp
DA.SetData("Geometry", gb);
```
若 gb 的数据类型为 List，那么该行语句将会报错，改为
```csharp
DA.SetDataList("Geometry", gb);
```
后便可正常运行

# 6.2
#### 缺少编译器要求的成员“Microsoft.CSharp.RuntimeBinder.CSharpArgumentInfo.Creat”
## 1 Error
```csharp
var func_info1 = Rhino.NodeInCode.Components.FindComponent("Rectangle3Pt");
var func1 = func_info1.Delegate as dynamic;
var result1 = func1(leftDown, leftUp, rightMid);
```
这是一段可能报错的代码，其功能主要是引用 Grasshopper 中 "Rectangle3Pt" 电池的功能
可能的报错会出现在第三行的 `func1()`，报错提示：

```csharp
缺少编译器要求的成员“Microsoft.CSharp.RuntimeBinder.CSharpArgumentInfo.Creat”
```
如图

![在这里插入图片描述](https://img-blog.csdnimg.cn/20200830104729749.png)
## 2 Solvement
在代码文件开头声明 `using Microsoft.CSharp;`
如果没有安装过，点击 引用 - 管理 NuGet 程序包，在打开的截面中搜索 Microsoft.CSharp，然后下载安装即可
![在这里插入图片描述](https://img-blog.csdnimg.cn/20200830104920559.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L3dlaXhpbl80MzcyODEzOA==,size_16,color_FFFFFF,t_70)

# 6.3
#### Component ID conflict
## 1 Error
![在这里插入图片描述](https://img-blog.csdnimg.cn/20201115140704424.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L3dlaXhpbl80MzcyODEzOA==,size_16,color_FFFFFF,t_70#pic_center)
## Solvement
这样类似的有关 Component ID 报错，基本都是因为 `.cs` 文件中 `ComponentGuid` 函数设置错误所导致的

例如在自定义新的电池模块时，往往会直接复制一个之前写过的电池作为模板。此时如果没有更换新的 ID (如下图黄框)，或更改格式错误，就会出现报错
![在这里插入图片描述](https://img-blog.csdnimg.cn/20201115141241545.png#pic_center)
只要重新更换一个 Guid 即可



