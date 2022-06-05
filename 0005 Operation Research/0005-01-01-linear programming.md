---
layout: post
title: Linear Programming (LP)
categories: Operation-Research
description: Personal Notes
keywords: LP, OR
---


*References*
1. [B站：【零基础教程】老哥：数学建模算法、编程、写作和获奖指南全流程培训！](https://www.bilibili.com/video/BV1kC4y1a7Ee?p=4)
2. 书籍：数学建模算法与程序（司守奎）

# 1. Definition
$$\min\;f(x_1,x_2,...,x_n)$$

$$s.t.\begin{cases}
g_i(x_1,x_2,...,x_n) \leq b_i & \forall i=1,...,m\\
x_j\in \mathbb{R} & \forall j=1,...,n
\end{cases}$$

where $f(\cdot),g_i(\cdot)$ are all **<font color=blue>linear</font>** functions 
 
> **Transformation**

$g_i(x)=b_i\Leftrightarrow g_i(x)\leq b_i\text{ and }-g_i(x)\leq -b_i$

> **Feasible region & optimal solutions**

- The **<font color=blue>feasible region</font>** is a set of feasible solutions
- An **<font color=blue>optimal solution</font>** performs the best in feasible region
- There maybe **<font color=blue>no</font>** optimal solution

> **Binding constraints**

$g_i(x)$ is binding at $\bar{x}$ if $g(\bar{x})=b$

> **Vectorized & Metrics form**

$$\underset{x}{\min}\;c^Tx$$

$$s.t.\; a_i^Tx\leq b_i\;\;\; \forall i=1,...,m$$

where $c,a_i\in\mathbb{R}^n$, $b_i\in\mathbb{R}$

$$\underset{x}{\min}\;c^Tx$$

$$s.t.\; Ax\leq b$$

where $A\in\mathbb{R}^{m\times n}$, $b\in\mathbb{R^m}$

# 2. LP 的 Matlab 标准型
$$\underset{x}{\min}\;c^Tx$$

$$s.t.\begin{cases}
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
$$\underset{x}{\max}\;2x_1-3x_2$$

$$s.t.\begin{cases}
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

# 3. 使用 Excel 求解 LP
如图，对应问题
$$\max\;700x_1 + 900x_2$$

$$s.t.\begin{cases}
3x_1 + 5x_2 \leq 3600\\
x_1 + 2x_2 \leq 1600\\
50x_1 + 20x_2 \leq 48000
\end{cases}$$


<img src="/images/2022-04/pic0413.png" width="100%">

# 0. 示例与衍生问题
## 0.1 可以转化为 LP 的问题
很多看起来不属于线性规划的问题，也可以通过一定的转换变成线性规划问题。如：
$$\underset{x}{\min}\;\vert x_1\vert+\vert x_2\vert+...+\vert x_n\vert,\;\;s.t.\;Ax\leq b$$

由于对于任意的 $x_i$，都存在 $u_i, v_i>0$ 满足 $x_i = u_i − v_i, \vert x_i\vert= u_i + v_i$。例如： 
$$u_i=\frac{\vert x_i\vert+x_i}{2},v_i=\frac{\vert x_i\vert-x_i}{2}$$

这样，记 $u=[u_1,...,u_n]^T,v_i=[v_1,...,v_n]^T$，从而即可把上面的问题转换为：
$$\underset{x}{\min}\;\sum_{i=1}^n(u_i+v_i)$$

$$s.t.\begin{cases}
A(u-v)\leq b\\
u,v\geq 0
\end{cases}$$

## 0.2 指派问题
### 0.2.1 数学模型
拟分配 $n$ 个人去干 $n$ 项工作，每个人只能干一项，令 $c_{ij}$ 表示分配第 $i$ 个人去干第 $j$ 项工作所需的时间，$x_{ij}=1$ 表示分配 $i$ 干工作 $j$，否则为零。可得指派的数学模型为：
$$\underset{x}{\min}\;\sum_{i=1}^n\sum_{j=1}^nc_{ij}x_{ij}$$

$$s.t.\begin{cases}
\sum_{i=1}^nx_{ij}=1 & \forall j=1,...,n \\
\sum_{j=1}^nx_{ij}=1 & \forall i=1,...,n
\end{cases}$$

### 0.2.2 求解指派问题的匈牙利算法
针对指派问题的特殊性，匈牙利数学家 Konig 提出的更为简便的解法——匈牙利算法。

该算法主要依据以下事实：对于矩阵 $C$，通过将其任意一行（或一列）中每一元素都加上或减去同一个数，可以得到一个新矩阵 $B$，并且 $C, B$ 为工作时间矩阵的指派问题具有**相同的最优指派**。例如：
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

因此，$\min\;\sum_{i=1}^n\sum_{j=1}^nc_{ij}x_{ij}=15+17+18+16=66$

对于更复杂的情况，即当矩阵 $B$ 没法划出 $n$ 个 $0^*$ 时，还有更高级的应对方法，参考书本 p7

## 0.3 示例：投资的收益和风险
### 0.3.1 问题概述
现有数额为 $M$ (相当大)的资金用作投资，投资对象为 $4$ 种资产 $s_i(i=1,..,4)$, 此时：
1. 购买 $s_i$ 的收益率为 $r_i$，风险损失率为 $q_i$
2. 购买 $s_i$ 需要付 $p_i$ 的交易费
3. 假定同期银行存款利率是 $r=5\%$，既无交易费又无风险

|$s_i$|$r_i(\%)$|$q_i(\%)$|$p_i(\%)$|
|---|---|---|---
|$s_1$| 28| 2.5| 1
|$s_2$| 21| 1.5| 2
|$s_3$| 23| 5.5| 4.5
|$s_4$| 25| 2.6| 6.5

### 0.3.2 基本假设与符号规定
1. 除了上述定义的 $s_i,r_i,q_i,p_i(i=1,...,4)$ 外，另令 $s_0$ 指存入银行，$r_0=5\%,p_0=q_0=0$
2. $x_i$ 表示投资 $s_i$ 的资金，
3. 定义 $M=\sum x_i=1$
4. 定义 **<font color=blue>总体风险</font>** 为投资的所有资产中风险最大的一个，$R=\max\{q_ix_i\}$
5. 定义 **<font color=blue>总体收益</font>**：$$Q=\sum_{i=0}^{n=4}(r_i-p_i)x_i$$
6. 假设 $r_i,q_i,p_i$ 在投资期间内不发生改变，且各个不同的投资项目之间相互独立

### 0.3.3 模型建立
该问题是一个多目标规划模型，目标是提高收益并降低风险（$\max Q,\min R$）：
$$\begin{cases}
\max\;\sum_{i=0}^{n=4}(r_i-p_i)x_i \\
\min\;\max\{q_ix_i\}
\end{cases}$$

约束条件为：
$$\begin{cases}
\sum_{i=0}^{n=4}(1+p_i)x_i=M=1 \\
x_i\geq0
\end{cases}$$

**针对多目标模型（目标1、目标2），我们通常可以通过固定目标1优化目标2，固定目标2优化目标1，或对目标1、2设置相对权重来转换为单目标模型**

> **模型一：固定风险，优化收益**

固定最大可承受的风险为 $a$，即需满足 $R/M\leq a$：

$$\max\;\sum_{i=0}^{n=4}(r_i-p_i)x_i$$$$s.t.\begin{cases}
(q_ix_i)/M\leq a\\
\sum_{i=0}^{n=4}(1+p_i)x_i=M
\end{cases}$$

> **模型二：固定收益，优化风险**

固定最小可承受的收益为 $k$，即需满足 $Q\geq k$：
$$\min\;\max\{q_ix_i\}$$$$s.t.\begin{cases}
\sum_{i=0}^{n=4}(r_i-p_i)x_i\geq k\\
\sum_{i=0}^{n=4}(1+p_i)x_i=M
\end{cases}$$

> **模型三：设置收益与风险的相对权重**

对风险、收益分别赋予权重 $s,(1-s)$：
$$\min\;s(\max\{q_ix_i\})-(1-s)\sum_{i=0}^{n=4}(r_i-p_i)x_i$$

$$s.t.\;
\sum_{i=0}^{n=4}(1+p_i)x_i=M$$

### 0.3.4 模型求解（以模型一为例）
<center>
    <img src="/images/2021-01/Snipaste_2021-01-25_15-35-22.jpg" style="zoom:90%">
</center>

由于 $a$ 是任意给定的风险度，因此不妨从 $a=0,\Delta=0.001$ 开始，循环探求不同 $a$ 对于最大收益的影响：

```matlab
clc; clear;

a = 0;
hold on

while a < 0.05
    c = [-0.05, -0.27, -0.19, -0.185, -0.185];
    A = [zeros(4,1), diag([0.025,0.015,0.055,0.026])];
    b = a * ones(4,1);
    Aeq = [1, 1.01, 1.02, 1.045, 1.065];
    beq =1; 
    LB = zeros(5,1);
    [x,Q] = linprog(c,A,b,Aeq,beq,LB);
    Q = -Q;
    plot(a,Q,'*k');
    a = a + 0.001; 
end

xlabel('a'); ylabel('Q');
```
输出结果如下：
<center>
    <img src="/images/2021-01/01251551.jpg" style="zoom:70%">
</center>

由图可知最大收益与风险承受能力的关系，特别的：
1. $a_1=0.006$ 是第一个拐点，其左侧最大收益随可承受的风险增加而快速增长，右侧的增长则较为缓慢。
2. $a_2=0.025$ 是第二个拐点，其右侧最大收益不再增长

因此，可以判断 $a=0.006$ 是一个比较好的风险承受能力，当选择 $a=0.006$ 时，求解线性规划可得：
$$Q=0.2019,x_0=0,x_1=0.24,x_2=0.4,x_3=0.1091,x_4=0.2212$$


