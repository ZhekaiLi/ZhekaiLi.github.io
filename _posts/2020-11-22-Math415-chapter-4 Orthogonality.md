---
layout: post
title: Math415 Chapter-4 Orthogonality
categories: Math415
description: Personal Notes
keywords: Math415，Calculas，Matrix
---

# Chapter 4 Orthogonality
## 4.1 Orthogonality of the Four Subspaces

> #### Def 1: Orthogonal subspaces
> $v^T w=0$ for all $v\in V$ and $w\in W$

![pic1](https://github.com/ZhekaiLi/PICTURE-for-markdown/raw/master/Snipaste_2020-10-29_10-16-01.png)

**The nullspace $N(A)$ and the row space $C(A^T)$ are orthogonal subspaces of $\R^n$.** Since $Ax = 0$, that is, every vector $x$ in $N(A)$ is perpendicular to every row of $A$. 

更具体的证明: Let $A^Ty$ be the combination of the basis of $C(A^T)$, $x\in N(A)$, then
$$x\cdot A^Ty=x^T(A^Ty)=(Ax)^Ty=0^Ty=0$$

**The left nullspace $N(A^T)$ and the column space $C(A)$ are orthogonal subspaces of $\R^m$.** 证明同上

![pic2](https://github.com/ZhekaiLi/PICTURE-for-markdown/raw/master/Snipaste_2020-10-29_10-27-54.png)

两个正交空间的交点为零空间 (在二维或者三维空间中的体现就是点 $(0,0)$ 或 $(0,0,0)$)

### 4.1.1 Orthogonal Complements
> #### Def 2: Orthogonal complement
> The orthogonal complement of a subspace $V$ contains every vector that is perpendicular to $V$. This orthogonal subspace is denoted by $V^\perp$

- **Fact 2.1**
若子空间 $A,B\subset \R^n$ 互为正交补，即 $A^\perp=B,B^\perp=A$ 那么 $\text{dim}(A)+\text{dim}(B)=n$

例如，$N(A),C(A^T)$ 正交且互为正交补 $(n-r)+r=n$；但是 $\R^3$ 中的两正交线条不能叫互为正交补 $1+1<3$

![pic3](https://github.com/ZhekaiLi/PICTURE-for-markdown/raw/master/Snipaste_2020-10-29_11-07-20.png)

这里的 $x$ 之所以能被写成 $x_r+x_n$，是因为 $C(A^T),N(A)$ 在 $\mathbb{R}$ 中互为正交补

![pic4](https://github.com/ZhekaiLi/PICTURE-for-markdown/raw/master/Snipaste_2020-10-29_11-10-05.png)

### 4.1.2 Combining Bases from Subspaces

令子空间 $A,B\subset S$，若 $A,B$ 正交，那么可以说子空间 $A, B$ 构成了整个空间 $S$，例如

1. For $A_{m\times n}$, if $C(A^T)\perp N(A)$, then every $x\in\R^n$ can be split into $x_r+x_n$
2. 对于列空间和左零空间同理

## 4.2 Projections

Define
1. initial vector $b$
2. projection $p$
3. projection matrix $P$

![pic5](https://github.com/ZhekaiLi/PICTURE-for-markdown/raw/master/Snipaste_2020-11-01_14-21-17.jpg)

如图，若 $p_1$ 是 $b$ 经 $P_1$ 在 $S$ 上的投影，而 $p_2$ 是 $b$ 经 $P_2$ 在 $S^\perp$ 上的投影，可得
1. $b=p_1+p_2$
2. $P_1+P_2=I$
### 4.2.1 Projection Onto a Line

Define
1. Let $a$ denote a line, $A$ denote a plane
2. error $e=b-p$
3. coefficient $\hat{x}$ that satisfies $p=\hat{x}a$ or $p=A\hat{x}$

计算 $\hat{x}$ 

![pic6](https://github.com/ZhekaiLi/PICTURE-for-markdown/raw/master/Snipaste_2020-11-01_14-34-12.jpg)

式 $p=\hat{x}a=a\hat{x}$ 这里的顺序没有讲究，因为当映射空间的维度为一时 $\hat{x}$ 为标量。再由 $p=Pb$ 可得（下面两式其实是一样的）
$$P_{line}=\frac{aa^T}{a^Ta}, P_{plane}=A(A^TA)^{-1}A^T$$

**Fact 1**
Projection a second time doesn't change any thing: $P=P^2=P^n$

**Fact 2**
When $P$ projects onto one subspace, $I - P$ projects onto the perpendicular subspace.

### 4.2.2 Projection Onto a Subspace

进一步的，对于被投影的子空间 $A_{m\times n}$，以及 $p_{m\times 1},b_{m\times 1},P_{m\times m}$，可得关于 $\hat{x},p,P$ 的表达式 (前提是 $A$ 列满秩，即 $r=n$)

![pic7](https://github.com/ZhekaiLi/PICTURE-for-markdown/raw/master/Snipaste_2020-11-01_14-55-01.jpg)

**Warning** 
对于 $P$ 的表达式，不能把 $(A^TA)^{-1}$ 拆成 $A^{-1}A^{-T}$，因为 $A$ 本身就是不可逆的（如果能拆的话，就会得出 $P=I$，离谱）


**Fact**
![pic8](https://github.com/ZhekaiLi/PICTURE-for-markdown/raw/master/Snipaste_2020-11-01_15-16-56.jpg)

**Proof** 

$A^TAx=0\to x^TA^TAx=0\to(Ax)^T(Ax)=0\to Ax=0$ (反推也成立)

因此 $A^TAx=0\iff Ax=0$，即如果 $N(A)=0$ 那么 $N(A^TA)=0$，又因为 $A^TA$ 为方阵，因此行列均满秩，因此可逆 (同时 $A^TA$ 也是一个对称矩阵)

## 4.3 Least Squares Approximations

对于 $e=b-p=b-Ax$，为了 minimize error，即使得 $e=0$，要想找到 $x$，那么 $Ax=b$ 必须有解。但是对于大部分情况而言，$Ax=b$ 无解（通常由于表达式多于未知数），此时 $||e||>0$

![pic9](https://github.com/ZhekaiLi/PICTURE-for-markdown/raw/master/Snipaste_2020-11-01_16-53-10.jpg)

### 4.3.1 Minimizing the Error

![pic10](https://github.com/ZhekaiLi/PICTURE-for-markdown/raw/master/Snipaste_2020-11-01_19-57-04.jpg)

![pic11](https://github.com/ZhekaiLi/PICTURE-for-markdown/raw/master/Snipaste_2020-11-01_19-58-29.jpg)

以上是从代数的角度来 minimize $e$，如果换成从 calculus 的角度，就相当于求解当偏微分等于 $0$ 时 $x$ 的值，结果是相同的 (见 Math415 Week-07 **L12.1**)

The partial derivatives of $\vert\vert Ax-b\vert\vert^2$ are zero when $A^TA\hat{x}=A^Tb$

### 4.3.2 The Big Picture for Least Squares

当 $Ax=b$ 无解时，big picture 将变为以下形式
为了计算方便，假使 $A$ 的列满秩，因此下图中 $N(A)$ 只有一个点

![pic12](https://github.com/ZhekaiLi/PICTURE-for-markdown/raw/master/Snipaste_2020-11-02_10-08-10.jpg)

### 4.3.3 Fitting a Straight Line

**Example 1**
![pic13](https://github.com/ZhekaiLi/PICTURE-for-markdown/raw/master/Snipaste_2020-11-02_10-16-30.jpg)
![pic14](https://github.com/ZhekaiLi/PICTURE-for-markdown/raw/master/Snipaste_2020-11-02_10-16-40.jpg)

**Example 2**
这个例子说明当 $A$ 的列向量 orthogonal 时，$A^TA$ 会呈现出良好的对角矩阵的形式
![pic15](https://github.com/ZhekaiLi/PICTURE-for-markdown/raw/master/Snipaste_2020-11-02_10-29-50.jpg)


### 4.3.4 Dependent Columns in $A$: What is $\hat{x}$?
略

### 4.3.5 Fitting by a Parabola
没看，感觉和 ppt 的内容没啥关系

## 4.4 Orthonormal Bases and Gram-Schmidt

> #### Def 1: Orthonormal
> The vectors $\bm{q}_1,...,\bm{q}_n$ are **orthonormal** if
$$\bm{q}_i^T\bm{q}_j=\begin{cases}
   0 &\text{when } i\neq j\text{ (orthogonal vectors)} \\
   1 &\text{when } i=j\text{ (unit vectors: }||\bm{q}_i||=1)
\end{cases}$$
A matrix with orthonormal columns is assigned the special letter $\bm{Q}$.

![pic16](https://github.com/ZhekaiLi/PICTURE-for-markdown/raw/master/Snipaste_2020-11-02_10-48-39.jpg)

由于 $Q^{-1}Q=I$，因 $Q^{-1}=Q^T$

> #### Def 2: Orthogonal matrix 正交矩阵
> 满足 transpose = inverse 的矩阵，即 $Q^{-1}=Q^T$，称作正交矩阵

例如，Rotation matrix: $\begin{bmatrix}
   \cos(\theta) & -\sin(\theta) \\
   \sin(\theta) & \cos(\theta)
\end{bmatrix}$， Permutation matrix: $\begin{bmatrix}
   0 & 1 & 0 \\
   0 & 0 & 1 \\
   1 & 0 & 0
\end{bmatrix}$

![pic17](https://github.com/ZhekaiLi/PICTURE-for-markdown/raw/master/Snipaste_2020-11-02_11-07-56.jpg)

### 4.4.1 Projections Using Orthonormal Bases: $Q$ Replaces $A$
![pic18](https://github.com/ZhekaiLi/PICTURE-for-markdown/raw/master/Snipaste_2020-11-02_11-11-08.jpg)

如果 $A$ 本身就是一个 orthonormal matrix，令 $Q=A$，那么就满足
$$p=Q\hat{x}=QQ^Tb$$
更进一步，如果 $Q$ 是一个方阵，那么 $Q^T=Q^{-1}$，此时有
$$p=b,P=I$$

### 4.4.2 The Gram-Schmidt Process

### 4.4.3 The Factorization $A=QR$
![pic19](https://github.com/ZhekaiLi/PICTURE-for-markdown/raw/master/Snipaste_2020-11-24_20-31-47.jpg)

then from $A^TA\hat{x}=A^Tb$, we get

![pic20](https://github.com/ZhekaiLi/PICTURE-for-markdown/raw/master/Snipaste_2020-11-24_20-47-13.jpg)































