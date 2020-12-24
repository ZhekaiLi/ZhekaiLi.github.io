---
layout: wiki
title: Python-scipy
categories: Programming Language
description: 
keywords: [Python]
---

## 1 scipy.interpolate
光滑拟合离散数据, 生成拟合函数
```py
spl = make_interp_spline(X, Y, 
    k=3 # B-spline degree. Default is cubic, k=3
)
```
对于新的数据点 X_test, 可以直接使用 `spl(X_test)` 来 predict