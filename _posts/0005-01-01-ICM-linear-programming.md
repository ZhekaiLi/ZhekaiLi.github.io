---
layout: post
title: Linear Programming
categories: ICM
description: Personal Notes
keywords: [Linear Programming, ICM]
---

# 1 线性规划
## 1.1 线性规划的 Matlab 标准形式
$$\underset{x}{\min}\;c^Tx,\;\;s.t.\begin{cases}
Ax\leq b\\
Aeq\cdot x=beq\\
lb\leq x\leq ub
\end{cases}$$

```matlab
% 最简形式
[x, fval] = linprog(c, A, b);

% 完整形式
[x, fval] = linprog(c, A, b, Aeq, beq, LB, UB, x0, OPTIONS);
```

例如，对于如下线性规划问题：
$$\underset{x}{\max}\;2x_1-3x_2,\;\;s.t.\begin{cases}
2x_1-5x_2\geq 10\\
x_1+2x_2\leq 12\\
x_1+x_2=7\\
x_1,x_2\geq0
\end{cases}$$

```matlab
c = [2; -3];
A = [-2, 5; 1, 2]; b = [-10; 12];
aeq = [1, 1]; beq = 7;

x = linprog(-c, A, b, aeq, beq, zeros(2,1))
value = c' * x
```

## 1.2 可以转化为线性规划的问题
很多看起来不是线性规划的问题也可以通过变换变成线性规划的问题来解决。如：
$$\underset{x}{\min}\;\vert x_1\vert+\vert x_2\vert+...+\vert x_n\vert,\;\;s.t.\;Ax\leq b$$

要把上面的问题变换成线性规划问题，只要注意到事实：对任意的 $x_i$，存在 $u_i, v_i>0$ 满足 $x_i = u_i − v_i, \vert x_i\vert= u_i + v_i$。事实上，只要取 
$$u_i=\frac{\vert x_i\vert+x_i}{2},v_i=\frac{\vert x_i\vert-x_i}{2}$$

这样，记 $u=[u_1,...,u_n]^T,v_i=[v_1,...,v_n]^T$，从而我们可以把上面的问题变成：
$$\underset{x}{\min}\;\sum_{i=1}^n(u_i+v_i),\;\;s.t.\begin{cases}
A(u-v)\leq b\\
u,v\geq 0
\end{cases}$$

# 2 指派问题
## 2.1 数学模型
拟分配 $n$ 个人去干 $n$ 项工作，每个人只能干一项，令 $c_{ij}$ 表示分配第 $i$ 个人去干第 $j$ 项工作所需的时间，$x_{ij}=1$ 表示分配 $i$ 干工作 $j$，否则为零。可得指派的数学模型为：
$$\underset{x}{\min}\;\sum_{i=1}^n\sum_{j=1}^nc_{ij}x_{ij},\;\;s.t.\begin{cases}
\sum_{i=1}^nx_{ij}=1\\
\sum_{j=1}^nx_{ij}=1
\end{cases}$$

## 2.2 求解指派问题的匈牙利算法
由于指派问题的特殊性，又存在着由匈牙利数学家 Konig 提出的更为简便的解法——匈牙利算法。算法主要依据以下事实：如果系数矩阵 $C = (c_{ij})$ 一行（或一列）中每一元素都加上或减去同一个数，得到一个新矩阵 $B = (bij)$，则以 $C, B$ 为系数矩阵的指派问题具有**相同的最优指派**。例如：
$$C=\begin{bmatrix}
16 & 15 & 19 & 22\\
17 & 21 & 19 & 18\\
24 & 22 & 18 & 17\\
17 & 19 & 22 & 16
\end{bmatrix}\to B=\begin{bmatrix}
1 & 0^* & 3 & 7\\
0^* & 4 & 1 & 1\\
7 & 5 & 0^* & 0\\
1 & 3 & 5 & 0^*
\end{bmatrix}$$

由 $B$ 可得，该问题有最优指派(工作的序号等于打星号的 $0$ 的位置)
$$\begin{pmatrix}
\text{第 i 个人}\\
\text{第 j 项工作}
\end{pmatrix}=\begin{pmatrix}
1 & 2 & 3 & 4\\
2 & 1 & 3 & 4
\end{pmatrix}$$

对于更复杂的情况，即当矩阵 $B$ 没法划出 $n$ 个 $0^*$ 时，还有更高级的应对方法，[参考书本 p7]()
