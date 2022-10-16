---
layout: post
title: Math415 Week 11-14
categories: Linear-Algebra
description: Personal Notes
keywords: Math415，Linear-Algebra，Matrix
mathjax: true
---
-

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
> - norm: $\|x\|=\sqrt{x\cdot x}=\sqrt{\sum x_i^2}$
> 2. 对于复数向量 $x,y\in\mathbb{C}^n$
> - dot product: $x\cdot y=x^T\overline{y}=\sum x_i\overline{y_i}$ 
> - norm: $\|x\|=\sqrt{x\cdot \overline{x}}$

> #### Def 3: Symmetric matrices
> 对称矩阵 $A\in\mathbb{R}^{n\times n}$ 具有如下性质
> 1. 特征根均为实数
> 2. diagonalizable 可对角化的，即其 Jordan form 为对角矩阵
> 3. 对应不同特征根的特征向量互相正交

# L18
Positive definite matrices and quadratic forms

(已看完)

## 18.1 正定矩阵

**首先要明确定义, 正定矩阵的"正"体现在其特征值都是正数.**

**其次要知晓前提, 即必须是一个对称矩阵**

> #### Def 1: Positive definite matrices (eigenvalues base)
> A **symmetric matrix** $A\in\mathbb{C}^{n\times n}$ is said to be positive definite if all its **eigenvalues are positive**

> #### Def 2: Energy base definition
> $x^TAx$ is interpreted as "energy of $x$", 正定就意味着对于任意 $x\in\mathbb{R}^n,x\neq 0$, 都有 $x^TAx > 0$ 

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

当然, 上式**假设**的是 $\text{rank}(A)=\min(m,n)=n$, 如果 $r<n$ 则 $\hat\Sigma_{n\times n}$ 将缩小成 $\hat\Sigma_{r\times r}$, 而 $\Sigma^\dagger$ 的维度保持不变, 只是多增加了一些 $0$
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

when $r<n$, $A^{-1}$ does not exist, and the optimal solution $\hat x$ is **not unique**, we have one of optimal solitions:
$$\hat x=A^\dagger b$$

接下来还有一个例子和一个证明, 篇幅有点长, 日后再补充

# L24
Complex matrices. Discrete Fourier transform
## 24.1 Complex vectors and matrices 
> #### Def 1: Conjugate transpose 共轭转置 (in L19)
> 又称 Hermitian transpose
$$A^*=(\overline{A})^T=\overline{(A^T)}$$
>
>又记做 $A^H,A^\dagger$

> #### Def 2: Unitary matrices
> Orthogonal matrix: 
$$Q\in\mathbb{R}^{n\times n}:Q^TQ=I,Q^{-1}=Q^T$$
> 
> Unitary matrix:
$$Q\in\mathbb{C}^{n\times n}:Q^*Q=I,Q^{-1}=Q^*$$

## 24.2 Fourier transform and its discretization
> #### Def 3: Fourier transform of $x(t)$ 时域转频域
> $$X(w)=\int_{-\infty}^\infty x(t)e^{-iwt}dt$$
> #### Inverse of Fourier transform for $X(w)$ 频域转时域
> $$x(t)=\frac{1}{2\pi}\int_{-\infty}^\infty X(w)e^{iwt}dw$$

**Theorem 1:**
If function $X(w)$ is piecewise constant, we can rewrite $x(t)$ as
$$x(t)=\frac{1}{2\pi}\sum X(k)e^{ikt}$$

where, $e^{ikt}=\cos(kt)+i\sin(kt)$

**Theorem 2:** If assume $x(t)=0$ when $t\in(-\infty,0)\cup (n,\infty)$, and funcion $x(t)$ is constant on invervals $[k,k+1)$, then
$$X(w)=\int_{0}^n x(t)e^{-iwt}dt=\sum_{k=0}^{n-1}x(k)e^{-iwk}$$

# L25

Review: Topics included in midterm 3

## 25.1 Matrix exponents

见 [Chapter 6.3](https://zhekaili.github.io/0001/01/06/Math415-chapter-06-Eigenvalues-and-Eigenvectors/#63-systems-of-differential-equations)

## 25.2 Symmetric matrices

见 [Chapter 6.4](https://zhekaili.github.io/0001/01/06/Math415-chapter-06-Eigenvalues-and-Eigenvectors/#64-symmetric-matrices)

## 25.3 Quadratic forms

见 [Week-10 L18](https://zhekaili.github.io/0001/04/10/Math415-slides-week-10/#l18)

## 25.4 Least square problems

见 [Week-13 L23.4](https://zhekaili.github.io/0001/04/13/Math415-slides-week-13/#234-connection-with-least-square-problem)

## 25.5 SVD, left and right inverse, pseudoinverse

1. SVD 就不多说了
2. left and right inverse 见 [Week-13 L23.2](https://zhekaili.github.io/0001/04/13/Math415-slides-week-13/#232-left-and-right-inverse)
3. pseudoinverse 见 [Week-13 L23.3](https://zhekaili.github.io/0001/04/13/Math415-slides-week-13/#233-pseudoinverse)

# L26

Final review



















