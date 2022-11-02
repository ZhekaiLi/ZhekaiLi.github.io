---
layout: wiki
title: PuLP
cate1: Python
cate2: -libs
description: 
keywords: Python
---

`PuLP` 可用于解决线性、整形规划问题


常用框架


```py
from pulp import *

## max 3 x + 5 y
## s.t.  x         <= 4
##              2y <= 12
##     3 x + 2 y <= 18
##       x         >= 0
##               y >= 0

prob = LpProblem("WynCor", LpMaximize)
# Decision variables
x = LpVariable("x", 0)
y = LpVariable("y", 0)
# Constraints
prob += x <=4
prob += 2*y <=12
prob += 3*x + 2*y <=18
# Objective
prob += 3*x + 5*y
# Solve
prob.solve()
LpStatus[prob.status]
# Results
x.varValue
y.varValue
value(prob.objective)
```



解决线性规划问题: [一个比较复杂的示例例 in Jupyter Notebook](../_files/JupyterNotebook/../../../_files/JupyterNotebook/Linear_programming_with_PuLP.ipynb)