---
layout: post
title: Clustering Algorithm 01 - K-means
categories: Machine-Learning
description: Personal Notes
keywords: [Machine-Learning, Python]
---

# K-means

K-means, 即 k-均值聚类算法, 属于非监督学习

## 1 Object 
Given number $k$ and data $D=\lbrace x_1,...,x_m\rbrace$, divide the data into $k$ different clusters $C=\lbrace C_1,...,C_k\rbrace$ with the **least square error (LSE)**
$$LSE=\sum_{i=1}^k\sum_{x\in C_i}\|x-u_i\|^2$$

where $u_i$ is the centroid of cluster $C_i$
## 2 Procedure (pseudocode)
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

## 3 Code
### 3.1 Use basic python
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
![pic1](https://github.com/ZhekaiLi/PICTURE-for-markdown/raw/master/Snipaste_2020-11-27_20-28-31.jpg)

### 3.2 Use KMeans in sklearn
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
### 3.3 Compare
The running time of my code is **at most half** of that of KMeans in sklearn. There is still much space to improve since I still use `for` loop and did not use Broadcast very well.

## 4 Cons and pros
### Pros
1. Easy and direct.
2. Running time is short when $k$ is not too large.

### Cons
1. Need the number of clusters $k$ first.
2. Sensitive to the initial centroids. For example,
![pic2](https://github.com/ZhekaiLi/PICTURE-for-markdown/raw/master/Snipaste_2020-11-27_21-28-31.jpg)
**Kmeans++** introduced in **Part 2.1.5** could help to save that.
3. Suitable for only circle like distribution, and therefore does not work well on other distribution shapes. For example,
![pic3]()
4. Sensitive to noise. (Could use the **median but not mean** to generate centroids)