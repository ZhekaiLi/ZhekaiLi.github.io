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

# 2. Probability
## 2.1 Types of Probability
**Classical Probability**
- Know all outcomes
- Every outcome is equally likely
- eg. roll a dice, flip a coin

**Empirical Proabbaility**
- Based on experimental or historical data
- eg. 某个球员投篮命中的概率

**Subjective Probability**
- Based on personal belief, not statistics
- eg. boss estimate that there's a 75% for a new project to be launched

## 2.2 Percentile
- 95th percentile = 5% top
- 50th percentile = median
- 100th percentile = 0% top *IMPOSSIBLE!*

> **Calculate percentile**
> $$\%\text{rank}=\frac{\#\text{values below }x+0.5}{\text{total }\#\text{values}}\times 100$$
> 
> **then round down to an integer**

For example, 20 students takes the exam, 2 students get 85, 6 students less than 85, others higher. Calculate the percentile of score 85:
$$\frac{6+0.5}{20}=32.5$$

The **round down** to be 32th percentile

## 2.3 Probability Trees
A simple but clear tool for multiple event probabilities:

For example, we know the percentage of three groups of different lifespan, and also know the percentage of the people who exercise more than 3 time a week of each lifespan group

Then use probability tree to calculate each detailed group:
<img src="/images/2022-12/Snipaste_2023-01-13_17-27-28.png" width="60%">

## 2.4 False Positive
False Positive (假阳性): actually negative but tested positive

False Negative (假阴性): actually positive but tested nagative

<img src="/images/2022-12/.png" width="60%">
<img src="/images/2022-12/.png" width="60%">
<img src="/images/2022-12/.png" width="60%">
<img src="/images/2022-12/.png" width="60%">
<img src="/images/2022-12/.png" width="60%">
<img src="/images/2022-12/.png" width="60%">