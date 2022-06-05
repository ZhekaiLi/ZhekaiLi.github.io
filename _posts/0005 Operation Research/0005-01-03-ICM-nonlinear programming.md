---
layout: post
title: Nonlinear Programming
categories: Operation-Research
description: Personal Notes
keywords: OR, ICM
mathjax: true
---

# 1 非线性规划的 Matlab 标准型
$$\underset{x}{\min}\;f(x),\;\;s.t.\begin{cases}
Ax\leq b\\
Aeq\cdot x=beq\\
C(x)\leq 0\\
Ceq(x)=0
\end{cases}$$

where, $C(x),Ceq(x)$ 是非线性向量函数
```matlab
% 完整形式
% NONLCON 为非线性约束条件 
[x,y] = fmincon('func', x0, A, b, Aeq, beq, LB, UB, NONLCON, OPTIONS)
```

# 2 示例
求解以下非线性规划问题：

<center>
    <img src="/images/2021-01/Snipaste_2021-01-16_11-19-52.jpg" style="zoom:50%"> <br>
    <div style="color: #999;">图 1 非线性规划示例</div>
</center><br>

```matlab
options = optimset('largescale','off');
[x,y] = fmincon('fun1',rand(3,1),[],[],[],[],zeros(3,1),[],'fun2', options)


function f = fun1(x)
    % 定义 f 为目标函数
    f = sum(x.^2) + 8;
end

function [g,h] = fun2(x)
    % 定义 g 为不等式约束,，h 为等式约束
    g = [-x(1)^2 + x(2) - x(3)^2,
        x(1) + x(2)^2 + x(3)^3 - 20];
    h = [-x(1) - x(2)^2 + 2,
        x(2) + 2*x(3)^2 - 3];
end
```

# 3 二次规划
二次规划为非线性规划中的一种，旨在解决目标函数为二次函数，但约束条件都是线性的非线性规划问题。
## 3.1 二次规划的 Matlab 标准型
$$\min\frac{1}{2}x^THx+f^Tx,\;\;s.t.\begin{cases}
Ax\leq b\\
Aeq\cdot x=beq
\end{cases}$$
```matlab
[x,fval] = quadprog(H, f, A, b, Aeq, beq, LB, UB, x0, OPTIONS);
```

## 3.2 示例
求解以下二次规划问题：
<center>
    <img src="/images/2021-01/Snipaste_2021-01-16_14-35-14.jpg" style="zoom:50%"> <br>
    <div style="color: #999;">图 2 二次规划示例</div>
</center><br>

```matlab
h = [4,-4;-4,8];
f = [-6;-3];
a = [1,1;4,1];
b = [3;9];

[x,value] = quadprog(h,f,a,b,[],[],zeros(2,1))
```

