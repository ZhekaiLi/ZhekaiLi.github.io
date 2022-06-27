---
layout: wiki
title: NumPy
cate1: Python
cate2: -libs
description: 
keywords: Python
mathjax: true
---

# 1. numpy.array
**Define**

```python
np.array([1,2,3])
np.zeros((n,m))      # n*m 的空矩阵
np.ones((n,m))
np.arange(4)         # array([0,1,2,3])
    np.arange(1,4)   # array([1,2,3])
    np.arange(1,6,2) # array([1,3,5])

np.zeros((n,m)) # n*m 的空矩阵
np.ones((n,m))
```
**Modify**

```py
arr = np.append(arr, 4)  # 从尾端添加元素
arr = arr.reshape(2,2)   # 改变数组的维度
arr = arr.ravel()        # 展平成一维数组（一行一行排）
```

## 1.1 Index

```py
arr.argmax()  # 最大值索引
arr.argmin()  # 最小值索引
```
寻找数组中符合条件的元素的位置 (index)

```py
np.argwhere(L == a) 

# Example
L = np.array([1, 2, 3, 2])
np.argwhere(L == 2)

>>> array([[1], [3]], dtype=int64)
```



## 1.2 Statistics

```py
arr.sum()
arr.mean()
arr.std()
arr.var()
arr.max()
    arr.max(axis=1) # 每行最大值（axis=0 每列）

arr.cumsum()  # 所有元素的累计和（累加） [1,2,3] >>> [1,3,6]
arr.cumprod() # 所有元素的累计积（累乘）
```


## 1.3 Sort

去除数组中的重复数字, 并进行排序之后输出

```py
np.unique([1, 2, 2, 3, 3])
>>> array([1, 2, 3])
np.unique([[1, 1], [2, 3]])
>>> array([1, 2, 3])
```



## 1.4 Save and Load
将 numpy.array 类型的数据已 `.npy` 为格式保存起来

```py
np.save('address/filename.npy', X)
```
读取 `.npy` 格式的文件

```py
X = np.load('address/filename.npy')
```

## 1.5 Combine
纵向堆叠 `np.vstack((a1, a2))`
```py
a1 = np.array([1, 2, 3])
a2 = np.array([4, 5, 6])
np.vstack((a1, a2))

>>> array([[1, 2, 3],
           [4, 5, 6])
```
横向堆叠 `np.hstack((a1, a2))`



---



# 2. Calculations
## 2.1 Matrices

```py
C = np.matmul(A, B)         # 矩阵乘法
C = np.dot(A, B)            # 矩阵乘法（和 matmul 差不多）
C = np.multiply(A, B)       # 点乘（各元素相乘）
u, s, vh = np.linalg.svd(C) # SVD(奇异值分解)

A.sum(axis=0) # 列求和（axis=1 行求和）
```

## 2.2 Broadcasting
计算矩阵中每个元素在其所在列的占的比例

```py
col_sum = A.sum(axis=0)
percent = 100*A/col_sum
```

阶乘（factorial）

```py
np.math.factorial(n)
```

# 3. numpy.random
从指定**范围**内随机选择（生成x行y列的随机二位数组）

```py
# [0,1)
np.random.rand(x, y)
# [5,15)
np.random.rand(x, y) * 10 + 5

# 正态分布（mean 0 variance 1）
np.random.randn(x, y)
```

从指定**列表**中随机选择

```py
# 等概率随机（可以反复选取同一个元素）
np.random.choise([1,2,3], size=2, replace=True)
# 等概率随机（一个元素只能被选去一次）
np.random.choise([1,2,3], size=2, replace=False)
# 指定概率随机
np.random.choise([1,2,3], size=100, replace=True, p=[0.2, 0.3, 0.5])
```