---
layout: post
title: Week-5
categories: Math415
description: Personal Notes
keywords: Math415，Calculas，Matrix
---

# L7 Independence, basis, dimension

## 7.1 Dimension of a sum of subspaces

Let $X$ be a vector space, $Y$ and $Z$ be a subspaces.

**Definition:** Sum of subspaces $Y+Z$ is $\{y+z,y\in Y, z\in Z\}$

Fact: $Y+Z,Y\cap Z$ are also subspaces, while $Y\cup Z$ is not

**Theorem:** 
$$\text{dim}(Y+Z)=\text{dim}(Y)+\text{dim}(Z)-\text{dim}(Y\cap Z)$$

## 7.2 Base in $\mathbb{E}^n$
**Theorem 1:** If $u_1, ...., u_n$ and $v_1, ...., v_n$ are two bases in $E^n$ then there exists an invertible matrix $B \in \mathbb{E}^{n\times n}$ such that
$$UB=V$$

**Theorem 2.1:** Let $A \in E^{n\times n}$ be invertible. If $u_1, ...., u_n$ is a basis in $E^n$, then $Au_1, ...., Au_n$ is also a basis in $E_n$.

**Theorem 2.2:** Let $A \in E^{n\times n}$ be invertible. If $u_1, ...., u_n$ is a basis in $E^n$, then $u_1A, ...., u_nA$ is also a basis in $E^n$.

**Proof:** (For Theorem 2.1) Let $b\in E^n$, then $A^{-1}b\in E^n$
then express $A^{-1}b=\sum c_ku_k\to b=A(A^{-1}b)=\sum c_k(Au_k)$

Similar for Theorem 2.2


### 7.2.1 How to find if $\{u_1,...,u_n\}\sub E^n$ is a basis
**The rule:** Compose a matrix using $\{u_1, ..., u_n\}$ as columns (or, alternatively, as rows). The set $\{u_1, ..., u_n\}$ is a basis if and only if $A$ is invertible.
Since Gauss-Jordan elimination procedure means multiplication on an invertible matrix, we can apply Gauss- Jordan elimination procedure to test matrix invertibility.

### 7.2.2 Infinite dimensional spaces
略，好像课件里没讲到啥内容

# L8 Four fundamental subspaces defined by a matirx

按照老师课件的要求，对 $R$ 得再进行一波换列操作，使得
$$R=\begin{pmatrix}
   I & F \\
   0_{(m-r)\times r} & 0
\end{pmatrix}$$

注意交换列之后自变量的顺序也要做对应的交换，例如交换 $2,3$ 列之后 $(x_1,x_2,x_3)\to(x_1,x_3,x_2)$

## 8.1 Dimension of linear manifolds
**Definition:** If $X$ is a linear space, $Y$ is a subspace, $a\in X$, $M = a + Y$ is a linear manifold, then we say that $\text{dim}(M) = \text{dim}(Y)$.

**Corollary:** Let $A\in E^{m\times n}$, $b\in E^n$. For a linear system $Ax = b$, all solutions $x\in E^n$ form a linear manifold
$$x_{part}+N(A)$$ 

in $E^n$ that has dimension $n-\text{rank}(A)$ ($x_{part}$ is the particular solution)

### 8.1.1 Lines and planes in $\R^3$
**Ex.1:** For any nonzero $a\in \R^3$ and $b\in \R$, let $Y = \{x\in\R^3 : a^Tx = b\}$. Find $Y$ and $\text{dim}(Y)$

1. $A=a^T$, then we get $Y=x_{part}+N(A)$
2. Since $m=1,n=3,\text{rank}(A)=1$, $\text{dim}(Y)=\text{dim}(N(A))\to Y$ is a plane

**Ex.2:** ) For $A\in\R^{3\times 3}$ and $b\in\R^3$, let $Y = \{x\in\R^3 : Ax = b\}$. Find $Y$ and $\text{dim}(Y)$

1. If $\text{rank}(A)=3$, $Y=x_{part}$, $\text{dim}(Y)=0$
1. If $\text{rank}(A)=2$, $Y=x_{part}+N(A)$, $\text{dim}(Y)=1$ ---- line
1. If $\text{rank}(A)=1$, $Y=x_{part}+N(A)$, $\text{dim}(Y)=2$ ---- plane
## 8.2 Linear Transformations

**Definition:** Define mapping $T:X\to Y$ is linear iff
$$T(\alpha x)=\alpha T(x),\;\;\;\;\;\forall \alpha\in E,x\in X \newline
T(x+y)=T(x)+T(y),\forall x,y\in X$$

将 $T$ 称之为 linear transformation/ linear mapping/ linear operator/ linear function，常常用 $Tx$ 指代 $T(x)$

**Ex.1: Linear transformations**
1. $X=E^n,Y=E^m$
$T(x)=Ax\;\;\;(A\in E^{m\times n})$ 
<br>
2. $X=E^{n\times n},Y=E^{n\times n}$
$T(x)=MxN\;\;\;(M,N\in X)$
<br>
3. $X=Y=\text{span}(1,t,t^2,...)$
$T(x)=\frac{dx}{dt}$
<br>
4. $X=Y=\Complex$
$T(x)=\text{Re}(\Complex)$
<br>
5. $X=\text{span}(1,t,t^2,...),Y=\R$
$T(x)=x(0)+\int_0^{10}(2x(t)+5)dt$

**Ex.2: Not linear**
1. $X=Y=\R$
$T(x)=x+1$, not linear since $T(0\cdot x)\neq0\cdot T(x)=0$
<br>
2. $X=Y=R$
$T(x)=|x|$
### 8.2.1 The case of $X=E^n,Y=E^m$

### 8.2.2 Matrices of linear transformations: general case

**Theoerm:** Let $T:X\to Y$ is a linear transformation from vector spaces $X$ and $Y$ with bases $\{u_j\}$ and $\{v_k\}$ respectively. Let $\{a_{ij}\}_{i\geq1}$ be the set of coordinates for $T(u_j)$ in the basis $\{v_k\}$, and let matrix $A$ be formed as $A = \{a_{ij}\}$. Then
$$T(x)=y\text{ iff } Ac=d$$

where $c$ is the vector column of x in the basis $\{u_j\}$, $d$ is the vector column of y in the basis $\{v_k\}$

**关于 $u,k,c,d,A$ 的维度**
1. 令 $X\in E^n, Y\in E^m$，因此 $u_j\in E^n, v_k\in E^m$
2. 再令 $\text{dim}(\{u_j\})=p$，即 $X$ 有 $p$ 个 bases
同时 $\text{dim}(\{v_k\})=q$，即 $Y$ 有 $q$ 个 bases
因此 $c\in E^p, d\in E^q$，验证： $x_{n\times 1}=\{u_j\}_{n\times p}\times c_{p\times 1}$
3. 注意，这里的 $A$ 并不是 $Ax=y$ 的变换矩阵，而通过 $Ac=d$ 易得 $A\in E^{q\times p}$

**理解 $T(x)=y\text{ iff }Ac=d$**
如果用一个公式来联系 $T(x)=y$ 与 $Ac=d$，
$$T(x)=T(\{u_j\}\times c)=\{v_k\}\times Ac=\{v_k\}\times d=y$$

具体示例详见以下示例的后半部分

**Ex.1:** Let $X=\text{span}\{1, t, t^2\}$, $Y=\text{span}\{1, t\}$ and the ransform $T=\frac{dx}{dt}$, find the matrix of tranform $T$

$u_j$ 有三个，$v_k$ 有两个 $\to c_{3\times 1}, d_{2\times 1}\to Ac=d \to A_{2\times 3}$ 

因为 $A$ 的第 $i$ 列相当于把 ${u_k}$ 转换成 $T(u_i)$ ，因此可得

$T(u_0)=0=0\cdot v_0+0\cdot v_1$
$T(u_1)=1=1\cdot v_0+0\cdot v_1$
$T(u_2)=2t=0\cdot v_0+2\cdot v_1$

Therefore $A=\begin{bmatrix}
0 & 1 & 0 \\
0 & 0 & 2
\end{bmatrix}$
