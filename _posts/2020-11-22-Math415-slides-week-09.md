---
layout: post
title: Math415 Week-09
categories: Math415
description: Personal Notes
keywords: Math415，Calculas，Matrix
mathjax: true
---

# L15 
Similar matrices and Jordan forms
## 15.1 Similarity
> #### Def 1: Similarity
> $A$ is similar to $B$ if for some invertible $Q$ <br>
> $$A=QBQ^{-1}$$
> Similar matrices share the following **same**:
> - Sets of eigenvalues
> - Dimension of null and column spaces
> - ranks
> - trace and determinent
> - Jordan forms
>
> **DO NOT** share the same Eigensapces and 四个子空间

**Theorem 1.1**: Similarity is an **equivalence relation**:
$$\begin{aligned} A\sim B&\to B\sim A \\
A\sim B, B\sim C&\to A\sim C\end{aligned}$$

**Theorem 1.2**: Similar matrices have the same characteristic polynomials (特征多项式)
- **Lemma**: $A\sim B\to A-\lambda I\sim B-\lambda I$
$\small{
    QAQ^{-1}=B\to Q(A-\lambda I)Q^{-1}=QAQ^{-1}-\lambda QQ^{-1}=B-\lambda I
    }$

then it's easy to get $\vert A-\lambda I\vert=\vert B-\lambda I\vert$ 

> #### Def 2: Algebraic multiplicity 代数重数
> Algebraic multiplicity of eigenvalue $\lambda$ of $A$ is $d$, where
$$\delta_A(\lambda)=\prod(\lambda-\lambda_k)^d$$

> #### Def 3: Geometric multiplicity 几何重数
> Algebraic multiplicity of eigenvalue $\lambda$ of $A$ is $\dim(N(A-\lambda I))$

例如，对于 $A=I_n$，$\lambda=1$ 的几何重数等于 $n$

## 15.2 Jordan form and Spectrum
> #### Def 4: Jordan form
> Any $A$ is similar to a specific matrix $J$
> $$J=\begin{bmatrix}
J_1 & 0 & ... & 0 \\
0 & J_2 & ... & 0 \\
... & ... & ... & ... \\
0 & 0 & ... & J_s
\end{bmatrix}$$
>
>where
$$J_i=\begin{bmatrix}
\lambda_k & 1 & 0  \\
0 & \lambda_k & 1  \\
0 & 0 & \lambda_k
\end{bmatrix}$$
>
> $J_i$ 被称作 *Jordan block*，是一个以特征值为对角线、对角线元素的上一个元素等于 $1$、其他元素均为 $0$ 的矩阵 (注意：这里的 $J_i$ 并不对应 $\lambda_i$，例如下面这个矩阵有两个 $J_i$ 但只有一个 $\lambda_k$)
> $$J=\begin{bmatrix}
2 & 0 & 0 \\
0 & 2 & 1 \\
0 & 0 & 2
\end{bmatrix}$$

**Theorem 4.1: 由 *Jordan form* 表示重数**
1. $\lambda_k$ 的**代数重数**，是 $J$ 中以 $\lambda_k$ 为主对角线元素的各 *Jordan* 子块的**阶数之和**
2. $\lambda_k$ 的**几何重数**，是 $J$ 中以 $\lambda_k$ 为主对角线元素的各 *Jordan* 子块的**个数** 

**Corallary 4.1**: Two matrices are similar if and only if they have the same Jordan form (up to permutation of Jordan blocks)

**Corollary 4.2**: $\text{rank}(A)$ = number of nonzero eigenvalues
- **Proof**: $A\sim J\to \text{rank}(A)=\text{rank}(J)$，而 $J$ 由于近乎于一个对角矩阵，因此 $J$ 的秩取决于其非零对角线元素的个数

**Corollary 4.3:** If $A\in\mathbb{C}^{n\times n}$ has eigenvalues $\lambda_1,...,\lambda_n$, then $p(A)$ has eigenvalues $p(\lambda_1),...,p(\lambda_n)$ for any polynomial $p$.
- **Proof:** 
1. $A=QJQ^{-1}\to A^2=QJ^2Q^{-1}=...$
2. Then from $p(A)=\sum c_kA^k$, we can get $p(A)=\sum c_kJ^k$
3. Since $p(J)$ has eigenvalues $p(\lambda_1),...,p(\lambda_n)$, same for $p(A)$

> #### Def 5: Spectrum 矩阵的谱
> 矩阵的谱又叫矩阵的谱半径，定义为
> $$\rho(A)=\max|\lambda_i|$$
>
>即特征值模的最大值

**Corollary 5.1:** 具有相同谱的矩阵不一定相似

例如对于矩阵 $$A=\left[\begin{matrix}
2 & 0 \\
0 & 2
\end{matrix}\right],B=\left[\begin{matrix}
2 & 1 \\
0 & 2
\end{matrix}\right]$$
它们具有相同的谱（特征根均为 $2$），但是 $A$ 的几何重数为 $2$，$B$ 为 $1$，也意味着 $A$ 有两个特征根而 $B$ 只有一个。因此 $A,B$ 不相似


**Ex 1:** If knowing $$A=\left[\begin{matrix}
0 & -1\\
1 & 0
\end{matrix}\right]$$ $B=A^{10}-3A+1$, find the spectrum of $B$

from $A$, we can solve $\lambda_A=\pm i$, then $\lambda_B=\lambda_A^{10}-3\lambda_A+1$, 从而易得 spectrum of $B$

**Ex 2:** Is it true that matrices with the same spectrum are similar?
$$\text{No.} \begin{pmatrix}
2 & 0 \\
0 & 2
\end{pmatrix},\begin{pmatrix}
2 & 1 \\
0 & 2
\end{pmatrix}\text{ has same spectrum but not similar}$$

# L16 
Jordan forms. Matrix exponents. Application to dynamical systems

## 16.1 Matrix exponent in the general case
> #### Def 1: $e^A, \cos(A), \sin(A)$
> $$\begin{aligned} e^A &=I+\frac{A}{1!}+...+\frac{A^n}{n!} \\
\cos(A)&=\sum_{m=0}^\infty(-1)^m\frac{A^{2m}}{(2m)!} \\
\sin(A)&=\sum_{m=0}^\infty(-1)^m\frac{A^{2m+1}}{(2m+1)!}
\end{aligned}$$

**Corollary 1.1:** Since $(A^n)^T=(A^T)^n$, 然后结合 $e^A$ 的展开式
$$e^{A^T}=(e^A)^T$$

**Corollary 1.2:** If $AB=BA$, then
$$e^{A+B}=e^Ae^B$$

**Corollary 1.3:** From Corollary 2, we get
$$e^{-A}=(e^A)^{-1}$$

since $e^Ae^{-A}=e^{A-A}=I$

**Corollary 1.4:**
$$e^A=Xe^{\Lambda}X^{-1}$$

It is even impossible to directly write $e^A$, while it's easy to get $e^\Lambda$ (就是将 $\Lambda$ 对角线上的 $\lambda_i$ 变成 $e^{\lambda_i}$)

> #### Def 2: Derivative
> $$\frac{d}{dt}e^{At}=Ae^{At}=e^{At}A$$

## 16.2 Dynamical systems: Linear differential equations
> #### Def 1: Systems of linear scalar differential equations of first order
> Let $y(t)=[y_1, y_2, ..., y_n]^T$, then we can simplify
$$\begin{aligned}y'_1(t)=a_{11}y_1+&...+a_{1n}y_n+b_1(t) \\ &... \\ y'_n(t)=a_{n1}y_1+&...+a_{nn}y_n+b_n(t)
\end{aligned}$$ into
$$\frac{d}{dt}y(t)=Ay(t)+B(t)$$
>
> The general solution of this ODE
> $$y(t)=e^{At}a+\int_0^t e^{A(t-\tau)}B(\tau)d\tau,\;\;y(0)=a$$




