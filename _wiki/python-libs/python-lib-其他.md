---
layout: wiki
title: 其他
cate1: Python
cate2: -libs
description: 
keywords: Python
---

# collections
## 1. collections.defaultdict
这是一个比普通 `dict()` 更好的数据结构
使用如下代码声明变量
```py
from collections import defaultdict

D = defaultdict(p1)
```

其中参数 `p1` 有比较多的选项，常见的有
> 1. `int, dict, set, str, list` 

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
Dd['key2'] >>> {}
Dl['l2'] >>> ()
```

需要注意的是, 虽然这些参数**不是强制的规定**, 譬如完全可以在 `defaultdic(str)` 中储存 `int`, 但是**不推荐这样做**

> 2. `lambda:  None` 

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

## 2. collections.Counter
统计
```py
from collections import Counter
a = [1,2,3,1,2,3,2,2,4,5,1]
cnt = Counter(a)

>>>
Counter({2: 4, 1: 3, 3: 2, 4: 1, 5: 1})
```




# folium
**Reference**
1.[知乎: Python绘制地图神器folium入门](https://zhuanlan.zhihu.com/p/112324234)

这是一个能够生成交互地图的包

## 1.folium.Map 创建地图
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
![pic1](/images/2020-12/Snipaste_2020-12-06_22-06-54.jpg)
![pic2](/images/2020-12/Snipaste_2020-12-06_22-07-14.jpg)
3. `zoom_start` 缩放值，默认为 10
4. `crs` 地理坐标参考系统，默认为 'EPSG3857'

## 2. Note the map 在地图上做标记
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
![pic3](/images/2020-12/Snipaste_2020-12-07_18-49-25.jpg)

# tqdm
这是常用于显示程序运行进度的包, 用在 for 循环语句非常好用, 例如
```py
from tqdm import tqdm

best_score, best_k = -1, 0

for k in tqdm(range(2, 100)):
    m = KMeans(n_clusters=k, random_state=1).fit(X)
    predictions = model.predict(X)
    
    curr_score = silhouette_score(X, predictions)
    if curr_score > best_score:
        best_k = k
        best_score = curr_score
        
print('K={}'.format(best_k))
print('Silhouette Score: {}'.format(best_score)) 
```
这段代码用于在 [2, 99] 区间内寻找使得 KMeans 拟合效果最好的 k 值. 运行效果如下
![pic](/images/2020-12/GIF%202020-12-15%2018-24-56.gif)







