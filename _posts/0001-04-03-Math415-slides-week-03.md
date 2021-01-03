---
layout: post
title: Math415 Week-03
categories: Math415
description: Personal Notes
keywords: Math415，Calculas，Matrix
---
**ATTENSION - If some LeTeX equations could not show well, pleae try to refresh this page.**

# L5 Vector spaces: Subspaces
In this lecture, we consider vector spaces over the field $E$ ($E=\R\text{ or }\Complex$)


## 5.1 Subspace
Let $X$ be a vector space, and $Y\subset X$. We say that $Y$ is a subspace of $X$ if **$Y$ is closed to addition and multiplication on scalars** ($Y$ 对加法和乘法封闭)
$$\text{If }\begin{cases}
   x,y\in Y &\text{then } x+y\in Y \\
   \alpha\in E,x\in Y &\text{then } \alpha x\in Y
\end{cases}$$

#### Fact

Any subspace contains **zero space**

#### Example
1. $Y$ is not a subspace of $X$ if $X=E=\Complex,Y=\{x\in X:\text{Im}(x)=0\}$
Since when $x=1\in Y,i*x\notin Y$
2. 三维空间中的一个**经过 $(0, 0, 0)$ 点**平面是 $\R^3$ 的子空间（注意！该平面并不是 $\R^2$，尽管看起来很像）

#### Lemma
1. For any two subspaces $Y,Z$ of a vector space $X$, $Y\cap Z$ is also a subspace of $X$
**proof:** let 

$$\begin{aligned}
&y,z\in Y\cap Z \\
&\to y\in Y, y\in Z, z\in Y, z\in Z \\
&\to y+z\in Y,y+z\in Z \\
&\to y+z\in Y\cap Z\end{aligned}$$

2. $Y-Z$ is also a subspace of $X$
证明类似
3. $Y\cup Z$ is **not** a subspace of $X$
例如 $Y=\{(0,\R)\},Z=\{(\R,0)\}\to Y\cup Z=\{(x,y)|xy=0\}$，但是 $(1,1)=(1,0)+(0,1)$ 并不在其中

## 5.2 Span
Let $X$ be a vector space, and $S\subset X$. Define the **span of $S$** as the set of all linear combinations of vectors from $S$ (denote: $\text{span}(S)$)

#### Lemma
For any set $S\subset X$, $Y=\text{span}(S)$ is a subspace of $X$

#### Example
Let $p,q\in\R^2$. What is the span of $S=\{p,q\}$?

Let $p=\begin{pmatrix}
   p_1 \\ p_2
\end{pmatrix},q=\begin{pmatrix}
   q_1 \\ q_2
\end{pmatrix}$, then $y=\alpha_1 p + \alpha_2 q=\begin{pmatrix}
   p_1 & q_1 \\ 
   p_2 & q_2
\end{pmatrix}\begin{pmatrix}
   \alpha_1 \\ \alpha_2
\end{pmatrix}$
Therefore if $p_1q_2\neq p_2q_1$, then $\text{span}(S)=\R^2$
## 5.3 Column space: $C(A)$
Define $A$ is a $m\times n$ matrix

Column space $C(A)$ consists of all linear combinations of the columns, $C(A)=\text{span}\{a_i\}$ is a subspace of $\R^m$

Solving $Ax=b$ 即用列的组合去表示 $b$。因此，$Ax=b$ is solvable iff $b\in C(A)$

**Theorem**
For matrix $A\in E^{n\times n}$, the following three statements are equivalent
1. $A$ 可逆
2. $N(A)=\{0\}$
3. $C(A)=E^n$

## 5.4 Null space: $N(A)$
Define $A$ is a $m\times n$ matrix

### 5.4.1 Def
$N(A)$ consists of all solutions to $Ax= 0$, where $x\in \R^n$, $N(A)$ is a subspace of $\R^n$（注意！此处的**维度与 $C(A)$ 不同**）

**Example**
When $A=[1\;2\;3]$, $N(A)$ 即为垂直于向量 $(1,2,3)$ 的平面

### 5.4.2 Special solution
![pic1](https://github.com/ZhekaiLi/PICTURE-for-markdown/raw/master/202010091502.JPG)

**如何求得 special solutions?**
1. 首先通过高斯消元找到 pivot columns & free columns ![pic2](https://github.com/ZhekaiLi/PICTURE-for-markdown/raw/master/202010091512.JPG)
2. 有几个 free columns 就有几个 special solutioins
$C$ 包含两个，因此设 $s_1=\begin{pmatrix}
   a_1 \\
   b_1 \\
   1 \\
   0
\end{pmatrix},s_2=\begin{pmatrix}
   a_2 \\
   b_2 \\
   0 \\
   1
\end{pmatrix}$
即分别将一个 free column 的值设为 $1$，其他 free columns 的值设为 $0$，分别代入 $Us=0$ 求 $a_1,...,a_n,b_1,...,b_n,...$，最后可得 
![pic3](https://github.com/ZhekaiLi/PICTURE-for-markdown/raw/master/202010091513.JPG)


### 5.4.3 The Reduced Row Echelon Form: $R$
将矩阵 $U$ 进一步进行如下消元得到矩阵 $R$
1. Use pivot rows to eliminate upward in $R$
2. Divide the whole pivot row by its pivot，即让 pivit = 1

记做 $R=\text{reff}(A)$，满足
$$N(A)=N(U)=N(R)$$

![pic4](https://github.com/ZhekaiLi/PICTURE-for-markdown/raw/master/202010091612.JPG)

![pic5](https://github.com/ZhekaiLi/PICTURE-for-markdown/raw/master/202010091614.JPG)

$C(A)$ consists of all vectors of the form $(b_1,b_2,b_3,0)$


# L6 Solution of equation $Ax=\bm{b}$


## 6.1 Linear manifolds
A linear manifold is a linear subspace that has possibly been shifted away from the origin. 
$$\text{Let }X\text{ be a vector space},\;a\in X,\;Y\text{ is a subspace of }X
\newline
\text{Then }a+Y\text{ is a linear manifold}$$

例如在 $\R^2$ 空间中，linear manifolds 可以是点、线或者 $\R^2$ 自身

其他部分详见 Chapter3
























