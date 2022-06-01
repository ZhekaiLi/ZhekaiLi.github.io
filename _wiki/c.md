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