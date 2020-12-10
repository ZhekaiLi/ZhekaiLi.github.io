---
layout: post
title: Math415 Week-11
categories: Math415
description: Personal Notes
keywords: Math415，Calculas，Matrix
mathjax: true
---
**ATTENSION - If some LeTeX equations could not show well, pleae try to refresh this page.**

# L19
Midterm-2 Review

# L20
## 20.1 Singular value decomposition
> #### Def 1: Singular value decomposition
> Having $A_{m\times n},\Sigma_{m\times n},U_{m\times m},V_{n\times n}$
> $$A=U\Sigma V^T$$
>
> where, 
>1. $\Sigma$ 所有元素均非负，且对角线上的元素非零
>2. $U_{m\times m},V_{n\times n}$ are orthonormal matrices

- **Rule:**
We will presume that SVD is selected s.t. $\sigma_1\geq\sigma_2\geq...\geq0$, where $\sigma_i$ is the diagonal elements of $\Sigma$, and is called **singular value**
- $A=\sigma_1u_1v_1^T+\sigma_2u_2v_2^T+...+\sigma_ru_rv_r^T$, where $r$ is the number of nonzero $\sigma_i$

**Theorem 1:** Any matrix allows SVD

**Lemma 1:** Let $A=U\Sigma V^T$ be SVD for $A$, and let $r$ be such that
$$\sigma_k=\begin{cases}
\neq0 &\text{when }k=1,...,r \\
=0 &\text{when }k>r
\end{cases}$$
Then $U=(u_1,...,u_m)$ and $V=(v_1,...,v_n)$, where $u_k, v_k$ are orthonormal eigenvectors of $AA^T$ and $A^TA$ such that
$$AA^Tu_i=\sigma_i^2u_i,\;A^TAv_i=\sigma_i^2v_i,\;i=1,...,r$$

- **Proof:**
$$AA^T=U\Sigma V^T(U\Sigma V^T)^T=U\Sigma\Sigma^TU^T$$
then 两边同乘 $u_i$，化简后即可得证

**Lemma 2:**
$$Av_i=\sigma_iu_i,\;A^Tu_i=\sigma_iv_i,\;i=1,...,r$$
- **Proof:**
Since $V$ is orthonormal matrix, then $V^T=V^{-1}$. Therefore
$$\begin{aligned}
A&=U\Sigma V^T=U\Sigma V^{-1}\to AV=U\Sigma \\
A&=U\Sigma V^T\to U^TA=\Sigma V^T\to A^TU=V\Sigma
\end{aligned}$$

## 20.2 $A$'s for subspaces
> #### Four subspaces
> $\text{rank}(A)=4$
> - $C(A)=\text{span}\lbrace u_1,...,u_r\rbrace$
> - $N(A)=\text{span}\lbrace v_{r+1},...,v_n\rbrace$
> - $C(A^T)=\text{span}\lbrace v_1,...,v_r\rbrace$
> - $N(A)=\text{span}\lbrace u_{r+1},...,u_m\rbrace$





















