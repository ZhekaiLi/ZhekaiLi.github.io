---
layout: post
title: Math415 Midterm-2 Review
categories: Math415
description: Personal Notes
keywords: Math415，Calculas，Matrix
---
**ATTENSION - If some LeTeX equations could not show well, pleae try to refresh this page.**

**多看看 L19**

![pic1](https://github.com/ZhekaiLi/PICTURE-for-markdown/raw/master/Snipaste_2020-11-24_11-18-12.jpg)

## D4.5
略
## D5.1
见 [Math415 Chapter-10](https://zhekaili.github.io/2020/11/22/Math415-chapter-10/#101-graphs-and-networks)
## HW5.4
见 [Math415 Week-05](https://zhekaili.github.io/2020/11/22/Math415-slides-week-05/#821-matrices-of-linear-transformations-general-case) 的最后两个例子
## D5.4
见 [Math415 Week-07](https://zhekaili.github.io/2020/11/22/Math415-slides-week-07/#113-projection-of-a-vector-onto-a-subspace-in-mathbbrn)
> #### Def 5: Prjection matrix $P$
> The projection $p$ of vector $b$ onto $S=C(A)$ is
$$p=Pb,\text{where }P=A(A^TA)^{-1}A^T$$

## HW6.6, 7, 8
![pic2](https://github.com/ZhekaiLi/PICTURE-for-markdown/raw/master/Snipaste_2020-11-24_20-50-53.jpg)
红框内等式成立是由于 $P_2$ 所映射的空间包含了 $P_1$ 所映射的空间，因此如果换位置则不一定成立 $P_1P_2\neq P_2$。当然这道题老老实实分别算出 $P_1,P_2$ 再乘起来也完全 OK
![pic3](https://github.com/ZhekaiLi/PICTURE-for-markdown/raw/master/Snipaste_2020-11-24_20-31-47.jpg)
![pic4](https://github.com/ZhekaiLi/PICTURE-for-markdown/raw/master/Snipaste_2020-11-24_20-47-13.jpg)
如果 $A$ 的形式比较简单，可以直接用 $\hat{x}=(A^TA)^{-1}A^Tb$

## D6.1, 2
[Math415 Week-08 L13.3](https://zhekaili.github.io/2020/11/22/Math415-slides-week-08/#133-properties-of-determinants) 中列举的行列式的部分性质，可以在求矩阵行列式时提供一定的帮助，例如
![pic5](https://github.com/ZhekaiLi/PICTURE-for-markdown/raw/master/Snipaste_2020-11-24_22-40-58.jpg)

再例如
![pic6](https://github.com/ZhekaiLi/PICTURE-for-markdown/raw/master/Snipaste_2020-11-25_08-56-48.jpg)
其中红框等式之所以成立，是因为从左至右相当于做了两次行交换，从 $[1;2;3]\to[3;1;2]$

## HW7.2
同上，略
## D7.2
Using matrix exponents, find solution $x(t)$ of equation
$$\frac{dx}{dt}=Ax,\;x(0)=a$$
for $$A=\begin{pmatrix}
2 & 1\\
0 & 1
\end{pmatrix},\;a=\begin{pmatrix}
0\\
1
\end{pmatrix},\;t=1/2$$
**Method 1:** 用正常的 ODE 来做
1. 求特征根和特征向量：
$$\lambda_1=1,\lambda_2=2,x_1=\begin{pmatrix}
-1\\
1
\end{pmatrix},x_2=\begin{pmatrix}
1\\
0
\end{pmatrix}$$
2. 求系数 $c_i$
$$\begin{aligned}
x(t)&=c_1x^{(1)}(t)+c_2x^{(2)}(t)=c_1\begin{pmatrix}
-1\\
1
\end{pmatrix}e^t+c_2\begin{pmatrix}
1\\
0
\end{pmatrix}e^{2t} \\
x(0)&=\begin{pmatrix}
-c_1+c_2\\
c_1
\end{pmatrix}=\begin{pmatrix}
0\\
1
\end{pmatrix}\to \begin{cases}
   c_1 = 1 \\
   c_2 = 1
\end{cases}\end{aligned}$$
3. 最后代入 $t=1/2$
$$x(\frac{1}{2})=\begin{pmatrix}
-1\\
1
\end{pmatrix}e^{1/2}+\begin{pmatrix}
1\\
0
\end{pmatrix}e=\begin{pmatrix}
-e^{1/2}+e\\
e^{1/2}
\end{pmatrix}$$

**Method 2:** 用 $e^{At}=Xe^{\Lambda t}X^{-1}$
1. 同 Method 1，求出特征根和特征向量后可得
$$X=\begin{pmatrix}
-1 & 1\\
1 & 0
\end{pmatrix},\Lambda=\begin{pmatrix}
1 & 0\\
0 & 2
\end{pmatrix}$$

2. 由题目中的条件 $\frac{dx}{dt}=Ax,x(0)=a$ 可得
$$x(t)=ae^{At}=\begin{pmatrix}
0\\
1
\end{pmatrix}X\begin{pmatrix}
e^t & 0\\
0 & e^{2t}
\end{pmatrix}X^{-1}$$

## D7.4, 5
Jordan Form, 略
## HW8.7
略








