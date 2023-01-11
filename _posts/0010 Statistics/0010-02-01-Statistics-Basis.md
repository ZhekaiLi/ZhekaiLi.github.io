---
layout: post
title: Statistics - Basis
categories: Statistics
description: Personal Notes
keywords:
mathjax: true
---


<center>

# Statistics - Basis
</center>

# 1. Data Description
## 1.1 Middle
1. **Mean**
2. **Medium**: 中位数 $(n+1)/2$
3. **Mode**: 众数
   - 可能没有众数: 每个数据都不一样
   - 可能有多个众数: [1,2,2,3,3] 中的 2 和 3

## 1.2 Variability
> **Range** = max - min

> **Standard deviation**
$$\sigma=\sqrt{\frac{\sum(x_i-\bar{x})^2}{N-1}}$$

> **Z-Score**: a data point's distance from the mean (in standard deviation) 是一种显示某个数据偏离程度的标准化的指标
$$\text{z-scrore}=\frac{x_i-\bar{x}}{\sigma}$$



An emperical rule for a **bell-shape(normal) distribution**, for example:
- Z-score >= 3, we call that an **outlier** (not among 99.7%)
<center><img src="/images/2022-12/Snipaste_2023-01-10_12-27-33.png" width="80%"></center>

> **Outliers**
Outlier is some data that is faraway from the center. It is not strictly defined (could be more than 1, 2 or 3 sigma, or just 20% larger than mean)
- in some cases, we have to omit outliers to make our model more reasonable
- but in others, **outliers might mean something important**, like a new trend that used to be omit

<img src="/images/2022-12/.png" width="60%">
<img src="/images/2022-12/.png" width="60%">
<img src="/images/2022-12/.png" width="60%">