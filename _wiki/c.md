---
layout: wiki
title: C
cate1: Others
cate2:
description: 
keywords: C
---

```c
#include <stdio.h> // 标准输入输出头文件
void main( ) {
    int input, min=0;
    scanf("%d", &input);
    if(input < min) min = input;
    else;
    printf("min = %d\n", min);
}
```

`stdio.h` standard input output head

```mermaid
graph LR
A(数据类型)
    A-->B1(基本类型)
        B1--->C11("字符型 (char)")
        B1--->C12("整型 (short, int, long, signed, unsigned)")
        B1--->C13("实型 (float, double)")
        B1--->C14("枚举型 (enum)")
    A-->B2(构造类型)
        B2--->C21("数组类型 ([ ])")
        B2--->C22("结构体类型 (struct)")
        B2--->C23("共用体类型 (union)")
    A-->B3("指针类型 (*)")
    A-->B4("空类型 (void)") 
```

# 1. 数据类型
> **常量**

```c
#define PI 3.14
```
> **转译字符**

```c
"\n" // 换行
"\t" // 横向跳格
"\b" // 退格
"\r" // 回车
"\\" // 反斜杠
"\'" // 单引号字符
```

## 1.1 变量
### 1.1.1 变量的存储特性
静态变量 `static`
- 静态局部变量，声明、使用于函数内部，特点是不会随着函数运行的结束而销毁，默认值为 `0` or `'\0'`。一般用于<span style="background-color: yellow; color: black;">保留该变量函数在上次调用结束后的值</span>
- 静态全局变量

寄存器 `register`
- 用于修饰需要被高频访问的变量，例如 `register int x;`。一般只允许声明两个寄存器变量

### 1.1.2 整型与浮点型
> **整型**

范围与大小
1. `short`,`int`: $-2^{15}\sim2^{15}-1$ (2 byte = 16 digit)
2. `long`: $-2^{31}\sim2^{31}-1$ (4 byte = 32 digit)

符号
```c
[signed] int n; // 默认有符号
unsigned int n; // 设置为无符号
```

八进制、十六进制整型
```c
int n8 = 012;   // = 1*8^1 + 2*8^0 = 10
int n16 = 0X12; // = 1*16^1 + 2*16^0 = 18
```

> **浮点型**

`float` 精确到7位（包括小数点前后）4 digit
`double` 精确到15位（包括小数点前后）8 digit

### 1.1.3 字符与字符串
C语言中没有字符串对象，因此使用字符数组来储存字符串
```c
char c = 'a';
char s[] = "abc";
```
相关函数
```c
#include <string.h>

strcmp(str1, str2);  // 比较字符串：相等返回0，str1>str2返回正整数，反之负整数
int l = strlen(str); // 计算长度
```

## 1.2 运算符
> **算术运算符** `+`, `-`, `*`, `/`, `%`(取余)

`++`, `--`: `a++` 先赋值再运算，`++a` 先运算再赋值（example见Section-逻辑运算符）

整形与整形相除得整形，整形与浮点型的任何算术操作均得浮点型

> **位运算符** 计算每个digit，`&`, `|`, `^`(异或)

> **关系运算符** `!=`

C语言使用 `0`, `1`(int) 表示 `False`, `True`。例如 `2<5<2 = 1<2 = 1` 

### 1.2.1 逻辑运算符
`!`, `&&`, `||`
逻辑变量与其他运算符之间的转换（注意方向性）：
- `0 || 0.0 || '\0' || NULL` $\to$ `False` $\to$ `0`
- `非零` $\to$ `True` $\to$ `1`

示例
```c
int a=0, b=1, c;
c = (a++) && (b=3) // 由于是先赋值再运算，因此左侧a=0=False，直接判假，并不再进行右侧的赋值操作

>>>
a = 1; b = 1; c = 0;
 ``` 

### 1.2.2 条件运算符
```c
int max, a=1, b=2;
max = a>b? a: b;
 ```

## 1.3 数据类型转换
**自动转换**：由所占空间小的向占空间大的方向转变，例如在运算中常发生的 `int`$\to$`double`

**赋值转换**: 
- `int=double` 把小数砍掉，但可能因为double太大导致数值剧变
- `double=int` 补满欠缺位，数值大小不变

**强制类型转换**: `a = (double)a`

# 2. 函数
## 2.1 常用函数
### stdio.h
#### 输入输出
> **标准输出**
```c
printf("格式说明", [变量名])
```
`格式说明` = `%[flag][width][.prec][F|N|h|L][type]`
- `[flag]`: 
`-` 左对齐右边补空格，否则右对齐左边补空格
`+`: 正数输出正号，负数输出负号
`空格`: 正数输出空格，负数输出负号
- `[width]`: 限定输出的最小的宽度，少则补空格，多不变
- `[.prec]`: 小数点后的精确位数
- `[F|N|h|L]`: 长度修饰符，与指针相关
- `[type]`: d整形，f浮点型，c字符, s字符串

示例：
```c
float pi = 3.14159;
printf("%+6.2f", pi);
