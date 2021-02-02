---
layout: wiki
title: Python-sympy
categories: Programming Language
description: 
keywords: [Python]
---

```py
import sympy as syp
```

## 1 sympy.solve 解方程
```py
x = smp.symbols('x')
smp.solve(x**2 + 2*x + 1, x)
```

## 2 sympy.integrate 求积分
$$\int_1^2x^2dx$$
```py
x = smp.symbols('x')
smp.integrate(x**2, (x, 1, 2))
```


