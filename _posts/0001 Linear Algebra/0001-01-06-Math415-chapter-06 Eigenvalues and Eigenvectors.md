---
layout: post
title: Math415 Chapter 06 Eigenvalues and Eigenvectors
categories: Math415:Linear-Algebra
description: Personal Notes
keywords: Math415，Linear-Algebra，Matrix
mathjax: true
---

## 6.1 Introduction to Eigenvalues

> #### Def 1: Eigenvector, Eigenvalue
> 矩阵 $A$ 的特征向量 $x$ 指的是那些经过线性变换 $Ax$ 之后方向不变，仅发生伸缩或反向变换的向量
$$Ax=\lambda x$$ 
>
> 其中特征向量 $\lambda$ 体现了 $x$ 发生的伸缩、取反变换

**Corollary 1:** 
$$A^nx=\lambda^nx,A^{-1}x=\lambda^{-1}x$$

> #### Def 2: Characteristic polynomial
> The characteristic polynomial of $A_{n\times n}$ has degree $n$
> $$\delta_A(\lambda)=\det(A-\lambda I)$$
>
> $\det(A-\lambda I)=0$ is called characteristic equation, it has $n$ roots

> #### Def 3: Trace 矩阵的迹
> $$\text{tr}(A)=\sum_{k=1}^n a_{kk}=\sum_{k=1}^n \lambda_k$$

> #### About Eigenvlues, Eigenvector, rank and trace
> 1. $n$ 阶矩阵有 $n$ 个特征值
> 2. 对称矩阵的秩 = 非零特征值的个数
> 3. 

## 6.2 Diagonalizing a Matrix
> #### Def 1: Diagonalizable matrix 可对角化矩阵
> $n$ independent eigenvectors (**normalized**) in $X$ diagonalize $A$
> $$A=X\Lambda X^{-1}$$
> 
> 判断一个矩阵是否为可对角化矩阵主要有以下几个途径
> 1. $n$ 个不同的特征值/ $n$ 个线性无关的特征向量
> 2. 代数重数 = 几何重数
> 3. 实对称矩阵

当存在相同的特征根时, $A$ **might** have too few independent eigenvectors. Then $X^{-1}$ fails.

## 6.3 Systems of Differential Equations

(已看完)

### 6.3.1 Solution of $du/dt = Au$
这部分可以用一个例题概括, 见 [Midterm 2 Review D7.2](https://zhekaili.github.io/0001/03/02/Math415-midterm-2-review/#d7)

### 6.3.2 Second Order Equations
这部分大概率不会考到, 如果考到最多也是长这样的 [Midterm 3 Review D7.2](https://zhekaili.github.io/0001/03/03/Math415-midterm-3-review/#d7)

### 6.3.3 Difference Equations (optional)
不考

### 6.3.4 Stability of 2 by 2 Matrices
不考 (不过挺有意思的, 有时间可以看看)

### 6.3.5 The Exponential of a Matrix

> #### Def 1 Matrix exponential $e^{At}$
> $$\begin{aligned}
e^x&= 1 + x + \frac{1}{2}x^2+\frac{1}{6}x^3+...=\sum_{k=0}^\infty{\frac{x^k}{k!}}\\
e^{At}&=I+At+\frac{1}{2}(At)^2+...=\sum\frac{(At)^k}{k!}
\end{aligned}$$
> 
> The eigenvalues of $e^{At}$ are $e^{\lambda t}$, since $(I+At+\frac{1}{2}(At)^2+...)\pmb{x}=(I+\lambda t+\frac{1}{2}(\lambda t)^2+...)\pmb{x}$

**Lemma 1:** If $A$ is diagonalized, then $e^{At}$ is also diagonalized
$$A=X\Lambda X^{-1}\to e^{At}=X[I+\Lambda t+\frac{1}{2}(\Lambda t)^2+...]X^{-1}$$

therefore
$$e^{At}=Xe^{\Lambda t}X^{-1}$$

可以利用这个性质来求解 Chapter 6.3.1 中的 $u(t)=e^{At}u(0)$

这一小节的其他部分应该也不会考, 不过可以看看下面这个 example, 它提供了一种求解二阶微分方程的新方法, 很有意思
![pic](/images/2020-12/Snipaste_2020-12-16_19-41-52.jpg)

## 6.4 Symmetric Matrices

### 6.4.1 Main

> #### Def 1: Symmetric diagonalization
> $$S=Q\Lambda Q^{-1}=Q\Lambda Q^T \text{ with } Q^{-1}=Q^T$$ 
>
>$Q$ is orthonormal.

**Proof:** Since symmetric matrix $S$ is diagonalizable, then $S=X\Lambda X^{-1}$, plus that $S^T=X^{-T}\Lambda X^T$ and $S^T=S$, we have
$$X^T=X^{-1}\to X\text{ orthonormal, denoted by }Q$$

**Theorem 1: Real Eigenvalues** All the eigenvalues of a real symmetric matrix are real.

**Theorem 2: Orthogonal Eigenvectors** Eigenvectors of a real symmetric matrix (when they correspond to different $\lambda$'s) are always perpendicular.

**Theorem 3:** For every symmetric matrices, we have
$$S=Q\Lambda Q^T=\lambda_1q_1q_1^T+...+\lambda_nq_nq_n^T$$

![pic](/images/2020-12/Snipaste_2020-12-17_10-01-03.jpg)

注: 上图中 (**rotation**)(**stretch**)(**rotate back**) 中的 (**stretch**) 会改变向量的方向, 并不是传统意义上的拉伸 (不改变方向), 譬如 $$\Lambda=\begin{bmatrix}
3 & 0\\
0 & 1
\end{bmatrix}\to \Lambda\begin{pmatrix}
x_1 \\ x_2
\end{pmatrix}=\begin{pmatrix}
3x_1 \\ x_2
\end{pmatrix}$$

### 6.4.2 Complex Eigenvalues of Real Matrices

后面个人感觉至少对于 midterm 3 不太重要, 等 final 再看