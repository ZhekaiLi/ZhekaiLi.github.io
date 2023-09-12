---
layout: post
title: Probability - Advanced
categories: Probability-Theory
description: Personal Notes
keywords: Risk-Analysis，Probability, Decision
mathjax: true
---



# 1. Model Evaluation
**R-squared** (R squared)
$$R^2=1-\frac{\sum(\hat{y}_i-y_i)^2}{\sum(y_i-\bar{y})^2}$$

$R^2=1$ 最佳预测，所有的预测值等于真值
$R^2\leq0$ 无效预测，预测表现逊于全部取平均值，说明模型很可能有误

# 2. Core to Solve Problem
The key thing to calculate event probability is understanding the question and given conditions, and converting them into math(probability) equations

## 2.1 Ex1
> **Given**: Alice has 3 kids and we know one of them is a girl
> **Ask**: What is the probability that all children are girls?
1. Convert question into equation: denote $n=$ number of girls
$$P(n=3\vert\text{one is girl})=\text{?}=\frac{P(\text{one is girl}\vert n=3)}{P(\text{one is girl})}P(n=3)$$
2. Calculate each components
$P(n=3)=1/8$
$P(\text{one is girl})=1/2$
$P(\text{one is girl}\vert n=3)=1$
3. Therefore, answer is 
$$P(n=3\vert\text{one is girl})=1/4$$

The possible obstacle here is we might don't know $P(\text{one is girl})=1/2$, so just think it easy because the probability for a kid to be boy and girl are equal



# 4. Central Limit Theorem (CLT)

For $X_i,i=1,2,...,n$ are **<font color=blue>iid</font>** (independent and identically distributed) with mean $\mu$ and variance $\sigma^2$ (regardless of the distribution). CLT implies that for large $n$(>30)

$$\begin{cases}
\bar X=\frac{1}{n}\sum X_i\sim N(\mu,\frac{\sigma^2}{n})
\\
\sum X_i\sim N(n\mu,n\sigma^2)
\end{cases}$$

对于任何同独立分布的数据，$n>30$ 抽样的均值的分布，接近正态分布

<span style="background-color: yellow; color: black;">But even if we take **small** random samples, the CLT tells us that the average of our sample means will be close to the true population mean.</span>


# 5. Strong Law of Large Numbers (SLLN)
For $X_i,i=1,2,...,n$ are **<font color=blue>iid</font>**, if $\mu=E[X_i]$ is finite, then for large $n$
$$\frac{X_1+...+X_n}{n}=E[X_i]$$




# 6. Multiple(Joint) Distributions
## 6.1 Joint PMF
$$p_{XY}(x,y)=P(X=x\cap Y=y)$$

(1) $0\leq p(x,y)\leq 1$

(2) $\sum_{\forall x}p(x,y)=p(y)$ **consistency rule**

(2) $\sum_{\forall x}\sum_{\forall y}p(x,y)=1$

## 6.2 Conditional PDF
$$p_{X\vert Y}(x\vert y)=P(X=x\vert Y=y)=\frac{p_{XY}(x,y)}{p_Y(y)}$$

## 6.3 Sample Space
$X=[x_1, x_2, ..., x_M], Y=[y_1, y_2, ..., y_M]$

(1) Sample mean: $E[X]=\bar{x}=\sum x_i/M$

(2) Sample variance: $S_x^2=\frac{1}{M}\sum(x-\bar{x})^2$

(3) $E[XY]=\frac{1}{M}\sum x_iy_i$

(4) $Cov[XY]=E[XY]-\bar{x}\bar{y}$

(5) $\rho=Cov[XY]/S_xS_y$

对于样本 $X,Y$ 在坐标系中的图像，如果是比较细的直线（点分布密集）则 $\rho=1$ or $-1$；如果比较粗（点分布稀疏），则 $\rho\in(-1,0)\cup(0,1)$；如果是分散的团状分布，则 $\rho=0$

# 7. Point Estimation
$\{X_1,X_2,...\}$ is a sequence of i.i.d. random variables with mean $\mu=E[X_i]$ and variance $\sigma_X^2=Var(X_i)$.

However, with a limited number of observations, we can only **estimate** the true mean $\mu$ and variance $\sigma_X^2$.
## 7.1 Sample Mean and Variance

**(1) Sample mean**: (unbiased) point estimator of $\mu$ based on finite sample $\{X_1,...,X_n\}$:
$$\bar{X_n}=\frac{1}{n}\sum X_i$$

**(2) Sample variance**: (unbiased) point estimator of $\sigma_X^2$...:
$$\begin{aligned}
S_X^2=\frac{1}{n-1}\sum(X_i-\bar{X_n})^2&=\frac{1}{n-1}\Big[\sum X_i^2-2\bar{X_n}\sum X_i+n\bar{X_n}^2\Big] \\
&=\frac{1}{n-1}\Big[\sum X_i^2-n\bar{X_n}^2\Big]
\end{aligned}$$

为什么是 $n-1$ 而不是 $n$？简单理解就是因为如下式子:
$$\begin{aligned}
\frac{1}{n}\sum(X_i-\bar{X_n})^2&=\frac{1}{n}\sum\big[(X_i-\mu)+(\mu-\bar{X_n})\big]^2\\
&= \frac{1}{n}\Big[\sum(X_i-\mu)^2-2(\mu-\bar{X_n})\sum(\mu-X_i)+n(\mu-\bar{X_n})^2\Big]\\
&=\sigma_X^2 - (\mu-\bar{X_n})^2
\end{aligned}$$

我们发现只要 $\bar{X_n}$ 并不正好等于 $\mu$，那么使用 $n$ 作为分母来估计的方差就会偏小，因此选择 $n-1$ 作为分母，起到矫正的作用。至于为什么不是 $n-2$ 或者其他，这个就需要一些复杂的数学推导了

## 7.2 Confidence Interval of Mean
由于 sample mean 在本质上是一个随机变量，因此我们可以给出一个区间，来表示这个随机变量的取值范围，这个区间就是 **confidence interval**，通常表示为 
$$100(1-\alpha)\%\text{ CI}$$

又根据 CLT，只要样本数量 $n$ 足够大(>30)，其均值的分布就会接近正态分布，因此我们可以使用正态分布的性质来计算 sample mean's CI:
$$\bar{X_n}\pm t_{n-1,\alpha/2}\frac{S_X}{\sqrt{n}}=\bar{X_n}\pm H(n,\alpha)$$

where
- $t_{n-1,\alpha/2}$ is the $\alpha/2$ quantile of the $t$ distribution with $n-1$ degrees of freedom
- $H(n,\alpha)$ is called **half-length** function

## 7.3 Sample Size
假设我们想要知道多大的样本数量 ($n^*$) 能够使其均值 $\mu$'s 100(1-alpha)% CI has a **<font color=blue>specific half-length</font>** $H(n,\alpha)\leq H^*$ 

首先，我们无法直接求出 $n$ 的大小，因为根据以下公式，$t,S_X,n$ 都和样本数量相关
$$t_{n-1,\alpha/2}\frac{S_X}{\sqrt{n}}=H^*$$

因此我们可以通过以下步骤求解 $n^*$:
1. Set an initial guess $n_0$, calculate $H(n_0,\alpha)$
2. If $H(n_0,\alpha)\leq H^*$, then use $n^*=n_0$
3. Else, since $H(n,\alpha)$ is proportional to $1/\sqrt{n}$
$$\frac{\sqrt{n^*}}{\sqrt{n_0}}=\frac{H(n_0,\alpha)}{H(n^*,\alpha)}\geq\frac{H(n_0,\alpha)}{H^*}$$
therefore, we can approximate $n^*$ by
$$n^*=\Big\lceil\Big(\frac{H(n_0,\alpha)}{H^*}\Big)^2n_0\Big\rceil$$

## 7.4 Quantile Estimation
Given:
$$x_p = F^{-1}(p)\;\;\;\;\; p\in (0,1)$$

### (1) Core Principles
(1) While the expected value (mean) measures central tendency, <span style="background-color: yellow; color: black;">quantiles are used to measure risk</span>

(2) Confidence intervals (CIs) for means measure estimation **error**, not future risk

Snipaste_2023-08-28_22-59-38.png

**<font color=blue>Goal</font>**: compute a point estimate


# 8. Monte Carlo Integration
To estimate the mean of function $f(t)$, we can use the following formula:
$$\mu=\int_a^bf(t)dt$$

then we can reprent $t$ by a random variable that follows standard uniform distribution: $u\sim U(0,1)$:
$$t=a+(b-a)u\;\;\;\;\; dt=(b-a)du$$

$$\begin{aligned}
\mu&=\int_0^1(b-a)f\big[a+(b-a)u\big]du\\
&=\int_0^1 h(u)du = \int_0^1h(u)g_U(u)du\\
&=E[h(U)]
\end{aligned}$$

where
- $h(u)=(b-a)f\big[a+(b-a)u\big]$
- $g_U(u)=1$ is the pdf of $U(0,1)$

如此，令 $Y_i=h(U_i)$，则 $X_i$ 是一个随机变量，我们就把一个积分运算转换为了求解 $\mu$ 的一个 unbiased estimator，即 $\bar{Y_n}$ (见 Chp 7. Point Estimation)

例如，对于 $i=1,..,n$, firstly generate a sample of $U_i$ from $U(0,1)$, then calculate $X_i=a+(b-a)U_i\implies Y_i=h(U_i)=f(X_i)$, afterwards we have:
- mean and variance estimator
$$\bar{Y_n}=\frac{1}{n}\sum Y_i\;\;\;\;\; S_Y^2=\frac{1}{n-1}\sum(Y_i-\bar{Y_n})^2$$
- 100(1-alpha)% CI
$$\bar{Y_n}\pm t_{n-1,\alpha/2}\frac{S_Y}{\sqrt{n}}=\bar{Y_n}\pm H(n,\alpha)$$


