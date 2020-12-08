---
layout: post
title: Math415 Week-13
categories: Math415
description: Personal Notes
keywords: [Math415，Calculas，Matrix]
mathjax: true
---

# L23
Left and right inverses. Pseudoinverse

## 23.1 Background

**Theorem 1:** Assume $A_{m\times n}$ has independent columns, then $A^TA$ invertible 
- **Proof:** Since $Ax=0$ only when $x=0$, then $x^TA^TAx=0$ only when $x=0$, finally for $A^TAx=0$

**Theorem 2:** The optimal solution $\hat{x}$ of minimizing $\vert\vert Ax-b\vert\vert$ is
$$\hat{x}=(A^TA)^{-1}A^Tb$$

where $\hat x$ is **unique** when $r=n$

## 23.2 Left and right inverse
> #### Def 1: Left inverse $A_{left}^{-1}$
> $$A_{left}^{-1}=(A^TA)^{-1}A^T$$
>
> It is clear that $A_{left}^{-1}A=I$, and $P=AA_{left}^{-1}$ is a **projection matrix** on $C(A)$

This time, we assume $A_{m\times n}$ has independent **rows**, then $AA^T$ invertible 
> #### Def 2: Right inverse $A_{right}^{-1}$
> $$A_{right}^{-1}=A^T(AA^T)^{-1}$$

## 23.3 Pseudoinverse
**Definition:** For $A_{m\times n}=U_{m\times m}\Sigma_{m\times n} V_{n\times n}^T$, assume $m>n$, then we define 
1. $\hat{\Sigma}$, a diagonal matrix, which contains the first $n$ rows of $\Sigma$, s.t.
$$\Sigma_{m\times n}=\begin{bmatrix}
\hat{\Sigma}_{n\times n} \\
0_{(m-n)\times n}
\end{bmatrix}$$
2. $\Sigma^\dagger$, enlarged inverse of $\hat{\Sigma}$, s.t.
$$\Sigma^\dagger_{n\times m}=\begin{bmatrix}
\hat{\Sigma}^{-1}_{n\times n} & 0_{n\times(m-n)}
\end{bmatrix}$$

当然, 上式**假设**的是 $\text{rank}(A)=\min(m,n)=n$, 如果 $r<n$ 则 $\hat\Sigma_{r\times r}$, $\Sigma^\dagger$ 的维度不变, 只是多增加了一些 $0$
> #### Def 3: Pseudoinverse $A^\dagger$
> $$A^\dagger=V\Sigma^\dagger U^T$$

**Lemma 1:**
$$\begin{aligned} A^\dagger u_i&=\begin{cases}
   \frac{1}{\sigma_i}v_i &\text{when } i\leq2 \\
   0 &\text{when } i>2
\end{cases} \\
(A^\dagger)^T v_i&=\begin{cases}
   \frac{1}{\sigma_i}u_i &\text{when } i\leq2 \\
   0 &\text{when } i>2
\end{cases}\end{aligned}$$

上式只要将 $A^\dagger$ 展开计算即可得证

**Lemma 2:** If columns of $A$ are independent, then
$$A^\dagger=A_{left}^{-1}$$

## 23.4 Connection with least square problem
For the problem 
$$\text{Minimize } \|Ax-b\| \text{ over } x\in\mathbb{R}^n$$

when $r<n$, the optimal solution $\hat x$ is **not unique**, we have one of optimal solitions:
$$\hat x=A^\dagger b$$

接下来还有一个例子和一个证明, 篇幅有点长, 日后再补充