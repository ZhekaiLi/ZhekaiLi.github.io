
# Stochastic Process
A **stochastic process** is a family of random variables $\{X_t, t\in\mathcal{T}\}$, where $\mathcal{T}$ is an index set.
- Example: Amount of inventory in stock at the start of day $t$

## 1. Stationary Process
$\{X_t\}$ is **stationary** IF $\forall s$, 
$(X_{s+t_1}, X_{s+t_2},\ldots, X_{s+t_k})$ is independent of $s$ when $t_1<t_2<\ldots<t_k$.
- Stationary implies equal mean and varaince $\mu = E(X_t)$ and $\sigma^2 = Var(X_t)$

### 1.1 Week Stationary
$\{X_t\}$ is **weakly stationary** IF the $X_t$ have equal mean, variance $\sigma_X = Var(X_t) < \infty$, and $Cov(X_t, X_{t+s})$ depends only on "lag" $s$.

If the joint distributions of the $X_t$ are normal with nonsingular covariance matrices, **weak stationarity implies stationarity** because the joint distribution of the vector $(X_{s+t_1}, X_{s+t_2},\ldots, X_{s+t_k})$ uniquely defined by the respective covariance matrix whose elements are independent of s.

考虑如下示例，因为 week stationarity，我们已知 (1) $\mu_t=\mu_{t+s}=\mu$, $\sigma_t=\sigma_{t+s}=\sigma_X$ (2) $\rho$ 只与 $s$ 相关。因此 $(X_t, X_{t+s})$ 与 $(X_{t+k}, X_{t+s+k})$ 的联合分布完全相同，从而证明了 stationarity

\[
\begin{bmatrix}
X_t \\
X_{t+s}
\end{bmatrix}
\sim \mathcal{N}
\left(
\begin{bmatrix}
\mu_t \\
\mu_{t+s}
\end{bmatrix},
\begin{bmatrix}
\sigma^2_t & \rho\sigma_t\sigma_{t+s} \\
\rho\sigma_t\sigma_{t+s} & \sigma^2_{t+s}
\end{bmatrix}
\right)
\]

### 1.2 Autocovariance and Autocorrelation
Autocovariance: $C_k = Cov(X_t, X_{t+k})$
Autocorrelation: $\rho_k = Corr(X_t, X_{t+k}) = C_k/\sigma_X^2$

\[
E\left(\sum_{i=1}^{n} a_i X_i + b\right) = \left(\sum_{i=1}^{n} a_i \mu\right) + b
\]

\[
\begin{aligned}
\text{Var}\left(\sum_{i=1}^{n} a_i X_i + b\right) &= \sum_{i=1}^{n} a_i^2 \text{Var}(X_i) + 2 \sum_{i<j} a_i a_j \text{Cov}(X_i, X_j)\\
&= \left(\sum_{i=1}^{n} a_i^2\right) \sigma_X^2 + 2 \sum_{i<j} a_i a_j C_{j-i}
\end{aligned}
\]

\[
\text{Cov}\left(\sum_{i=1}^{n} a_i X_i + b, \sum_{j=1}^{m} c_j Y_j + d\right) = \sum_{i=1}^{n} \sum_{j=1}^{m} a_i c_j \text{Cov}(X_i, Y_j)
\]

### 1.3 Paramter Estimation
$\delta=\mu=E(X_t)$

**(1) Sample mean**
$\delta_n = \bar{X}_n = \frac{1}{n}\sum_{i=1}^{n} X_i$

**(2) Variance of sample mean**
$$\begin{aligned}
Var(\bar{X}_n) &= \frac{1}{n^2} Var\left(\sum_{i=1}^{n} X_i\right) = \frac{1}{n^2}\left[\sum_{i=1}^{n} Var(X_i) + 2\sum_{i<j} C_{j-i}\right]\\
&= \frac{1}{n^2}\left[n\sigma_X^2 + 2\sum_{k=1}^{n-1} (n-k) C_k\right]\\
&= \frac{\sigma_X^2}{n}\left[1 + 2\sum_{k=1}^{n-1} \left(1-\frac{k}{n}\right) \rho_k\right]\\
&= \frac{\sigma_X^2}{n}a_n
\\
\end{aligned}$$

Since $Var(\bar{X}_n) = \sigma^2_X/n$ if $X_t$ are independent, we can see $\frac{2}{n}\sum_{k=1}^{n-1} \left(1-\frac{k}{n}\right) C_k$ as the **autocorrelation penalty**

**(3) Variance**
\[
\sigma^2 = \lim_{{n \to \infty}} n \text{Var}(\bar{X}_n) = \sum_{{k=-\infty}}^{\infty} C_k = \sigma_X^2 + 2 \sum_{{k=1}}^{\infty} C_k
\]



If the following exists

\[
\lim_{{n \to \infty}} \sum_{{k=1}}^{n-1} \left(1 - \frac{k}{n}\right) C_k < \infty \iff \sum_{{k=-\infty}}^{\infty} C_k < \infty
\]

### 1.4 CLT for Stationary Processes
\[
\frac{\bar{X}_n - \mu}{\sigma/\sqrt{n}} \xrightarrow{d} \mathcal{N}(0,1)
\]


When $X_t$ are positively correlated, so that $a_n > 1$
\[
E\left(\frac{S^2_n}{n}\right) = \frac{n/a_n - 1}{n - 1} \text{Var}(\bar{X}_n) < \text{Var}(\bar{X}_n)
\]

then the confidence interval

\[ \bar{X}_n \pm t_{n-1,1-\alpha/2} \frac{S_n}{\sqrt{n}} \]






## 2. Moving Average Process
Suppose $\{\varepsilon_i\}$ is an i.i.d. sequence with $E(\varepsilon_i)=0$ and $Var(\varepsilon_i)=\sigma^2_\varepsilon < \infty$. The **MA Process** of order $q$ is defined by

\[ X_t = \beta_0\varepsilon_t + \beta_1\varepsilon_{t-1} + \ldots + \beta_q\varepsilon_{t-q} \]

where $\beta_0 \neq 0$ and $\beta_1, \ldots, \beta_q$ are constants.

We can easily know that $E(X_t)=0$, $Var(X_t)=\sigma^2_\varepsilon\sum_{i=0}^{q}\beta_i^2$

\[C_k = Cov(X_t, X_{t+k}) = \begin{cases}
\sigma^2_\varepsilon\sum_{i=0}^{q-k}\beta_i\beta_{i+k} & \text{if } 0 \leq k \leq q\\
0 & \text{if } k > q
\end{cases}\]

that's because $Cov(\varepsilon_i, \varepsilon_j)=0$ for $i \neq j$.






## 3. Autoregressive Process
**AR Process** is defined as
\[X_t=\alpha_1X_{t-1} + \alpha_2X_{t-2} + \ldots + \alpha_pX_{t-p} + \varepsilon_t\]

where $\alpha_1, \ldots, \alpha_p$ are constants and $\varepsilon_t$ is a white noise process with $E(\varepsilon_t)=0$ and $Var(\varepsilon_t)=\sigma^2_\varepsilon < \infty$.

### 3.1 AR(1) Process
\[X_t=\alpha X_{t-1} + \varepsilon_t\]

assuming zero mean $E(X_t)=0$. Therefore,
\[X_t=\alpha^tX_0 + \sum_{i=0}^{t-1}\alpha^i\varepsilon_{t-i}\]

when $|\alpha| < 1$ and $t \to \infty$, we have

\[X_t = \sum_{i=0}^{\infty}\alpha^i\varepsilon_{t-i}\]

if non-zero mean $E(X_t)=\mu$, then $X_t-\mu$ is AR(1)

Because $\varepsilon_t$ are iid, then the marginal variance:

\[\sigma_X^2 = Var(X_t) = \sigma^2_\varepsilon(1+\alpha^2+\alpha^4+\ldots) = \frac{\sigma^2_\varepsilon}{1-\alpha^2}\]

If we multiply both sides of $X_t=\alpha X_{t-1} + \varepsilon_t$ by $X_{t-1}$ and take expectation, we have

\[\begin{align*}
X_{t-k}X_t &= \alpha X_{t-k}X_{t-1} + X_{t-k}\varepsilon_t \\
E(X_{t-k}X_t) &= \alpha E(X_{t-k}X_{t-1}) + E(X_{t-k})E(\varepsilon_t) \quad \text{(independence)} \\
C_k &= \alpha C_{k-1}
\end{align*}
\]

that's because:
- $Cov(X,Y)=E[(X-E(X))(Y-E(Y))]$
- $E[X_t]=0$ and $E[\varepsilon_t]=0$

Plus that $C_0=Var(X_t)=\sigma^2_X$, we have

\[C_k = \alpha^k\sigma^2_X\;\;\;\text{and}\;\;\;\rho_k=\alpha^k\]

Some Facts:
- AR(1) is weakly stationary if $|\alpha| < 1$

### 3.1 Gaussian AR(1) Process
Assume $\varepsilon_t \sim \mathcal{N}(0, 1-\alpha^2)$ and $X_0 \sim \mathcal{N}(0, 1)$

Easily to show that
1. $X_t \sim \mathcal{N}(0, 1)$ (by take expectation of AR(1) expression)
2. $C_k = \alpha^k$ (since $\sigma_X^2=1$)

The asymptotic variance of this process


