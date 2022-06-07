---
layout: wiki
title: Basis
cate1: Python
cate2:
description: 
keywords: Python
mathjax: true
---

# 0. ipython
ipython 是一个交互式 shell，同时被应用于 jupyter。有很多方便的魔法命令：

1. **自动补全** `Tab`
2. **执行终端命令** `!` + `终端命令`
例如 `!ifconfig`
3. **模糊查找** `查找内容` + `?`
例如 `list_1.*pp*?` 能查找目标对象所有名字中带有 pp 字段的方法/属性
4. **查看信息** `对象/方法` + `?`
例如 `list_1?`, `list_1.append?`
5. **查看函数代码** `函数名` + `??`
6. **运行python程序** `%run` + `文件名.py`
7. **使用前面代码块的输出结果** `_` 前面第一个, `__` 前面第二个, `_n` 序号为n的代码块：
<img src="/images/2022-01/Screenshot 2022-01-22 at 8.35.57 PM.png" width="70%">

### 为地址设置书签
设置书签 `%bookmark 书签名 地址`
删除书签 `%bookmark -d 书签名`
删除所有书签 `%bookmark -r`
显示所有书签 `%bookmark -l`
跳转地址 `cd 书签名`

示例：

<img src="/images/2022-01/Screenshot 2022-01-22 at 8.49.22 PM.png" width="90%">

### 代码调试 
1. 打开代码调试: `%pdb on`
2. 之后如果运行错误代码，则会跳转到报错的前一行，并打开调试器，进入 pdb 调试模式，例如：
<img src="/images/2022-01/Screenshot 2022-01-22 at 8.02.17 PM.png" width="80%">
3. 在调试器内输入调试命令，例如
```py
p 变量名 # 查看变量值
```
4. 退出调试: `q(uit)`

# 1. 数据结构
## 1.1 set 集合
> **创建**

集合由大括号或 `set()` 命令创建，集合内元素唯一，且不存在顺序
```py
S = {1, "4", (5, 10)}
T = set("aabb12")

>>>
T = {'b', '1', 'a', '2'}
```
> **操作符**

|操作符| 描述|
|-|-|
|S \|= T| 更新集合S，包括S与T中的所有元素|
|S -= T| 更新集合S，包括S但不包括T中的元素|
|S &= T| 更新集合S，包括同时在S与T中的元素|
|S ^= T| 更新集合S，包括S与T中不相同的元素|

以上操作符都可以去掉等号单独使用，例如 `H = S - T`

> **操作函数**
```py
S.add(x)     # 添加元素
S.discard(x) # 移除元素，如果x不在S中不报错
S.remove(x)  # 移除元素，如果x不在S中报错，KeyError
S.clear()    # 移除所有元素
S.pop()      # 随意移除并返回一个元素，如果S为空报错，KeyError
```
> **应用场景**
1. **列表数据去重**
将list转化为set，再将set转回list

## 1.2 list 列表

```py
L[a:b:c] # 表示在第a至第b-1个元素之间，隔c-1个元素取值
```
例如 `L[0:-1:2]` 表示在第一个至最后一个元素之间，隔1个元素取值

```py
L = [1, 2, 3, 4, 5, 6]
L[0:-1:2]

>>>
[1, 3, 5]
```

```py
L[::-1] # 表示从右至左逆序

>>>
[6, 5, 4, 3, 2, 1]
```

**列表推导式**（list内嵌复合表达式）
```py
[x for x in data if condition]

[x+1 if condition else x-1 for x in data]
```

**其他操作**
`range(left, right, step)`

```py
list(range(3,10,3))

>>>
[3, 6, 9]
```
`zip(list1, list2)`

```py
list(zip(['A','B'], [1,2]))   >>> [('A',1), ('B',2)]
dict(zip(['A','B'], [1,2]))   >>> {'A':1, 'B':2}
```

## 1.3 字典, 键值对
> **操作函数**
```py
d.get(k, <default>) # 键k存在，则返回相应值，不存在则返回<default>
d.pop(k, <default>) # 键k存在，则取出相应值，不存在则返回<default>
d.popitem()         # 随机取出一个键值对，以元组形式返回
```



---

# 2. 文件操作
> **开关**
```py
f = open(<文件名>, <打开模式>)
# 代码块
f.close()
```
|打开模式| 描述|
|-|-|
|'t'| 文本文件模式，只读，默认值|
|'b'| 二进制文件模式，只读|
|'r'| 只读，若文件不存在会报错|
|'w'| 覆盖写入|
|'x'| 创建写入，若文件存在则报错|
|'a'| 追加写入|
|'+'| 与r/w/x/a一同使用，在原功能基础上增加同时读写功能|
|'wb'| 二进制覆盖写|
|'...'| ...|

> **读写**
```py
# 读
f.read(size)      # 读入全部（可选参数：读取前size长度）
f.readline(size)  # 读入一行（可选参数：读取前size长度）
f.readlines(hint) # 读入全部行，返回一个列表（可选参数：读取前hint行）

# 写
f.write(s)          # 写入一个字符串或字节流
f.writelines(lines) # 写入一个字符串列表
f.seek(offset)      # 改变文件操作指针的位置（0: 文件开头，1: 当前位置，2: 文件结尾）
```
例如：
```py
f.writelines(["aa", "bb"])
f.seek(0) # 不写这一行代码，该程序将不会输出任何内容
for line in f:
    print(line)
f.close()

>>>
"aabb"
```


---
# 3. 函数
## 3.1 常用函数
**eval()**
执行并返回一个字符串表达式的值
```py
a = eval("1 + 4")
b = eval("a * 6")
```

**map(参数1, 参数2)**
将参数1的方法作用于参数2得每一个元素
```py
list(map(eval, ["1+1", "2*2"]))

>>>
[2, 4]
```

---
# 4. 库
可以在 pypi.org 上根据关键字搜索第三方库
```py
pip install <库名>
pip uninstall <库名>
pip install -U <库名> # 更新库
pip download <库名> # 下载但不安装
pip show <库名> # 查看库的详细信息
pip search <库名> # 检索与该库相关的信息
```

## 4.1 常用库
> **数据处理**

**数据分析**
numpy, pandas, scipy

**数据可视化**
matplotlib (matplotlib.pyplot)
seaborn (统计类数据)
Mayavi (三维数据可视化)

**文本处理**
PyPDF2 (处理pdf文件)
NLTK (自然语言文本处理)
Python-docx (Word文件)

wordcloud (绘制词云)

**机器学习**
Sickit-learn
TensorFlow
MXNet (基于神经网络的深度学习计算框架)

> **web**

**网络爬虫**
Requests, Scrapy, pysipder

**Web信息提取**
Beautiful Soup, Re (正则表达式), Python-Goose

**Web网站开发**
Django (大型网站), Pyramid (中型), Flask (简易)

**网络应用开发**
WeRobot (微信小程序), aip (百度AI框架), MyQR (定制二维码)
...

> **人机交互与设计**

**图形用户界面 GUI**
PyQt5, wxPython, PyGObject

**游戏开发**
PyGame (简单)
Panda3D (3D渲染和游戏开发)
cocos2d (专业级2D游戏)





