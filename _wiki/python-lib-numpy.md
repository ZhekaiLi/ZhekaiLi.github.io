---
layout: wiki
title: numpy
cate1: Python
cate2: -libs
description: 
keywords: Python
mathjax: true
---

## 1. numpy.array
```py
arr = np.array([1,2,3])
arr = np.append(arr, 4)  # 从尾端添加元素
arr = arr.reshape(2,2)   # 改变数组的维度
```

### 1.1 Opertations with index
寻找数组中符合条件的元素的位置 (index)
```py
np.argwhere(L == a) 
```
示例
```py
L = np.array([1, 2, 3, 2])
np.argwhere(L == 2)

>>> array([[1],
           [3]], dtype=int64)
```
### 1.2 Statistics
```py
arr.sum()
arr.mean()
arr.std()
arr.var()
arr.argmax()  # 最大值索引
arr.argmin()  # 最小值索引
arr.cumsum()  # 所有元素的累计和（累加）
arr.cumprod() # 所有元素的累计积（累乘）
```

### 1.3 Sort
#### 1.3.1 Delete duplications and sort
去除数组中的重复数字, 并进行排序之后输出
```py
np.unique([1, 2, 2, 3, 3])
>>> array([1, 2, 3])
np.unique([[1, 1], [2, 3]])
>>> array([1, 2, 3])
```
### 1.4 Save and Load
将 numpy.array 类型的数据已 `.npy` 为格式保存起来
```py
np.save('address/filename.npy', X)
```
读取 `.npy` 格式的文件
```py
X = np.load('address/filename.npy')
```

### 1.5 Join
纵向堆叠 `np.vstack((a1, a2))`
```py
a1 = np.array([1, 2, 3])
a2 = np.array([4, 5, 6])
np.vstack((a1, a2))

>>> array([[1, 2, 3],
           [4, 5, 6])
```
横向堆叠 `np.hstack((a1, a2))`
示例略

## 2. numpy.math
### 2.1 Calculation
阶乘（factorial）
```py
np.math.factorial(n)
```

## 3. numpy.random
从指定**范围**内随机选择
```py
# 从[0,1)中生成x行y列的随机多维数组
np.random.rand(x, y)
# 从[5,15)中生成x行y列的随机多维数组
np.random.rand(x, y) * 10 + 5
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