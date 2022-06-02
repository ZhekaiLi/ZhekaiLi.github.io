---
layout: wiki
title: 与时间相关的库
cate1: Python
cate2: -libs
description: 
keywords: Python
---

# datetime

将字符串形式的数据转化为datetime时间对象
```py
import datetimes as dt
```

```py
import dateutil
dateutil.parser.parse('01/11/2011')
>>>
datetime.datetime(2011, 1, 11, 0, 0)
```
各种形式都可以 `2011/01/11` `2011-01-11` `2021-JAN-11`

当前时间
```py
dt.date.today()
```

减去/加上一段时间
```py
dt.timedelta(days=n)
```
`days=`, `hours=`, `minutes=`, `seconds=`
