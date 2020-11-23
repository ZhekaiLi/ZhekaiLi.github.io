---
layout: post
title: Week-7
categories: Math415
description: Personal Notes
keywords: Math415，Calculas，Matrix
---

# L11 Orthogonality
## 11.1 Normed vector spaces
> ##### Def 1: Normed vector space
> $X$ is normed if there is a function $\|\cdot\|:X\to\mathbb{R}$, such that
$$\begin{aligned}
\|x\| &\geq 0 \\
\|x+y\| &\leq \|x\|+\|y\|
\end{aligned}$$

**Examples**
1. When $X=\mathbb{R}^2$
$\begin{aligned}\|x\|_1=\vert x_1\vert+\vert x_2\vert \\
\|x\|_2=\sqrt{x_1^2+x_2^2}\end{aligned}$
2. When $X=\{\text{all polynomials on }[0,1]\}$
$\begin{aligned}\|x\|_1&=\int_0^1 \vert x(t)\vert dt \\
\|x\|_2&=\sqrt{\int_0^1  x^2(t) dt}\end{aligned}$

## 11.2 Euclidean norm in $\mathbb{R}^n$
> ###### Def 2: Euclidean norm
> $$\begin{aligned}
\|x\|&=(x\cdot x)^{1/2} \\[5pt]
\|x\|^2&=x\cdot x=x^Tx=\sum x_i^2
\end{aligned}$$

![pic1](https://github.com/ZhekaiLi/PICTURE-for-markdown/raw/master/Snipaste_2020-11-23_08-19-44.jpg)

## 11.3 Orthogonality in $\mathbb{R}^n$
Vector $x\perp y$ iff
1. $x\cdot y=0$
2. $\|x\|^2+\|y\|^2=\|x+y\|^2$

> ##### Def 3: Orthogonal subspaces
> Let $S,T$ be subspaces in $\mathbb{R}^n$, $x\in \mathbb{R}^n$
> 1. $x\perp S$ if $x$ is orthogonal to any vector from $S$
> 2. $S\perp T$ if any from $S$ is orthogonal to any from $T$
> 3. Orthogonal complement $S^{\perp}=\{x:x\perp S\}$

**Facts:**
(a) $T=S^\perp \iff S=T^\perp$
(b) $(S^\perp)^\perp=S$

**Theorem 1:** For $A_{m\times n}$,
$$N(A)^\perp=C(A^T)$$
- **Proof:** It's equal to show $N(A)=C(A^T)^\perp$
(a) We know that if we can prove $a\to b, \neg a\to \neg b$, then we get $a=b$
(b) For $x\in N(A)\to x\in C(A^T)^\perp$, correct
(c) For $x\notin N(A)\to x\notin C(A^T)^\perp$, $x$ 不属于零空间就说明 $x$ 与 $A$ 的某一列相乘不得零

## 11.3 Projection of a vector onto a subspace in $\mathbb{R}^n$

**Theorem 2:** For any $S\subset\mathbb{R}^n$, any vector $x\in\mathbb{R}^n$ can be represent as $x=p+e$, where $p\in S,e\in S^\perp$

> ##### Def 4: Projection
> Denote $p$ in theorem above is the **projection** of $x$ onto $S$, that
$$p=P_Sx$$

**Facts:**
(a) Projection is uniquely defined 
(b) $P_S$ is a linear transformation in $\mathbb{R}^n$
(c) $P_S=P_S^2=P_S^n$
(d) $I-P_S=P_{S^\perp}$
- **Proof:** Since $e=P_{S^\perp}x$, plus that $(I-P_S)x=x-P_Sx=(p+e)-p=e$, therefore proven

**Example:**
Let $x=(x_1,x_2,x_3)^T,S=\{(0,0,x_3)^T\}$
then $S^\perp=\{(x_1,x_2,0)^T\}$
$$P_S=\begin{pmatrix}
0 & 0 & 0 \\
0 & 0 & 0 \\
0 & 0 & 1
\end{pmatrix},P_{S^\perp}=I-P_S=\begin{pmatrix}
1 & 0 & 0 \\
0 & 1 & 0 \\
0 & 0 & 0
\end{pmatrix}$$

## 11.4 Projection onto a span of given vectors
Let $A=(a_1,...,a_n)\in\mathbb{R}^{m\times n},m>n$
