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
> $X$ is normed if there is a function $\vert\vert\cdot\vert\vert$, such that
$$\begin{aligned}
\|x\| &\geq 0 \\
\|x+y\| &\leq \|x\|+\|y\|
\end{aligned}$$

**Examples**
1. When $X=\mathbb{R}^2$
$$\begin{aligned}\|x\|_1=\vert x_1\vert+\vert x_2\vert \\ \|x\|_2=\sqrt{x_1^2+x_2^2}\end{aligned}$$
2. When $X=\{\text{all polynomials on }[0,1]\}$
$$\begin{aligned}\|x\|_1&=\int_0^1 \vert x(t)\vert dt \\
\|x\|_2&=\sqrt{\int_0^1  x^2(t) dt}\end{aligned}$$

## 11.2 Euclidean norm in $\mathbb{R}^n$
> ###### Def 2: Euclidean norm
> $$\begin{aligned}
\|x\|&=(x\cdot x)^{1/2} \\[5pt]
\|x\|^2&=x\cdot x=x^Tx=\sum x_i^2
\end{aligned}$$

![pic1](https://github.com/ZhekaiLi/PICTURE-for-markdown/raw/master/Snipaste_2020-11-23_08-19-44.jpg)

## 11.3 Orthogonality in $\mathbb{R}^n$
Vector $x\perp y$ iff
1. $x\cdot y=0$ or
2. $\vert\vert x\vert\vert^2+\vert\vert y\vert\vert^2=\vert\vert x+y\vert\vert^2$

> ##### Def 3: Orthogonal subspaces
> Let $S,T$ be subspaces in $\mathbb{R}^n$, $x\in \mathbb{R}^n$
> 1. $x\perp S$ if $x$ is orthogonal to any vector from $S$
> 2. $S\perp T$ if any from $S$ is orthogonal to any from $T$
> 3. Orthogonal complement $S^{\perp}=\{x:x\perp S\}$

**Facts:**
1. $T=S^\perp \iff S=T^\perp$
2. $(S^\perp)^\perp=S$

**Theorem 1:** For $A_{m\times n}$,
$$N(A)^\perp=C(A^T)$$

**Proof:** It's equal to show $N(A)=C(A^T)^\perp$
1. We know that if we can prove $a\to b, \neg a\to \neg b$, then we get $a=b$
2. For $x\in N(A)\to x\in C(A^T)^\perp$, correct
3. For $x\notin N(A)\to x\notin C(A^T)^\perp$, $x$ 不属于零空间就说明 $x$ 与 $A$ 的某一列相乘不得零

## 11.3 Projection of a vector onto a subspace in $\mathbb{R}^n$

**Theorem 2:** For any $S\subset\mathbb{R}^n$, any vector $b\in\mathbb{R}^n$ can be represent as $b=p+e$, where $p\in S,e\in S^\perp$

> ##### Def 4: Projection
> Denote $p$ in theorem above is the **projection** of $x$ onto $S$, that
$$p=P_Sb$$

**Facts:**
1. Projection is uniquely defined 
2. $P_S$ is a linear transformation in $\mathbb{R}^n$
3. $P_S=P_S^2=P_S^n$
4. $I-P_S=P_{S^\perp}$

**Proof:** Since $e=P_{S^\perp}b$, plus that $(I-P_S)b=b-P_Sb=(p+e)-p=e$, therefore proven

## 11.4 Projection onto a span of given vectors

**Theorem 3:** Let $A=(a_1,...,a_n)\in\mathbb{R}^{m\times n},m>n$, then $A^TA$ is invertible

**Proof:** For $A^TAx=0\to x^TA^TAx=0\to \|Ax\|=0\to x=0$

**Theorem 4:** Let $S=\text{span}(a_1,...,a_n)$, then we have
$$S=C(A)=\{Ax,x\in\mathbb{R}^n\}$$

> ##### Def 5: Prjection matrix $P$
> The projection $p$ of vector $b$ onto $S=C(A)$ is
$$p=Pb,\text{where }P=A(A^TA)^{-1}A^T$$

**Proof:**
1. Since $C(A)=N(A^T)^\perp\to C(A^\perp=N(A^T)$, therefore $p\in C(A),e\in N(A^T)$
2. To find $P$, assume $\hat{x}$ that $A\hat{x}=p$, then we have $A\hat{x}-b=-e\in N(A^T)$
3. From 2, we get $A^T(A\hat{x}-b)=0$, then $\hat{x}=(A^TA)^{-1}A^Tb$
4. Finally, $p=A\hat{x}=A(A^TA)^{-1}A^Tb$

**Corollary:** $P_S^T=P_S$

# L12
## 12.1 Least squares approximation

For a model 
$$b\approx a_1x_1+a_2x_2+...+a_nx_n$$

where $\{a_i\}$ are paramters and $\{x_i\}$ are variables

When $\{x_i,b\}$ are given, we want to estimate a set of $\{a_i\}$ to make $\sum a_ix_i$ close to $b$ as possible, that's why we need **LSA** (least squares approximation)

> ##### Def 1: Fitting error $e_k$
> $$e_k=b_k-\sum_{i=1}^na_{ki}x_i$$

> ##### Def 2: Quadratic criterion
> $$\text{Minimize }e_1^2+...+e_n^2\text{ over }x_1,...,x_n\in\mathbb{R}$$

**Example**: Find a line $y=C+Dx$ that is closest to $(0,6),(1,0),(2,0)$

$$\begin{aligned}
e_1&=6-(C+0) \\
e_2&=0-(C+D) \\
e_3&=0-(C+2D)
\end{aligned}$$

then we get $f(C,D)=e_1^2+e_2^2+e_3^2$

After solveing $f'_C=0$ and $f'_D=0$, we get $C=5,D=-3$

## 12.2 Matrix reformulation
For $A_{m\times n}$, we can reformulate the probelm before into 
$$\text{Minimize }\|Ax-b\|\text{ over }x\in\mathbb{R}^n$$

From **L11**, it is obvious that the optimal solution $\hat{x}$ of the problem is $\hat{x}=(A^TA)^{-1}A^Tb$, which makes $$\|A\hat{x}-b\|=\|p-b\|=\|e\|$$

## 12.3 Alternative solution
> ##### Def 3: 矩阵求导
> $$\begin{aligned}
\frac{d}{dx}(Ax)&=A^T \\
\frac{d}{dx}(x^TA)&=A \\
\frac{d}{dx}(x^TAx)&=(A^T+A)x
\end{aligned}$$

Since 
$$\min\|Ax-b\|\iff\min\|Ax-b\|^2\iff\min(Ax-b)^T(Ax-b)$$

therefore 
$$f(x)=(x^TA^T-b^T)(Ax-b)=x^TA^TAx-2x^TA^Tb+b^Tb$$

then from **Def 3**, we get
$$\frac{df}{dx}=2x^TA^TA-2b^TA$$

finally from $\frac{df}{dx}=0$, we get $x=(A^TA)^{-1}A^Tb$, as in **L12.2**

## 12.4 Orthogonal and orthonormal matrices and bases
> ##### Def 4: Orthogonal matrix
> A matrix $Q_{n\times n}$ is orthogonal if $Q^TQ=I$ or $Q^{-1}=Q^T$

**Examples:**
1. Permutation matrix
2. Rotation matrix

> ##### Def 5: Orthonormal vectors
> 1. A system of vectors $\{q_i\}$ is **orthogonal** if $q_i^Tq_j=0$ when $i\neq j$
> 2. A system of vectors $\{q_i\}$ is **orthonormal** if $q_i^Tq_j=0$ when $i\neq j$ and $\vert\vert q_i\vert\vert=1$



