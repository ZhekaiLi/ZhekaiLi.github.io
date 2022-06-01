---
layout: wiki
title: Java
cate1: Others
cate2:
description: 
keywords: Java
---

# 1. Intellij IDEA 操作

## 1.1 在目标语句后加上 `.XXX` 以补全
for循环
```java
list.for
for (Integer integer : list) {}
```

索引for循环
```java
list.fori
for (int i = 0; i < list.size(); i++) {}
```

索引倒序for循环
```java
list.forr 
for (int i = list.size() - 1; i >= 0; i--) {}
```

声明变量
```java
123.var
int i = 123;
```

if语句
```java
i == 4.if
if (i == 4) {}
```

try-catch
```java
File file = new File(filename);.try
try {
    File file2 = new File(filename);
} catch (Exception e) {
    e.printStackTrace();
}
```

## 1.2 简写补全
main函数 `psvm`
println函数 `sout`

## 1.3 其他
改变相同变量的命名：选中该变量，按shift+F6

# 2. 数据结构
> **List**

```java
int[] L1 = new int[10];
int[] L2 = {0, 1};

int[][] LL = { {1, 0}, {0, 1} };
```
```java
[int] Arrays.stream(L2).sum();                // 一维数组求和
[int[]] Arrays.stream(L2).sorted().toArray(); // 由小至大排序
```

> **ArrayList**

```java
ArrayList<Integer> al = new ArrayList();
```
```java
al.add(0);       // 添加元素
[int] al.size();
```
```java
Collection.reverse(al); // 逆序
```

> **LinkedList**

```java
Queue<Integer> queue = new LinkedList<>();
```
```java
queue.add(0);          // 从队尾插入
[int] queue.remove(0); // 从队头取出
```

> **TreeSet**

TreeSet 的本质是一个<font color=red>有序的，并且没有重复元素的集合</font>，它是通过 TreeMap 实现的
```java
TreeSet<Integer> ts = new TreeSet();
TreeSet<Integer>[] tss = new TreeSet[10];
tss[0] = ts;
tss[1] = new TreeSet<Integer>();
```
```java
ts.add(0); // 添加元素
[boolean] ts.contains(0); // 是否包含元素
[int] ts.size();          // 包含的元素个数
```
遍历
```java
for (int i: ts) { 语句块; }
```

> **HashMap** 键值对

```java
HashMap<keyType, valueType> hm = new HashMap<>();
```
```java
hm.put(key1, value1);           // 覆盖性赋值
[valueType] hm.get(key1);       // 读取value
[Set<keyType>] hm.keySet();     // 读取键的集合
[boolean] hm.containsKey(key1); // 是否包含键
```

# 3. 异常处理
> **throw eror**

```java
throw new 错误类型("报错信息");
```
```java
if (input < 0>)
    throw new IllegalArgumentException("input is invalid");
```

# 4. 常用类
> **StringBuilder**：构建字符串

```java
StringBuilder sb = new StringBuilder();
```
```java
sb.append(String.format("%d + %d = %d", 1, 2, 3));
sb.append(String.format('\n'));
sb.append(String.format("%d * %d = %d", 1, 2, 2));

String string = sb.toString();
```
