---
layout: post
title: Queing Theory
categories: Operation-Research
description: Personal Notes
keywords: ICM, OR
mathjax: true
---

# 1 基本概念
<center>
    <img src="/images/2021-01/Snipaste_2021-01-14_10-26-29.jpg"> <br>
    <div style="color: #999;">图 1-1 排队模型</div>
</center><br>
## 1.1 排队系统的组成和特征
一般的排队过程都由输入过程、排队规则、服务过程三部分组成：
### 1.1.1 输入过程
输入过程是指顾客到来时间的规律性：
1. 顾客的组成可能是**有限**的，也可能是**无限**的。 
2. 顾客到达的方式可能是**一个一个**的，也可能是**成批**的。 
3. 顾客到达可以是相互**独立**的，即以前的到达情况对以后的到达没有影响；否则是**相关**的。 
4. 输入过程可以是**平稳的**，即相继到达的间隔时间分布及其数学期望、方差等数字特征都与时间无关；否则是**非平稳的**。

### 1.1.2 排队规则
排队规则指到达排队系统的顾客按怎样的规则排队等待：
1. **损失制（消失制）**。当顾客到达时，所有的服务台均被占用，顾客随即离去。
2. **等待制**。当顾客到达时，所有的服务台均被占用，顾客就排队等待，直到接受完服务才离去。例如出故障的机器排队等待维修就是这种情况。 
3. **混合制**。介于损失制和等待制之间的是混合制，即既有等待又有损失。有队列长度有限和排队等待时间有限两种情况，在限度以内就排队等待，超过一定限度就离去。 

排队方式还分为**单列、多列和循环队列**。

### 1.1.3 服务过程
1. **服务机构**。主要有以下几种类型：单服务台；多服务台并联（每个服务台同时为不同顾客服务）；多服务台串联（多服务台依次为同一顾客服务）；混合型。 
2. **服务规则**。按为顾客服务的次序采用以下几种规则： 
- 先到先服务，这是通常的情形。 
- 后到先服务，如情报系统中，最后到的情报信息往往最有价值，因而常被优先处理。 
- 随机服务，服务台从等待的顾客中随机地取其一进行服务，而不管到达的先后。
- 优先服务，如医疗系统对病情严重的病人给予优先治疗。

## 1.2 排队模型的符号表示
$$X /Y / Z / A/ B /C$$

- $X$ 表示顾客到达流或顾客到达间隔时间的分布
- $Y$ 表示服务时间的分布
- $Z$ 表示服务台数目
- $A$ 是系统容量限制
- $B$ 是顾客源数目
- $C$ 是服务规则，如先到先服务 FCFS，后到先服务 LCFS 等。

并约定，如略去后三项，即指 $X /Y / Z / \infty / \infty / FCFS$ 的情形。我们只讨论先到先服务 FCFS 的情形，所以略去第六项。

表示 $X,Y$，即顾客到达间隔时间和服务时间的分布的约定符号为：
- $M$：指数分布（ M 是 Markov 的字头，因为指数分布具有无记忆性，即 Markov性） 
- $D$：确定型（Deterministic） 
- $E_k$：k 阶爱尔朗(Erlang)分布 
- $G$：一般（general）服务时间的分布
- $GI$：一般相互独立（General Independent）的时间间隔的分布

## 1.3 排队系统的运行指标
1. **平均队长**：指系统内顾客数（包括正被服务的顾客与排队等待服务的顾客）的数学期望，记作 $L_s$。 
2. **平均排队长**：指系统内等待服务的顾客数的数学期望，记作 $L_q$。 
3. **平均逗留时间**：顾客在系统内逗留时间（包括排队等待的时间和接受服务的
时间）的数学期望，记作 $W_s$。 
4. **平均等待时间**：指一个顾客在排队系统中排队等待时间的数学期望，记作 $W_q$。 
5. **平均忙期**：指服务机构连续繁忙时间（顾客到达空闲服务机构起，到服务机
构再次空闲止的时间）长度的数学期望，记为 $T_b$。

# 2 输入过程与服务时间的分布
## 2.1 泊松流域指数分布
设 $N(t)$ 表示在时间区间 $[0,t)$ 内到达的顾客数($t > 0$)，令 $P_n(t_1,t_2)$ 表示在时间区间 $[t_1,t_2)$ 内有 $n(\geq0)$ 个顾客到达的概率，即

$$P_n(t_1,t_2) = P\{N(t_2) − N(t_1) = n\}\;\;(t_2 > t_1,n\geq 0)$$

当 $P_n(t_1,t_2)$ 合于下列三个条件时，我们说顾客的到达形成**泊松流**：
1. (**条件1**) 在不相重叠的时间区间内顾客到达数是相互独立的，我们称这性质为无后效性。 
2. (**条件2**) 对充分小的 $\Delta t$，在时间区间 $[t,t + \Delta t)$ 内，顾客到达的概率与 $t$ 无关，而约与区间长 $\Delta t$ 成正比，即 
$$\tag{1} P_1(t,t + \Delta t) = λ\Delta t + o(\Delta t)$$
其中 $o(\Delta t)$，当 $\Delta t\to 0$ 时，是关于 $\Delta t$ 的高阶无穷小。$\lambda(> 0)$ 是常数，它表示单位时间有一个顾客到达的概率，称为概率强度。 
3. (**条件3**) 对于充分小的 $\Delta t$，在时间区间 $[t,t +\Delta t)$ 内有两个或两个以上顾客到达的概率极小，以致可以忽略，即 
$$\tag{2} \sum_{n=2}^\infty P_n(t,t+\Delta t)=o(\Delta t)$$

在上述条件下，我们研究顾客到达数 $n$ 的概率分布。简记 $P_n(0,t)=P_n(t)$

由条件1与条件2：
$$\begin{aligned}
& P_0(t+\Delta t)=P_0(t)P_0(\Delta t) \\
& P_n(t+\Delta t)=\sum_{k=0}^n P_{n-k}(t)P_k(\Delta t)
\end{aligned}$$

由条件2与条件3：
$$P_0(\Delta t)=1-\lambda\Delta t+o(\Delta t)$$

因而有：
$$\begin{aligned}
& \frac{P_0(t+\Delta t)-P_0(t)}{\Delta t}=-\lambda P_0(t)+\frac{o(\Delta t)}{\Delta t} \\
& \frac{P_n(t+\Delta t)-P_n(t)}{\Delta t}=-\lambda P_n(t)+\lambda P_{n-1}(t)+\frac{o(\Delta t)}{\Delta t}
\end{aligned}$$

假设所涉函数可导，由上式可得以下微分方程：
$$\begin{aligned}
& \frac{dP_0(t)}{dt}=-\lambda P_0(t) \\
& \frac{dP_n(t)}{dt}=-\lambda P_n(t)+\lambda P_{n-1}(t)\;\; n=1,2,...
\end{aligned}$$