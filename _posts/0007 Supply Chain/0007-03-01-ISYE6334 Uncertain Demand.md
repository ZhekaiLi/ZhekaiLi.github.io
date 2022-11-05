---
layout: post
title: ISYE6334 Uncertain Demand
categories: Supply-Chain
description:
keywords: SCE, Supply-Chain
mathjax: true
topmost: true
---

# Multi-period Inventory Model with Uncertain Demand
# 1. EOQ with Uncertain Demand (Ch 16.6)

Notations:
- $K=$ set up cost per order
- $h=$ holding cost per item per time
- $L=$ lead time (positive, could be constant or stochastic)
- $D=$ demand (annually, stochastic) 
- $c_B=$ backorder cost per item
- $OHI(t)=$ on-had inventory at time $t$
- $B(t)=$ # backordered items at time $t$
- $I(t)=OHI(t)-B(t)$
- $B_r=$ # backordered items during the lead time with reorder point $r$ 
- <span style="background-color: yellow; color: black;">$q=$ order quantity</span>
- <span style="background-color: yellow; color: black;">$r=$ reorder point</span>

Derived Notations:
- $ss = r-E[X]$ (safety stock)
- average stock level $=ss+q/2$ 

> $X$ is a random variable representing <span style="background-color: yellow; color: black;">demand during lead time</span>
> - If demand during each period is independent and $L$ constant
> $$E[X]=L\cdot E[D]\text{ and }Var(X)=L\cdot Var(D)$$
> - If demand during each period is independent, as well as $L$
> $$E[X]=E[L]E[D]\text{ and }Var(X)=E[L]Var(D)+E[D^2]Var(L)$$

## 1.1 Back-ordered Case
$$TC(q,r)=\text{set up cost + holding cost + backordered cost + no-care}$$

- "$\text{no-care}$" indicates the costs that have nothing to do with $q,r$, including **purchasing cost** ($E[D]p$), **in-transit cost** ($E[D]Lh$)
- 
<center>
    <img src="/images/2022-11/pic0314.jpeg" width="45%"> <br>
</center><br>

> $$\begin{aligned}
TC(q,r)
&=K\frac{E[D]}{q}+h\cdot\frac{1}{2}[(r-E[X]+q)+(r-E[X])]+c_BE[B_r]\frac{E[D]}{q} \\
&=K\frac{E[D]}{q}+h(r-E[X]+\frac{q}{2})+c_BE[B_r]\frac{E[D]}{q} \\
\end{aligned}$$

To find the optimal $q$ and $r$, we need the expression of $E[B_r]$ and $\frac{\partial}{\partial r}E[B_r]$:
- $E[B_r]=E[(X-r)^+]=\int_r^\infty(x-r)f(x)dx$
- $\frac{\partial}{\partial r}E[B_r]=-Pr(X>r)$

关于公式 $\frac{\partial}{\partial r}E[B_r]$ 的理解: 该公式的数值随着 $r$ 的增加逐渐从 $-1\to 0$, 这意味着 $E[B_r]$ 将是一个单调递减的函数，符合我们的直觉(reorder point 越大, stockout 的数量越少)

> **Special Case: normally distributed $X$**
> (a) Firsly definde the **normal loss function** $L(\cdot)$
> $$L(c)=E[(Z-c)^+]=\phi(c)-c(1-\Phi(c))$$
> 
> where $Z\sim N(0,1)$; $\phi,\Phi$ are standard pdf and cdf
> (b) Lemma:
> $$L(-c)=c+L(c)$$
> 
> (c) Then for $X\sim N(\mu_X,\sigma^2_X)$
> $$E[B_r]=E[(X-r)^+]=\sigma_XL(\frac{r-\mu_X}{\sigma_X})$$

Assume $X$ is normally distributed (special case), then we are ready to calculate the optimal $q$ and $r$:

> $$q^*=\sqrt{\frac{2E[D](K+c_BE[B_r])}{h}}\text{ and }Pr(X>r^*)=\frac{hq^*}{c_BE[D]}$$

**<font color=red>Note: there is a bug that $q^*,r^*$ are dependent to each other</font>. Two approaches:**
- Heuristic: approximate $q^*$ by $\text{EOQ}=\sqrt{2KE[D]/h}$, and then solve $r^*$
- Exact: start with EOQ and solve iteratively until $(q,r)$ converges

## 1.2 Lost Sales Case
Lost Sale means customer will not want any late items, therefore cost of lost sales per item per time is
$$c_{LS}=c_B+\text{(sale price - sell price)}$$

> $$TC(q,r)= K\frac{E[D]}{q}+h(r-E[X]+E[B_r]+\frac{q}{2})+c_{LS}E[B_r]\frac{E[D]}{q}$$

> $$q^*=\sqrt{\frac{2E[D](K+c_{LS}E[B_r])}{h}}\text{ and }Pr(X>r^*)=\frac{hq^*}{hq^*+c_{LS}E[D]}$$


# 2. Service Levels for a Continuous-Review Policy (Ch 16.7)

## 2.1 Fillrate


## 2.2 Stockout Probablity

> **Useful properties of Gamma**
> (a) If $G_1,G_2\sim\Gamma(k,\theta)$ and they are independent, then $G_1+G_2\sim\Gamma(k_1+k_2,\theta)$
> (b) If $G\sim\Gamma(k,\theta)$, then $cG\sim\Gamma(k,c\theta)$ for a real constant c





# Discrete-Time Markov Chains
vs. Continuous-Time Markov Chains

# 6.1 Definition of DTMC
A DTMC has the following elements:
1. $X_n=$ system state at $n$
   can be \$ after $n$ tosses, or inventory level at the end of week $n$
2. State space $S$: set of possible outcomes(possible values of $x_n$)
3. Transition(probability) matrix $\mathbf{P}=[P_{ij}]$
   $$P_{ij}=Pr\Big(X_{n+1}=j\vert X_n=i\Big)$$
4. Initial(state) distribution $\mathbf{a}^{(0)}$
   $$a^{(0)}_i=Pr(X_0=i)$$






