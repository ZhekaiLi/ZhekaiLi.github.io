---
layout: wiki
title: os
cate1: Python
cate2: -libs
description: 
keywords: Python
---

```py
import os
```

## 1. os.path 路径操作

```py
import os.path as op
```

```py
op.abspath(path) # 绝对路径
op.relpath(path) # 相对路径
op.dirname(path) # 目录名
op.basename(path) # 文件名
op.exists(path) # 判断文件或目录是否存在
op.isfile(path) # 判断路径是否为文件
op.isdir(path) # 判断路径是否为目录
op.getsize(path) # 返回文件的字节大小
```

## 2. 运行命令与程序

```py
os.system(程序路径/ 命令)
```

可以填一个exe文件路径，也可以填诸如 "pip install numpy" 这样的命令

## 3. 环境参数

```py
os.getcwd()    # 返回当前路径(绝对路径)
os.chdir(path) # 修改当前程序执行的路径
    os.chdir(os.path.dirname(__file__)) # 修改当前程序执行的路径为当前文件所在目录

os.getlogin()  # 获取当前系统登陆用户名
os.cpu_count() # 获取当前计算机cpu数量
```


