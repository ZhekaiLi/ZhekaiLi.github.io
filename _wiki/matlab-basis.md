---
layout: wiki
title: Basis
cate1: Matlab
cate2:
description: 
keywords: Matlab
mathjax: true
---

# 1. Basic
## 1.1 常用功能
### 1.1.1 帮助
除了 `help` 指令之外，还可以使用 `lookup`，该指令能够更具用户提供的可能不够完整的关键词，去搜索一组与其相关的指令。例如：
```matlab
lookfor integral  % 查找有关积分的指令
```
### 1.1.2 字符串
使用单引号声明字符串，matlab 中不存在双引号






# 2. Statistics
## 2.1 常用函数
```matlab
[max, argmax] = max(List); % max / argmax
```

## 2.2 Random
```matlab

```








# 3. Math
## 3.1 矩阵
### 3.1.1 矩阵运算
```matlab
A' % 共轭转置
```

### 3.1.2 特殊矩阵
**(1) 空矩阵**是一种特殊矩阵，其大小为零，可用于删除矩阵中的行与列。例如
```matlab
A = eye(3);
A(2:3, :) = [] 

>>>
[1 0 0]
```

**(2) 对角矩阵**
```matlab
A = diag(v)  % 由向量创建对角矩阵
v = diag(A)  % 由矩阵的对角元素创建向量

vp = diag(A, 1)  % 得到矩阵对角线上移一行的元素组成的列向量
vm = diag(A, -1)  % 得到矩阵对角线下移一行的元素组成的列向量
```

### 3.1.3 扩充矩阵
```matlab
A = [1, 2, 3];
repmat(A, 3, 2)

>>>
[[1,2,3,1,2,3]
[1,2,3,1,2,3]
[1,2,3,1,2,3]]
```

### 3.1.4 特征向量与特征值
```matlab
[v, d] = eig(A);

p = poly(A)  % 矩阵的特征多项式
p = poly(v)  % 以向量中元素为根的多项式
```

## 3.2 多项式
### 3.2.1 表达与计算
对于以下多项式
$$y(x)=x^3 + 2x^2+3x+4$$
```matlab
syms x;
p = [1, 2, 3, 4];

% 表达式
poly2sym(p, 'x') >>> x^3 + 2*x^2 + 3*x + 4
% 求值
polyval(p, [0, 1]) >>> [4, 10]
% 求根
roots(p) >>>   -1.6506 + 0.0000i
-0.1747 + 1.5469i
-0.1747 - 1.5469i
```

### 3.2.3 多项式的矩阵运算
`y = polyvalm(p, A)`  相当于用矩阵 $A$ 代替多项式的变量来对矩阵而不是对数组进行运算，$A$ 必须是方阵。例如：
$$A=\begin{pmatrix}
1 & 2\\
3 & 4
\end{pmatrix},\;\;p(A)=A^2+3A+2I$$
```matlab
A = [1, 2; 3, 4];
p = [1, 3, 2];

polyvalm(p, A)
```

### 3.2.4 多项式的卷积与除法运算
```matlab
conv(u, v);  % 卷积

[q, r] = deconv(u, v);  % q 商多项式；r 余数多项式
```

## 3.3 代数式
```matlab
syms x a b c;
y = a*x^2 + b*x + c;
```
$$y=ax^2 + bx + c$$

代入数值：`a=1, b=2, c=1`
```matlab
y = subs(y, [a,b,c], [1,2,1]);
```
$$y=x^2 + 2x + 1$$

将代数式转化为关于 `x` 的函数
```matlab
y_func = matlabFunction(y);
ans = y_func(1)

>>> ans = 4
```




## 3.4 解方程组和不等式
**二元一次方程组**
```matlab
syms a b;
eq1 = a - 2b - 6;
eq2 = 2a + b - 2;
vpasolve([eq1,eq2], [a,b])
```

**求定义域内的方程解：使用不等式限定定义域**。例如下例中 `cos(2*x)=cos(x)` 有无数解，但在限定定义域之内解唯一
```matlab
syms x;

cond1 = x > 1;
cond2 = x < 3;
cond3 = cos(2*x) - cos(x);
conds = [cond1, cond2, cond3];

solve(conds, x)
```

## 3.5 导数与积分
```matlab
subs(expr, x, x-t); % 将表达式中的变量x替换为x-t
```

# 4. Data Structure
## 4.1 结构数组
### 4.1.1 结构数组的定义
**方法 1**
```matlab
结构名(index).属性名 = 属性值;
```
例如：
```matlab
student.name = 'John'; 
student.ID = '000'; 

student(2).name = 'Rose'; 
student(2).ID = '001'; 
```
**方法 2**
```matlab
结构名 = struct(属性1, 属性值1, ...);
```
例如:
```matlab
student = struct('name', 'John', 'ID', '000');
student(2) = struct('name', 'Rose', 'ID', '001');
```
### 4.2 相关函数
```matlab
fieldnames()  % 查询结构数据的属性名
getfield()  % 查询结构数据的属性值
setfield()  % 设置结构数据的属性值
rmfield()  % 删除属性
isfield()  % 检查是否为数组的属性
isstruct()  % 检查数组是否为结构型
```

## 4.2 细胞数组
使用大括号 `{}`，能够吧不同类型、维数的数组组成为一个数组。例如：
```matlab
c = {A, sum(A), sum(sum(A))};
```

### 4.2.1 细胞数组的生成、查看
示例：
```matlab
A = cell(2, 2)  % 声明细胞数组的维度，这行不写也行

A{1, 1} = [1:5; 6:10]; 
A{1, 2} = 'Anne'; 
A{2, 1} = 3+7i; 
A{2, 2} = 0:pi/10:pi;

A{2, 2}(1) >>> 0
A{4}(1) >>> 0  % 效果同上一行
```

### 4.2.2 相关函数
```matlab
celldisp()  % 显示细胞数组的内容 
cell()      % 生成细胞数组 
cellplot()  % 用图形方式显示细胞数组 
num2cell()  % 把数值型转换为细胞型 
deal()         % 输入和输出的匹配 
cell2struct()  % 把细胞数组转换为结构数组 
struct2cell()  % 把结构数组转换为细胞数组 
iscell()       % 检验数组是否为细胞型
```

# 5. Function
基本框架
```matlab
function [output1, ...] = func_name(input1, ...)
    ...
end
```

## 5.1 Basic
### 5.1.1 读取输入参数的个数

示例：
```matlab
function [c] = plus(a,b)
    if nargin < 2, b = 1;
        if nargin < 1, a = 1;
        end, end
    c = a + b;
end
```

