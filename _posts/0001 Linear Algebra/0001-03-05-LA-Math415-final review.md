---
layout: post
title: Math415 Final Review Sample
categories: Linear-Algebra
description: Personal Notes
keywords: Math415，Linear-Algebra，Matrix
mathjax: true
---


**其他重要的材料 for final**
1. [Discussions and Homeworks](https://zhekaili.github.io/0001/02/01/Math415-discussions-and-homeworks/)
2. [Math415 Midterm-1 Review](https://zhekaili.github.io/0001/03/01/Math415-midterm-1-review/)
3. [Math415 Midterm-2 Review](https://zhekaili.github.io/0001/03/02/Math415-midterm-2-review/)
4. [Math415 Midterm-3 Review](https://zhekaili.github.io/0001/03/03/Math415-midterm-3-review/)


# P4
![pic](/images/2021-01/Snipaste_2021-01-03_11-40-46.jpg)

> **(a)**

$$Aq_j=\lambda_jq_j\to q_j=\lambda_jA^{-1}q_j\to A^{-1}q_j=\frac{1}{\lambda_j}q_j$$

> **(b)**

利用 $q_j$ 的标准正交性, 两边同乘 $q_1^T$

$$q_1^Tb=c_1$$

> **(c)**

同 (b) 两边同乘 $q_1^T$

$$d_1=q_1^TA^{-1}b=q_1^TA^{-1}\sum c_iq_i$$

Since $A^{-1}q_j=\frac{1}{\lambda_j}q_j$, 注意题干里是给了 $\lambda_j$ 作为已知的

$$d_1=q_1^T\sum\frac{c_i}{\lambda_i}q_i=\frac{c_1}{\lambda_1}$$

# P6
**Let** $$A=I-cE=\begin{bmatrix}
1 & & \\
& 1 & \\
& & 1 \\
\end{bmatrix}-c\begin{bmatrix}
1 & 1 & 1 \\
1 & 1 & 1 \\
1 & 1 & 1 \\
\end{bmatrix}$$

> **(a) 找到 $c$ 使得 $A$ 为 projection matrix**

$A$ 为 projection matrix $\iff A^2=A$
像这样的在证明复合矩阵运算时, 不妨就拆开来算, 即证 $(I-cE)^2=I-cE$, 这要比直接证明 $A^2=A$ 要简便的多

> **(b) 找到 $c$ 使得 $A$ 为 orthogonal matrix**

Orthogonal matrix 的定义是 $A^T=A^{-1}$ or $A^TA=I$, 也就是说, orhogonal matrix 是由 orthonormal vectors 构成的, 而不是 orthogonal vectors

$$I=A^TA=A^2=(I-cE)^2$$

> **(c) 找到 $c$ 使得 $A$ 为 diagonalizable matrix**

Since $A=A^T$, $A$ is always diagonalizable

> **(d) Find eigenvalues of $A^{-1}$ in terms of $c$**

$$Ax=\lambda x\to A^{-1}x=\frac{1}{\lambda}x$$

To find $\lambda$, we need to find the eigenvalues of $I, E$. For $I$, $\lambda_I=[1,1,1]$; For $E$
$$\begin{cases}
&\text{rank}(E)=1,E\text{ is symmetric}\to E\text{ has one non-zero eigenvalue} \\
&\text{tr}(E)=\sum e_{ii}=\sum \lambda_i=3\to\lambda_E=[3,0,0]
\end{cases}$$

Therefore, 
$$\lambda=\lambda_I-c\lambda_E=[1-3c,1,0]$$

> **(e) 找到 $c$ 使得 $A$ 为 positive definite matrix**

由 (d) 可知, 只需使得 $1-3c>0$ 即可满足正定