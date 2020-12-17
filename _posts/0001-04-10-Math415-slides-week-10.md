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
> #### Def 1: Conjugate transpose 共轭转置
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

> #### Def 2: Dot product, norm, and orthogonality for complex vectors 复数向量的点乘、范数以及正交性
> 1. 对于实数向量 $x,y\in\mathbb{R}^n$
> - dot product: $x\cdot y=x^Ty=\sum x_iy_i$
> - norm: $||x||=\sqrt{x\cdot x}=\sqrt{\sum x_i^2}$
> 2. 对于复数向量 $x,y\in\mathbb{C}^n$
> - dot product: $x\cdot y=x^T\overline{y}=\sum x_i\overline{y_i}$ 
> - norm: $||x||=\sqrt{x\cdot \overline{x}}$

> #### Def 3: Symmetric matrices
> 对称矩阵 $A\in\mathbb{R}^{n\times n}$ 具有如下性质
> 1. 特征根均为实数
> 2. diagonalizable 可对角化的，即其 Jordan form 为对角矩阵
> 3. 对应不同特征根的特征向量互相正交

# L18
Positive definite matrices and quadratic forms

## 18.1 正定矩阵

> #### Def 1: Positive definite matrices (eigenvalues base)
> A **symmetric matrix** $A\in\mathbb{C}^{n\times n}$ is said to be positive definite if all its **eigenvalues are positive**

> #### Def 2: Energy base definition
> $x^TAx$ is interpreted as "energy of $x$", 正定就意味着对于任意 $x\in\mathbb{R}^n,x\neq 0$, 都有 $x^TAx > 0$ 

**Theorem 1**: Def 1 $\iff$ Def 2

**等效性质** (以下性质可于正定互推)
- All pivots are positive
- All the upper left deteminants are positive
- $A=B^TB, B\in\mathbb{R}^{m\times n}$ with independent columns

**其他性质**
- 正定一定满秩, 反推不成立

> #### Def 3: 负定, 半正定和不确定矩阵
> **Negative definite**
> 1. Eignvalues of $A$ are negative
> 2. $x^TAx<0$ if $x\neq0$ 
>
> **Positive semi-definite**
> 1. Eignvalues of $A$ are non-negative
> 2. $x^TAx \geq 0$ if $x\neq 0$ 
>
> 对于 Negative semi-definite，性质恰好相反
>
> **Indefinite**
> $A$ is indefinite 如果同时存在正的和负的特征值

## 18.2 Quadratic forms

> #### Def 4: Quadratic form 
> Quadratic form is the mappings $F:\mathbb{R}^n\to\mathbb{R}$ defined as
$$F(x)=x^TAx=\sum_{i,j=1}^na_{ij}x_ix_j,\;x=\begin{pmatrix}
x_1 \\ ... \\ x_n
\end{pmatrix}$$

**Fact:** Any quadratic form can be represented as $x^TAx$ for some symmetric matrix $A$
- **Proof:** 
$$\begin{cases}
   F(x)=x^TBx \\
   F^T(x)=x^TB^Tx \\
   F(x)=F^T(x)
\end{cases}\to F(x)=\frac{1}{2}(x^TBx+x^TB^Tx)=x^T\frac{B+B^T}{2}x$$
where $\frac{B+B^T}{2}$ is ofcourse symmetric, proved

> #### Def 5: Definite, semidefinite, and indefinite quadratic forms
> $$\text{Quadratic form is}\begin{cases}
   \text{正定} &\text{if }F(x)>0\text{ for }x\neq0  \\
   \text{半正定} &\text{if }F(x)\geq0\text{ for all }x  \\
   \text{负定, 半负定} &\text{上边俩的符号反向} \\
   \text{不确定} &\text{if }F(x)\text{ 可正可负 }  \\
\end{cases}$$

**Theorem 1:** 如果 $A$ 的二次型 $x^TAx$ 是 "X定" 的, 那么 $A$ 也是 "X定" 的

**Lemma 1:** $A$ is positive definite $\iff$ the form $F(x) = x^TAx$ has an unique point of miniumum $x = 0$.

**Lemma 2:** $A$ is positive semi-definite $\iff$ the form $F(x) = x^TAx$ has a miniumum at $x = 0$ and this minimum is not unique.

**Lemma 3:** $A$ is indefinite $\iff$ the form $F(x) = x^TAx$ has a saddle point at $x = 0$.

> #### Def 6: Differentiation of quadratic forms
> $$\begin{aligned}
F(x)&= x^TAx \\
\frac{dF}{dx}(x)&= 2x^TA \\
\frac{d^2F}{dx^2}(x)&= 2A
\end{aligned}$$

