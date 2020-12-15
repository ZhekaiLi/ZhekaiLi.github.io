---
layout: wiki
title: Python
categories: Programming Language
description: 
keywords: Python, Numpy
---

# Collections

## 1.1 collections.defaultdict
这是一个比普通 `dict()` 更好的数据结构
使用如下代码声明变量
```py
from collections import defaultdict

D = defaultdict(p1)
```
### 1.1.1 参数 `p1` 
`p1` 有比较多的选项，常见的有
#### `int, dict, set, str, list` 
使用这些参数时, 将规定 defaultdict 中 value 的**默认**数值类型, 也就是说, 当 ‘key1’ 不存在时, `D[‘key1’]` 将会返回对应的空值 (int: 0, dict: {}, list: ()). 例如
```py
Dd = defaultdict(dict)
# Dd['key1'] = {'key1.1': 'value1.1'} 用这个也可以
Dd['key1']['key1.1'] = 'value1.1'
```
defaultdict(dict, {'key1': {'key1.1': 'value1.1'}})
```py
Dl = defaultdict(list)
Dl['l1'] = [1, 2, 3]
```
defaultdict(list, {'l1': [1, 2, 3]})
```py
Dd['key2']
```
{}
```py
Dl['l2']
```
() 

需要注意的是, 虽然这些参数**不是强制的规定**, 譬如完全可以在 `defaultdic(str)` 中储存 `int`, 但是**不推荐这样做**

#### `lambda:  None` 

该参数表示当 ‘key1’ 不存在时, 使用 `D[‘key1’]` 什么都不会返回 (可以把 None 更换为任意参数, 例如 `lambda: 0` 表示返回数值 0)
```py
D = defaultdict(lambda: None)
D['key1']
```
啥都不返回, 此时 `D = defaultdict(<function __main__.<lambda>>, {'key1': None})`

```py
D = defaultdict(lambda: 0)
D['key1']
```
0 (参数 `lambda: 0` 的效果近似于 `int`)

# Folium
**Reference**
1.[知乎: Python绘制地图神器folium入门](https://zhuanlan.zhihu.com/p/112324234)

这是一个能够生成交互地图的包

## 1 folium.Map 创建地图
```py
folium.Map(location=None, 
    tiles='OpenStreetMap', 
    zoom_start=10, 
    crs='EPSG3857'
)
```
参数:
1. `location=[LAT, LON]` 经纬度坐标位置
2. `tiles` 显示样式，默认为'OpenStreetMap'，也就是开启街道显示 (上、左下、右下分别对应 OpenStreetMap, Stamen Toner, and Stamen Terrain)
![pic1](https://github.com/ZhekaiLi/PICTURE-for-markdown/raw/master/Snipaste_2020-12-06_22-06-54.jpg)
![pic2](https://github.com/ZhekaiLi/PICTURE-for-markdown/raw/master/Snipaste_2020-12-06_22-07-14.jpg)
3. `zoom_start` 缩放值，默认为 10
4. `crs` 地理坐标参考系统，默认为 'EPSG3857'

## 2 Note the map 在地图上做标记
### 2.1 folium.CircleMaker 画圆

<font color=red>以下代码可能存在一些问题: 本人在使用过程中发现在 for 循环中使用以下添加代码可能导致只能画出一个标记点, 尚未查明错误原因, 但将 `popup=, fill=, fill_color` 这三行删去之后可以正常运行</font>
```py
folium.CircleMaker(location=None,
    radius=5, # 标记圆圈的半径
    # 标记圆圈的名字，在点击后出现 
    # 其中 re.sub() 利用正则表达式避免乱码
    popup=re.sub(r'[a^-zA-Z]+', '', 'name'),
    color='#1787FE',
    fill=True,
    fill_color='#1787FE'   
).add_to(m)
```
效果如下 (注意! 不要忘了在函数结尾括号外添加 `.add_to(m)`, 否则将无法显示标记)
![pic3](https://github.com/ZhekaiLi/PICTURE-for-markdown/raw/master/2020-12/Snipaste_2020-12-07_18-49-25.jpg)



# Matplotlib
## 1 matplotlib.pyplot
### 1.1 Scatter
```py
plt.scatter(x=X[:, 0], y=X[:, 1], 
    s=10, 
    alpha=0.5
)
```
参数
1. `s` size，即点的大小
2. `alpha` 透明度，取值区间为 $[0,1]$


---


# Numpy
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
```
```
array([[1],
       [3]], dtype=int64)
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


---


# Pandas
## 1 pandas.Dataframe
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

### 1.4 Drop, Delete
去除重复数据以及 NaN
```py
df.drop_duplicates(subset=['LON', 'LAT'], # 将查重范围限制在特定的列中
    keep='first', # 保留重复数据的第一个
    inplace=True # 删除重复数据
)
df.dropna(inplace=True)
```


### 1.5 Type Convertion
#### 1.5.1 Convert to Numpy array
```py
X = df[['column name']]
```
例如将 dataframe 中的 'LON', 'LAT' 两列转化为一个 $m\times2$ 的数组
```py
X = df[['LON', 'LAT']]
```

### 1.6 Access 访问
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


---


# Sklearn
## 1 sklearn.datasets
### 1.1 生成数据
```py
X_blobs, _ = sklearn.datasets.make_blobs(n_samples=1000, 
    centers=10, # 团的个数
    n_features=2, # 数据维度
    cluster_std=0.5, 
    random_state=4
)
```
## 2 sklearn.matrics
### 2.1 Value the clustering 检查聚类算法的性能
```py
sklearn.matrics.silhouette_score(X_blobs, # 原数据
    class_prediction # 分类标签, 例如以下表示有三类 array([0, 1, 2, 1, 1, 2])
)
```