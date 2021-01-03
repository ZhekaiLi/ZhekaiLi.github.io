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
**Attention:**
1. 定义 $m$ 为样本数
2. 定义 $n$ 为样本所包含的特征数

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
> #### Def 2: Euclidean norm of matrix
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
c_{xy}&=\frac{1}{n-1}\sum_{i=1}^n(x_i-\mu_x)(y_i-\mu_y) \\
\rho_{xy}&=\frac{c_{xy}}{\sqrt{S^2_xS^2_y}}
\end{aligned}$$
> 相关系数 (Correlation) 体现了两个样本集之间的关联度
> $$\rho\begin{cases} >0 \text{ positive correlation: }x_i>\mu_x\to\text{more chance that } y_i>\mu_y \\
< 0 \text{ negative correlation: }x_i>\mu_x\to\text{more chance that } y_i<\mu_y \\
= 0 \text{ no correlation}
\end{cases}$$

For vector samples
$$X_{m\times n}=\begin{pmatrix}
x_1^T \\
x_2^T \\
... \\
x_m^T
\end{pmatrix}=\begin{pmatrix}
x_{11} & x_{12} & ... & x_{1n} \\
x_{21} & x_{22} & ... & x_{2n} \\
... & ... & ... & ... \\
x_{m1} & x_{m2} & ... & x_{mn}
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
\end{pmatrix}\to C_X=\frac{1}{m-1}XX^T$$

# L22
Principal component analysis (PCA). Change of basis

From last lecture, we get the matrix $X_{m\times n}$ and $C_X$, now lets focus on $XX^T$
> #### Def 1: SVD of $XX^T$
> $$XX^T=U\Sigma U^T$$
> 
> Define $Y=U^TX$, then we get
> $$\begin{aligned}(n-1)C_Y&=YY^T=U^TXX^TU=\Sigma \\
C_Y&=\frac{1}{n-1}\Sigma \text{ (对角矩阵)} \\
S^2_{Y_k}&=\frac{\sigma_k^2}{n-1}\;(Y_k\text{ 的样本方差})
\end{aligned}$$ 

> #### Def 2: PVE (percentage of variance explained)
> $$\text{PVE for component }k=\frac{S^2_{Y_k}}{\sum_{i=1}^mS^2_{Y_i}}$$

> #### Def 3: Idea of PCA
> 保留特征值较大的特征，去除小的，详见如下示例

**Example:**
假设对于一个 $2\times n$ 的数据，满足以下特征
$$\begin{aligned}(n-1)C_X&=XX^T=U\Sigma U^T,u_1=\begin{pmatrix}
0.6 \\
0.8
\end{pmatrix},u_2=\begin{pmatrix}
-0.8 \\
0.6
\end{pmatrix} \\
\Sigma&=\begin{pmatrix}
\sigma_1^2 & 0 \\
0 & \sigma_2^2
\end{pmatrix} = \begin{pmatrix}
57 & 0 \\
0 & 3
\end{pmatrix}
\end{aligned}$$

Since $57 >> 3$, 去除第二个特征，因此
$$Y=U^TX=\begin{pmatrix}
u_1^TX \\
u_2^TX
\end{pmatrix}\to\bar{Y}=\begin{pmatrix}
u_1^TX \\
0
\end{pmatrix}=0.6x_1+0.8x_2$$
## 22.1 Basis changes
> #### Def 4: Orthonormal matrices in $\mathbb{C}^{n\times n}$
> Remind that we defined 共轭转置 as $x^*=\overline{(x^T)}=(\overline{x})^T$, and $\vert\vert x\vert\vert=(x^*x)^{1/2}=(\sum \overline{x_i}x_i)^{1/2}$. Then for orthonormal matrices $Q\in\mathbb{C}^{n\times n}$,
$$Q^*=Q^{-1},Q^*Q=QQ^*=I$$

**Lemma 1:** Let $x_1,...,x_n$ be a basis in X, $B$ be an invertible matrix, then $Bx_1,...,Bx_n$ is also a basis in $X$

**Lemma 2:** Let $x_1,...,x_n$ be an **orthonormal** basis in X, $Q$ be an orthogonal matrix, then $Qx_1,...,Qx_n$ is also an orthonormal basis in $X$

> #### Def 5: Change of basis: new coordinates
> In vector space $X$, define two basis, $U=\lbrace u_i\rbrace,W=\lbrace w_i\rbrace$, then denote
$$[v]_U=
\begin{pmatrix}
c_1 \\
... \\
c_n
\end{pmatrix},[v]_W=
\begin{pmatrix}
d_1 \\
... \\
d_n
\end{pmatrix},i.e.\;v=c_1u_1+...+c_nu_n
$$
>
> Also, denote transform matrix $A=\lbrace a_{ij}\rbrace$, such that
$$\begin{aligned}
u_1&= a_{11}w_1+...+a_{n1}w_n \\
... \\
u_n&=a_{1n}w_1+...+a_{nn}w_n
\end{aligned}$$
>
> then we can find that
$$[v]_W=A[v]_U\text{ or }d=Ac$$
>
> That $A$ can be called as $A_{U\to W}$, we can alos find $A_{W\to U}$ similarly, such that
$$\begin{aligned}
[v]_W&=A_{U\to W}[v]_U \\
[v]_U&=A_{W\to U}[v]_W \\
A_{U\to W}&= ([u_1]_W,...,[u_n]_W) \\
A_{W\to U}&= ([w_1]_U,...,[w_n]_U) \\
I&=A_{U\to W}A_{W\to U}
\end{aligned}$$ 

后面还差一页没有理