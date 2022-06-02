---
layout: wiki
title: tushare
cate1: Python
cate2: -libs
description: 
keywords: Python
---

tushare 包是一个金融领域的大数据接口，可以方便地查看股票、基金、期货等数据

```py
import pandas as pd
import tushare as ts

pro = ts.pro_api('接口token')
```

**日K线数据**
```py
df = pro.daily(ts_code='000001.SZ', start_date='20210101', end_date='20220121')
```
