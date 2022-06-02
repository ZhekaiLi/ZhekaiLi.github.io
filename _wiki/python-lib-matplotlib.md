---
layout: wiki
title: matplotlib
cate1: Python
cate2: -libs
description: 
keywords: Python
---


## Key Points
==为方便之后的操作，更建议使用以下代码作为绘图代码的首行==
（不要使用 `plt.figure()`）
```py
import matplotlib.pyplot as plt
fig, ax = plt.subplots(figsize=(10, 7))
```
- `fig`: 画布
- `ax`: 绘制对象（重点）


## 1. 常用功能
### 1.1 图类型
**散点图**
```py
ax.scatter(x=X[:, 0], y=X[:, 1], 
    color='red',
    s=10,  # size，即点的大小
    alpha=0.5  # 透明度, 取值区间为 [0, 1]
)
```
**折线图**
```py
ax.plot([x1, x2], [y1, y2], '样式', label='Name')
```
- `样式=点形+线形+颜色`，例如 `o-r` 表示红色圆点实线
- 分开表示样式：`linestyle` `marker` `color`

### 1.2 插入文字

```py
ax.text(x, y, "content")
```
示例: 在图中显示各点的坐标
```py
for i_x, i_y in zip(X, Y):
    ax.text(i_x, i_y, '({:.2f}, {:.2f})'.format(i_x, i_y))
```

### 1.4 坐标轴

**(1) 设置坐标轴范围**
```py
ax.xlim(_min, _max)
```
当然也可以只设定最大/ 最小值，例如：
```py
ax.xlim(xmin=0)
ax.ylim(ymin=0)
```
**(2) 取消刻度显示**

```py
ax.set_xticks([])
ax.set_yticks([])
```
**(3) 设置刻度字体大小**
```py
ax.tick_params(labelsize=13)
```

### 1.5 生成网格
```py
ax.grid()
```

### 1.6 保存绘图
```py
plt.savefig('figname.jpg')
```

### 1.7 绘制子图
绘制两行三列共六个子图
```py
fig, ax = plt.subplots(2, 3, figsize=(10, 7))
ax[0].plot(...)
ax[1].scatter(...)
...
```

