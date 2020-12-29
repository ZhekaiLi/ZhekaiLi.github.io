---
layout: post
title: Clustering Algorithm - Introduction
categories: Machine-Learning
description: Personal Notes
keywords: [Machine-Learning, Python]
---

**Reference**
1.[万门大学: 实用数据挖掘与人工智能一月特训班，第26讲: 聚类与代码实战](https://www.wanmen.org/courses/59df20a60dcf357a8bc0000c/lectures/5aab7757f1f2ef4816e8634f)
2.[scikit-learn clustering](https://scikit-learn.org/stable/modules/clustering.html)


- **Partitioning based clustering:** K-means, Mean shift
- **Hierarchical clustering:** Agglomerative clustering, BIRCH
- **Density based clustering:** DBSCAN
- **Model based clustering:** GMM

## 1 Basic components
### 1.1 Cluster
The cluster is defined to 
1. maximize the similarity inside the cluster
2. minimize the similarity between clusters

### 1.2 Distance
1. **Minkowski Distance:**
$$dist_{mk}=(\sum_{i=1}^n\vert x_i-y_i\vert^p)^{\frac{1}{p}}$$
2. **Euclidean Distance:** $dist_{mk}$ with $t=2$
$$dist_{mk}=\sqrt{\sum_{i=1}^n\vert x_i-y_i\vert^2}$$




## 2.3 DBSCAN




