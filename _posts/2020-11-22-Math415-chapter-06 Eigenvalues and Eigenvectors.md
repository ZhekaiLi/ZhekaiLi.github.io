---
layout: post
title: Math415 Chapter-06 Eigenvalues and Eigenvectors
categories: Math415
description: Personal Notes
keywords: [Math415，Calculas，Matrix]
---

## 6.1 Introduction to Eigenvalues

> #### Def 1: Eigenvector, Eigenvalue
> 矩阵 $A$ 的特征向量 $x$ 指的是那些经过线性变换 $Ax$ 之后方向不变，仅发生伸缩或反向变换的向量
$$Ax=\lambda x$$ 
>
> 其中特征向量 $\lambda$ 体现了 $x$ 发生的伸缩、取反变换

**Corollary 1:** 
$$A^nx=\lambda^nx$$

> #### Def 2: Characteristic polynomial
> The characteristic polynomial of $A_{n\times n}$ has degree $n$
> $$\delta_A(\lambda)=\det(A-\lambda I)$$
>
> $\det(A-\lambda I)=0$ is called characteristic equation, it has $n$ roots

> #### Def 3: Trace 矩阵的迹
> $$\text{tr}(A)=\sum_{k=1}^n a_{kk}=\sum_{k=1}^n \lambda_k$$


## 6.2 Diagonalizing a Matrix
> #### Def 1: Diagonalizable matrix 可对角化矩阵
> 判断一个矩阵是否为可对角化矩阵主要有以下几个途径
> 1. $n$ 个线性无关的特征向量
> 2. 代数重数 = 几何重数
> 3. $n$ 个不同的特征值
> 4. 实对称矩阵

