---
layout: post
title: Math415 Midterm-1 Review
categories: Math415:Linear-Algebra
description: Personal Notes
keywords: Math415，Linear-Algebra，Matrix
mathjax: true
---
-

# P1
对于 $Ax=b$ 的**解的可能性** ($A_{m\times n},b_{m\times 1}$)

首先，所有的解都能表示成 $x=x_p+x_n$
- 无解
$x_p$ 不存在 $C(A)$ 的维度低于消元后的 $b$. 例如
$$A=\begin{bmatrix}
1 & 0\\
0 & 1\\
0 & 0
\end{bmatrix},b=\begin{bmatrix}
1\\
1\\
1
\end{bmatrix}$$
- 唯一解：
$x=x_p+0\to N(A)=\{0\}\to r=n$
- 无数解：
$x_n$ 存在 $\to \text{dim}(N(A))=n-r \geq 1$
# P2
<font color='red'>Attention plz!</font>
1. 在求解 $x_p,x_n$ 时等号右边的东西是不一样的，别搞混了：
$$Rx=d,Rx=0$$
2. 求解 $x_p$, all free column = 0; 求解 $x_n$, one free column = 1, other = 0

# P3 
从 $R$ 中提炼原矩阵 $A$ 的列的信息
例如

$$R=\begin{bmatrix}
   1 & 4 & 0 & 0 & 0 \\
   0 & 0 & 0 & 1 & 0 \\
   0 & 0 & 0 & 0 & 1 
\end{bmatrix}$$
逐列分析
1. 主元列：矩阵 $A$ 的 column 1, 4, 5 为 pivots column, 同样也是 $C(A)$ 的 basis ($C(A)=\R^3$)
2. 零元素列：矩阵 $A$ 的 column 3 为零向量
3. 列列关系：矩阵 $A$ 的 (column 2) = 4(column 1)