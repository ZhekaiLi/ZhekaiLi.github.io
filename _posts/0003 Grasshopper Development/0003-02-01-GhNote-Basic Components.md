---
layout: post
title: Grasshopper Development-GhNote-01 Basic Components
categories: Grasshopper-Development
description: Personal Notes
keywords: Grasshopper-Development, Grasshopper, C#
---

# 1. Grasshopper Window
## 1.1 在不同文件之间切换
点击右上角文件名即可查看
<img src="https://img-blog.csdnimg.cn/20200805212310217.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L3dlaXhpbl80MzcyODEzOA==,size_16,color_FFFFFF,t_70" width="80%" alt="">

# 2. Panel Textbox
文本框是一个基础组件，主要用于显示电池的输出以及作为数据的输入。

需要注意的是当作为输入时，panel 的内容默认为 text 类型，但是可以根据电池输入端的要求进行变更。如图，在 panel 内输入字符 3 后，text 电池与 number 电池都没有报错（这两个电池的功能在于检查输入的数据类型）
<img src="https://img-blog.csdnimg.cn/202008071349282.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L3dlaXhpbl80MzcyODEzOA==,size_16,color_FFFFFF,t_70" width="30%" alt="">

此外，输完数字后要通过点击外部区域来确认输入，不能敲回车键。因为敲回车键会使得 Panel 的内容变成 3\n，此时就不能变更为 number 了，敲回车键后的效果如下图
<img src="https://img-blog.csdnimg.cn/20200807135232614.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L3dlaXhpbl80MzcyODEzOA==,size_16,color_FFFFFF,t_70" width="30%" alt="">

# 3. Bettery
## 3.1 将在 Rhino 中创建的 geometry 赋值给电池
以 Curve 为例，具体步骤：
1. 右键单击组件，选择 Set one Curve
2. 返回 Rhino 图形界面选择已经绘制完成的曲线
<img src="https://img-blog.csdnimg.cn/20200805152340882.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L3dlaXhpbl80MzcyODEzOA==,size_16,color_FFFFFF,t_70" width="50%" alt="">
## 3.2 删除电池间的连线
按住 Crtl 键，点击一段连线的尾部（此时会出现一个红色的箭头图标），再把连线从尾部拖回头部即可完成删除
## 3.3 Bake：将 Rhino 与 GH 分离
将 GH 中的虚拟模型导入至 Rhino 中变为实体（即可在 Rhino 中做进一步的建模分析导出扥操作）
以 Point 为例
1. 在 GH 中绘制一个点
<img src="https://img-blog.csdnimg.cn/20200813133220124.png" width="50%" alt="">
2. 右键单击电池，选择 Bake
<img src="https://img-blog.csdnimg.cn/20200813133240666.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L3dlaXhpbl80MzcyODEzOA==,size_16,color_FFFFFF,t_70" width="50%" alt="">
4. 可以看到不管是"取消 Preview", "选择 Enable" 还是 "删除电池"，Rhino 中创建的点都不会消失
<img src="https://img-blog.csdnimg.cn/20200813133337437.png" width="50%" alt="">

##  3.4 Internalise data：将 GH 与 Rhino 分离
将 Rhino 中的模型参数固化于电池（即可在 Rhino 中做的改变将不会影响电池中储存的模型）
以 Point 为例
1. 同 Section 3.1 赋值完成后，右键单击电池，选择 Internalise data
<img src="https://img-blog.csdnimg.cn/20200813133934963.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L3dlaXhpbl80MzcyODEzOA==,size_16,color_FFFFFF,t_70" width="50%" alt="">
2. 可以看到在 Rhino 中点的移动不会影响电池储存的点
<img src="https://img-blog.csdnimg.cn/20200813134340931.png" width="50%" alt="">
## 3.5 Ctrl + Alt + 左键：电池在菜单内的位置



 




