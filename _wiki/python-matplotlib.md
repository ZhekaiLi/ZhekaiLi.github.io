---
layout: wiki
title: Python-matplotlib
categories: Programming Language
description: 
keywords: [Python]
---

## 1 matplotlib.pyplot
### 1.1 plt.scatter
```py
plt.scatter(x=X[:, 0], y=X[:, 1], 
    s=10, # size，即点的大小
    alpha=0.5 # 透明度, 取值区间为 [0, 1]
)
```

### 1.2 plt.text
在图像中插入文字
```py
plt.text(x, y, "content")
```
示例: 在图中显示各点的坐标
```py
for i_x, i_y in zip(X, Y):
    plt.text(i_x, i_y, '({:.2f}, {:.2f})'.format(i_x, i_y))
```

### 1.3 plt.figure
```py
plt.figure(figsize=(l, w) # 调整图像大小
)
```
