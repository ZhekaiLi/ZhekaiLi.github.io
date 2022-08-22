---
layout: post
title: Clustering Algorithm:Kmeans, BIRCH, DBSCAN
categories: Machine-Learning
description: Personal Notes
keywords: Machine-Learning, Python, Clustering
mathjax: true
topmost: true
---

*Reference*
[scikit-learn clustering](https://scikit-learn.org/stable/modules/clustering.html)

Family of clustering:
- **Partitioning based clustering:** K-means, Mean shift
- **Hierarchical clustering:** Agglomerative clustering, BIRCH
- **Density based clustering:** DBSCAN
- **Model based clustering:** GMM

# 1. Basic components
## 1.1 Cluster
The cluster is defined to 
1. maximize the similarity inside the cluster
2. minimize the similarity between clusters

## 1.2 Distance
1. **Minkowski Distance:**
$$dist_{mk}=(\sum_{i=1}^n\vert x_i-y_i\vert^p)^{\frac{1}{p}}$$
2. **Euclidean Distance:** $dist_{mk}$ with $t=2$
$$dist_{mk}=\sqrt{\sum_{i=1}^n\vert x_i-y_i\vert^2}$$

# 2. K-means

K-means, 即 k-均值聚类算法, 属于非监督学习

## 2.1 Object 
Given number $k$ and data $D=\lbrace x_1,...,x_m\rbrace$, divide the data into $k$ different clusters $C=\lbrace C_1,...,C_k\rbrace$ with the **least square error (LSE)**
$$LSE=\sum_{i=1}^k\sum_{x\in C_i}\|x-u_i\|^2$$

where $u_i$ is the centroid of cluster $C_i$
## 2.2 Procedure (pseudocode)
以下是伪代码
```py
# Randomly select k number of data as the initial cluster centroids
centroids = [random select] 

LSE = float('inf')
LSE_last = 0

# When LSE do not change, it reaches minimun
while LSE_last != LSE:
    LSE_last = LSE

    # 1. Calculate an k*m distance matrix DIST.
    # where DIST_ij means the distance between centroid u_i and data point x_j
    # 2. Renew centroids with centroids of new clusters
    centroids, LSE, clusters = Renew()
```

## 2.3 Code
### 2.3.1 Use basic python
```py
import numpy as np
import matplotlib.pyplot as plt
from sklearn import datasets
```
**Generate data**
```py
n_samples = 1500
centers = [[0, 0], [5, 0], [0, 5]]
random_state = 6
X, y = datasets.make_blobs(n_samples=n_samples, centers=centers, cluster_std=0.6, random_state=random_state)
```
**Functions**
```py
def Compute_distance(centroids, X):    
    cx = centroids[:, 0]
    cy = centroids[:, 1]
    Xx = X[:, 0]
    Xy = X[:, 1]
    
    dx = cx.reshape(-1, 1) - Xx.reshape(1, -1)
    dy = cy.reshape(-1, 1) - Xy.reshape(1, -1)    
    return np.sqrt(dx**2 + dy**2)

def Renew(DIST, X):
    """Renew centroids, LSE and return clusters"""
    clusters = np.argmin(DIST, 0)
    k = DIST.shape[0]
    
    centroids = []
    error = 0
    for i in range(k):
        label = np.array(np.where(clusters == i))
        data = X[label.reshape(-1, 1), :].reshape(-1, 2)
        
        centroid = np.mean(data, 0)
        centroids.append(centroid)
        
        delta = data - centroid
        error = error + np.sum(delta[:, 0]**2) + np.sum(delta[:, 1]**2)       
    return centroids, error, clusters
```
**Main**
The main code I write is just very similar to the **pseudocode in Part 2.1.2**
```py
k = 3
centroids = X[np.random.randint(n_samples, size=k)]

LSE = float('inf')
LSE_last = 0

while LSE_last != LSE:
    LSE_last = LSE
    
    DIST = Compute_distance(centroids, X)
    
    centroids, LSE, clusters = Renew(DIST, X)
    centroids = np.array(centroids)

colors = np.array(['#377eb8', '#ff7f00', '#4daf4a', '#a65628'])
plt.scatter(X[:, 0], X[:, 1], color = colors[clusters]
```
![pic1](/images/2020/Snipaste_2020-11-27_20-28-31.jpg)

### 2.3.2 Use KMeans in sklearn
```py
import numpy as np
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans
```
```py
k = 3
random_state = 6
y_pred = KMeans(n_clusters=k, random_state=random_state).fit_predict(X)

colors = np.array(['#377eb8', '#ff7f00', '#4daf4a', '#a65628'])
plt.scatter(X[:, 0], X[:, 1], color = colors[clusters])
```
### 2.3.3 Compare
The running time of my code is **at most half** of that of KMeans in sklearn. There is still much space to improve since I still use `for` loop and did not use Broadcast very well.

## 2.4 Cons and pros
### Pros
1. Easy and direct.
2. Running time is short when $k$ is not too large.

### Cons
1. Need the number of clusters $k$ first.
2. Sensitive to the initial centroids. For example, the unsuitable initial centroids make the result looked awful. The algorithm **Kmeans++** introduced next could help to avoid that.

![pic2](/images/2020/Snipaste_2020-11-27_21-28-31.jpg)

3. Suitable for only circle like distribution, and therefore does not work well on other distribution shapes. For example,

4. Sensitive to noise. (Could use the **median but not mean** to generate centroids)


# 3. BIRCH

BIRCH, Balanced Iterative Reducing and Clustering Using Hierarchies, 简言之就是使用一种特殊的树结构, 聚类特征树 CF-tree (Clustering Feature Tree), 以实现快速聚类.

## 3.1 Backgrouds
> #### CF 聚类特征
> Define $CF$ as 
$$CF_i=(N_i,LS_i,SS_i)$$
>
> where,
$i$: 第 $i$ 个簇 <br> $N_i$: 第 $i$ 个簇所包含的样本个数 <br> $LS_i$: Linear Sum. 第 $i$ 个簇中所有样本点的线性和 <br> $SS_i$: Squre Sum. 第 $i$ 个簇中所有样本点的平方和

例如, 若簇 $i$ 包含 $(1,2),(2,4)$ 这两个样本点, 则有 <br> $N_i=2$ <br> $LS_i=(1,2)+(2,4)=(3,6)$ <br> $SS_i=(1^2,2^2)+(2^2,4^2)=(5,20)$

**Theorem:** $CF$ 具有**良好的可加性**. 令两个不相交簇 $i,j$ 的聚类特征分别为 $CF_i,CF_j$, 则由簇 $i,j$ 合并而成的大簇的聚类特征为 $CF_i+CF_j$

> #### CF-tree 聚类特征树


# 4. DBSCAN

DBSCAN, Density-based spatial clustering of applications with noise, 是一种基于密度的聚类方法


$$
\begin{aligned}
&\text{Input: Data Set }D=(x_1,x_2,...,x_m), \text{Neighborhood Parameter }(\epsilon, minPts) \\
&\text{1. Initialize the core objects sets: } \Omega=\text{\O} \\
&\text{2. For }j=1,2,...,m,\text{ find all core objects and add them to }\Omega \\
&\text{3. Initialize the number of clusters: }k=0 \\
&\text{4. Initialize the set of unaccessed samples: }\Gamma=D \\
&\text{5. while }\Omega\neq\text{\O}\text{ do}\\
&\qquad\text{Record the recent unaccessed samples set: }\Gamma_{old}=\Gamma\\
&\qquad\text{Select a core object }o\in\Omega,\text{ initialize a queue }Q=<o> \\
&\qquad\text{while }Q\neq\text{\O}\text{ do}\\
&\;\;\;\qquad\text{Pop out the first sample }q\text{ from }Q\\
&\;\;\;\qquad\text{if }q\in\Omega\text{ then}\\
&\;\;\;\;\;\;\qquad\text{Define }\Delta=\Gamma\bigcap\text{Neighbors of }q\\
&\;\;\;\;\;\;\qquad\text{Add }\Delta\text{ into }Q\\
&\;\;\;\;\;\;\qquad\text{}\Gamma=\Gamma-\Delta\\
&\;\;\;\qquad\text{end if}\\
&\qquad\text{end while}\\
&\qquad\text{}k=k+1,\text{ generate the cluster }C_k=\Gamma_{old}-\Gamma\\
&\qquad\text{}\Omega=\Omega-C_k\\
&\;\;\;\;\text{end while}\\
&\text{Output: Cluster Division }C
\end{aligned}
$$



