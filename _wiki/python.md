---
layout: wiki
title: Python
categories: Programming Language
description: 
keywords: Python, Numpy
---

# Numpy
## 1 Array
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
```
```
array([[1],
       [3]], dtype=int64)
```

# Pandas
## 1 Dataframe
### 1.1 Read
例如，将 csv 表格文件转化为 pandas 的 dataframe 数据结构
```py
# dataframe
df = pd.read_csv('...address')
```
### 1.2 View 
#### 1.2.1 View first five data line
```py
df.head()
```
查看 dataframe 的前五行 (可用于判断读取的数据是不是我们实际需要的)

| | LON     | LAT      | NAME                        |
|-| --------| ---------| ----------------------------|
|0| 28.17858| -25.73882| 11th Street Taxi Rank       |
|1| 28.17660| -25.73795| 81 Bazaar Street Taxi Rank  |
|2| 27.83239| -26.53722| Adams Road Taxi Rank        |
|3| 28.12514| -26.26666| Alberton City Mall Taxi Rank|
|4| 28.10144| -26.10567| Alexandra Main Taxi Rank    |
### 1.3 Check 
#### 1.3.1 Check duplication
```py
df.duplicated(subset=['col1', 'col2']])
```
查看 $m\times n$ 的 dataframe 中是否存在重复数据，返回一个 `pandas.core.series.Series` 类型的数据
- 其中 `True` 说明对应行的数据重复了，反之 `False`。
- 可以用 `.values` 的方式将其转换为 $m\times 1$ 的 array

其他可选参数：
1. `subset=['column name']` 将查重范围限制在特定的列中

**应用场景：检查数据集中是否存在一、二两列元素相同的数据**
```py
df.duplicated(subset=['LON', 'LAT']]).values.any()
```
- 其中 `L.any()` 用于检测列表中是否包含 `True` 元素，包含则返回 `True`，全元素均为 `False` 则返回 `False`
- 当然，类似的还可以用于**检查是否存在 NaN 数值**： `df.isna().values.any()`
#### 1.3.2 Check NaN
```py
df.isna()
```
该函数的使用可以参考上一个 section

### 1.4 Drop, Delete



