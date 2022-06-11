---
layout: wiki
title: SymPy
cate1: Python
cate2: -libs
description: 
keywords: Python
---

```py
import sympy as sy
```

## 1 sympy.solve 解方程
### 一元方程
```py
x = sy.symbols('x')

sy.solve(x**2 + 2*x + 1, x)
```
### 二元方程
```py
x = smp.symbols('x')
y = smp.symbols('y')

eqs = [65000-x-y/np.sqrt(6.7e-4),
    82000-x-y/np.sqrt(3.15e-5)]
sy.solve(eqs, [x, y])
```

## 2 sympy.integrate 求积分
$$\int_1^2x^2dx$$
```py
x = sy.symbols('x')
sy.integrate(x**2, (x, 1, 2))
```

## 3 sympy.diff 求导
```
x = sy.symbols('x')
sy.diff(x**2, x)
```


