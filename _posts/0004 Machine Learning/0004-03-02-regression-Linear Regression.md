---
layout: post
title: Linear and Non-Linear Regression
categories: Machine-Learning
description:
keywords: Machine-Learning, Linear-Regression, Regression, Python
mathjax: true
---

```python
import pandas as pd
import numpy as np
import sklearn
import matplotlib.pyplot as plt
```

# 1. Linear regression
## 1.1 Simple linear regression 
使用数据集 $[X_1, Y]$，训练目标函数 $\hat{y}=\theta_0 + \theta_1x$
### 1.1.1 Mathematical solution
<img src="/images/2022-03/Snipaste_2022-03-17_19-30-39.png" width="80%">

对上图 $\theta_1$ 公式的解释：
$$\theta_1 = \frac{\sum(x_i-\bar{x})[(\theta_0+\theta_1x_i)-(\theta_0+\theta_1\bar{x})]}{\sum(x_i-\bar{x})^2} =
\frac{\sum(x_i-\bar{x})^2\theta_1}{\sum(x_i-\bar{x})^2}$$

### 1.1.2 Python solution (sklearn)
1. 分割数据为 train + test
2. 提取数据集 $\{X_1\}, \{Y\}$，并转换为 $n\times 1$ 的 array
```py
# 假设数据已经转化成 pd.DataFrame()
msk = np.random.rand(len(df)) < 0.8
train_x = np.asarray(df[msk].X1).reshape(len(df[msk]), 1)
train_y = np.asarray(df[msk].Y).reshape(len(df[msk]), 1)

test_x = np.asarray(df[~msk].X1).reshape(len(df[~msk]), 1)
test_y = np.asarray(df[~msk].Y).reshape(len(df[~msk]), 1)
```

3. 训练模型并预测，再根据预测误差为模型打分（0-1）
```py
from sklearn import linear_model

regr = linear_model.LinearRegression()
regr.fit(train_x, train_y)

predictions = regr.predict(test_x)
score = sklearn.metrics.r2_score(test_y, predictions)
```

4. 绘制数据点以及表示回归结果的直线
```py
theta0 = regr.intercept_[0]
theta1 = regr.coef_[0][0]

plt.scatter(train_x, train_y_,  color='blue')
plt.plot(train_x, theta0 + theta1*train_x, '-r')
```

<img src="/images/2022-03/Snipaste_2022-03-16_20-07-26.png" width="40%">

## 1.2 Multiple linear regression

$$y=\theta_0 + \theta_1x_1 + ... + \theta_nx_n=\theta^TX$$

Python 代码类似 simple linear regression


# 2. Non-Linear regression
非线形回归的目标函数
<img src="/images/2022-03/Snipaste_2022-03-17_21-35-54.png" width="55%">

## 2.1 Polynomial regression
使用数据集 $[X_1, Y]$，训练目标函数 $y=\theta_0 + \theta_1x + \theta_2x^2$
- 分割数据为 train + test
- `train_x` $\to$ `train_x_poly`
$$\left[
    \begin{array}{l}
    x_{11} \\
    \vdots \\ 
    x_{1n}
    \end{array}
\right] \to \left[
    \begin{array}{l}
    1      & x_{11} & x_{11}^2  \\
    \vdots & \vdots & \vdots    \\ 
    1      & x_{1n} & x_{1n}^2 
    \end{array}
\right]$$

```py
from sklearn.preprocessing import PolynomialFeatures
from sklearn import linear_model

msk = np.random.rand(len(df)) < 0.8
train_x = np.asarray(df[msk].X1).reshape(len(df[msk]), 1)
train_y = np.asarray(df[msk].Y).reshape(len(df[msk]), 1)

test_x = np.asarray(df[~msk].X1).reshape(len(df[~msk]), 1)
test_y = np.asarray(df[~msk].Y).reshape(len(df[~msk]), 1)

poly = PolynomialFeatures(degree=2)
train_x_poly = poly.fit_transform(train_x)
test_x_poly = poly.fit_transform(test_x)
```
- 训练模型，预测 + 打分 + 画图

```python
regr = linear_model.LinearRegression()
train_y_poly = regr.fit(train_x_poly, train_y)
predictions = regr.predict(test_x_poly)
score = sklearn.metrics.r2_score(test_y, predictions)

theta_0 = regr.intercept_[0]
theta_1, theta_2 = regr.coef_[0][1], regr.coef_[0][2]

plt.scatter(train_x, train_y,  color='blue')
XX = np.arange(0.0, 10.0, 0.1)
yy = theta_0 + theta_1*XX + theta_2*XX**2
plt.plot(XX, yy, '-r' )
```

<img src="/images/2022-03/Snipaste_2022-03-17_08-40-00.png" width="40%">

(上图实际为 `PolynomialFeartures(degree=3)` 时的情况)

## 2.2 Other non-linear regression
其他形式的非线形回归可以借助 `scipy.optimize.curve_fit()` 求解，例如该链接内代码拟合了一个 sigmoid 函数: [Note-wiki-scipy-函数拟合](../../_wiki/python-lib-scipy.md#23-函数拟合)


