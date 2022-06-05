---
layout: post
title: Grasshopper Development-C#-04 Write Own Class
categories: Grasshopper-Development
description: Personal Notes
keywords: Grasshopper-Development, Grasshopper, C#
---

**【本文重点】**
1. 查文档：(1) [RhinoCommon SDK](https://developer.rhino3d.com/5/api/RhinoCommon/html/N_Rhino.htm#!) (2) [Grasshopper API](https://developer.rhino3d.com/api/grasshopper/html/T_Grasshopper_DataTree_1.htm#!)
2. 专栏地址：[专栏：Rhino (Grasshopper) 二次开发 (C#)](https://blog.csdn.net/weixin_43728138/category_10266504.html)

**【参考资料】**
1. Youtube: [C# Scripting and Plugin Development for Grasshopper](https://www.youtube.com/watch?v=urWRRpy1fCw&t=5224s)

# 1 Class in C# 组件
使用 Grasshopper 内置的 C# 组件可以就编写一个简单的类（关于该组件的知识点请查看 [Rhino (Grasshopper) 二次开发 (C#) Part 1 - Introductions to the C# Coding in Grasshopper](https://blog.csdn.net/weixin_43728138/article/details/107799933)），如下图
![在这里插入图片描述](https://img-blog.csdnimg.cn/20200808165041952.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L3dlaXhpbl80MzcyODEzOA==,size_16,color_FFFFFF,t_70)
但是这样创建的类有许多缺点，譬如 代码长度可能过长（不能分割成多个文件）、难以调试等，因此我们一般还是在 Visual Studio 中创建
# 2 Class in Plug-in

```csharp
using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;

using Rhino.Geometry;

namespace Workshop
{
    class Pyramid
    {
        public Plane BasePlane;
        public double Length;
        public double Width;
        public double Height;
		
		// 构造函数
        public Pyramid(Plane basePlane, double length, double height, double width)
        {
            BasePlane = basePlane;
            Length = length;
            Width = width;
            Height = height;
        }
		
		// 求角锥体的 8 条棱
        public List<LineCurve> ComputeDisplayLines()
        {
            Point3d A = BasePlane.Origin + BasePlane.XAxis * Length * 0.5 + BasePlane.YAxis * Width * 0.5;
            Point3d B = BasePlane.Origin - BasePlane.XAxis * Length * 0.5 + BasePlane.YAxis * Width * 0.5;
            Point3d C = BasePlane.Origin - BasePlane.XAxis * Length * 0.5 - BasePlane.YAxis * Width * 0.5;
            Point3d D = BasePlane.Origin + BasePlane.XAxis * Length * 0.5 - BasePlane.YAxis * Width * 0.5;
            Point3d M = BasePlane.Origin + BasePlane.ZAxis * Height;

            List<LineCurve> displayLines = new List<LineCurve>();

            displayLines.Add(new LineCurve(A, B));
            displayLines.Add(new LineCurve(B, C));
            displayLines.Add(new LineCurve(C, D));
            displayLines.Add(new LineCurve(D, A));

            displayLines.Add(new LineCurve(A, M));
            displayLines.Add(new LineCurve(B, M));
            displayLines.Add(new LineCurve(C, M));
            displayLines.Add(new LineCurve(D, M));

            return displayLines;
        }
    }
}
```
# 3 Debug in VS2019
### 3.1 设置
双击 Properties - 调试 - 启动外部程序，绑定 Rhino.exe 的路径
![在这里插入图片描述](https://img-blog.csdnimg.cn/20200808213804339.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L3dlaXhpbl80MzcyODEzOA==,size_16,color_FFFFFF,t_70)
# 3.2







