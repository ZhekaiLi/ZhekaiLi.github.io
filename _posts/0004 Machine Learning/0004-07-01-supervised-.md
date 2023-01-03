---
layout: post
title: Supervised Learning - 
categories: Machine-Learning
description: Personal Notes
keywords: Machine-Learning, Python, Clustering
mathjax: true
---

<center>

# Supervised Learning - 
</center>

Supervised learning techniques
- Feature selection
Mutual information
- Bayes decision rule 
Naïve Bayes
- Linear classifier
Logistic regression 
Support vector machine 
- Nonlinear classifier
K-nearest neighbors
- Neural networks
Single neuron ≈ logistic regression
Deep neural networks
- Regression
Linear regression
Polynomial regression
Ridge regression

# 1. Classifiers
## 1.1 Naive Bayes Classifier
<img src='/images/2022-12/Snipaste_2022-12-12_11-27-18.png' width='90%'>

## 1.2 Nearest Neighbor Classifier (KNN)
<img src='/images/2022-12/Snipaste_2022-12-12_11-28-32.png' width='80%'>

<img src='/images/2022-12/Snipaste_2022-12-12_11-33-47.png' width='80%'>

## 1.3 Maximum Margin Classifier (SVM)

<img src='/images/2022-12/Snipaste_2022-12-12_12-15-43.png' width='80%'>

因为这里的 $c$ 为常数，因此可以除到 "$\ge$" 左侧的参数 $w,b$ 中，这样就得到了 Support Vector Machine(SVM) 的基本形式
$$\min_{w,b}\|w\|^2$$

$$s.t.\text{ }y^i(w^Tx^i+b)\ge 1,\forall i$$

where $y^i=\pm 1$ 表示 $x^i$ 属于 Class 1 or Class 2

<span style="background-color: yellow; color: black;">Support Vectors are the points on the lines $w^Tx+b=\pm 1$</span>

### 1.3.1 Dual problem of SVM
Firstly convert SVM equation to standard form
$$\min_{w,b}\frac{1}{2}w^Tw$$

$$s.t.\text{ }1-y^i(w^Tx^i+b)\le 0,\forall i$$

Then construct Lagrangian function
$$L(w,\alpha,\beta)=\frac{1}{2}w^Tw+\sum_{i=1}^m\alpha_i(1-y^i(w^Tx^i+b))$$

- when $1-y^i(w^Tx^i+b)=0,\alpha_i > 0$
- when $1-y^i(w^Tx^i+b)\ne 0,\alpha_i = 0$

Take derivative and set to zero (找最优的 $w^*$)
$$\frac{\partial L}{\partial w}=0\to w=\sum_{i=1}^m\alpha_iy^ix^i$$

$$\frac{\partial L}{\partial b}=0\to \sum_{i=1}^m\alpha_iy^i=0$$

Plug back into Lagrangian and simplify to get the **dual problem of SVM**:
$$L(w,\alpha,\beta)=\sum_{i=1}^m\alpha_i-\frac{1}{2}\sum_{i,j=1}^m\alpha_i\alpha_jy^iy^j({x^i}^Tx^j)$$

$$s.t.\begin{cases}
  \alpha_i\ge 0 \text{ }\forall i\\
  \sum_i^m\alpha_iy^i=0
\end{cases}$$

通过求解以上 quadratic programming，求得 $\alpha_i^*,y^i$

### 1.3.2 Solve dual problem

<img src='/images/2022-12/Snipaste_2022-12-12_17-44-19.png' width='90%'>

首先求出 $w$:
$$w=\sum_{i=1}^m\alpha_iy^ix^i$$

在对于任意 data $i$ such that $\alpha_i>0$，求出 $b$:
$$1-y^i(w^Tx^i+b)=0$$



## Linear Regression Model


<img src='/images/2022-12/Snipaste_2022-12-12_22-18-03.png' width='80%'>


## Ridge Regression


<img src='/images/2022-12/Snipaste_2022-12-12_22-20-34.png' width='80%'>

## Nonlinear Regression

<img src='/images/2022-12/Snipaste_2022-12-13_09-46-14.png' width='80%'>


<img src='/images/2022-12/.png' width='70%'>
<img src='/images/2022-12/.png' width='70%'>
<img src='/images/2022-12/.png' width='70%'>
<img src='/images/2022-12/.png' width='70%'>
<img src='/images/2022-12/.png' width='70%'>



<center><img src='/images/2022-12/.png' width='70%'></center>
<center><img src='/images/2022-12/.png' width='70%'></center>
<center><img src='/images/2022-12/.png' width='70%'></center>
<center><img src='/images/2022-12/.png' width='70%'></center>
<center><img src='/images/2022-12/.png' width='70%'></center>
<center><img src='/images/2022-12/.png' width='70%'></center>
<center><img src='/images/2022-12/.png' width='70%'></center>
<center><img src='/images/2022-12/.png' width='70%'></center>


