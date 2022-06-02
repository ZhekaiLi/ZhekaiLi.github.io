---
layout: wiki
title: openseespy
cate1: Python
cate2: -libs
description: 
keywords: Python
mathjax: true
---

文档：[OpenSeesPy](https://openseespydoc.readthedocs.io/en/latest/index.html)

```py
import openseespy as ops
```

# 1. Intro
## 1.1 如何正确地输入参数

下图是在官方文档中某函数的输入参数：
<img src="/images/2022-03/Snipaste_2022-03-02_16-10-14.png" width="100%">

该函数可以表示为如下结构：
```py
eleLoad(
    '-ele', *eleTags, 
    '-range', eleTag1, eleTag2, 
    '-type', 
        '-beamUniform', Wy, <Wz>, Wx=0.0,
        '-beamPoint', Py, <Pz>, xL, Px=0.0, 
        '-beamThermal', *tempPts
)
```

可知该函数的输入分为两层：
- 第一层：`'-ele', '-range', 'type'`
- 第二层：`'-beamUniform', '-beamPoint', '-beamThermal'`

以上每一层内的元素之间都是并列的，而第二层的所有元素均属于第一层中的 `'-type'`，因此在输入第二层相关的参数时需要在前面加上 `'-type'`

**具体参数**：
- `*eleTags`：星号表示可以输入多个相关参数
- `<Wz>`：尖括号表示该参数只在某些条件下才需要输入
- `Wx=0.0`：默认赋0值，因此可以不输入

**示例**：
```py
# 在1、3、4、5号杆的中间位置: xL=0.5
# 施加y方向(locally)、大小为-20的力: Py=-20
# 该模型为二维模型，而输入Pz的前提是三维模型，因此不输入
ops.eleLoad(
    '-ele', 1, 
    '-range', 3, 5, 
    '-type', 
        '-beamPoint', -20, 0.5)
```

# 2. 常用函数

铰接 Hinge
```py
# 通过两个重合的节点实现铰接
# 这两个节点需要满足位移一致、转动不一定一致
ops.node(3, 0.2, 0.2)
ops.node(4, 0.2, 0.2)
ops.equalDOF(3,4,1,2) # 关联3、4节点在第一、第二自由度上的运动（x,y轴）
```

节点荷载
```py
ops.load(nodeTag, *loadValues)
ops.load(1, Fx, Fy, M) # 二维节点
```

杆荷载
```py
# Point load
# 杆件的局部坐标系(local axis)：以杆件中轴为x轴，垂直中轴方向为y轴
# Fy: 在局部坐标系上施加一个y方向的力
# xL: 施力位置，范围[0,1]，例如xL=0.5表示在杆件中间施加荷载
ops.eleLoad(
    '-ele', 1,
    '-range', 3, 5,
    'type',
        '-beamPoint', Fy, xL
)

# Uniform distributed load
ops.eleLoad(
    '-ele', 1,
    '-range', 3, 5,
    'type',
        '-beamUniform', Wy
)
```