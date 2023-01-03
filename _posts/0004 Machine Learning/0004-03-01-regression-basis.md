<!-- ---
追求精品，暂不发布
layout: post
title: Regression Basis
categories: Machine-Learning
description:
keywords: Machine-Learning, Regression, Python
mathjax: true
--- -->


Regression is **the process of predicing a continuous value**, like predicting CO2 emmisions:
<img src="/images/2022-03/Snipaste_2022-03-16_16-21-41.png" width="80%">

## Model Evaluation
Split sample into:
- **Training** dataset to train the model
- **Testing** dateset to evaluate the model's accuracy

> **Evaluation method: K-fold cross-validation**
将数据集划分为K块（下图为四块），每次以其中一块作为测试集，其他为训练集，执行四次并计算 accuracy 的均值
<img src="/images/2022-03/Snipaste_2022-03-17_19-41-04.png" width="80%">

## Evaluation Matrics
> **Mean Abosolute Error**
$$MAE = \frac{1}{n}\sum_{i=1}^n \vert y_i-\hat{y}_i\vert$$

> **Mean Square Error**
$$MSE = \frac{1}{n}\sum_{i=1}^n(y_i-\hat{y}_i)^2$$

> **Root MSE**: $RMSE = \sqrt{MSE}$

> **Relative Absolute Error**
$$RAE = \frac{\sum_{i=1}^n\vert y_i-\hat{y}_i\vert}{\sum_{i=1}^n\vert y_i-\bar{y}\vert}$$
>
> - 分子：使用训练后的模型预测产生的误差
> - 分母：使用 $y=\bar{y}$ 预测产生的误差（基准误差）
>
> 因此 RAE 越小越好（说明模型误差远小于基准误差）

> **Relative Square Error**
$$RSE = \frac{\sum_{i=1}^n(y_i-\hat{y}_i)^2}{\sum_{i=1}^n(y_i-\bar{y})^2}$$

> **R Square** (<span style="background-color: yellow; color: black;">衡量线性回归的最佳指标</span>)
$$R^2 = 1-RSE$$

## Applications of regression
- Sales forecasting
- Satisfaction analysis
- Price estimation
- Employment income

## Regression algorithms
- Ordinal regression
- Poisson regression
- Fast forest quantile regression
- Linear, Polynomial, Lasso, Stepwise, Ridge regression
- Bayesian linear regression
- Neural network regression
- Decision forest regression
- Boosted decision tree regression
- KNN (K-nearest neighbors) 既可用于 classification 也可用于 regression
