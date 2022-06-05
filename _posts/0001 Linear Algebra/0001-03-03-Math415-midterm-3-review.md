---
layout: post
title: Math415 Midterm-3 Review
categories: Math415:Linear-Algebra
description: Personal Notes
keywords: Math415，Linear-Algebra，Matrix
mathjax: true
---
-

Discussions sessions 7, problem 2 <br> Discussions sessions 8, problem 4 <br> Discussions sessions 9, problems  1-3 <br> Discussions sessions 10 problem 1 <br> Discussions sessions 10, problem 2 <br> Discussions sessions 8, problem 3 <br> 

HW8, problems 3,5 <br> HW9, problem 3,4,6 <br> HW10 problems 2, 6 <br> HW11, problem 1 <br> 

[Week-14 L25](https://zhekaili.github.io/0001/04/14/Math415-slides-week-14/#l25)


## D7

> **D7.2**
> 
> ![pic](/images/2020-12/Snipaste_2020-12-10_15-18-46.jpg)

- (a). $$\cos(A)x=x-\frac{1}{2!}A^2x+\frac{1}{4!}A^4x-...=x(1-\frac{1}{2!}\lambda^2x+\frac{1}{4!}\lambda^4x...)=\cos(\lambda)x$$
So $x$ is the eigenvector of $\cos(A)$ and eigenvalue is $\cos(\lambda)$

- (b). 将两个特征向量分别代入 $Ax_i=\lambda_ix_i$, 求出两个特征值 $\lambda_1=\pi,\lambda_2=0$. 对于 $\cos(A)$, 它的**特征向量与 $A$ 相同, 特征值为 $A$ 特征值的开根号**, 由此可得 $\cos(A)$
$$\cos(A)=\begin{bmatrix}
1 & 1\\
1 & -1
\end{bmatrix}\begin{bmatrix}
\cos(\pi) & 0\\
0 & \cos(0)
\end{bmatrix}\begin{bmatrix}
1 & 1\\
1 & -1
\end{bmatrix}^{-1}$$
(之所以能够这样计算, 是因为 $A,\cos(A)$ 都是可对角化 (diagonalizable) 的矩阵, 详见 [Chapter 6.2](https://zhekaili.github.io/0001/01/06/Math415-chapter-06-Eigenvalues-and-Eigenvectors/#62-diagonalizing-a-matrix))

- (c). 填空: 
1. Expand $u(0)=c_1x_1+c_2x_2+c_3x_3$
2. Multiply those eigenvectors by $\cos(\lambda_1t),\cos(\lambda_2t),\cos(\lambda_3t)$. 
3. Add up the solution $u(t)=c_1\cos(\lambda_1t)x_1+c_2\cos(\lambda_2t)x_2+c_3\cos(\lambda_3t)x_3$. 

**示例: 定义如下, solve $u(t)$**

$$A=\begin{bmatrix}
\pi & \pi\\
\pi & \pi
\end{bmatrix},\lambda_1=2\pi, \lambda_2=0,x_1=\begin{bmatrix}
1\\
1
\end{bmatrix},x_2=\begin{bmatrix}
1\\
-1
\end{bmatrix}$$$$\frac{d^2u}{dt^2}=-A^2u,u'(0)=0,u(0)=\begin{bmatrix}
4\\
2
\end{bmatrix}$$
1. Expand: 
$$u(0)=\begin{bmatrix}
4\\
2
\end{bmatrix}=c_1\begin{bmatrix}
1\\
1
\end{bmatrix}+c_2\begin{bmatrix}
1\\
-1
\end{bmatrix}\to\begin{cases}
c_1=3\\
c_2=1
\end{cases}$$
2. Multiply and add up:
$$u(t)=c_1\cos(\lambda_1t)x_1+c_2\cos(\lambda_2t)x_2=3\cos(2\pi t)\begin{bmatrix}
1\\
1
\end{bmatrix}+1\cos(0t)\begin{bmatrix}
1\\
-1
\end{bmatrix}$$

## D8

> **D8.3**
>
>![pic](/images/2020-12/Snipaste_2020-12-10_22-17-01.jpg)

这道题比较偏而且内容不多, 个人感觉应该不太会考

> **D8.4**
同 [Midterm 2 Review D7.2](https://zhekaili.github.io/0001/03/02/Math415-midterm-2-review/#d7)

## D9
D9.1, 2, 3 这三题讲的都是奇异值分解 SVD, 选一道比较复杂的为例
> **D9.3**
Find the singular values of 
$$A=\begin{bmatrix}
0 & 1 & 1\\
\sqrt2 & 2 & 0\\
0 & 1 & 1
\end{bmatrix}$$ and find the SDV decomposition of $A$

1. Compute $$AA^T=\begin{bmatrix}
2 & 2 & 2\\
2 & 6 & 2\\
2 & 2 & 2
\end{bmatrix}\to\det(A)=0:-\lambda(\lambda-8)(\lambda-2)$$
2. $\lambda=8,2,0$ are eigenvalues of $AA^T$, and therefore the singular vlues of $A$ is $\sigma=2\sqrt2,\sqrt2,0$, then we get $\Sigma$
$$\Sigma=\begin{bmatrix}
2\sqrt2 & 0 & 0\\
0 & \sqrt2 & 0\\
0 & 0 & 0
\end{bmatrix}$$
3. For $\lambda=8,2,0$, we find three eigenvectors $u_1,u_2,u_3$, after **normalizing** them, we therefore get $U$
4. Similarly, use $A^TA$ to find $V$. 还可以使用如下方式来计算 $v_i$
$$v_i=\frac{1}{\sigma_i}A^Tu_i$$
如果先算的是 $A^TA$ 和 $V$ 的话, 使用相似公式计算 $u_i$
$$u_i=\frac{1}{\sigma_i}Av_i$$
5. 该题的 $\sigma_3=0$, 这意味着无法使用上述公式由 $u_3$ 求得 $v_3$, 此时只能通过 $N(A^TA)$ 来计算 $v_3$ 

## D10

> **D10.1**
重复上题内容, 略

> **D10.2**
> Find the pseudoinverse of
$$A=\begin{bmatrix}
-1 & 2 & 2
\end{bmatrix}$$

1. Compute $AA^T=9$, then $\lambda=9,\sigma=3$, and ($\Sigma, A$ 的 shape 相同)
$$U=[1], \Sigma=\begin{bmatrix}
3 & 0 & 0
\end{bmatrix}$$
2. 由于 $u_i$ 只有一个, 因此我们能够计算出的 $v_i$ 也只有一个
$$v_1=\frac{1}{\sigma_1}A^Tu_1=\begin{bmatrix}
-\frac{1}{3}\\
\frac{2}{3}\\
\frac{2}{3}
\end{bmatrix}$$
3. 已知 $V_{3\times 3}$ orthonormal, 因此由 $v_1$ 可以推测 $v_2,v_3$, 最后求得 $V$
$$V=\begin{bmatrix}
-\frac{1}{3} & \frac{2}{3} & \frac{2}{3}\\
\frac{2}{3} & -\frac{1}{3} & \frac{2}{3}\\
\frac{2}{3} & \frac{2}{3} & -\frac{1}{3}
\end{bmatrix}$$
4. 由于 $A^\dagger=V\Sigma^\dagger U^T$, 还差一个 $\Sigma^\dagger$
$$\Sigma^\dagger=\begin{bmatrix}
\frac{1}{3}\\
0\\
0
\end{bmatrix}\to A^\dagger=\begin{bmatrix}
-\frac{1}{9}\\
\frac{2}{9}\\
\frac{2}{9}
\end{bmatrix}$$

<font color=red>注 1:</font> 作者认为该题从小推大不够严谨, 应使用大推小, 改进方法参考 [Midterm-3 Review HW11.1](https://zhekaili.github.io/0001/03/03/Math415-midterm-3-review/#hw11)

<font color=red>注 2:</font> 对于 $v_i$ 的计算, 要注意各个 $v_i$ 之间是相互正交的, 例如这里先求得是 $v_1$, 那么 $v_1$ 就会对 $v_2,v_3$ 造成一个限制 (本题就出现了 $v_2,v_3$ 自由度过高的问题, 此时就需要 $v_1$ 的限制)

## HW8

HW8.3 略

HW8.5 需要用到[欧拉公式](https://zhekaili.github.io/0001/05/02/Math415-some-math-concepts/)


## HW9

> **HW9.3**
![pic](/images/2020-12/Snipaste_2020-12-15_14-23-30.jpg)

> **HW9.4**
Whether positive definite or not
$$\frac{1}{9}\begin{bmatrix}
-2 & 2 & 8\\
2 & 7 & 10\\
8 & 10 & 4
\end{bmatrix}$$

由 [Math415 Week-10 L18.1](https://zhekaili.github.io/0001/04/10/Math415-slides-week-10/#181-%E6%AD%A3%E5%AE%9A%E7%9F%A9%E9%98%B5) 中判断正定的各种方法可得, 由于该函数第一个 upper left determinant 就小于 0 了, 因此显然不正定 

> **HW9.6**
Suppose $C$ is positive definite and $A$ has independent columns. Apply the energy test to $x^TA^TCAx$ to show that $S=A^TCA$ is positive definite.

$A$ is positive definite $\iff$ $x^TAx>0$, when $x\neq0$, 然后根据 $C$ 和 $A$ 的性质来做

## HW10

HW10.2 略 (代值硬算, 没啥好写的)


HW10.6 略 (这道题题目本身就有问题, 应该是要给出 $U,\Sigma,V$ 这些数据来做计算的

## HW11

> **HW11.1**
> Find SVD for the matrix
$$A=\begin{bmatrix}
1 & 0 & 1 & 0\\
0 & 1 & 0 & 1
\end{bmatrix}$$

这是一道更一般化的 SVD 计算题, 即 $A_{m\times n}$ when $m\neq n$. 此时会出现 $u_i, v_i$ 个数不对等的情况, 对此大概有两种解法

**Method 1:** 小推大 (**不严谨, 不建议**)

使用已知的 $m$ 个 $u_i$, 利用正交的方式求出剩下的 $n-m$ 个 $u_i$, 具体如下:
$$AA^T=\begin{bmatrix}
2 & 0\\
0 & 2
\end{bmatrix},\vert AA^T\vert=0\to \lambda_1=\lambda_2=2$$

由此可得
$$u_1=\begin{pmatrix}
1\\0
\end{pmatrix},u_2=\begin{pmatrix}
0\\1
\end{pmatrix}$$

再由 $v_i=\frac{1}{\sigma_i}A^Tu_i$ 求出 $v_1,v_2$, 然后使用正交的方式根据 $v_1,v_2$ 求出 $v_3,v_4$ (作者认为该方法的不严谨性就体现在这一步)

**Method 2:** 大推小

使用已知的 $n$ 个 $v_i$, 由 $u_i=\frac{1}{\sigma_i}Av_i$ 求得前 $m$ 个 $v_i$. 该方法因为没用到正交, 所以足够严谨, 但是也面临着 $\det(A^TA-\lambda I)=0$ 计算太麻烦的问题.

解决方法是先用 $\det(AA^T-\lambda I)=0$ 算出 $\lambda_1=\lambda_2=2$, 再由 $AA^T,A^TA$ 特征根相同可直接得到 $\lambda_3=\lambda_4=0$. 这样就能求得四个 $v_i$, 最后再用 $v_1,v_2$ 求 $u_1,u_2$

当然, 还存在更加极端的情况, 例如对于下例中的 $A$, 其对应三个 $u$ 与两个 $v$, 但是三个奇异值中却只有一个非零, 这意味着只有 $u_1,v_1$ 能通过 $u_1=\frac{1}{\sigma_1}Av_1$ 关联起来, 此时的解决方案时同时用 $A^TA$ 与 $AA^T$

$$A=\begin{bmatrix}
1 & 0\\
3 & 0\\
0 & 0\\
\end{bmatrix},A^TA=\begin{bmatrix}
10 & 0\\
0 & 0
\end{bmatrix}\to \sigma_1=\sqrt{10},\sigma_2=\sigma_3=0$$

Let $\lambda=10$

$$A^TA-10I=\begin{bmatrix}
0 & 0\\
0 & -10
\end{bmatrix}\to v_1=\begin{bmatrix}
1 \\
0
\end{bmatrix},u_1=\frac{1}{\sigma_1}Av_1=\frac{1}{\sqrt{10}}\begin{bmatrix}
1 \\
3 \\
0
\end{bmatrix}$$

Let $\lambda=0$

$$A^TA-0I=\begin{bmatrix}
10 & 0\\
0 & 0
\end{bmatrix}\to v_2=\begin{bmatrix}
0 \\
1
\end{bmatrix}$$

剩下的 $u_2,u_3$ 使用 $AA^T - 0I$ 来求



















