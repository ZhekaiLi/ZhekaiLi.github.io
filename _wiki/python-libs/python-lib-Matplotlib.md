---
layout: wiki
title: Matplotlib
cate1: Python
cate2: -libs
description: 
keywords: Python
---


## Key Points
<span style="background-color: yellow; color: black;">为方便之后的操作，更建议使用以下代码作为绘图代码的首行</span>
（不要使用 `plt.figure()`）
```py
import matplotlib.pyplot as plt
fig, ax = plt.subplots(figsize=(10, 7))
```
- `fig`: 画布
- `ax`: 绘制对象（重点）


## 1. 常用功能
### 1.1 图类型
#### 散点图 Scatter
```py
ax.scatter(x=X[:, 0], y=X[:, 1], 
    color='red',
    s=10,  # size，即点的大小
    alpha=0.5  # 透明度, 取值区间为 [0, 1]
)
```

#### 折线图
```py
ax.plot([x1, x2], [y1, y2], 
    '样式',
    linewidth=5,
    label='Name'
)
```
- `样式=点形+线形+颜色`，例如 `o-r` 表示红色圆点实线
- 分开表示样式：`linestyle` `marker` `color`

#### 柱状图 + histogram
```py
ax.bar(X, Y)
```

柱状统计图（统计数据的分布）
- `bins`: 柱子的个数，默认为10，数量越多画出来的图越精细
```py
plt.hist(X, bins=100)
```


### 1.2 插入文字

```py
ax.text(x, y, "content", fontsize=10)
```
示例: 在图中显示各点的坐标
```py
for i_x, i_y in zip(X, Y):
    ax.text(i_x, i_y, '({:.2f}, {:.2f})'.format(i_x, i_y))
```

### 1.3 标题 & 图例
```py
ax.set_title("chart name")
```

```py
ax.plot(..., label="line1")
ax.plot(..., label="line2")
ax.legend()
```

### 1.4 坐标轴
```py
# 设置坐标轴名
ax.set_xlabel('X')
ax.set_ylabel('Y')
```

**(1) 设置坐标轴范围**
```py
ax.set_xlim(_min, _max)
```

当然也可以只设定最大/ 最小值，例如：
```py
ax.set_ylim(ymin=0)
```

**(2) 取消刻度(标签)显示**
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

方法1: 绘制两行三列共六个子图

```py
fig, ax = plt.subplots(2, 3, figsize=(10, 7))
ax[0][0].plot(...)
ax[0][1].scatter(...)
...
```

方法2: 绘制大小不同的子图（效果如下）
<img src="/images/2023-05/Snipaste_2023-06-09_13-50-58.png" width="80%">

```py
f = plt.Figure(figsize=(10, 7))
a1 = f.add_subplot(121) # 把整个画布分成一行二列，当前画在第一个位置（第一行第一列）
a2 = f.add_subplot(222) # 把整个画布分成二行二列，当前画在第二个位置（第一行第二列）
a3 = f.add_subplot(224) # 把整个画布分成二行二列，当前画在第四个位置（第二行第二列）
```


### 1.8 设置右侧 y 轴
```py
fig, axl = plt.subplots(figsize=(10, 7))
axr = axl.twinx()

axl.bar(...)
axr.plot(...)
```

<img src="/images/2022-08/Snipaste_2022-09-03_22-14-59.png" width="70%">


### 1.9 输出图片
```py
fig, ax = plt.subplots(figsize=())
fig.savefig('pic1.png')
```
可选参数
- `bbox_inches='tight'`: 缩小输出的图片中可能存在的大面积白色外框

## 2. 几何图
### 2.1 画方块
```py
from matplotlib import patches

fig, ax = plt.subplots(figsize=(7, 7))
# 设置坐标轴范围，否则可能因为太小而无法显示画的图
ax.set_xlim(0, 10)
ax.set_ylim(0, 10)

ax.add_patch(
    patches.Rectangle(
        (x, y), # location
        w,      # width
        h,      # height
        color='grey'
    )
)
```




Sampling?

