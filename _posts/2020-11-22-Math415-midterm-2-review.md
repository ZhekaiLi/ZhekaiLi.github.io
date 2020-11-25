---
layout: post
title: Math415 Midterm-2 Review
categories: Math415
description: Personal Notes
keywords: Math415，Calculas，Matrix
---

![pic1](https://github.com/ZhekaiLi/PICTURE-for-markdown/raw/master/Snipaste_2020-11-24_11-18-12.jpg)

- P5 of Discussion 4 略
- P1 of Homework 5 略
- P4 of Homework 5 见 Math415 Week-05 的最后两个例子
- **P4 of Discussion 5 见 Math415 Week-07**
> #### Def 5: Prjection matrix $P$
> The projection $p$ of vector $b$ onto $S=C(A)$ is
$$p=Pb,\text{where }P=A(A^TA)^{-1}A^T$$

- **P6, 7, 8 of Homework 6**
![pic2](https://github.com/ZhekaiLi/PICTURE-for-markdown/raw/master/Snipaste_2020-11-24_20-50-53.jpg)
红框内等式成立是由于 $P_2$ 所映射的空间包含了 $P_1$ 所映射的空间，因此如果换位置则不一定成立 $P_1P_2\neq P_2$。当然这道题老老实实分别算出 $P_1,P_2$ 再乘起来也完全 OK
![pic3](https://github.com/ZhekaiLi/PICTURE-for-markdown/raw/master/Snipaste_2020-11-24_20-31-47.jpg)
![pic4](https://github.com/ZhekaiLi/PICTURE-for-markdown/raw/master/Snipaste_2020-11-24_20-47-13.jpg)
如果 $A$ 的形式比较简单，可以直接用 $\hat{x}=(A^TA)^{-1}A^Tb$

- **P1, 2 of Discussion 6**
[Math415 Week-08](https://zhekaili.github.io/2020/11/22/Math415-slides-week-08/) **L13.3** 中列举的行列式的部分性质，可以在求矩阵行列式时提供一定的帮助，例如
![pic5](https://github.com/ZhekaiLi/PICTURE-for-markdown/raw/master/Snipaste_2020-11-24_22-40-58.jpg)

- P2 of Homework 7 同上，略
- **P2 of Discussion 7**
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
$$x(t)=c_1x^{(1)}(t)+c_2x^{(2)}(t)=c_1\begin{pmatrix}
-1\\
1
\end{pmatrix}e^t+c_2\begin{pmatrix}
1\\
0
\end{pmatrix}e^{2t}$$
$$x(0)=\begin{pmatrix}
-c_1+c_2\\
c_1
\end{pmatrix}=\begin{pmatrix}
0\\
1
\end{pmatrix}$$
3. 由上可得 $c_1=c_2=1$，因此
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
\end{pmatrix},\;\Lambda=\begin{pmatrix}
1 & 0\\
0 & 2
\end{pmatrix}$$






