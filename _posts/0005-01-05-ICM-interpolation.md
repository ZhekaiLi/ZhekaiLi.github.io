---
layout: post
title: Interpolation
categories: ICM
description: Personal Notes
keywords: [Interpolation]
---

插值算法解决的是 “已知函数在某区间(域)内若干点处的值，求函数在该区间(域)内其它点处的值”。而一维插值可描述为 “已知函数在 $x_0,...,x_n$ 处的值 $y_0,...,y_n$，求简单函数 $p(x)$，使 $p(x_i)=y_i$”。

常用的插值方法包括 Lagrange 插值法与 Newton 插值法

# Lagrange 插值法
对于 k + 1 个已知点，$(x_0,y_0),...,(x_k,y_k)$，定义**拉格朗日差值多项式**：
$$L(x):=\sum_{j=0}^ky_j\ell_j(x)$$ $$\ell_j(x):=\prod_{i=0,i\neq j}^k\frac{x-x_i}{x_j-x_i}$$

## .1 Matlab 实现
```matlab
y = lagrange(x0, y0, x);
% x0, y0 为已知点集，x 为插值点，y 为插值结果
```
示例：
```matlab

```
