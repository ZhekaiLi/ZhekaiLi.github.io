---
layout: wiki
title: Python-matplotlib
categories: Programming Language
description: 
keywords: [Python]
---

## 1 matplotlib.pyplot
### 1.1 Scatter
```py
plt.scatter(x=X[:, 0], y=X[:, 1], 
    s=10, 
    alpha=0.5
)
```
参数
1. `s` size，即点的大小
2. `alpha` 透明度，取值区间为 $[0,1]$
