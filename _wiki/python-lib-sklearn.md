---
layout: wiki
title: sklearn
cate1: Python
cate2: -libs
description: 
keywords: Python
mathjax: true
---

## 1. sklearn.datasets
### 1.1 生成数据
```py
from sklearn import datasets
```
生成团状样本点集
```py
X, y = datasets.make_blobs(n_samples=1000, 
    # 团的个数
    # 默认随机生成分布, 也可以自定义质心
    # 例如 centers=[[1,2], [2,3]] 
    centers=10,
    n_features=2,  # 数据维度
    cluster_std=0.5, 
    random_state=4,
    s=10  # 样本点的大小
)
```
生成内外两个环状分布的样本点集
```py
X, y = datasets.make_circles(n_samples=1000, 
    # 取值 [0, 1), 决定了内外两个环之间的距离
    # 靠近 0 时, 内环在中央聚合成一个团
    # 靠近 1 时, 内环外扩与外环合并
    factor=0.5,
    noise=0.05 # 噪音
)
```



## 2. sklearn.matrics
### 2.1 Value the clustering 检查聚类算法的性能

```py
sklearn.matrics.silhouette_score(X_blobs,  # 原数据
    class_prediction  # 分类标签, 例如以下表示有三类 array([0, 1, 2, 1, 1, 2])
)
```


## sklearn.linear_model

```py
from sklearn.linear_model import LinearRegression

lr = LinearRegression()
lr.fit(X, y)
```

```py
lr.coef_      # 系数
lr.intercept_ # 截距
```