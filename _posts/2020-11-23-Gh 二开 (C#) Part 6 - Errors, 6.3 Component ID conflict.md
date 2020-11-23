---
layout: post
title: Gh 二开 (C#) Part 6 - Errors, 6.3 Component ID conflict
categories: Grasshopper Development
description: Personal Notes
keywords: Grasshopper Development, Grasshopper, C#
---

**【说明】
1.本专栏的 Part 6 主要介绍作者在学习和实践中所遇到的一些程序运行问题的解决方案，如有差错或更优解，欢迎指正
2.您如果碰到有关 GH 二开的任何问题，欢迎在本专栏的任意一篇博文下留言交流**

**【本文重点】
1.查文档：(1) [RhinoCommon SDK](https://developer.rhino3d.com/5/api/RhinoCommon/html/N_Rhino.htm#!) (2) [Grasshopper API](https://developer.rhino3d.com/api/grasshopper/html/T_Grasshopper_DataTree_1.htm#!)
2.专栏地址：[专栏：Rhino (Grasshopper) 二次开发 (C#)](https://blog.csdn.net/weixin_43728138/category_10266504.html)**

# 1 Error
![在这里插入图片描述](https://img-blog.csdnimg.cn/20201115140704424.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L3dlaXhpbl80MzcyODEzOA==,size_16,color_FFFFFF,t_70#pic_center)
# Solvement
这样类似的有关 Component ID 报错，基本都是因为 `.cs` 文件中 `ComponentGuid` 函数设置错误所导致的

例如在自定义新的电池模块时，往往会直接复制一个之前写过的电池作为模板。此时如果没有更换新的 ID (如下图黄框)，或更改格式错误，就会出现报错
![在这里插入图片描述](https://img-blog.csdnimg.cn/20201115141241545.png#pic_center)
只要重新更换一个 Guid 即可


