---
layout: wiki
title: Python-numpy
categories: Programming Language
description: 
keywords: [Python]
---

## 1 numpy.array
### 1.1 Opertations with index
#### 1.1.1 Find index
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
#### 1.1.2 Find index of max/ min
寻找数组中最大/ 最小值的位置 (index)
```py
np.argmax(L) 
np.argmin(L) 
```

### 1.2 Sort
#### 1.2.1 Delete duplications and sort
去除数组中的重复数字, 并进行排序之后输出
```py
np.unique([1, 2, 2, 3, 3])
>>> array([1, 2, 3])
np.unique([[1, 1], [2, 3]])
>>> array([1, 2, 3])
```
### 1.3 Save and Load
将 numpy.array 类型的数据已 `.npy` 为格式保存起来
```py
np.save('address/filename.npy', X)
```
读取 `.npy` 格式的文件
```py
X = np.load('address/filename.npy')
```

### 1.4 Join
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