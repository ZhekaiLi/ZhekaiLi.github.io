<!-- ---
layout: wiki
title: Basis
cate1: Python
cate2:
description: 
keywords: Python
mathjax: true
mermaid: true
--- -->


找到数组里第二小的元素

```py
def secondMin(arr):
    if arr[0] <= arr[1]:
        m,m2 = arr[0], arr[1]
    else:
        m,m2 = arr[1], arr[0]
    for i in range(2,len(arr)):
        if arr[i] <= m:
            m2 = m
            m = arr[i]
    return m2
```


