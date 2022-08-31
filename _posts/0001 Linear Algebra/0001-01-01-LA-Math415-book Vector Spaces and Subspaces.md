---
layout: post
title: Math415 Chapter 03 Vector Spaces and Subspaces
categories: Linear-Algebra
description: Personal Notes
keywords: Math415，Linear-Algebra，Matrix
mathjax: true
---
Definde $A$ is an $m\times n$ matrix

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


