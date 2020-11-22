---
layout: post
title: Discussions and Homeworks
categories: Math415
description: Personal Notes
keywords: Math415，Calculas，Matrix
---

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
If $A$ if a square matrix such that $I-A$ is nonsingular, prove that
$$A(I-A)^{-1}=(I-A)^{-1}A$$

**Ans**
已知等式 $A(I-A)=(I-A)A$ 恒成立
对于等式两边的两边都乘上 $(I-A)^{-1}$，可得
$$(I-A)^{-1}A(I-A)(I-A)^{-1}=(I-A)^{-1}(I-A)A(I-A)^{-1}$$

$$(I-A)^{-1}A=A(I-A)^{-1}$$  

得证

## 2.2
可以用高斯消元的方式来求逆矩阵 $AA^{-1}=I$，即
$$[A\;|\;I]\to[I\;|\;A^{-1}]$$

也可以用来求 $AX=B$ 中的 $X$
$$[A\;|\;B]\to[I\;|\;X]$$

## 2.3
![pic1](https://github.com/ZhekaiLi/PICTURE-for-markdown/raw/master/202010201539.JPG)

# DH3
## 3.1
在判断某一集合是否为 subspace 时，首先可以检查一下该集合是否存在 0，如果不存在，直接否定。例如 $\{x|Ax=b,\text{where }A_{m\times n}\neq 0\text{ and }b_n\neq 0\}$ 显然不是一个 subspace

## 3.2
![pic2](https://github.com/ZhekaiLi/PICTURE-for-markdown/raw/master/202010201653.JPG)

这道题的解法真的很妙，以下的思考方式非常关键
1. $A$ is nonsingular $\iff$$Ax=0$ iff $x = 0$
2. $Ax=0\iff A_1x=0,A_2x=0$
3. $x\in N(A_1), N(A_1)=C(A_2^T)\iff \exist\;y,s.t.\;A^T_2y=x$
4. prove that $x$ could only equal to $0\to$ prove $x^Tx=0$
5. $x^Tx=(A^T_2y)^Tx=y^T(A_2x)=0$