---
layout: wiki
title: Data Structure
cate1: Python
cate2:
description: 
keywords: Python
mathjax: true
mermaid: true
---



# 1. Set 集合
集合由大括号或 `set()` 命令创建，集合内元素唯一，且不存在顺序
```py
S1 = {1, "4", (5, 10)}
S2 = set("aabb12") >>> {'b', '1', 'a', '2'}
S3 = set([1, 2, 3]) >>> {1, 2} # 自动去重
```

## 1.1 操作符 & 操作函数
|操作符| 描述| 对应函数
|-|-|-|
|S \|= T| 更新集合S，取S, T的并集| `S.union(T)`
|S &= T| ...，取S, T的交集| `S.intersection(T)`
|S -= T| ...，取在S中但不在T中的元素| `S.difference(T)`
|S ^= T| ...，取S与T中不相同的元素| 

以上操作符都可以去掉等号单独使用，例如 `S = S - T`
```py
S.add(x)     # 添加元素
S.discard(x) # 移除元素，如果x不在S中不报错
S.remove(x)  # 移除元素，如果x不在S中报错，KeyError
S.clear()    # 移除所有元素
S.pop()      # 随意移除并返回一个元素，如果S为空报错，KeyError
```

## 1.2 Application

**1. 列表数据去重**
将list转化为set，再将set转回list

**2. 统计列表中出现频率最高的元素**
```py
a = [1,2,3,1,2,3,2,2,4,5,1]
max(set(a), key=a.count) >>> 2
```






# 2. List 列表

```py
L.append(x)  
L.extend(L2)
L.insert(index, x) # 在指定位置插入元素

### 删除
L.remove(x)  # 删除值为 x 的第一个元素，如果没有则会报错
x = L.pop(i) # 删除指定位置的元素并将其返回
del L[i]     # 删除指定位置元素

L.index(x)  # 返回值为 x 的第一个元素索引，如果没有则会报错
L.count(x)  # 返回 x 在列表中出现的次数
L.reverse() # 颠倒列表
L.sort()    # 升序排序
```

> **<font color=blue>NOTEs: List 为引用类型的数据</font>(本质为地址)**，因此 `l2 = l1` 这样的操作会使得对 `l1` 的修改也相当于对 `l2` 的修改。**解决方法: deep copy**

```py
l2 = l1.copy()
l2 = l1[:]
l2 = l1[::]
```

<span style="background-color: yellow; color: black;">但如果 L 是一个多维数组，以上方法全部失效，需要使用 deepcopy</span>
```py
from copy import deepcopy
L1 = deepcopy(L)
```


## 2.1 Slice, Sampling
`L[a:b:c]` 表示在第 a 至第 b-1 个元素之间，隔 \|c-1\| 个元素取值
```py
L = [1, 2, 3, 4, 5, 6]

L[0:-1:2] # 表示在第一个至最后一个元素之间，隔1个元素取值
>>> [1, 3, 5]
```

`L[::c]` 表示从左至右(+)/从右至左(-)，每隔 \|c\|-1 个元素取值
```py
L[::2] >>> [1, 3, 5]
L[::-2] >>> [6, 4, 2]

# 从右至左逆序
L[::-1] >>> [6, 5, 4, 3, 2, 1]
```



## 2.2 列表推导式（内嵌复合表达式）

```py
[x for x in data if condition]

[x+1 if condition else x-1 for x in data]
```



## 2.3 其他操作

`range(left, right, step)`

```py
list(range(3,10,3)) >>> [3, 6, 9]
```

**zip(list1, list2)**
```py
list(zip(['A','B'], [1,2]))   >>> [('A',1), ('B',2)]
dict(zip(['A','B'], [1,2]))   >>> {'A':1, 'B':2}
```

还可以对二维列表实现类似转置的效果
```py
original = [['a','b'],['c','d'],['e','f']]
transposed = list(zip(*original))

>>>
[('a', 'c', 'e'), ('b', 'd', 'f')]
```






# 3. Dict 字典 (键值对)

```py
D.fromkeys(keys, vals) # 创建字典

D.items()  # 返回所有 (键, 值)
D.keys()   # 返回所有键
D.values() # 返回所有值
```

> **操作函数**

```py
d.get(k, default=None) # 键 k 存在，返回相应值，不存在则返回<default>

d.pop(k, default=None) # 键 k 存在，删除并返回相应值，不存在则返回<default>
d.popitem()            # 随机取出一个键值对，以元组形式返回
del(d[k])              # 删除键值对 k

d.has_key(k)           # 键 k 存在，返回true，否则返回false
```

sort dictionary by its value
```py
sorted(d.items(), key=lambda x: x[1])
```




# 4. String
```py
text = "Data Science"

text.upper()      >>> "DATA SCIENCE"
text.lower()      >>> "data science"
text.capitalize() >>> "Data science"
```

**Get index of a substring/char**: `.index()` or `.find()`
```py
text.index('Data')   >>> 0
text.find('Science') >>> 5

text.index('data') >>> ERROR
text.find('data')  >>> -1
```

**(1) Concact list to string**
```py
L = ["Hello", "World"]
string = " ".join(L) >>> "Hello World"
```

**(2) Reverse string**

```py
s1 = "abc"
s2 = s1[::-1] >>> "cba"
```
- **reverse integer through converting it into string**
 
```py
i1 = 123
i2 = int(str(i1)[::-1]) >>> 321
```



