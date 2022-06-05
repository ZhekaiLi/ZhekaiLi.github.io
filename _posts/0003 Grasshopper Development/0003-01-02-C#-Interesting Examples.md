---
layout: post
title: Grasshopper Development-C#-02 Interesting Examples
categories: Grasshopper-Development
description: Personal Notes
keywords: Grasshopper-Development, Grasshopper, C#
---

**【本文重点】**
1. 查文档：(1) [RhinoCommon SDK](https://developer.rhino3d.com/5/api/RhinoCommon/html/N_Rhino.htm#!) (2) [Grasshopper API](https://developer.rhino3d.com/api/grasshopper/html/T_Grasshopper_DataTree_1.htm#!)
2. 专栏地址：[专栏：Rhino (Grasshopper) 二次开发 (C#)](https://blog.csdn.net/weixin_43728138/category_10266504.html)

**【参考资料】**
1. Youtube: [C# Scripting and Plugin Development for Grasshopper](https://www.youtube.com/watch?v=urWRRpy1fCw&t=5224s)

# 1 画一条随机游动的小蛇
效果如图
<img src="https://img-blog.csdnimg.cn/2020080523253616.gif" width="30%" alt="">
### 1.1 涉及内容
1. Random 语句：见 [C# 学习笔记](https://blog.csdn.net/weixin_43728138/article/details/107802603) Section 1.4
2. toggle & timer 模块：见 [Rhino (Grasshopper) 二次开发 (C#) Part 1](https://editor.csdn.net/md/?articleId=107799933) Section 1.1.2 & 1.1.3
### 1.2 具体电池组与代码
<img src="https://img-blog.csdnimg.cn/20200805233409682.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L3dlaXhpbl80MzcyODEzOA==,size_16,color_FFFFFF,t_70" width="30%" alt="">

```csharp
private void RunScript(bool ifRenew, ref object A, ref object B) {
    if (ifRenew) { // 初始化点和线
        p = new Point3d(0, 0, 0);
        ps = new List<Point3d>();
        ls = new List<LineCurve>();

        for (int i = 0; i < 10; i++) {
	        ps.Add(p);
	        ls.Add(new LineCurve(p, p));
        }
    }
    else {
        double x = randomGenerator.NextDouble() - 0.5;
        double y = randomGenerator.NextDouble() - 0.5;

        ls.Add(new LineCurve(p, p += new Vector3d(x, y, 0)));
        ps.Add(p);
        ls.RemoveAt(0);
        ps.RemoveAt(0);
    }
    A = ps;
    B = ls;
}

Point3d p = new Point3d(0, 0, 0);
Random randomGenerator = new Random();
List<Point3d> ps = new List<Point3d>();
List<LineCurve> ls = new List<LineCurve> ();
```
# 2
需要下载的 dll
[百度云下载链接：提取码 0523](https://pan.baidu.com/s/1pV82u7zJIMiL521pNVGqGA) ，将压缩包内的所有文件移动至 `C:\Users\Administrator\AppData\Roaming\Grasshopper\Libraries` 
![在这里插入图片描述](https://img-blog.csdnimg.cn/20200809150241412.png)


