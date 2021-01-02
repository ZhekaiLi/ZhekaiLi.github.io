---
layout: post
title: Math415 Discussions and Homeworks
categories: Math415
description: Personal Notes
keywords: Math415，Calculas，Matrix
---
**ATTENSION - If some LeTeX equations could not show well, pleae try to refresh this page.**

<font color='red'>矩阵计算就一步一步小心算, 一算快还是挺容易出错的</font>

# DH1
## 1.1 Schwarz Inequality
$$||\bm{w}||\geq(\bm{v}\cdot\bm{w})/||\bm{v}||$$

## 1.2 Linearly Independent
**Definition**
$\text{Let }x_1,...,x_n \in \R^n, \text{we say that they are linearly independent if, for any }c_1,...,c_n \in \R, \text{if } \sum_{i=1}^n c_ix_i=0 \text{ then } c_i=0 \text{ for all } i$

根据这一定义，使用反证法可得：
$\text{If }x_1=0\;(i.e\;||x_1||=0),\text{ then the system }x_1,...,x_n\in\R^n \text{is not independent}$

## 1.3 
Let $x_1,x_2,x_3$ 为矩阵 $X$ 的列向量，且有 $Ax_1=b_1,Ax_2=b_2,Ax_3=b_3$ 则
$$AX=[Ax_1,Ax_2,Ax_3]=[b_1,b_2,b_3]$$

# DH2
## 2.1
> If $A$ if a square matrix such that $I-A$ is nonsingular, prove that
$$A(I-A)^{-1}=(I-A)^{-1}A$$

**Ans** <br> 已知等式 $A(I-A)=(I-A)A$ 恒成立, 对于等式两边的两边都乘上 $(I-A)^{-1}$，可得
$$(I-A)^{-1}A(I-A)(I-A)^{-1}=(I-A)^{-1}(I-A)A(I-A)^{-1}$$

$$(I-A)^{-1}A=A(I-A)^{-1}$$  

## 2.2
可以用高斯消元的方式来求逆矩阵 $AA^{-1}=I$，即
$$[A\;|\;I]\to[I\;|\;A^{-1}]$$

也可以用来求解 $AX=B$
$$[A\;|\;B]\to[I\;|\;X]$$

若是求解 $XA=B$, given $A,B$, 不妨先观察一下 $A,B$ 两者间是否存在关系 (是否可以通过 elimination or permutation 由 $A$ 得到 $B$)

## 2.3
![pic1](https://github.com/ZhekaiLi/PICTURE-for-markdown/raw/master/202010201539.JPG)

## 2.4 LU Factorization
1. 计算 $L=E^{-1}$ 时, 一个一个把 $E_{ij}^{-1}$ 乘起来就行 (将 $E_{ij}$ 非对角元素取负即可得到 $E_{ij}^{-1}$)
2. 使用 $PA=LU$ 辅助计算 $Ax=b$ 时, 记得 $b$ 也要进行对应的置换
$$Ax=b\to LUx=Pb$$


# DH3
## 3.1 If a subspace
1. 在判断某一集合是否为 subspace 时，首先可以检查一下**该集合是否存在 0**，如果不存在，直接否定。(例如 $\{x|Ax=b,\text{where }A_{m\times n}\neq 0\text{ and }b_n\neq 0\}$ 显然不是一个 subspace)

2. 然后再判断其余两个条件是否也同时满足
$$\text{If }\begin{cases}
   x,y\in Y &\text{then } x+y\in Y \\
   \alpha\in E,x\in Y &\text{then } \alpha x\in Y
\end{cases}$$

## 3.2
> ![pic2](https://github.com/ZhekaiLi/PICTURE-for-markdown/raw/master/202010201653.JPG)

这道题的解法真的很妙，
1. $A$ is nonsingular: $$ Ax=0 \iff x = 0$$
2. $$Ax=0\to \begin{bmatrix}
A_1\\
A_2
\end{bmatrix}x=0$$
3. $$\begin{cases}x\in N(A_1) 
\\N(A_1)=C(A_2^T)\end{cases}\to \exist\;y\neq 0,s.t.\;x=A^T_2y$$
4. $$x^Tx=(A^T_2y)^Tx=y^T(A_2x)$$

由于 $y\neq 0$, $x^Tx=0$ 当且仅当 $x=0$

## 3.3 If $b\in C(A)$
$b\in C(A)$ 的充要条件为 $Ax=b$ 有解

# DH4
## 4.1
> **T/F: A vector space has infinitely many different bases**

False (counter example: $V=\{0\}$) 不要忘了**零空间**啊

## 4.2
> ![pic](https://github.com/ZhekaiLi/PICTURE-for-markdown/raw/master/2021-01/Snipaste_2021-01-02_10-58-10.jpg)

To show $S_{max}$ is linearly independent, suppose
$$0=\alpha_0p+\sum_{i=1}^{n-r}\alpha_i(p+h_i)=(\sum_{i=0}^{n-r}\alpha_i)p+\sum_{i=1}^{n-r}\alpha_ih_i$$

两边同乘 $A$, 由于 $Ah_i=0,Ap=b$, 可得 
$$(\sum_{i=0}^{n-r}\alpha_i)b=0\to\sum_{i=0}^{n-r}\alpha_i=0$$

再代回原式, plus that $\{h_i\}$ independent, 可得
$$0=\sum_{i=1}^{n-r}\alpha_ih_i\to a_i=0$$

Therefore, we can conclude that the only solution to $0=\alpha_0p+\sum_{i=1}^{n-r}\alpha_i(p+h_i)$ is $a_i=0$, and then $S_{max}$ is an independetn set

# DH5
## 5.1 
看一下 [Chapter-10](https://zhekaili.github.io/0001/01/10/Math415-chapter-10/)