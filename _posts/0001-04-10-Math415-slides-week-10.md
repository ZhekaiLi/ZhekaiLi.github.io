---
layout: post
title: Math415 Week-10
categories: Math415
description: Personal Notes
keywords: Math415，Calculas，Matrix
---
**ATTENSION - If some LeTeX equations could not show well, pleae try to refresh this page.**

# L17
Symmetric matrices
## 17.1 On dot product for complex vectors
> ##### Def 1: Conjugate transpose 共轭转置
> 又称 Hermitian transpose
$$A^*=(\overline{A})^T=\overline{(A^T)}$$
>
>又记做 $A^H,A^\dagger$

例如，对于矩阵 
$$A=\left[\begin{matrix}
1 & i \\
0 & 2
\end{matrix}\right],A^T=\left[\begin{matrix}
1 & 0 \\
i & 2
\end{matrix}\right],A^*=\left[\begin{matrix}
1 & 0 \\
-i & 2
\end{matrix}\right]$$

> ##### Def 2: Dot product, norm, and orthogonality for complex vectors 复数向量的点乘、范数以及正交性
> 1. 对于实数向量 $x,y\in\mathbb{R}^n$
> - dot product: $x\cdot y=x^Ty=\sum x_iy_i$
> - norm: $||x||=\sqrt{x\cdot x}=\sqrt{\sum x_i^2}$

> ##### Def 3: Symmetric matrices
> 对称矩阵 $A\in\mathbb{R}^{n\times n}$ 具有如下性质
> 1. 特征根均为实数
> 2. diagonalizable 可对角化的，即其 Jordan form 为对角矩阵
> 3. 对应不同特征根的特征向量互相正交

# L18
Positive definite matrices and quadratic forms

## 18.1 正定矩阵

> **Def 1: Positive definite matrices (eigenvalues base)**
A symmetric matrix $A\in\mathbb{C}^{n\times n}$ is said to be positive definite if all its **eigenvalues are positive**

> **Def 2: Energy base definition**
$x^TAx$ is interpreted as "energy of $x$", 正定就意味着对于任意 $x\in\mathbb{R}^n,x\neq 0$, 都有 $x^TAx > 0$ 

**Theorem 1**: Def 1 与 Def 2 可以相互转化

**等效性质** (以下性质可于正定互推)
- All pivots are positive
- All the upper left deteminants are positive
- $A=B^TB, B\in\mathbb{R}^{m\times x}$ with independent columns

**其他性质**
- 正定一定满秩, 反推不成立

## 18.2
> **Def 1: Negative definite**
> 1. Eignvalues of $A$ are negative
> 2. $x^TAx<0$ if $x\neq0$ 

> **Def 2: Positive semi-definite**
> 1. Eignvalues of $A$ are non-negative
> 2. $x^TAx \geq 0$ if $x\neq 0$ 
>
> 对于 Negative semi-definite，性质恰好相反

> **Def 3: Indefinite**
> $A$ is indefinite 如果同时存在正的和负的特征值