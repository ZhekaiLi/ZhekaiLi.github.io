---
layout: post
title: TextBook - Introduction to Linear Algebra
categories: Linear-Algebra
description: Personal Notes
keywords: Math415，Linear-Algebra，Matrix
mathjax: true
---
![[Snipaste_2023-05-17_09-37-22 1.png]]

# TextBook: *Introduction to Linear Algebra*

Definde $A$ is an $m\times n$ matrix

# Chapter 3: Vector Spaces and Subspaces
## 3.1 Space of Vectors

### 3.1.1 Vector space 向量空间
向量空间是一个很广义的概念，并不一定指由向量张成的空间（即 $\R^2,...,\R^n,\Complex^n$），还可以是诸如：
1. 零空间 $Z=0$
2. 由 $2\times2$ 的矩阵张成的向量空间 $M$
3. 由多项式张成的向量空间 $F$

## 3.2 The Nullspace of $A$: Solving $Ax=0$ and $Rx=0$
详见 week3.md

## 3.3 The Complete Solution to $Ax=\bf{b}$
Define the augmented matrix $[\;A\;\bf{b}\;]$
do the same elimations for $\bf{b}\to\bf{d}$ as $A\to R$
then we get $[\;R\;\bf{d}\;]$ 
这两个增广矩阵的解集相同

### 3.3.1 One Particular Solution $Ax_p=\bf{b}$

求解 $x_p$：将所有 free columns 对应的 free variables 均设为 $0$, 再求解剩下的 pivots varibales

![pic1](/images/2020/202010100941.JPG)

求解 $x_n$ 的具体过程在 Chapter 3.2 中有详细的介绍，总的来说就是分别将每个 free variable 设为 $1$，其他 free varibales 设为 $0$，再求出对应的 pivots variables 的值（例如下图中一个令 $x_2=1$，另一个令 $x_4=1$）

![pic2](/images/2020/202010100942.JPG)
![pic3](/images/2020/202010100945.JPG)

![pic4](/images/2020/202010101005.JPG)
![pic5](/images/2020/202010101006.JPG)
上图中的第三点和第二点其实在讲同一个东西
![pic6](/images/2020/202010101007.JPG)
![pic7](/images/2020/202010101008.JPG)

$r<m$ means there are $m-r$ zero rows
$r<n$ means there are $n-r$ free columns 

## 3.4 Independence, Basis and Dimension
### 3.4.1 Linear Independence

这块内容比较简单，下面仅给出一些定义
1. The columns of $A$ are linearly independent when the only solution to $A\bf{x}=0$ is $\bf{x}=0$
2. Similar to the sequence of vectors when they are linearly independent
3. Any set of $n$ vectors in $\R^m$ must be linearly dependent if $n > m$

### 3.4.2 Vectors that Span a Subspace

**Definition**:
A set of vectors **span** a space if their linear combinations fill the space (这些向量可以是相互独立的，也可以存在依赖关系)

#### Row Space
![pic8](/images/2020/202010110954.JPG)

### 3.4.3 A Basis of a Vector Space
![pic9](/images/2020/202010111011.JPG)
![pic10](/images/2020/202010111021.JPG)

这里需要注意的是，
1. $C(A)\neq C(R)$, $\text{dimension}(C(A))=\text{dimension}(C(R))$
2. $C(A^T)=C(R^T)$（因为 $R$ 就是由 $A$ 通过行的线性组合所简化而来的）

![pic11](/images/2020/202010111022.JPG)

### 3.4.4 Dimension of a Vector Space
**Theorm 1:** If $v_1, ... , v_m$ and $w_1, ... , w_n$ are both bases for the same vector space $S$, then $m = n$.

**Proof:** let assume $m < n$
Since 
1. $v_1,...,v_m$ are bases of $S$
2. $w_1,...,w_n \in S$

we can use the linear combination of $v_1,...,v_m$ to express $w_i$, such that
$$[w_1,...,w_n]=[v_1,...,v_m]A_{m\times n}$$

For $m\times n$ matrix $A$, since $m < n$, there must exist $x$ satisfying $Ax=0$,
then we can derive $VAx=0\to Wx=0$

Therefore, $W$ are not bases of $S$ when $m < n$. Proof done.

### 3.4.5 Bases for Matrix Spaces and Function Spaces
![pic12](/images/2020/202010111056.JPG)
![pic13](/images/2020/202010111057.JPG)
![pic14](/images/2020/202010111100.JPG)

## 3.5 Dimensions of the Four Subspaces

![pic15](/images/2020/202010111106.JPG)

![pic16](/images/2020/202010111127.JPG)

### 3.5.1 The Four Subspaces for $R$

### 3.5.2 The Four Subspaces for $A$

**在 Section 3.4.3 中，有提到 $C(A^T)=C(R^T)$ (列空间相同)，但 $C(A)\neq C(R)$ (行空间不同)。
当拓展到零空间与左零空间时，相反的，$N(A)=N(R)$ (零空间相同_，但 $N(A^T)\neq N(R^T)$ (左零空间不同)**

![pic17](/images/2020/202010111851.JPG)

上图主要基本表达了关于四个子空间的所有重要的信息，
其中之前没有提及的是
1. $N(A)\perp C(A^T)$, 即零空间与行空间正交
2. $C(A)\perp N(A^T)$, 即列空间与左零空间正交


**Exapmle 1**:
对于 $A=[1\;2\;3]$，$m=1,n=3,r=1$

column space $C(A^T)$: dimension = $r=1$
row space $C(A)$: dimension = $r=1$
null space $N(A)$: dimension = $n-r=2$
null space $N(A^T)$: dimension = $m-r=0$，i.e. $N(A^T)=Z$

### 3.5.2 Rank One Matrix

![pic18](/images/2020/202010111828.JPG)
**Rank Two Matrix = Rank One plus Rank One = $u_1v_1^T+u_2v_2^T$**


## 3.A Textbook Problems 3.1 - 3.3
### 3.A.1
#### 3.A.1.1 True of false

The vectors $b$ that are not in the column space $C(A)$ form a subspace

**False**. There is no zero space. Addition rule sometimes do not satisfy

### 3.A.2 
#### 3.A.2.1 
Construct a matrix for which $N(A)=$ all combinations of $(2,2,1,0)$ and $(3,1,0,1)$

**Ans**: let $B=\begin{bmatrix}
2 & 2 & 1 & 0\\
3 & 1 & 0 & 1
\end{bmatrix}$ then we get $AB^T=0$

therefore $BA^T=0$, so columns of $A^T$ are in $N(B)$. 因此如果 $x_1,x_2$ 为 $Bx=0$ 的 special solutions, 那么 $A$ can be $\begin{bmatrix}
x_1^T\\
x_2^T
\end{bmatrix}$

---

# Chapter 4: Orthogonality
## 4.1 Orthogonality of the Four Subspaces

> #### Def 1: Orthogonal subspaces
> $v^T w=0$ for all $v\in V$ and $w\in W$

![pic1](/images/2020/Snipaste_2020-10-29_10-16-01.png)

**The nullspace $N(A)$ and the row space $C(A^T)$ are orthogonal subspaces of $\R^n$.** Since $Ax = 0$, that is, every vector $x$ in $N(A)$ is perpendicular to every row of $A$. 

更具体的证明: Let $A^Ty$ be the combination of the basis of $C(A^T)$, $x\in N(A)$, then
$$x\cdot A^Ty=x^T(A^Ty)=(Ax)^Ty=0^Ty=0$$

**The left nullspace $N(A^T)$ and the column space $C(A)$ are orthogonal subspaces of $\R^m$.** 证明同上

![pic2](/images/2020/Snipaste_2020-10-29_10-27-54.png)

两个正交空间的交点为零空间 (在二维或者三维空间中的体现就是点 $(0,0)$ 或 $(0,0,0)$)

### 4.1.1 Orthogonal Complements
> #### Def 2: Orthogonal complement
> The orthogonal complement of a subspace $V$ contains every vector that is perpendicular to $V$. This orthogonal subspace is denoted by $V^\perp$

- **Fact 2.1**
若子空间 $A,B\subset \R^n$ 互为正交补，即 $A^\perp=B,B^\perp=A$ 那么 $\text{dim}(A)+\text{dim}(B)=n$

例如，$N(A),C(A^T)$ 正交且互为正交补 $(n-r)+r=n$；但是 $\R^3$ 中的两正交线条不能叫互为正交补 $1+1<3$

![pic3](/images/2020/Snipaste_2020-10-29_11-07-20.png)

这里的 $x$ 之所以能被写成 $x_r+x_n$，是因为 $C(A^T),N(A)$ 在 $\mathbb{R}$ 中互为正交补

### 4.1.2 Combining Bases from Subspaces

令子空间 $A,B\subset S$，若 $A,B$ 正交，那么可以说子空间 $A, B$ 构成了整个空间 $S$，例如

1. For $A_{m\times n}$, if $C(A^T)\perp N(A)$, then every $x\in\R^n$ can be split into $x_r+x_n$
2. 对于列空间和左零空间同理

## 4.2 Projections

> #### Define
>1. initial vector $b$
>2. projection $p$
>3. projection matrix $P$
>
> 通过计算 $A^2$ 是否等于 $A$ 来判断该矩阵是否可以是 projection matrix 

![pic5](/images/2020/Snipaste_2020-11-01_14-21-17.jpg)

如图，若 $p_1$ 是 $b$ 经 $P_1$ 在 $S$ 上的投影，而 $p_2$ 是 $b$ 经 $P_2$ 在 $S^\perp$ 上的投影，可得
1. $b=p_1+p_2$
2. $P_1+P_2=I$
### 4.2.1 Projection Onto a Line

>#### Define
>1. Let $a$ denote a line, $A$ denote a plane
>2. error $e=b-p$
>3. coefficient $\hat{x}$ that satisfies $p=\hat{x}a$ or $p=A\hat{x}$

计算 $\hat{x}$

![pic6](/images/2020/Snipaste_2020-11-01_14-34-12.jpg)

这里的 $\hat{x}$ 为系数，类似于 [Math415 Week-05](https://zhekaili.github.io/2020/11/22/Math415-slides-week-05/) 中 L8.2.1 的 $c,d$, 因此当映射空间的维度为 $1$ 时, $p=\hat{x}a=a\hat{x}$。再由 $p=Pb$ 可得（下面两式其实是一样的）
$$P_{line}=\frac{aa^T}{a^Ta}, P_{plane}=A(A^TA)^{-1}A^T$$

**Fact 1**
Projection a second time doesn't change any thing: $P=P^2=P^n$

**Fact 2**
When $P$ projects onto one subspace, $I - P$ projects onto the perpendicular subspace.

### 4.2.2 Projection Onto a Subspace

进一步的，对于被投影的子空间 $A_{m\times n}$，以及 $p_{m\times 1},b_{m\times 1},P_{m\times m}$，可得关于 $\hat{x},p,P$ 的表达式 (前提是 $A$ 列满秩，即 $r=n$)

![pic7](/images/2020/Snipaste_2020-11-01_14-55-01.jpg)

**Warning** 
对于 $P$ 的表达式，不能把 $(A^TA)^{-1}$ 拆成 $A^{-1}A^{-T}$，因为 $A$ 本身就是不可逆的（如果能拆的话，就会得出 $P=I$，离谱）


**Fact**
![pic8](/images/2020/Snipaste_2020-11-01_15-16-56.jpg)

- **Proof** 
$$A^TAx=0\to x^TA^TAx=0\to(Ax)^T(Ax)=0\to Ax=0$$ 
(反推也成立) 因此 $A^TAx=0\iff Ax=0$，即如果 $N(A)=0$ 那么 $N(A^TA)=0$，又因为 $A^TA$ 为方阵，因此行列均满秩，因此可逆 (同时 $A^TA$ 也是一个对称矩阵)

## 4.3 Least Squares Approximations

对于 $e=b-p=b-Ax$，为了 minimize error，即使得 $e=0$，要想找到 $x$，那么 $Ax=b$ 必须有解。但是对于大部分情况而言，$Ax=b$ 无解（通常由于表达式多于未知数），此时 $\|e\|>0$

![pic9](/images/2020/Snipaste_2020-11-01_16-53-10.jpg)

### 4.3.1 Minimizing the Error

![pic10](/images/2020/Snipaste_2020-11-01_19-57-04.jpg)

![pic11](/images/2020/Snipaste_2020-11-01_19-58-29.jpg)

以上是从代数的角度来 minimize $e$，如果换成从 calculus 的角度，就相当于求解当偏微分等于 $0$ 时 $x$ 的值，结果是相同的 (见 Math415 Week-07 **L12.1**)

The partial derivatives of $\vert\vert Ax-b\vert\vert^2$ are zero when $A^TA\hat{x}=A^Tb$

### 4.3.2 The Big Picture for Least Squares

当 $Ax=b$ 无解时，big picture 将变为以下形式
为了计算方便，假使 $A$ 的列满秩，因此下图中 $N(A)$ 只有一个点

![pic12](/images/2020/Snipaste_2020-11-02_10-08-10.jpg)

### 4.3.3 Fitting a Straight Line

**Example 1**
![pic13](/images/2020/Snipaste_2020-11-02_10-16-30.jpg)
![pic14](/images/2020/Snipaste_2020-11-02_10-16-40.jpg)

**Example 2**
这个例子说明当 $A$ 的列向量 orthogonal 时，$A^TA$ 会呈现出良好的对角矩阵的形式
![pic15](/images/2020/Snipaste_2020-11-02_10-29-50.jpg)


### 4.3.4 Dependent Columns in $A$: What is $\hat{x}$?
略

### 4.3.5 Fitting by a Parabola
没看，感觉和 ppt 的内容没啥关系

## 4.4 Orthonormal Bases and Gram-Schmidt

> #### Def 1: Orthonormal
> The vectors $\bf{q}_1,...,\bf{q}_n$ are **orthonormal** if
$$\bf{q}_i^T\bf{q}_j=\begin{cases}
   0 &\text{when } i\neq j\text{ (orthogonal vectors)} \\
   1 &\text{when } i=j\text{ (unit vectors: }\|\bf{q}_i\|=1)
\end{cases}$$
A matrix with orthonormal columns is assigned the special letter $\bf{Q}$.

![pic16](/images/2020/Snipaste_2020-11-02_10-48-39.jpg)

由于 $Q^{-1}Q=I$，因 $Q^{-1}=Q^T$ (这些是当 $Q$ 为**方阵**的时候才满足的性质，再比如 $QQ^T=Q^TQ=I$)

> #### Def 2: Orthogonal matrix 正交矩阵
> 满足 transpose = inverse 的矩阵，即 $Q^{-1}=Q^T$，称作正交矩阵 (正交矩阵一定是方阵)

例如，Rotation matrix: $\begin{bmatrix}
   \cos(\theta) & -\sin(\theta) \\
   \sin(\theta) & \cos(\theta)
\end{bmatrix}$， Permutation matrix: $\begin{bmatrix}
   0 & 1 & 0 \\
   0 & 0 & 1 \\
   1 & 0 & 0
\end{bmatrix}$

![pic17](/images/2020/Snipaste_2020-11-02_11-07-56.jpg)

### 4.4.1 Projections Using Orthonormal Bases: $Q$ Replaces $A$
![pic18](/images/2020/Snipaste_2020-11-02_11-11-08.jpg)

如果 $A$ 本身就是一个 orthonormal matrix，令 $Q=A$，那么就满足
$$p=Q\hat{x}=QQ^Tb$$
更进一步，如果 $Q$ 是一个方阵，那么 $Q^T=Q^{-1}$，此时有
$$p=b,P=I$$

### 4.4.2 The Gram-Schmidt Process

### 4.4.3 The Factorization $A=QR$
![pic19](/images/2020/Snipaste_2020-11-24_20-31-47.jpg)

then from $A^TA\hat{x}=A^Tb$, we get

![pic20](/images/2020/Snipaste_2020-11-24_20-47-13.jpg)

---

# Chapter 06: Eigenvalues and Eigenvectors
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

---

# Chapter 09-10 FFT and Graph

## 9.3 The Fast Fourier Transform (FFT)
For the equation $z^n=1$, the solutions $z$ are the "$n$th roots of unity", which are evenly spaced points around the unit circle in the complex plane. For example, when $n=8,z^8=1$
![pic](/images/2020-12/Snipaste_2020-12-10_10-29-46.jpg)

> #### Def 1: Fourier matrix
> Fourier matrix with $n=4,w=e^{2\pi i/4}=i$
$$F=\begin{bmatrix}
1 & 1 & 1 & 1 \\
1 & w & w^2 & w^3 \\
1 & w^2 & w^4 & w^6 \\
1 & w^3 & w^6 & w^9 \\
\end{bmatrix}=\begin{bmatrix}
1 & 1 & 1 & 1 \\
1 & i & i^2 & i^3 \\
1 & i^2 & i^4 & i^6 \\
1 & i^3 & i^6 & i^9 \\
\end{bmatrix}$$

**Fact 1:** $\frac{1}{\sqrt n}F$ is a **unitary matrix**, since
$$(\frac{1}{\sqrt n}F^H)(\frac{1}{\sqrt n}F)=I$$

**Fact 2:** From $F^HF=nI$, we have
$$F^{-1}=\frac{1}{n}F^H=\frac{1}{n}\overline F$$

> #### Def 2: Fourier series
> Fourier series with $n=4$, we have
$$y_j=\sum_{k=0}^3 c_ke^{ikx}, x=2\pi j/4$$
>
> $$\begin{bmatrix}
y_0 \\
y_1 \\
y_2 \\
y_3 \\
\end{bmatrix}=Fc=\begin{bmatrix}
1 & 1 & 1 & 1 \\
1 & w & w^2 & w^3 \\
1 & w^2 & w^4 & w^6 \\
1 & w^3 & w^6 & w^9 \\
\end{bmatrix}\begin{bmatrix}
c_0 \\
c_1 \\
c_2 \\
c_3 \\
\end{bmatrix}$$

## 10.1 Graphs and Networks
### 10.1.1 The Incidence Matrix

The incidence matrix of a graph，即图的**关联矩阵**，能够表示图中节点之间是如何连接的

对于一个 $m\times n$ 的关联矩阵 $A$
1. $n$ 列表示有 $n$ 个节点
2. $m$ 行表示有 $m$ 条连接线
3. $\text{rank}(A)=n-1$
$$a_{ij}=\begin{cases}
   -1 &\text{then 节点 j 为连接线 i 的起点}\\
   0 &\text{then 节点 j 与连接线 i 无关}\\
   1 &\text{then 节点 j 为连接线 i 的终点}\\
\end{cases}$$

例如
![pic1](/images/2020/202010231651.JPG)

**$m,n$ 之间的关系**
1. $m_{max}=\frac{1}{2}n(n-1)$
2. $m_{min}=n-1$

**Elimination reduce any graph to a tree**

Rows are dependent when edges form a loop. Independent 
rows come from trees.