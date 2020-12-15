---
layout: wiki
title: Python-sklearn
categories: Programming Language
description: 
keywords: [Python]
---

## 1 sklearn.datasets
### 1.1 生成数据
```py
X_blobs, _ = sklearn.datasets.make_blobs(n_samples=1000, 
    centers=10, # 团的个数
    n_features=2, # 数据维度
    cluster_std=0.5, 
    random_state=4
)
```
## 2 sklearn.matrics
### 2.1 Value the clustering 检查聚类算法的性能
```py
sklearn.matrics.silhouette_score(X_blobs, # 原数据
    class_prediction # 分类标签, 例如以下表示有三类 array([0, 1, 2, 1, 1, 2])
)
```