---
layout: wiki
title: SciPy
cate1: Python
cate2: -libs
description: 
keywords: Python
mathjax: true
---

# 1. scipy.interpolate
光滑拟合离散数据, 生成拟合函数
```py
spl = make_interp_spline(X, Y, 
    k=3 # B-spline degree. Default is cubic, k=3
)
```
对于新的数据点 X_test, 可以直接使用 `spl(X_test)` 来 predict






# 2. scipy.optimize
```py
import scipy.optimize as opt
```

## 2.1 最小平方误差
例如对于 $$y=Ax$$

已知过量的数据组 $[y, A]$ 求参数 $x$
```py
errorValue = lambda x,y,A: y - np.dot(A, x)
x_init = np.array([1] * 6)

x = opt.leastsq(errorValue, x_init, args=(y, A))[0]
```

## 2.2 求函数极值
一元函数，在定义域内的最小值
```py
f = lambda x: x**2 + np.sin(x) + 1

opt.minimize_scalar(f, bounds=(-1,1), method="bounded")
```

多元函数，在定义域内的最小值
```py
f = lambda x: x[0]**2 - x[1]**2
x0 = np.array([2, 1]) # 设置函数参数的起始点
bds = ((0,5), (0,6))  # 设置每个参数的定义域

opt.minimize(f, x0=x0, bounds=bds)
```

## 2.3 函数拟合
```py
# 自定义函数
def func(x, Beta_1, Beta_2):
    return 1 / (1 + np.exp(-Beta_1*(x-Beta_2)))

# 数据拟合：返回参数 popt 储存Beta_1, Beta_2的拟合值
popt, pcov = opt.curve_fit(func, train_x, train_y)

# 预测
predictions = func(test_x, *popt)
```





# 3. scipy.integrate
```py
from scipy import integrate
```

## 3.1 求积分
```py
f = lambda x: 7* x**6
ans,err = integrate.quad(f, 1, 3)
print(ans)
```

积无限
```py
f = lambda x: (x-2)* 0.5 * np.exp(-0.5 * x)
ans,err = integrate.quad(f, 2, np.inf)
```

多重积分 $\int_{x=0}^{3}\int_{y=0}^{x}3xydydx$
```py
f = lambda y, x: 3*x*y
ans,err = integrate.dblquad(f, 0, 3, lambda x: 0, lambda x: x)
```