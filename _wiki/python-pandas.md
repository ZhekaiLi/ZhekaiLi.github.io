---
layout: wiki
title: Python-pandas
categories: Programming Language
description: 
keywords: [Python]
---

## 1 pandas.Dataframe
### 1.1 Create
#### 1.1.1 Create from csv
例如，将 csv 表格文件转化为 pandas 的 dataframe 数据结构
```py
df = pd.read_csv('...address')
```
#### 1.1.2 Create from np.array()
```py
df = pd.DataFrame(a1)
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
#### 1.2.2 View row name and column name
```py
df.index # 行名
```
```py
df.columns # 列名
```

### 1.3 Check 
#### 1.3.1 Check duplication
```py
df.duplicated(subset=['col1', 'col2']])
```
查看 $m\times n$ 的 dataframe 中是否存在重复数据，返回一个 `pandas.core.series.Series` 类型的数据
- 其中 `True` 说明对应行的数据重复了，反之 `False`。
- 可以用 `.values` 的方式将其转换为 $m\times 1$ 的 array

参数:
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

### 1.4 Change, Delete
#### 1.4.1 更改行列名
```py
df.index = [] # 行名, 可以是 list or array
df.columns = [] # 列名
```
#### 1.4.2 去除数据
去除重复数据
```py
df.drop_duplicates(subset=['LON', 'LAT'], # 将查重范围限制在特定的列中
    keep='first', # 保留重复数据的第一个
    inplace=True # 删除重复数据
)
```
去除 NaN
```py
df.dropna(inplace=True)
```


### 1.5 Type Convertion
#### 1.5.1 Convert to Numpy array
```py
X = df[['column name']]
```
示例: 将 dataframe 中的 'LON', 'LAT' 两列转化为一个 $m\times2$ 的数组
```py
X = df[['LON', 'LAT']]
```

### 1.6 Access
#### 1.6.1 访问列
```py
df.columnName
```
访问列的第一个元素
```py
df.columnName[0]
```
#### 1.6.2 访问行
使用 generator fuction `df.iterrows()` 来访问行。

例如将 df 中 'col1' 列的所有元素赋值为 0
```py
for _, row in df.iterrows():
       row.col1 = 0
```
如果 'col1' 就是第一列的话，也可以直接用索引的方式: `row[0] = 0`