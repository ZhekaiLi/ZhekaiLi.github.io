---
layout: post
title: Math415 Week-12
categories: Math415
description: Personal Notes
keywords: Math415，Calculas，Matrix
mathjax: true
---

# L21
Geometry of SVD. Principal component analysis (PCA).
## 21.1 Geometry of SVD
> #### Def 1: Geometry of SVD
> For SVD
$$A=U\Sigma V^T$$
>
>where
> 1. $U_{m\times m},V_{n\times n}$ is orthogonal matrix, and therefore could be considered as **rotation matrix**
> 2. Let $r=\min({m,n})$, then $\Sigma_{m\times n}$ contains an $r\times r$ diagonal matrix with all other elements equal to $0$. Therefore, we can consider it as an **streching matrix** 

**Ex 1:**
Let $m=3,n=2$, then $A_{3\times 2}=U_{3\times 3}\Sigma_{3\times 2} V_{2\times 2}^T$. 此时线性变换矩阵 $A$ 相当于做了如下操作
1. 将 $x$ 在 $\mathbb{R}^2$ 空间内做一个旋转变换
$$V^Tx=x_A:(x_1,x_2)\to(x_1',x_2')$$
2. 将旋转后的 $x$ 进行伸缩变换，并添加一个新的维度
$$\Sigma x_A=x_B:(x_1',x_2')\to (\sigma_1x_1',\sigma_2x_2',0)$$ 
3. 近似于步骤 1，不过此时是在 $\mathbb{R}^3$ 空间内的旋转
$$Ux_B=x_C:(\sigma_1x_1',\sigma_2x_2',0)\to (x_1'',x_2'',x_3'')$$

## 21.2 Matrix norm
**Presume:** SVD is selected that $\sigma_1\geq\sigma_2\geq...$
#### Def 2: Euclidean norm of matrix
> If $A=U\Sigma V^T$, then
$$\|A\|=\max\vert A_{ij}\vert=\max\|Ax\|=\sigma_1,\;\|x\|\leq 1$$
- **Proof:** 
1. Let $\vert\vert x\vert\vert=1$, then
$$\begin{aligned}
\|Ax\|^2&=x^TA^TAx=x^TV\Sigma^TU^TU\Sigma V^Tx \\
&=y^T\Sigma^T\Sigma y=\sum\sigma_i^2y_i^2
\end{aligned}$$
where, $y=V^Tx$, and $y^Ty=x^Tx=1$ 
2. Since $\sigma_1\geq\sigma_2\geq...$, to maximize $\vert\vert Ax\vert\vert^2$, $y$ should equal to $(1,0,0,...)^T$

**Theorem**
$$\begin{aligned}
\sigma_2&=\|A-\sigma_1u_1v_1^T\| \\
\sigma_3&=\|A-\sigma_1u_1v_1^T-\sigma_2u_2v_2^T\| \\
...
\end{aligned}$$

## 21.3 PCA: Principle Concepts Analysis
samples, mean, variance 就不提了
> #### Def 3: Covariance and Correlation
> $$\begin{aligned}
c_{XY}&=\frac{1}{m-1}\sum_{i=1}^m(X_i-\mu_X)(Y_i-\mu_Y) \\
\rho_{XY}&=\frac{c_{XY}}{\sqrt{S^2_XS^2_Y}}
\end{aligned}$$
> 相关系数 (Correlation) 体现了两个样本集之间的关联度
> $$\rho\begin{cases} >0 \text{ positive correlation: }X_i>\mu_X\to\text{more chance that } Y_i>mu_i \\
< 0 \text{ negative correlation: }X_i>\mu_X\to\text{more chance that } Y_i<mu_i \\
= 0 \text{ no correlation}
\end{cases}$$

For vector samples
$$X_{m\times n}=\begin{pmatrix}
x_1^T \\
x_2^T \\
... \\
x_m^T
\end{pmatrix}\to C_X=\begin{pmatrix}
S_{x_1}^2 & c_{x_1,x_2} & ... & c_{x_1,x_m} \\
c_{x_2,x_1} & S_{x_2}^2 & ... & c_{x_1,x_m} \\
... & ... & ... & ... \\
c_{x_m,x_1} & ... & ... & S_{x_m}^2
\end{pmatrix}$$

**Theorem:** 将数据**归一化**，可以极大减少运算量，例如
$$X_{m\times n}=\begin{pmatrix}
x_1^T - \mu_{x_1} \\
x_2^T - \mu_{x_2} \\
... \\
x_m^T - \mu_{x_m}
\end{pmatrix}\to C_x=\frac{1}{m-1}XX^T$$