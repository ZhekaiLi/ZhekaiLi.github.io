---
layout: post
title: Linear Programming (LP)
categories: Operation-Research
description: Personal Notes
keywords: LP, OR
mathjax: true
---

LINKs Back:
[Wiki: Operation Reseach - Linear Programming](./0005-01-01-linear%20programming.md)


很多看起来不属于线性规划的问题，也可以通过一定的转换变成线性规划问题

# 1. Linearize Absolute Function
## Ex 1
$$\underset{x}{\min}\sum\vert x_i\vert\;\;\;s.t.\;Ax\leq b$$

**Linearization**: 对于任意的 $x_i$，都存在 $u_i, v_i>0$ 满足 $x_i = u_i − v_i, \vert x_i\vert= u_i + v_i$。因此： 
$$u_i=\frac{\vert x_i\vert+x_i}{2},v_i=\frac{\vert x_i\vert-x_i}{2}$$

记 $u=[u_1,...,u_n]^T,v_i=[v_1,...,v_n]^T$，从而即可把上面的问题转换为：
$$\underset{x}{\min}\;\sum_{i=1}^n(u_i+v_i)$$

$$s.t.\begin{cases}
A(u-v)\leq b\\
u,v\geq 0
\end{cases}$$


## Ex 2
假设总共给两个人分¥1000，其中给第一个人分¥$x_1$，第二个¥$x_2$。问: 如何分钱最公平（答案显示是均分最公平，关键是如何给这个问题建模）

$$\min\vert x_2-x_1\vert$$

$$s.t.\begin{cases}
x_1+x_2=1000 \\
x_i\geq 0\;\;\;\forall i=1,2
\end{cases}$$

**Linearization**: set $w\geq\vert x_2-x_1\vert=\max\{x_2-x_1,x_1-x_2\}$
Threfore, $w\geq x_2-x_1$ and $w\geq x_1-x_2$，从而把上面的问题转换为:

$$\min w$$

$$s.t.\begin{cases}
x_1+x_2=1000 \\
w\geq x_2-x_1 \\
w\geq x_1-x_2 \\
x_i\geq 0\;\;\;\forall i=1,2
\end{cases}$$




# 2. Linearize Max/Min Function

$$\min\;\max\{x_1,x_2\}\iff \min w\;\;s.t.\begin{cases}
w\geq x_1 \\
w\geq x_2
\end{cases}$$

$$\max\;\min\{x_1,x_2\}\iff \max w\;\;s.t.\begin{cases}
w\leq x_1 \\
w\leq x_2
\end{cases}$$

$$\min w$$

$$s.t.\begin{cases}
x_1+x_2=1000 \\
w\geq x_2-x_1 \\
w\geq x_1-x_2 \\
x_i\geq 0\;\;\;\forall i=1,2
\end{cases}$$



# 3. Linearize Other Scenarios
## Senario 1: 是否同时生产
假设某工厂有两台机器，分别可以生产一种商品（共两种）:
- 第一种每个利润10，第二种每个利润20
- 第一台机器启动费用20，第二胎机器启动费用25

**Object**: 最大化利润

**Decision Variables**:
- $z_1,z_2\in\{0,1\}$ 分别表示是否启动两台机器
- $x_1,x_2\leq 0$ 分别表示两种商品的产量

> **Senario 1A**

额外条件: 两台机器如果同时启动，则能 **<font color=blue>节省</font>** 10的费用

$$\max\;(10x_1+12x_2-20z_1-25z_2)+10z_1z_2$$

$$s.t.\begin{cases}
x_1\leq 3z_1 \\
x_2\leq 4z_2
\end{cases}$$

Set $w\leq z_1z_2\iff w\leq z_1$ and $w\leq z_2$, therefore:

$$\max\;(...)+10w\;\;\;s.t.\begin{cases}
x_1\leq 3z_1 \\
x_2\leq 4z_2 \\
w\leq z_1 \\
w\leq z_2 \\
w\in\{0,1\}
\end{cases}$$


> **Senario 1B**

额外条件: 两台机器如果同时启动，则会额外 **<font color=blue>花费</font>** 10的费用

$$\max\;(...)-10z_1z_2\;\;\;s.t.\begin{cases}
x_1\leq 3z_1 \\
x_2\leq 4z_2
\end{cases}$$

因为是 max + 负号，相当于 min，因此 set $w\geq z_1z_2\iff w\geq z_1+z_2-1$, therefore:

$$\max\;(...)-10w\;\;\;s.t.\begin{cases}
x_1\leq 3z_1 \\
x_2\leq 4z_2 \\
w\geq z_1+z_2-1 \\
w\in\{0,1\}
\end{cases}$$


> **Senario 1C & 1D**

额外条件: $z_1z_2$ 作为 Constraints 的一部分

$$\max ...\;\;\;s.t.\begin{cases}
x\leq 5z_1z_2\\
x\geq 0
\end{cases}\implies s.t.\begin{cases}
x\leq 5w\\
x\geq 0 \\
w\leq z_1, w\leq z_2\\
w\in\{0,1\}
\end{cases}$$

类似的
$$\max ...\;\;\;s.t.\;x\geq 5z_1z_2\implies s.t.\begin{cases}
x\geq 5w\\
w\geq z_1+z_2-1\\
w\in\{0,1\}
\end{cases}$$



## Senario 2: 是否生产
相较于 Senario 1, Senario 2 使用一台机器即可生产两种产品

**Parameters**: 
- $z=\{0,1\}$ 表示是否开工
- $x_1,x_2\leq 0$ 分别表示两种商品的产量

> **Senario 2A**

$x_iz$ 之于 max

$$\max\;(10x_1+12x_2)z-15z$$

$$s.t.\begin{cases}
2x_1+x_2\leq 6 \\
x_1+2x_2\leq 8 \\
x_1,x_2\geq 0 \\
z\in\{0,1\}
\end{cases}$$

Set $w_1\leq x_1z$，此时我们 **<font color=blue>不能</font>** 像 Senario 1A 那样使用 $w_1\leq x_1$ and $w_1\leq z$ 来替代，因为 $w_1\leq z$ 意味着即使开工，商品1也只能生产一个，荒谬

观察关于 $x_1,x_2$ 的两个不等式，发现 $x_1\leq 3$ 是不等式成立的必要条件，因此修改 $w_1\leq z\implies w_1\leq 3z$。同理修改 $w_2\leq z\implies w_2\leq 4z$, therefore:

$$\max\;10w_1+12w_2-15z$$

$$s.t.\begin{cases}
... \\
w_1\leq x_1, w_1\leq 3z\\
w_2\leq x_2, w_2\leq 4z
\end{cases}$$

> **Scenario 2B**

$-x_iz$ 之于 max

$$\max\;50z-(10x_1+12x_2)z$$

$$s.t.\begin{cases}
2x_1+x_2\geq 6 \\
x_1+2x_2\geq 8 \\
x_1,x_2\geq 0 \\
z\in\{0,1\}
\end{cases}$$

Set $w_1\geq x_1z$，同样这里也 **<font color=blue>不能</font>** 像 Senario 1B 那样使用 $w_1\geq x_1+z-1$ 来替代

首先考虑 $w_1\geq x_1z$，我们希望能通过一个只包含加减的线性表达式来实现:
- 当 $z=0$, $w_1\geq$ 小于或等于0的数
- 当 $z=1$, $w_1\geq x_1$

**那么如何让这个线性表达式满足当 $z=0$ 时一定小于或等于0呢？** 观察关于 $x_1,x_2$ 的两个不等式，发现 $x_1\geq 8$ 是不等式成立的充分条件，因此构造 $w_1\geq x_1-8(1-z)$。同理 $w_2\geq x_2-6(1-z)$, therefore:

$$\max\;50z-10w_1-12w_2$$

$$s.t.\begin{cases}
... \\
w_1\geq x_1-8(1-z)\\
w_2\geq x_2-6(1-z)\\
w_1,w_2\geq 0
\end{cases}$$

> **Scenario 2C & 2D**

$x_iz$ 之于 Constraints。结合 Senario 1C, 1D, 2A, 2B

$$\max ...\;\;\;s.t.\begin{cases}
x_1z\geq 5x_2 \\
x_1+x_2\leq 10\\
x_1,x_2\geq 0\\
z\in\{0,1\}
\end{cases}\implies s.t.\begin{cases}
w\geq 5x_2\\
x_1+x_2\leq 10\\
x_1,x_2\geq 0\\
z\in\{0,1\}\\
w\leq x_1,w\leq 10z\\
w\geq 0
\end{cases}$$

类似的

$$\max ...\;\;\;s.t.\begin{cases}
x_1z\leq 5x_2 \\
x_1+x_2\leq 10\\
x_1,x_2\geq 0\\
z\in\{0,1\}
\end{cases}\implies s.t.\begin{cases}
w\leq 5x_2\\
x_1+x_2\leq 10\\
x_1,x_2\geq 0\\
z\in\{0,1\}\\
w\geq x_1-10(1-z)\\
w\geq 0
\end{cases}$$
