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



