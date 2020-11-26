---
layout: post
title: Cluster Algorithm
categories: Machine-Learning
description: Personal Notes
keywords: [Machine-Learning, Python]
---

【参考资料】
1.[万门大学: 实用数据挖掘与人工智能一月特训班，第26讲: 聚类与代码实战](https://www.wanmen.org/courses/59df20a60dcf357a8bc0000c/lectures/5aab7757f1f2ef4816e8634f)



# 1 Introduction
- **Partitioning based clustering:** K-means, Mean shift
- **Hierarchical clustering:** Agglomerative clustering, BIRCH
- **Density based clustering:** DBSCAN
- **Model based clustering:** GMM

## 1.1 Basic components
### 1.1.1 Cluster
The cluster is defined to 
1. maximize the similarity inside the cluster
2. minimize the similarity between clusters

### 1.1.2 Distance
1. **Minkowski Distance:**
$$dist_{mk}=(\sum_{i=1}^n\vert x_i-y_i\vert^p)^{\frac{1}{p}}$$
2. **Euclidean Distance:** $dist_{mk}$ with $t=2$
$$dist_{mk}=\sqrt{\sum_{i=1}^n\vert x_i-y_i\vert^2}$$

# 2 Partition Based Clustering
> ## Alogrithm 1 K-means
> ### 1.1 Object 
> Given number $k$ and data $D=\lbrace x_1,...,x_m\rbrace$, divide the data into $k$ different clusters $C=\lbrace C_1,...,C_k\rbrace$ with the **least square error (LSE)**
$$LSE=\sum_{i=1}^k\sum_{x\in C_i}\|x-u_i\|^2$$
>
> where $u_i$ is the centroid of cluster $C_i$
### 1.2 Procedure (pseudocode)
```py
# Randomly select k number of data as the initial cluster centroids
centroids = [random select] 

LSE = float('inf');
LSE_last = 0;

# When LSE do not change, it reaches minimun
while(LSE_last == LSE):
    LSE_last = LSE

    # Calculate an k*m distance matrix DIST.
    # where DIST_ij means the distance between centroid u_i and data point x_j
    DSIT = [calculate distance]

    # Renew centroids with centroids of new clusters
    centroids = centroids.renew()
    LSE = LSE.renew()
```

### 1.3 Code
#### 1.3.1 Use basic python
```py

```


