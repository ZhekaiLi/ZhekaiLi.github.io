---
layout: wiki
title: pandas
cate1: Python
cate2: -libs
description: 
keywords: Python
topmost: true
---

`DataFrame` 与 `Series` 是 pandas 中最重要的两种数据类型

**区别**:
- `Series`: 一维数据结构，由 index 和 value 组成
- `DataFrame`: 二维结构，由 index、column 和 value 组成。

**联系**:

`DataFrame` 由多个 `Series` 组成，无论是行还是列，单独拆分出来都是一个 `Series`。因此，<span style="background-color: yellow; color: black;">对数据表的行/列操作，与对数据序列的操作是一致的

# 1. pandas.DataFrame
## 1.1 Create & Trans & Save
```py 
df = pd.DataFrame()
df = pd.DataFrame(colums=['col_1', 'col_2'])

df = pd.DataFrame({'col_1':[1,2],'col_2':[3,4]}, 
index=['a','b']) # 不填index则默认为下标，从0开始
```
| |col_1|col_2|
|-|-----|-----|
|a|1    |3    | 
|b|2    |4    |

**Create from pd.Series()**

- Method 1

```py
sr1 = pd.Series([1], index=['a'])
sr2 = pd.Series([1,2], index=['a','b'])
df = pd.DataFrame({'col_1':sr1,'col_2':sr2})
```
| |col_1|col_2|
|-|-----|-----|
|a|1    |1    | 
|b|NaN  |2    |

- Method 2

```py
df = sr.to_frame('col_1') # 相当于给序列加了个列标题，从而变成了表格
```

**Create from .csv**

```py
df = pd.read_csv('地址')
```
- `index_col='列名'` 指定某一列为行索引
- `parse_dates=['列名'])` 将指定列字符串格式的时间转换为datetime格式
- `header=None` 指定程序不将csv文件的第一行读取为列名
- `na_values=['None','null']` 指定程序将一些特定字符串视为NaN

**Create from np.array()**

```py
df = pd.DataFrame(arr1)
```
**Transform to np.array()**

```py
arr = df.values
```
**Save to .csv**

```py
df.to_csv('1.csv')
```
- `header=False` 不输出列名
- `index=False` 不输出行名



## 1.2 Modify
**添加数据**

```py
df = pd.DataFrame(columns=['c1','c2'])
df.loc['a1'] = 1       # 添加一行1
df.loc['a2', 'c2'] = 1 # 添加一个1
df['c3'] = 0           # 添加一列0

# 添加一行数据（长度必须等于现有列数）
df.loc['a3'] = [0, 0, 0] 
```
|  |c1   |c2   |c3|
|--|-----|-----|--|
|a1|1    |1    |0 |
|a2|NaN  |1    |0 |
|a3|0    |0    |0 |

**更改行列**

```py
df.index = []   # 更改行名, 可以是 list or array
df.columns = [] # 更改列名

# 单独更改某个或某些行/列名
# df.rename({'old':'new'}, axis=(1 for cols, 0 for rows), inplace=True)
df.rename({'old_col', 'new_col'}, axis=1, inplace=True)

df.set_index('col_1', inplace=True) # 把指定列设置为 Index
df.reset_index(inplace=True)        # 重新改为默认的数字 Index
```

参数 `inplace` 默认为 Flase，即返回更改后的 DataFrame 的同时**不更改**原 DataFrame。如果设置为 True，则在效果上 `df.rename(..., inplace=True)` 等同于 `df = df.rename(...)` 

**删除数据**

```py
df.drop(columns = df.columns[0], inplace=True) # 删除第一列
```



## 1.3 Arributes

```py
df.head(i)  # 查看前 i 条数据
df.tail(i)

df.index.values   # 查看行名
df.columns.values # 列名
df.values         # 值数组
df.T              # 转置
df.shape          # (n, m) n行m列
df.size           # n*m 元素个数
```



## 1.4 Access
**访问列**
```py
df['columnName']    # 访问单列
df.columnName
df[['col1','col2']] # 访问多列
```

**访问行**
```py
df.loc['rowName',:]      # 访问单行
df.loc[['row1', 'row2']] # 访问多行
```

或使用 `df.iterrows()`
例如，将 df 中 'col1' 列的所有元素赋值为0：
```py
for _, row in df.iterrows():
       row.col1 = 0
```

**索引和切片**

```py
# 推荐方式
df.loc['rowName','columnName'] # 使用行列名索引
df.iloc[x,y]                   # 使用下标索引
df.loc[['r1','r3'], 'c2']      # 使用行列名切片
df.iloc[[0:5], [2:3]]          # 使用下标切片

# 不推荐
df['columnName']['rowName']
df.columnName['rowName']
```


```py
df.sample()                     # 随机获取一行
    df.sample(frac=1, inplace=True) # 随机打乱整个 DataFrame
```

**筛选（mask）**

```py
mask1 = df.Poplation > 1000000                       # 人口大于一百万的地区
mask2 = df.Region.apply(lambda x: x.startswith('A')) # 名字以 A 开头的地区

df[mask1]         # 人口大于一百万的地区的所属行
    df.loc[mask1] # 同上
df[mask1 & mask2] # 人口大于一百万以及名字以 A 开头的地区的所属行
df[mask1 | mask2]
```



## 1.6 NaN & Duplication
### NaN

```py
df.isna()            # 检查每个数据是否为NaN
    df.isna().any()  # 检查每列是否包含NaN
    df.isna().mean() # 查看每列中NaN的比例

df.fillna(0, inplace=True)            # 为NaN赋0
    df['col1'].fillna(method='ffill') # propagate last valid observation forward
    df['col1'].fillna(method='bfill') # use next valid observation to fill gap

df.dropna(inplace=True)               # 删去所有包含NaN的行
    df.dropna(how='all')              # 删去所有只包含NaN的行
    df.dropna(axis=1)                 # 删去所有包含NaN的列
    df.dropna(subset=['col1','col2']) # 删去所有指定列包含NaN的行
```

### Duplication

```py
df.duplicated(subset=['col1', 'col2']])
```
查看是否存在重复数据，返回一个 `pd.Series()`
- 其中 `True` 说明对应行的数据重复了，反之 `False`
- 可以用 `.values` 的方式将其转换为 `np.array()`

**应用：检查在指定两列中，是否存在相同的数据**
```py
df.duplicated(subset=['LON', 'LAT']]).values.any()
```
- 其中 `L.any()` 用于检测列表中是否包含 `True` 元素，包含则返回 `True`，全元素均为 `False` 则返回 `False`
- 当然，类似的还可以用于**检查是否存在 NaN 数值**： `df.isna().values.any()`

**去除重复数据**

```py
df.drop_duplicates(subset=['LON', 'LAT'], # 将查重范围限制在特定的列中
    keep='first', # 保留重复数据的第一个
    inplace=True # 删除重复数据
)
```



## 1.8 Plot
画出两列数据，横坐标为 `df.index`

```py
df['col1'].plot()            # index-col1 折线图
df['col1'].plot(kind='bar')  # 柱状图

# 直方图（表示数据分布）
df['col1'].plot(kind='hist')
df.hist('col1')
df.hist('col1', by='col_category') # 对每个 category 单独画图


df.plot(x='col_x', y='col_y', kind='scatter') # col_x-col_y 散点图
```

### 1.8.1 Plot Time Series


## 1.9 分组
### Groupby

```py
# grouping = df.groupby(col_to_group_by)
grouping = products.groupby('Category')
```
products:
| |Category |Price |Name  |Amount|
|-|---------|------|------|------|
|0|Drink    |4     |Cola  |100   |
|1|Snack    |10    |Nut   |50    |
|2|Drink    |3     |Fenta |200   |

Groupby object is kind of like a list of pairs `[(group_name, df)]`

```py
for name, df in grouping:
    print(name, df.Price.mean())

"""
Drink 3.5
Snack 10
"""
```
#### .1 属性 & 方法

```py
grouping = products.groupby('Category')
grouping.indices # 获取各个组所包含的商品 Index

# {'Drink':array([0,2]), 'Snack':array([1])}
```
**方法**

```py
# 获取某个组所有商品的信息（不包含 `Category` 列）
grouping.get_group('Drink')
```
| |Price |Name  |Amount|
|-|------|------|------|
|0|4     |Cola  |100   |
|2|3     |Fenta |200   |
#### .2 统计

```py
# 返回数值类型列的统计值（例如 Name 列就不会被返回）
grouping = products.groupby('Category')
grouping.mean()
grouping.min()
grouping.max()
grouping.sum()
```
|     |Price |Amount|
|-----|------|------|
|Drink|7     |300   |
|Snack|10    |50    |

```py
# 为不同的列定义统计方式
grouping.agg({'Price':'mean', 'Amount':'sum'})
```

|     |Price |Amount|
|-----|------|------|
|Drink|3.5   |300   |
|Snack|10    |50    |

#### .3 col_of_interest.apply()
**获取各组的某个列在外部函数/lambda上的统计值**

```py
df.groupby(col_to_group_by).col_of_interest.apply(func)
```
- `col_to_group_by`: 分组对象
- `col_of_interest`: 根据分组来进行统计的对象
- `func`: 应用于统计对象的函数（自定义函数/lambda/来自于其他库的函数）

Ex1: 统计每个航线的平均延误（多种方式）

```py
# 返回数据: 以航线类型为 Index，以平均延误为 Value
flights.groupby('Airline')['Arrival_delay'].apply(np.mean)
flights.groupby('Airline').Arrival_delay.apply(np.mean)
flights.groupby('Airline').Arrival_delay.mean()

# 返回数据: 保持原表的 Index，以平均延误为 Value
flights.groupby('Airline')['Arrival_dealy'].transform(np.mean)
```
Ex2: 统计每个航线有多少航班的延误时间大于10小时

```py
flights.groupby('Airline')['Arrival_delay'].apply(
    lambda ls: np.sum(ls>10)
)
```
Ex3: 统计每个航班在每个月的平均延误（**多层分组**）

```py
flights.groupby(['Airline','Month'])['Arrival_delay'].apply(np.mean)
```
#### .4 Groupby + Sort

```py
products.groupby('Category').mean().sort_values(
    by=['Price'], ascending=False
)
```


## 1.10 数据处理
### Statistic
```py
# 查看各列的统计数据（count, mean, std, percentile...）
df.describe() 

df.mean()           # 各列平均
    df.mean(axis=1) # 各行平均
df.sum()            # 各列求和
```

### Sort

```py
df.sort_values(by='col1') # 根据指定列做升序排列
df.sort_values(by='col1', ascending=False) # 降序
df.sort_index() # 根据行名做升序排列
```

### Rolling
Rolling object is a kind of list contains all the windows

```py
# roll = df.rolling(window_length)
prodroll = products.rolling(2)
```


products:
| |Category |Price |Name  |Amount|
|-|---------|------|------|------|
|0|Drink    |4     |Cola  |100   |
|1|Snack    |10    |Nut   |50    |
|2|Drink    |3     |Fenta |200   |
|3|Drink    |2     |Water |500   |

```py
# df.rolling(window_length).col_of_interest.apply(func)
products.rolling(2).Price.apply(np.mean)

"""
0 NaN
1 7
2 6.5
3 2.5
"""
```


### Trend (Change)
数据的变化幅度（百分比）

```py
df.pct_change()

"""
  Price
0 10
1 15
2 30
3 33

>>>
  Price
0 NaN
1 0.5
2 1
3 0.1
"""
```



---



# 2. pandas.Series
一种类似于一维数组的对象，由一组数据和一组与之相关的数据标签（索引）组成

创建方式：
```py
# 由数组创建，默认标签为数组下标
pd.Series([2, 4, 6])
# 由数组创建，并设置标签
pd.Series([2, 4, 6], index=['a', 'b' 'c']) 
# 由字典创建
pd.Series({'a':2, 'b':4, 'c':6})
# 创建一个全部值为零的Series
pd.Series(0, index=['a', 'b' 'c'])
```

获取值数组和索引数组：
```py
sr.index
sr.values
```

## 2.1 特性
### 类似array的特性（下标）
- **从ndarray创建Series**
- **标量运算**：`sr*2`
- **两个Series运算**：
`sr1 + sr2`
`sr1.add(sr2)`

```py
sr1 = pd.Series([1,2], index=['a','b'])
sr2 = pd.Series([1,2], index=['b','a'])
sr3 = pd.Series([1], index=['b'])

# 运算时会按照标签进行数据对齐
sr1 + sr2 
>>>
a    3
b    3

# 缺失值相加会默认设置为NaN
sr1 + sr3
>>>
a    NaN
b    3

# 但可以通过.add()设置为0
sr1.add(sr3, fill_value=0)
>>>
a    1
b    3
```

- **下标索引、切片**：`sr.iloc[0]` `sr.iloc[[1, 3]]` `sr.iloc[0:3]`
- **布尔值过滤**：`sr[sr>0]`
- **通用函数**：`np.abs(sr)` `np.argmax(sr)` `...`


### 类似字典的特性（key）
- 从字典创建Series
- 键索引：`sr.loc['a']` `sr.loc[['a', 'c']]`
- in运算查看是否包含指定key：`'a' in sr`

### 独有特性
- 键切片（头尾均包含）：`sr.loc['a':'c']` 



## 2.2 数据处理
**平移 Shift**

```py
sr.shift(1) # 向右平移一个单位
```
**缺失值 NaN**

```py
# 删除
sr = sr[sr.notnull()] # 布尔值过滤
sr = sr.dropna()


sr = sr.fillna(sr.mean()) # 替换为平均值
```
**分组 Cut**

```py
pd.cut()
```



## 2.3 统计

```py
sr.value_counts() # 统计每个数值出现的次数
sr.quantile(p)    # 百分位：p从0至1

sr.mad()          # Mean Absolute Deviation
sr.var()          # 方差
sr.std()          # 标准差
sr1.cov(sr2)      # 协方差

sr.cumsum()       # 逐个累加 [1,3,2] >>> [1,4,6]
sr.cummax()       # 累计最大值 [1,3,2,4] >>> [1,3,3,4]
sr.cumprod()      # 累乘（累积）
```


## 2.4 Plot

```py
# Line Chart(横坐标为 Index)
sr.plot()

# Bar Chart: 显示每个元素出现的次数
sr.value_counts().plot(kind='bar')
```


## 2.5 分组

```py
# pd.cut(numerical_series, edge_numbers_to_split_by, labels_for_groups)
pd.cut(sr, [-1, 50, 100], [1,2]) # 分成两组 1:[-1,50) 2:[50,100)
```

# 3. Time Series
## 3.1 创建 datetime 对象

```py
# 将数据表的一列字符串格式的时间转换为 datetime
df['date'] = pd.to_datetime(df['date'])
# 将字符串格式的时间批量转换为 datetime
pd.to_datetime(['2011-01-11', '2021/FEB/22'])
```
创建一段时间range

```py
# 生成一个包含了，从1月11到1月22之间，共12天日期的数组
pd.date_range('2011-01-11', '2011-01-22')
# 从1月11开始往后，共20天的日期
pd.date_range('2011-01-11', peirods=20)
```
更改频率 `freq=` 
- `'D'` day, default 
- `'H'` hour 
- `'W'` week, `'W-MON'` 表示每个周一
- `'M'` mounth
- `'B'` work day 
- `'A'` year
- 其它一些自定义，例如 `'1h20min'` 表示间隔1时20分钟

```py
# 从1月11日0点开始往后，共20小时的时间
pd.date_range('2011-01-11', periods=20， freq='H')
# 从1月11往后的第一个周二开始，共20个周二的日期
pd.date_range('2011-01-11', periods=20， freq='W-TUE')
```
## 3.2 时间序列
以 datetime 对象为索引的 Series 或 DataFrame，例如

```py
sr = pd.Series(np.arange(11), pd.date_range('2011-01-22', period=11))
```
时间序列的便利性

```py
# 切片
sr['2011-01'] # 切片，包含所有索引为2011年1月的数据
sr['2011']    # ...索引为2011年...
sr['2011-01-11':'2012-02']

# 统计
sr.resample('W').sum()  # 将每周的数据求和
sr.resample('M').mean() # 求每月数据的均值
sr.resample('M').first()# 第一条记录
sr.resample('M').last() # 最后一条
```


