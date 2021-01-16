---
layout: post
title: Integer Programming
categories: ICM
description: Personal Notes
keywords: [Integer Programming, ICM]
---

相较于线性规划，整数规划要复杂的多，一般可以用以下几种方法来求解

# 1 分支定界法
分支定界法主要由三步构成，分支、定界和剪枝：
1. **分支**：根据线性规划的结果，把可行解空间反复分割为越来越小的子集。
2. **定界**：对分支后的每个子集，使用线性规划计算其目标上界和下界。
3. **剪枝**：每次分支后，凡是界限超出已知可行解目标值的子集不再进行进一步分支

1, 2 循环进行，并穿插 3，直到找到整数解。例如求解以下整数规划问题：
$$\max\;z=40x+90y,\;\;s.t.\begin{cases}
9x+7y\leq56\\
7x+20y\leq70\\
x,y\in N
\end{cases}$$

### 1.1 分支 1-2：$B_1,B_2$
使用线性规划求最优解（非整数），可得 $x=4.81,y=1.82,z=355.88$
```matlab
c = [40; 90];
A = [9, 7; 7, 20]; b = [56; 70];

x = linprog(-c, A, b, [], [], zeros(2,1))
value = c' * x
```
从而得到目标最优值的上下界 $z\in[0,356]$。利用 $x$ 进行分支（由于 4-5 之间不存在整数，故可忽略）
$$x=4.81\to x\in[0,4]+x\in[5,\infty)$$

$B_1:$
$$\max\;z=40x+90y,\;\;s.t.\begin{cases}
9x+7y\leq56\\
7x+20y\leq70\\
0\leq x\leq 4\\
x,y\in N
\end{cases}$$

$B_2:$
$$\max\;z=40x+90y,\;\;s.t.\begin{cases}
9x+7y\leq56\\
7x+20y\leq70\\
x\geq 5\\
x,y\in N
\end{cases}$$

### 1.2 定界
分别对 $B_1,B_2$ 使用线性规划求最优解（代码略），可得：
$$\begin{aligned}
& B_1: x=4,y=2.1,z=349\\
& B_2: x=5,y=1.57,z=341.43
\end{aligned}$$

此时更新目标最优值的上下界 $z\in[0,349]$
### 1.3 分支 1-4：$B_{11},B_{12},B_{21},B_{22}$
同分支 1，此时可以利用 $y$ 进行分支：
$$\begin{aligned}
& B_1: y=2.1\to y\in[0,2]+y\in[3,\infty)\\
& B_2: y=1.57\to y\in[0,1]+y\in[2,\infty)
\end{aligned}$$

从而得到新的分支 $B_{11},B_{12},B_{21},B_{22}$

### 1.4 定界
同 1.2，
$$\begin{aligned}
& B_{11}: x=4,y=2,z=340\\
& B_{12}: x=1.43,y=3,z=327.14
\end{aligned}$$

此时由于 $B_{11}$ 为整数解且其结果大于 $B_{12}$，可以直接剪掉 $B_{12}$（**剪枝 1**）

$$\begin{aligned}
& B_{21}: x=5.44,y=1,z=307.78\\
& B_{22}: \text{无解}
\end{aligned}$$

同理，剪去 $B_{21}, B_{22}$（**剪枝 2**），并最终得到该整数规划的最优解 $B_{11}: x=4,y=2,z=340$

# 2 蒙特卡罗法
当解空间过大时，可以使用概率的方法随机选择部分解尽心验证，当随机解足够多是便能大概率获得最优解。例如求解以下非线性规划的问题：

<center>
    <img src="https://github.com/ZhekaiLi/PICTURE-for-markdown/raw/master/2021-01/Snipaste_2021-01-16_10-57-39.jpg"> <br>
    <div style="color: #999;">图 1 蒙特卡罗法示例</div>
</center><br>

```matlab
rng(sum(clock));  % 根据时间改变随机种子
p0 = 0;
for i=1:10^6
    x = 99 * rand(5,1);
	x1 = floor(x); x2 = ceil(x);
	[f,g] = mengte(x1);
    if sum(g<=0) == 4
        if p0 <= f
            x0 = x1; p0 = f;
        end
    end
    [f,g] = mengte(x2);
    if sum(g<=0) == 4
        if p0 <= f
            x0 = x2; p0 = f;
        end
    end
end

function [f,g] = mengte(x)
    % 定义 f 为目标函数值，g 为不等式约束（令规定 h 代表等式约束，不过此题没有）
    f = x(1)^2 + x(2)^2 + 3*x(3)^2 + 4*x(4)^2 + ...
        2*x(5) - 8*x(1) - 2*x(2) - 3*x(3) - x(4) - 2*x(5);
    g = [sum(x) - 400,
        x(1) + 2*x(2) + 2*x(3) + x(4) + 6*x(5) - 800,
        2*x(1) + x(2) + 6*x(3) - 200,
        x(3) + x(4) + 5*x(5) - 200];
end
```
