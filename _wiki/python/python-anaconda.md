---
layout: wiki
title: Anaconda
cate1: Python
cate2:
description: 
keywords: Python
mathjax: true
mermaid: true
---

Using Command Line to mange python environments & use Anaconda

打开 jupyter
```py
jupyter lab
jupyter notebook
```

关闭 jupter `Crtl + C `


# Environment

```py
conda env list # 查看所有虚拟环境
conda list     # 查看当前环境下安装的包
```

导出当前环境下安装的所有包的版本信息
```py
pip freeze > requirements.txt
```

then in `requirements.txt`:
```txt
altgraph==0.17.3
asttokens==2.2.1
auto-py-to-exe==2.36.0
backcall==0.2.0
bottle==0.12.25
bottle-websocket==0.2.9
cffi==1.15.1
colorama==0.4.6
comm==0.1.3
contourpy==1.1.0
cx-Oracle==8.3.0
cycler==0.11.0
debugpy==1.6.7
decorator==5.1.1
...
```

安装 `requirements.txt` 内的所包含的包及其指定版本

```py
pip install -r requirements.txt
```
