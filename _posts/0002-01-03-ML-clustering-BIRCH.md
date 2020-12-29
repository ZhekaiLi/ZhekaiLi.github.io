---
layout: post
title: Clustering Algorithm 02 - BIRCH
categories: Machine-Learning
description: Personal Notes
keywords: [Machine-Learning, Python]
---

# BIRCH

BIRCH, Balanced Iterative Reducing and Clustering Using Hierarchies, 简言之就是使用一种特殊的树结构, 聚类特征树 CF-tree (Clustering Feature Tree), 以实现快速聚类.

## 1 Backgrouds
> #### CF 聚类特征
> Define $CF$ as 
$$CF_i=(N_i,LS_i,SS_i)$$
>
> where,
$i$: 第 $i$ 个簇 <br> $N_i$: 第 $i$ 个簇所包含的样本个数 <br> $LS_i$: Linear Sum. 第 $i$ 个簇中所有样本点的线性和 <br> $SS_i$: Squre Sum. 第 $i$ 个簇中所有样本点的平方和

例如, 若簇 $i$ 包含 $(1,2),(2,4)$ 这两个样本点, 则有 <br> $N_i=2$ <br> $LS_i=(1,2)+(2,4)=(3,6)$ <br> $SS_i=(1^2,2^2)+(2^2,4^2)=(5,20)$

**Theorem:** $CF$ 具有**良好的可加性**. 令两个不相交簇 $i,j$ 的聚类特征分别为 $CF_i,CF_j$, 则由簇 $i,j$ 合并而成的大簇的聚类特征为 $CF_i+CF_j$

> #### CF-tree 聚类特征树