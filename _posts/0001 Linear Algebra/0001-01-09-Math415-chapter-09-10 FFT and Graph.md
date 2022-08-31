---
layout: post
title: Math415 Chapter 09-10 FFT and Graph
categories: Linear-Algebra
description: Personal Notes
keywords: Math415，Linear-Algebra，Matrix
mathjax: true
---

## 9.3 The Fast Fourier Transform (FFT)
For the equation $z^n=1$, the solutions $z$ are the "$n$th roots of unity", which are evenly spaced points around the unit circle in the complex plane. For example, when $n=8,z^8=1$
![pic](/images/2020-12/Snipaste_2020-12-10_10-29-46.jpg)

> #### Def 1: Fourier matrix
> Fourier matrix with $n=4,w=e^{2\pi i/4}=i$
$$F=\begin{bmatrix}
1 & 1 & 1 & 1 \\
1 & w & w^2 & w^3 \\
1 & w^2 & w^4 & w^6 \\
1 & w^3 & w^6 & w^9 \\
\end{bmatrix}=\begin{bmatrix}
1 & 1 & 1 & 1 \\
1 & i & i^2 & i^3 \\
1 & i^2 & i^4 & i^6 \\
1 & i^3 & i^6 & i^9 \\
\end{bmatrix}$$

**Fact 1:** $\frac{1}{\sqrt n}F$ is a **unitary matrix**, since
$$(\frac{1}{\sqrt n}F^H)(\frac{1}{\sqrt n}F)=I$$

**Fact 2:** From $F^HF=nI$, we have
$$F^{-1}=\frac{1}{n}F^H=\frac{1}{n}\overline F$$

> #### Def 2: Fourier series
> Fourier series with $n=4$, we have
$$y_j=\sum_{k=0}^3 c_ke^{ikx}, x=2\pi j/4$$
>
> $$\begin{bmatrix}
y_0 \\
y_1 \\
y_2 \\
y_3 \\
\end{bmatrix}=Fc=\begin{bmatrix}
1 & 1 & 1 & 1 \\
1 & w & w^2 & w^3 \\
1 & w^2 & w^4 & w^6 \\
1 & w^3 & w^6 & w^9 \\
\end{bmatrix}\begin{bmatrix}
c_0 \\
c_1 \\
c_2 \\
c_3 \\
\end{bmatrix}$$

## 10.1 Graphs and Networks
### 10.1.1 The Incidence Matrix

The incidence matrix of a graph，即图的**关联矩阵**，能够表示图中节点之间是如何连接的

对于一个 $m\times n$ 的关联矩阵 $A$
1. $n$ 列表示有 $n$ 个节点
2. $m$ 行表示有 $m$ 条连接线
3. $\text{rank}(A)=n-1$
$$a_{ij}=\begin{cases}
   -1 &\text{then 节点 j 为连接线 i 的起点}\\
   0 &\text{then 节点 j 与连接线 i 无关}\\
   1 &\text{then 节点 j 为连接线 i 的终点}\\
\end{cases}$$

例如
![pic1](/images/2020/202010231651.JPG)

**$m,n$ 之间的关系**
1. $m_{max}=\frac{1}{2}n(n-1)$
2. $m_{min}=n-1$

**Elimination reduce any graph to a tree**

Rows are dependent when edges form a loop. Independent 
rows come from trees.