---
layout: post
title: Math415 Week-01
categories: Math415
description: Personal Notes
keywords: Math415，Calculas，Matrix
---
**ATTENSION - If some LeTeX equations could not show well, pleae try to refresh this page.**

# L1
1. 矩阵乘法：需满足列数 = 行数，即 $(a\times b)(b\times c)$
2. 对于单位矩阵 $I_{n\times n}$，以及可逆矩阵 $A_{n\times n}$，满足
$A=IA=AI$
$A^{-1}A=AA^{-1}=I$
3. 点乘 Dot Product
$x,y\in\mathbb{R}^n$
$x\cdot y=x^T y=\sum_{i=1}^n x_i y_i$
$x\cdot y=y\cdot x$
但是对于 $x,y\in \mathbb{C}^n$，点乘的定义不同
4. 范式
$||x||=(\sum_{i=1}^n|x_i|^2)^{1/2}=(x\cdot x)^{1/2}$

# L2
## 2.1 Lines on $\mathbb{R}^2$
$L$ is a line if stasify
$$L=\{(x,y):ax+by=c\}$$
where,
1. $a,b,c,x,y\in \mathbb{R}$
2. $\vert a\vert+\vert b\vert\neq 0$

**EX**
1. $x=1,\;L=\{(1,y),y\in\mathbb{R}\}$
2. $y=x+1,\;L=\{(x,x+1),x\in\mathbb{R}\}$

## 2.2 Lines and planes on $\mathbb{R}^3$
$$P=\{(x,y,z)\in\mathbb{R}^3:ax+by+cz=d\}$$
$$L=P_1\cap P_2\to\begin{cases}
   \text{plane} &\text{if } P_1=P_2\\
   \text{line}  &\text{if } P_1,P_2 \text{ are not paralled}\\
   \empty  &\text{if } P_1 || P_2 \text{ and } P_1 \neq P_2
\end{cases}$$
$$P_1\cap P_2=\{(x,y,z):eq_1,eq_2\}$$

where,
1. $eq_1=a_1x+b_1y+c_1z=d_1$
2. $eq_2=a_2x+b_2y+c_2z=d_2$

## 2.3 Hyperplain
Consider the dimensions
1. $\mathbb{R}^3\to \text{dimension } 3\to 3D$
2. $\text{plains in }\mathbb{R}^3\to 2D$
3. $\text{lines in }\mathbb{R}^2\text{ and }\mathbb{R}^3\to 1D$

Then we define huperplain
$$P=\{\mathbf{x}\in\mathbb{R}^n:\textbf{a}\cdot\textbf{x}=b\}$$
where,
1. $P$ has dimension $n-1$
2. $\textbf{a}\in\mathbb{R}^n,\;b\in \mathbb{R}$

## 2.4 Multidemensional system
$$\textbf{A}\textbf{x}=\textbf{b}\to\begin{cases}
   & a_{11}x_1+...+a_{1n}x_n=b_1\\
   & ......\\
   & a_{m1}x_1+...+a_{mn}x_n=b_m
\end{cases}$$
where,
1. $\textbf{A}=\begin{bmatrix}
   a_{11} & a_{12} & ... & a_{1n} \\
   a_{21} & a_{22} & ... & a_{2n} \\
   ...    & ...    & ... & ...    \\
   a_{m1} & a_{m2} & ... & a_{mn}
\end{bmatrix}$
2. $\textbf{b}=(b_1,...,b_m)^T,\;\textbf{x}=(x_1,...,x_n)^T$

令 $\tilde{a}_k=(a_{k1},...a_{km})\in\mathbb{R}^n$
由此可得 $m$ 个超平面 $H_k$
$$H_k=\{x\in\mathbb{R}^n:\tilde{a}_k \textbf{x}=b_k\}\to\begin{cases}
   & H_1:\tilde{a}_1 \textbf{x}=b_1\\
   & ......\\
   & H_m:\tilde{a}_m \textbf{x}=b_m
\end{cases}$$

**dimension** of $H_k=n-1$
### Solution of system $x\in\cap_{k=1}^mH_k$
1. when $x\in\cap_{k=1}^mH_k$ is empty: no solution
2. many solutions
3. single solution

例如当 $m=2,\;n=3$（三维空间中的两个面），除了两面不想交时没有解之外，还可能有直线解或者平面解（这里的 many solutions 由于涉及到高维空间，没有必要从几何的角度理解，只要把它看做是矩阵有多个解就行了）

## 2.5 Elimination
$$
\begin{pmatrix}
   3 & 2 & 1& |&39 \\
   2 & 3 & 1& |&34 \\
   1 & 2 & 3& |&26
\end{pmatrix}
\xrightarrow[l_{21}=\frac{2}{3}]{(2,1)}
\begin{pmatrix}
   3 & 2 & 1 & |&39 \\
   0 & \frac{5}{3} & \frac{1}{3}& |&8 \\
   1 & 2 & 3& |&26
\end{pmatrix}
\xrightarrow[]{}...\xrightarrow[]{}
\begin{pmatrix}
   3 & 2 & 1& |&39 \\
   0 & \frac{5}{3} & \frac{1}{3}& |&8 \\
   0 & 0 & \frac{12}{5}& |&\frac{33}{5}
\end{pmatrix}
$$
where,
1. $(2,1)$ 表示第二行减去第一行
2. $l_{21}=\frac{2}{3}$ 表示 $l_2-\frac{2}{3}l_1$

## 2.6 Operations Counting
每次高斯消元过程均由相同数量的乘法以及减法操作组成
对于 $n\times n$ 的矩阵 
$$\begin{pmatrix}
   x & x & ... & x \\
   x & x & ... & x \\
   ... & ... & ... & ... \\
   x & x & ... & x \\
\end{pmatrix}$$

第一次高斯消元需要进行 $n(n-1)$ 步的乘法以及减法操作，后转换成如下矩阵
$$\begin{pmatrix}
   x & x & ... & x \\
   0 & x & ... & x \\
   ... & ... & ... & ... \\
   0 & x & ... & x \\
\end{pmatrix}$$

随后第二次、第三次......直至最后一次高斯消元，各需要进行 $(n-1)(n-2),(n-2)(n-3)$...步的操作，由此
$$\text{Total Operations} =\sum_{k=2}^n k(k-1)=\frac{n^3-n}{3}\approx n^3$$
