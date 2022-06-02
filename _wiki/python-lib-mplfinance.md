---
layout: wiki
title: mplfinance
categories: Programming Language
cate1: Python
cate2: -libs
description: 
keywords: Python
---
金融画图工具，源于matplotlib
```py
import mplfinance as fin
import matplotlib.pyplot as plt
```

**K线图**
```py
fig, ax = plt.subplots()
fin.candlestick_ochl(ax, arr) 
```
其中 `arr` 需为一个 N*4 的数组，依次包含 open, close, high, low 四列数据
