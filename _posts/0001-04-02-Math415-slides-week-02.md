---
layout: post
title: Math415 Week-02
categories: Math415
description: Personal Notes
keywords: Math415，Calculas，Matrix
---
**ATTENSION - If some LeTeX equations could not show well, pleae try to refresh this page.**

# L3
## 3.1 Matrix multiplication
### 3.1.1 Properties
1. $(AB)^T=B^TA^T$
2. $ABC=(AB)C=A(BC)$
3. $(AB)^{-1}=B^{-1}A^{-1}$
## 3.2 Matrix inverse
Defined only for square matrices
The unit matrix $I$ satisfy
$$IA=AI=A,\;\text{for any }A$$

$$\text{Let }A\in\mathbb{C}^{n\times n},\;A^{-1}\text{ is the inverse of }A\text{ if }AA^{-1}=I$$
### 3.2.1 Properties
1. If $A$ has inverse $A^{-1}$, then it is unique
2. $(AB)^{-1}=B^{-1}A^{-1}$
3. $(A^T)^{-1}=(A^{-1})^T$
4. $\text{Let }A\in\mathbb{C}^{n\times n},\;x\in\mathbb{C}^n,\;\text{if there } \exist\;A^{-1},\;s.t.\;Ax=0$
$\text{Then }x=0$
5. $\text{If } \exist\;x\in\mathbb{C}^n,\;x\neq 0\;\text{and let }Ax=0$
$\text{Then }A \text{ cannot have inverse (is singular)}$


这些概念中，4、5 两点可以从线性变换矩阵的角度来理解（详见 [Some Math Concepts Section 2.3.1](https://zhekaili.github.io/0001/05/02/Math415-some-math-concepts/#23-%E8%A1%8C%E5%88%97%E5%BC%8F)）

## 3.3 Calculation of inverse
Solving $A^{-1}$ is equal to solve $X$ in the following problem
$$AX=I$$

Use Gauss Elimination:
$$(A|I)\to (I|A^{-1})$$


**Example**
$$A=\begin{bmatrix}
   1 & 3 \\
   2 & 7
\end{bmatrix}$$
$$\begin{pmatrix}
   1 & 3 &|& 1 & 0\\
   2 & 7 &|& 0 & 1
\end{pmatrix}\to \begin{pmatrix}
   1 & 3 &|& 1 & 0\\
   0 & 1 &|& -2 & 1
\end{pmatrix}\to \begin{pmatrix}
   1 & 0 &|& 7 & -3\\
   0 & 1 &|& -2 & 1
\end{pmatrix}$$
$$A^{-1}=\begin{pmatrix}
   7 & -3\\
   -2 & 1
\end{pmatrix}$$

当然，对于 $2\times 2$ 矩阵可以直接写出其逆矩阵 
$$A^{-1}=\frac{1}{ad-bc}\begin{pmatrix}
   d & -b\\
   -c & a
\end{pmatrix}$$

## 3.4 Permutation matrix
$$P_{ij} \in \R^{n\times n}\text{ is obtained from }I\text{ by switching }i_{th}\text{ and }j_{th}\text{ rows}$$
$$P_{23}=\begin{bmatrix}
   1 & 0 & 0 \\
   0 & 0 & 1 \\
   0 & 1 & 0
\end{bmatrix}$$

**Properties**
1. $P_{12}=P_{12}^{-1}=P_{21}$
2. $P_{31}P_{21}\neq P_{21}P_{31}$

## 3.5 Elimination matrix
$\text{Let } A\in\mathbb{C}^{n\times n}\text{ be given}$
$E_{ij}$ is the matrix such that $E_{ij}A$ means 
$$i_{th}\text{ row} - l_{ij}\times j_{th}\text{ row}$$
where $l_{ij}=\frac{a_{ij}}{a_{jj}}$
相当于
$$(a_{i1},...,a_{in})-(a_{j1},...,a_{jn})\times \frac{a_{ij}}{a_{jj}}$$

$$\begin{aligned}
E_{ij}&=I-\begin{bmatrix}
   0 & 0 & 0 \\
   0 & l_{ij} & 0\\
   0 & 0 & 0 
\end{bmatrix} \\
E_{ij}A&=A-\begin{bmatrix}
   0 & ... & 0 \\
   a_{i1}l_{ij} & ... & a_{in}l_{ij}\\
   0 & ... & 0 
\end{bmatrix}\end{aligned}$$

**Example**
$$A=\begin{bmatrix}
   3 & 1 \\
   1 & 0
\end{bmatrix}\to E_{21}A=\begin{bmatrix}
   3 & 1 \\
   0 & -\frac{1}{3}
\end{bmatrix}\to E_{21}=\begin{bmatrix}
   1 & 0 \\
   -\frac{1}{3} & 1
\end{bmatrix}$$

## 3.6 Triangular Mtrices

set $U$ represent **upper triangular** matix, satisfying $u_{ij}=0,\;i<j$
set $L$ represent **lower triangular** matix, satisfying $l_{ij}=0,\;i<j$

**Property**
n 个上三角矩阵的乘积仍为上三角矩阵（下三角同理）
即 $\text{If } L_1,...,L_n \in L,\;\text{then }(L_1L_2...L_n)\in L$

## 3.7 LU-Decomposition 
= LU-Factorization
### 3.7.1 Def 
$$\text{If }A=LU,\text{ then we say that }A\text{ allows LU-decomposition}$$

并不是所有矩阵都能被 LU 分解，例如 $$\begin{bmatrix}
   0 & 1 \\
   1 & 1
\end{bmatrix}$$
但是可以通过构造一个 Permutaion Matrix $P$ 使得任何 $A\in\mathbb{C}^{n\times n}$ 都能被 LU 分解

### 3.7.2 Find P, L, U from A
1. From $A\to U:U=E_{n(n-1)}E_{n(n-2)}E_{(n-1)(n-2)}...E_{32}E_{n1}...E_{31}E_{21}A=EA$
2. Then $A=E^{-1}U=LU$
3. Therefore, $L=E^{-1}$
(if need $P$, similarly, $U=EPA,\;PA=E^{-1}U=LU$)

LU-factorization is **not unique**, since $P$ is not unique (不同的换行方式会使得 $PA$ 变得不同)

### 3.7.3 Lemma

**1. $A\in\mathbb{C}^{n\times n}$ is invertible $\iff$$\forall\;b\in\mathbb{C}^n,\exist\;x\in\mathbb{C}^n$ satisfy $Ax=b$**
- **Proof:**
左到右好证（$x=A^{-1}b$）<br> 右到左，可令 $b_1,...,b_n$ 为 $n$ 个标准基向量，例如 $b_1=[1,0,...,0]^T,b_2=[0,1,...,0]^T$

**2. $A$ is singular $\iff U$ has zero element on diagonal**
- **Proof:**
不需要证明，存在零元素就意味着存在 free column

### 3.7.4 Use LU-Decomposition to solve $Ax=b$
$$Ax=LUx=b\to Ly=b,Ux=y$$






















