---
layout: post
title: Math415 Week-08
categories: Math415
description: Personal Notes
keywords: Math415，Calculas，Matrix
---

# L13 Determinants

**Facts**
1. 不可逆矩阵的行列式等于 $0$
2. For a $2\times 2$ matrix $A$, $\det(A)=|A|=\begin{vmatrix}
   a & b \\
   c & d
\end{vmatrix}=ad-bc$

## 13.1 Definition of the determinant (Big formula)

> #### Def 1: Permutation and $\text{sgn}(\pi)$
> 对数组 $(1, 2, ..., n)$ 进行排列组合，共可以得到 $n!$ 个不同的数组
我们定义 $\text{sgn}(\pi')$ 来表示 $\pi'$ 相较于 $\pi$ 变化的程度
$$\text{sgn}(\pi)=\begin{cases}
   1 &\text{number of permutations is even} \\
   -1 &\text{number of permutations is odd} 
\end{cases}$$
>
>例如, $\text{sgn}([3, 2, 1])=-1,\text{sgn}([3, 1, 2])=1$

> #### Def 2: Determinant
> $$\det(A)=\sum_{\pi}\text{sgn}(\pi)a_{1\pi(1)}a_{2\pi(2)}...a_{n\pi(n)}$$
>
> For $n=2$
we have $\pi_1=[1,2],\pi_2=[2,1], \text{sgn}(\pi_1)=1,\text{sgn}(\pi_2)=-1$, then
$$\begin{aligned}
\det(A)&=\text{sgn}(\pi_1)a_{1\pi_1(1)}a_{2\pi_1(2)}+\text{sgn}(\pi_2)a_{1\pi_2(1)}a_{2\pi_2(2)} \\
&=1\cdot a_{11}a_{22}+(-1)\cdot a_{12}a_{21} \\
&=ad-bc
\end{aligned}$$

**Fact**
Let a permutation matrix $P$ transfers matrix $A$ consisting of **rows** $a_1, ..., a_n$,
into matrix $PA$ with rows ordered as $a_{\pi(1)}, ...., a_{\pi(n)}$, then 
$$\det(P) = \text{sgn}(P)$$

## 13.2 Laplace formula for determinant
这里要用到在 **L14.1** 中定义的 Minor and Cofactor
> #### Def 3: Laplace formula
> $$\det(A)=\sum_{j=1}^n a_{ij}C_{ij}$$

**Example:** When we choose $i=1$
![pic1](https://github.com/ZhekaiLi/PICTURE-for-markdown/raw/master/Snipaste_2020-11-23_18-08-40.jpg)

## 13.3 Properties of determinants

> #### Basic properties of determinant
> 1. For triangular matrix $A_{n\times n}$, $\det(A)=a_{11}a_{22}...a_{nn}$
> 2. $\det(AB)=\det(A)\det(B)$ 
> 3. $\det(A^{-1})=(\det(A))^{-1}$
> 4. $\det(A^T)=\det(A)$

(2, 3, 4 这三点从矩阵行列式的几何属性的角度非常好理解，详见 week2_appendix.md)

> #### Properties related to matrix transformations
> 1. 对矩阵的任意一行、列乘上 $c$，那么其行列式也会变成原先的 $c$ 倍
> 2. 每做一次行、列交换，其行列式就需要变一次号

> #### $\det(A)=0\iff A$ is singular
> 具体表现例如：
> 1. $A$ 的任意一行、一列的所有元素均为 $0$
> 2. $A$ 有两个一样的行或两个一样的列
> 3. $A$ 行或列线性相关, linearly dependent

至于证明当 $A$ 可逆时 $\det(A)\neq 0$，可以由 $PA=LU$ 得到 ($\det(P), \det(L), \det(U)$ 均不为 $0$) 



## 13.4 Pivot formula for determinant
**Theorem 1:** If $A=LU$, then $\det(A)=\det(U)=u_{11}...u_{nn}$
**Theorem 2:** If $PA=LU$,  then $\det(A)=\det(U)/\det(P)=\pm u_{11}...u_{nn}$

## 13.5 Other properties
If we have $$A=\begin{pmatrix}
   a & b \\
   c & d
\end{pmatrix}, B=\begin{pmatrix}
   e & f \\
   c & d
\end{pmatrix},C=\begin{pmatrix}
   a+e & b+f \\
   c & d
\end{pmatrix}$$

then $\det(C)=\det(A)+\det(B)$
# L14
## 14.1 Representation of $A^{-1}$ via cofactors
$$A^{-1}=\frac{1}{|A|}C^{T},C=\{C_{ij}\}^n_{i,j=1}$$

具体证明在 **Def 3** 之后

> #### Def 1: Minor 余子式
> 将 $A_{i,j}$ 的余子式记做 $M_{i,j}$，等于是将第 $i$ 行第 $j$ 列去掉后剩下矩阵的行列式。
例如下图中 $M_{1,1}=5\times9-6\times8=-3$
![pic1](https://github.com/ZhekaiLi/PICTURE-for-markdown/raw/master/Snipaste_2020-11-05_10-41-21.jpg)
进一步可得矩阵 $M_A$
![pic2](https://github.com/ZhekaiLi/PICTURE-for-markdown/raw/master/Snipaste_2020-11-05_10-41-52.jpg)

> #### Def 2: Cofactor
> $$C_{i,j}=(-1)^{i+j}M_{i,j}$$
>
>承接上边的例子，可得 $C$
>![pic3](https://github.com/ZhekaiLi/PICTURE-for-markdown/raw/master/Snipaste_2020-11-06_10-25-31.jpg)

> #### Def 3: Adjugate Matrix 伴随矩阵
>$$adj(A)=C^T \to
A^{-1}=\frac{1}{|A|}adj(A)=\frac{1}{|A|}C^T$$

**Proof**
以三阶矩阵为例
$AC^T=\begin{bmatrix}
   a_{11} & a_{12} & a_{13} \\
   a_{21} & a_{22} & a_{23} \\
   a_{31} & a_{32} & a_{33} 
\end{bmatrix}\begin{bmatrix}
   c_{11} & c_{21} & c_{31} \\
   c_{12} & c_{22} & c_{32} \\
   c_{13} & c_{23} & c_{33} 
\end{bmatrix}$

1. 先看对角线部分，
$$[a_{11}, a_{12}, a_{13}]
\begin{bmatrix}
   c_{11} \\
   c_{12} \\
   c_{13}
\end{bmatrix}=\det(A)$$
2. 再看非对角线部分，例如 $$[a_{21}, a_{22}, a_{23}]
\begin{bmatrix}
   c_{11} \\
   c_{12} \\
   c_{13}
\end{bmatrix}$$ 由于这三个 $c_{1j}$ 为矩阵 $A$ 第二行和第三行的行列式，而 $a_{2j}$ 恰为原矩阵第二行，因此非对角线部分的乘积式就相当于一个两行相同的矩阵的行列式，因此这个式子等于 $0$
3. 由此可得 $AC^T=\vert A\vert$，得证

## 14.2 Cramer's rule
Consider equation $Ax=b$ for invertible $A\in\mathbb{E}^{n\times n}$
$$x=A^{-1}b=\frac{1}{|A|}\beta$$

where, $\beta=C^Tb$

剩下的本课件中有关矩阵特征根、特征值以及特征分解等部分，会结合书本呈现在 Chapter-6.md 中