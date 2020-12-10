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

# D7.2
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

# D8.4
同 [Midterm 2 Review D7.2]()














