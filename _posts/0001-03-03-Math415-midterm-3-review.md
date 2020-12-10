Discussions sessions 7, problem 2
Discussions sessions 8, problem 4 
Discussions sessions 9, problems  1-3  
Discussions sessions 10 problem 1
Discussions sessions 10, problem 2
Discussions sessions 8, problem 3

HW8, problems 3,5
HW9, problem 3,4,6
HW10 problems 2, 6
HW11, problem 1

## D7.2
![pic](https://github.com/ZhekaiLi/PICTURE-for-markdown/raw/master/2020-12/Snipaste_2020-12-10_15-18-46.jpg)
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
(之所以能够这样计算, 是因为 $A,\cos(A)$ 都是可对角化的矩阵, 详见 [Chapter 6.2](https://zhekaili.github.io/0001/01/06/Math415-chapter-06-Eigenvalues-and-Eigenvectors/#62-diagonalizing-a-matrix))

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
\end{bmatrix},$$$$\frac{d^2u}{dt^2}=-A^2u,u'(0)=0,u(0)=\begin{bmatrix}
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

## D8.4
同 [Midterm 2 Review D7.2](https://zhekaili.github.io/0001/03/02/Math415-midterm-2-review/#d72)

## D9.1, 2, 3
这三题讲的都是奇异值分解 SVD, 选一道比较复杂的为例
> Find the singular values of 
$$A=\begin{bmatrix}
0 & 1 & 1\\
\sqrt2 & 2 & 0\\
0 & 1 & 1
\end{bmatrix}$$ and find the SDV decomposition of $A$

**Solution:**
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

## D10.1
重复上题内容, 略

## D10.2
> Find the pseudoinverse of
$$A=\begin{bmatrix}
-1 & 2 & 2
\end{bmatrix}$$

**Solution:**
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

## D8.3
这道题比较偏而且内容不多, 个人感觉应该不太会考
![pic](https://github.com/ZhekaiLi/PICTURE-for-markdown/raw/master/2020-12/Snipaste_2020-12-10_22-17-01.jpg)

## HW8.3, 5
这之后的 solution bb 上还没给, 过几天再整














