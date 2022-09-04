---
layout: post
title: Class Notes (CEE491)
categories: Probability Theory
description: Personal Notes
keywords: CEE491，Risk-Analysis，Probability, Decision
mathjax: true
---

# L6

> **Probability Mass Function (PMF)**

Let $X$ be a random variable, and $x_1,...,x_M$ are possible outcomes

Then we define PMF as:
$$p_X(x)=P(X=x)$$

And the probability of a certain range is:
$$P(a< X\leq b)=F_X(b)-F_X(a)$$

> **Probability Density Function (PDF)**

For continuous random variables, the probability at any single point is zero. That's why we need PDF:

$$P(a< X\leq b)=\int_a^bf_X(x)dx$$

> **Cumulative Distribution Function (CDF)**

For discrete r.v.:
$$F_X(a)=P(X\leq a)=\sum_{x\leq a}p_X(x)$$

For continuous:
$$F_X(a)=P(X\leq a)=\int_{-\infty}^af_X(x)dx$$

$$f_X(x)=\frac{dF_X(x)}{dx}$$

But for **Mixed Random Varaibles**, 其实就是两者的结合体，但是体现在公式方面则会另有区别，详见 September 9 的课件







# Statistics Descriptor
**Expectation (mean)**: $E[X]=\mu_X=\begin{cases}\sum_{\forall x}xp(x) \\ \int_{-\infty}^\infty xf(x)dx\end{cases}$

**Median:** $x_{0.5}\to F(x_{0.5})=0.5$

**Mode:** $\tilde{x}\to \max f(x)=f(\tilde{x})$

**Mean Square:** $E[X^2]=\begin{cases}\sum_{\forall x}x^2p(x) \\ \int_{-\infty}^\infty x^2f(x)dx\end{cases}$

**Variance:** $V[X]=E[(X-\mu_X)^2]=E[X^2]-E[X]^2$
$$=\begin{cases}\sum_{\forall x}(x-\mu_X)^2p(x) \\ \int_{-\infty}^\infty (x-\mu_X)^2f(x)dx\end{cases}$$

**Standard Deviation (std):** $\sigma=\sqrt{V[X]}$

**Coefficient of Variance (c.o.v.):** $\delta=\sigma/\mu$

**Skewness Coefficient:** $\gamma=\frac{E[(X-\mu_X)^3]}{\sigma^3}$

> **Relations**

(1) $V[X]=E[X^2]-E^2[X]$

(2) $E[(X-\mu_X)^3]=E[X^3]-3E[X^2]E[X]+2E^3[X]$
Shape of $f(x)$ could be roughly known through:
$$E[(x-\mu_X)^3]\begin{cases} 
\gt 0 & \text{means it has a tail to rightside}\\
=0 & \text{symmetric}\\
<0 & \text{a tail to leftside}
\end{cases}$$


## Calculation Rules
(1) $E[aX]=aE[X], E[X+b]=E[X]+b$

(2) $V[aX]=a^2V[X], V[X+b]=V[X]$

(3) $V[X_1+X_2]=V[X_1]+V[X_2]$, where $x_1,x_2$ S.I.

(4) $V[X_1X_2]=E[X_1^2]E[X_2^2]-E^2[X_1]E^2[X_2]$

> **For Joint Distributions**

(1) $E[X+Y]=E[X]+ E[Y]$

(2) $cov(X,Y)=E[(X-\mu_X)]E[(Y-\mu_Y)]-E[X]E[Y]$

(3) $V(X+Y)=V(X)+2cov(X.Y)+V(Y)$





# 8. Discrete Probability Function
## 8.1 Bernoulli Distribution
$$P(x)=\begin{cases}
1-p & \text{for }x=0\\
p & \text{for }x=1
\end{cases}$$

In Bernoulli, just a **single** trial is conducted

## 8.2 Binomial
$$P(X=k)=\begin{pmatrix}n \\ k\end{pmatrix}p^k(1-p)^{n-k}$$

$$\begin{pmatrix}n \\ k\end{pmatrix}=C_n^k=C(n,k)=\frac{n!}{k!(n-k)!}$$

(1) $\mu_X=np$

(2) $V[X]=np(1-p)$

(3) $\sigma=\sqrt{np(1-p)}$

(4) $\delta=\frac{\sigma}{\mu} = \sqrt{\frac{1-p}{np}}$

(5) $E[(x-\mu_X)^3]=np(2p^3-3p+1)$

(6) $\gamma=\frac{E[(x-\mu_X)^3]}{\sigma^3}=\frac{1-2p}{\sqrt{np(1-p)}}$

## 8.3 Poisson
当一个随机事件，例如来到某公共汽车站的乘客、显微镜下某区域中的白血球等，以固定的平均瞬时速率 $\nu$（或称密度）随机且独立地出现时，那么这个事件在单位时间（面积或体积）内出现的次数或个数就近似地服从泊松分布 $P(x)$

$$P(X=x)=\frac{\nu^x}{x!}\exp(-\nu)$$

where $\nu>0, x=0,1,2,...$

(1) $\mu_X=\nu$

(2) $E[X^2]=\nu^2+\nu$

(3) $V[X]=E[X^2]-E^2[X]=\nu$

(4) $\sigma=\sqrt\nu$

(5) $\delta=\frac{1}{\sqrt\nu}$

示例：已知一个粒子平均每小时衰变5次，则其在3个小时内共衰变10次的概率为 $P(x=10)=\frac{(5*3)^{10}}{10!}\exp(-5*3)$

## 8.4 Exponential
$$f(x)=\lambda\exp(-\lambda x)$$

$$F(x)=1-\exp(-\lambda x)$$

where $x\geq0, \lambda>0$

(1) $\mu_X=\frac{1}{\lambda}$

(2) $E[X^2]=\frac{2}{\lambda^2}$ 

(3) $V[X]=\frac{1}{\lambda^2}$

(4) $E[(x-\mu_X)^3]=\frac{2}{\lambda^3}$

(5) $\gamma=2$

Using part of exponential distribution, we could construct a new pdf function (unchecked):
$$f(x)=cx^{k-1}\exp(-\lambda x)$$

where $k$ is the shape parameter, $c>0$

As a pdf, it should satisfy $\int_{-\infty}^\infty f(x)dx=1$

$$\begin{split}
   \int_{-\infty}^\infty f(x)dx &= \int_0^\infty cx^{k-1}\exp(-\lambda x)dx \\
   &= c\int_0^\infty(\frac{u}{\lambda})^{k-1}\exp(-u)\frac{1}{\lambda}du \\
   &= \frac{c}{\lambda^k}\int_0^\infty u^{k-1}\exp(-u)du \\
   &= \frac{c}{\lambda^k}\Gamma(k)
\end{split}$$

Here we define **Gamma Function** as $\Gamma(k)=\int_0^\infty u^{k-1}\exp(-u)du$, then $c=\frac{\lambda^k}{\Gamma(k)}$, so finally:
$$f(x)=\frac{\lambda^k}{\Gamma(k)}x^{k-1}\exp(-\lambda x)$$

> **Properties of $\Gamma(k)$**
(1) $\Gamma(k) = (k-1)!$
(2) $\Gamma(k+1) = k\Gamma(k)$
(3) $\Gamma(\frac{1}{2})=\pi$

## 8.5 Gamma
Gamma 分布等同于多个独立且相同分布（idd）的指数分布变量的和的分布

<span style="background-color: yellow; color: black;">Same as the equation mentioned right above</span>

$$f(x)=\frac{\lambda(\lambda x)^{k-1}}{\Gamma(k)}\exp(-\lambda x)$$

$$F(x)=\frac{\Gamma(k, \lambda x)}{\Gamma(k)}$$

> **Process of getting CDF**
$$\begin{split}
F(x) &=\int_0^x \frac{\lambda(\lambda z)^{k-1}}{\Gamma(k)}\exp(-\lambda z)dz \\
& \text{let }u=\lambda z, dz=\frac{1}{\lambda}du,\text{ then}\\
&= \int_0^{\lambda x} \frac{u^{k-1}}{\Gamma(k)}\exp(-u)du \\
&= \frac{1}{\Gamma(k)}\int_0^{\lambda x} u^{k-1}\exp(-u)du \\
&= \frac{\Gamma(k, \lambda x)}{\Gamma(k)}
\end{split}$$

(1) $E[X^m]=\frac{\Gamma(k+m)}{\lambda^m\Gamma(k)}=\frac{(k+m-1)(k+m-2)...k}{\lambda^m}$

> **Process**
$$\begin{split}
E[X^m] &= \frac{\Gamma(k+m)}{\Gamma(k+m)}\frac{\lambda^m}{\lambda^m}\int_0^\infty x^m\frac{\lambda(\lambda x)^{k-1}}{\Gamma(k)}\exp(-\lambda x)dx \\
&= \frac{\Gamma(k+m)}{\lambda^m\Gamma(k)} \int_0^\infty \frac{\lambda(\lambda x)^{k+m-1}}{\Gamma(k+m)}\exp(-\lambda x)dx \\
&= \frac{\Gamma(k+m)}{\lambda^m\Gamma(k)}
\end{split}$$

(2) $E[X]=\frac{k}{\lambda}$, $E[X^2]=\frac{k(k+1)}{\lambda^2}$, $E[X^3]=\frac{k(k+1)(k+2)}{\lambda^3}$

(3) $V[X]=\frac{k}{\lambda^2}, \delta=\frac{1}{\sqrt{k}}, \gamma=\frac{2}{\sqrt k}$

(4) When $k=1$, $f(x)=\lambda\exp(-\lambda x)$, **exponential distribution!**

# 9. Continuous Probability Functions
## 9.1 Uniform Distribution
$$f(x)=\frac{1}{b-a}\quad F(x)=\frac{x-a}{b-a}$$

where $a\leq x\leq b$

(1) $E[X^m] = \int_{a}^b \frac{x^m}{b-a}dx = \frac{b^{m+1}-a^{m+1}}{(m+1)(b-a)}$

(2) $E[X]=\frac{b+a}{2}$, $E[X^2]=\frac{b^2+ab+a^2}{3}$$

(3) $V[X]=\frac{(b-a)^2}{12}$, $\sigma=\frac{b-a}{2\sqrt 3}$

(4) $E[(X-\mu_X)^3]=0$, because of symmetric (see Section 7.1)

(5) **Standard Uniform Distribution**: $b=1, a=0$


## 9.2 Normal
$N(\mu, \sigma^2)$
$$f(x)=\frac{1}{\sqrt{2\pi}\sigma}\exp[-\frac{1}{2}(\frac{x-\mu}{\sigma})^2]$$

$$F(x)=\Phi(\frac{x-\mu}{\sigma})$$

(1) $E[(X-\mu)^m]=0$ for odd $m$, $\frac{m!\sigma^m}{(m/2)!2^{m/2}}$ for even $m$

### 9.2.1 Standard Normal Distribution
Denoted as $U$ or $N(0,1)$
$$f_U(u)=\phi(u)=\frac{1}{\sqrt{2\pi}}\exp(-\frac{1}{2}u^2)$$

$$F_U(u)=\Phi(u)=\int_{-\infty}^u\frac{1}{\sqrt{2\pi}}\exp(-\frac{1}{2}z^2)dz$$

Obviously, $\Phi(-u)=1-\Phi(u)$

### 9.2.2 Lognormal Distribution
$LN(\lambda, \xi)$:
$$f(x)=\frac{1}{\sqrt{2\pi}\xi x}\exp[-\frac{1}{2}(\frac{\ln x-\lambda}{\xi})^2]$$

$$F(x)=\Phi(\frac{\ln x-\lambda}{\xi})$$

where $x>0$

(1) $\mu=\exp(\lambda+\frac{1}{2}\xi^2)$

(2) $\delta=\frac{\sigma}{\mu}=\sqrt{\exp(\xi^2)-1}$

(3) $\xi=\sqrt{\ln(1+\delta^2)}$

(4) $\lambda=\ln\mu-\frac{1}{2}\xi^2$

(5) $\xi\approx\delta$, when $\delta^2$ is very small










# L10
$$P(E)=\sum_{\forall x}P(E\vert x)p(x)$$

$$P(E)=\int P(E\vert x)f(x)dx$$

## 10.1 Conditional Distribution
$f(x\vert E)$:
$$\begin{split}
f(x\vert E)dx &= P(x\leq X\leq x+dx\vert E) \\
&= \frac{P(x\leq X\leq x+dx\cap E)}{P(E)}
\end{split}$$

And for $E_1,E_2,...,E_m$ mutually exclusive & collectively exhausted
$$f(x)=\sum_{i=1}^m f(x\vert E_i)P(E_i)$$

Applying Baye's rule:
$$f(x\vert E)=\frac{P(E\vert x)}{P(E)}f(x)$$

## 10.2 Joint PMF
$$p_{XY}(x,y)=P(X=x\cap Y=y)$$

(1) $0\leq p(x,y)\leq 1$

(2) $\sum_{\forall x}p(x,y)=p(y)$ **consistency rule**

(2) $\sum_{\forall x}\sum_{\forall y}p(x,y)=1$

## 10.3 Conditional PDF
$$p_{X\vert Y}(x\vert y)=P(X=x\vert Y=y)=\frac{p_{XY}(x,y)}{p_Y(y)}$$

# L13
## 13.1 Conditional Discripter
(1) $E[X\vert Y]=\int xf(x\vert y)dx$

(2) $V[X\vert Y]=\int (x-\mu_{x\vert y})^2f(x\vert y)dx$

(3) $E[X]=\int E[X\vert Y]f(y)dy$

## 13.2 Sample Space
$X=[x_1, x_2, ..., x_M], Y=[y_1, y_2, ..., y_M]$

(1) Sample mean: $E[X]=\bar{x}=\sum x_i/M$

(2) Sample variance: $S_x^2=\frac{1}{M}\sum(x-\bar{x})^2$

(3) $E[XY]=\frac{1}{M}\sum x_iy_i$

(4) $Cov[XY]=E[XY]-\bar{x}\bar{y}$

(5) $\rho=Cov[XY]/S_xS_y$

对于样本 $X,Y$ 在坐标系中的图像，如果是比较细的直线（点分布密集）则 $\rho=1$ or $-1$；如果比较粗（点分布稀疏），则 $\rho\in(-1,0)\cup(0,1)$；如果是分散的团状分布，则 $\rho=0$

# L14 Multinormal Distribution
$$f(\bf{x})=(2\pi)^{-\frac{n}{2}}\vert\bf\Sigma\vert^{-\frac{1}{2}} \exp\Big[-\frac{1}{2}(\bf{x}-\bf{\mu})^T\vert\bf\Sigma\vert^{-1}(\bf{x}-\bf{\mu})\Big]$$

where
1. $\bf{x-\mu}=[x_1-\mu_1,...,x_n-\mu_n]^T$
2. $\bf\Sigma=\begin{bmatrix}
   \sigma_1^2 & 0 & ... & 0 \\
   0 & \sigma_2^2 & ... & 0 \\
   ... & ... & ... & .... \\
   0 & ... & 0 & \sigma_n^2
\end{bmatrix}$

### 14.1 (m=1) (Univariate) Normal Distribution
$$f(x)=\frac{1}{\sqrt{2\pi}\sigma}\exp\Big[-\frac{1}{2}(x-\mu)\sigma^{-2}(x-\mu)\Big]$$


### 14.2 (m=2) Bi-variate Normal Distribution
$$f(x_1,x_2)=\frac{1}{2\pi\sigma_1\sigma_2\sqrt{1-\rho^2}}\exp\Big\{-\frac{1}{2(1-\rho^2)}\Big[(\frac{x_1-\mu_1}{\sigma_1})^2-2\rho(\frac{x_1-\mu_1}{\sigma_1})(\frac{x_2-\mu_2}{\sigma_2})-(\frac{x_2-\mu_2}{\sigma_2})^2\Big]\Big\}$$