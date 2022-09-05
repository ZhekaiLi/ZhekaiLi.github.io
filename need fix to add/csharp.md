---
layout: wiki
title: Csharp
cate1: Others
cate2:
description: 打造好用的 Windows Terminal
keywords: Windows Terminal
---

# 创建项目 & VS 设置
使用平台：Visual Studio 2019

**创建项目**：选择 `控制台应用 (.NET Framework)`
<img src="https://img-blog.csdnimg.cn/20210416202637939.png" width="80%">
**创建完成后的初始页面**：
区域1：引用区
引用 `命名空间 namespace`（类似 Python 中的 import 库）

区域2：代码区
由大到小分别为 `命名空间 namespace` > `类 class` > `方法 method`，分别对应区域 2, 2.1, 2.1.1（可以将这三者<span style="background-color: yellow; color: black;">粗略地</span>理解为 Python 中的 库 > 类 > 方法）
<img src="https://img-blog.csdnimg.cn/20210416202949880.png" width="80%">

**修改字体：建议使用 Consolas**

工具 $\to$ 选项 $\to$ 字体和颜色
<img src="https://img-blog.csdnimg.cn/20210416232705144.png" width="80%">

**更改启动项目**
在默认情况下，不管解决方案中含有几个项，默认情况下在点击启动 & F5 时只会运行第一个项，例如下图中的 ConsoleApp2。
<img src="https://img-blog.csdnimg.cn/20210416233145416.png" width="80%">

若想要运行其他项，例如上图中的 ConsoleApp3，则需进行一些设置：右键单击解决方案 $\to$ 属性 $\to$ 更改启动项目为 "当前选定内容"
<img src="https://img-blog.csdnimg.cn/20210416233437775.png" width="35%"> <img src="https://img-blog.csdnimg.cn/20210416233526709.png" width="61%">

# Hello World

```csharp
using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace ConsoleApp2
{
    class Program
    {
        static void Main(string[] args)
        {
            Console.WriteLine("Hello World!");
            Console.ReadKey(); // 获取用户按下的下一个字符
        }
    }
}
```
第二行代码 `Console.ReadKey();` 功能见注释，目的在于<span style="background-color: yellow; color: black;">暂停程序，防止控制台闪退</span>（如果不添加，控制台在输出 "Hello World" 后将马上退出）

**运行：单击运行按钮 & F5**

**错误检查：点击生成解决方案 & F6**

# 注释
**单行注释 `//`**

```csharp
// 这是单行注释
```
**多行注释 `/**/`**

```csharp
/* 这是
多行注释 */
```
**快捷注释 `Ctrl + K + C`**
选中目标区域后按下 `Ctrl + K + C` （取消注释为 `Ctrl + K + U`）

**文档注释 `///`**
在命名空间、类、方法前输入 `///`，会自动生成一个文档注释模板，例如:

```csharp
/// <summary>
/// 
/// </summary>
/// <param name="n1"></param>
/// <param name="n2"></param>
/// <returns></returns>
public static int GetMax(int n1, int n2)
{
    int n = 1;
    return n1 > n2 ? n1 : n2;
}
```
填入内容后:

```csharp
/// <summary>
/// 求两个整数中的较大值
/// </summary>
/// <param name="n1">第一个整数</param>
/// <param name="n2">第二个整数</param>
/// <returns>较大的整数</returns>
public static int GetMax(int n1, int n2)
{
    return n1 > n2 ? n1 : n2;
}
```

# 快捷键
`Ctrl + S` 保存
`F1` 查看文档
`Ctrl + K + C`  快捷注释（取消注释为 `Ctrl + K + U`）

`#region ... # endregion` 折叠冗余代码，使整体代码更加简洁，如下图：
1. 三个大红框分别为：折叠前，添加后，折叠后
2. 左侧出现的加减符号用于折叠及展开
![在这里插入图片描述](https://img-blog.csdnimg.cn/20210417124445343.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L3dlaXhpbl80MzcyODEzOA==,size_16,color_FFFFFF,t_70)

# 变量和数据类型
示例:

```csharp
int n1 = 1;
double n2 = 3.14;
string name = "小红";
char gender = '女';

bool ifCorrect = true;
```
## .1 变量的作用范围
在一个 `{}` 内声明的变量仅在当前大括号内生效（可读、可写），这个范围包括大括套的嵌套。

而在两个平行的函数之间，由于无法在函数1中访问函数2内定义的变量，我们可以通过<span style="background-color: yellow; color: black;">在类中创建静态变量</span>的方式，来模拟全局变量。以下代码展示了静态变量的基础应用:

```csharp
class Program
{
    static double _PI = 3.14;
    static void Main(string[] args)
    {
    	double r = 2;
    	double A = _PI * r * r;
		
        AccuratedPI();
        double A_accurated = _PI * r * r;
        Console.WriteLine("Initial:{0}, Accurated:{1}", A, A_accurated);
        Console.ReadKey();
    }
    
    static void AccuratedPI()
    {
        _PI = 3.14159265;
    }
}

"Initial:12.56, Accurated:12.5663706"
```

## .2 值类型 vs 引用类型
<span style="background-color: yellow; color: black;">注意：这个 Section 中有大量在之后的博客中才会具体介绍的内容，读者可以先跳过</span>

C# 中的变量主要分为这两种类型。其中：

值类型：`int`, `double`, `char`, `enum`, `struct`

引用类型：`string`, `自定义类`, `数组`

还有一种特殊的 `var` 类型，能够根据输入自动为变量分配数据类型。例如下例中的 n 会被自动分配为 int 类型，ns 为 int[] 类型

```csharp
var n = 3;
var ns = new int[] { 0, 1 };
```
> 不理解以上 `enum, struct, 自定义类, 数组` 这几个概念的读者请忽略他们，这些内容将在之后的两篇博客中具体描述：[精简 C# 入门（二）](https://blog.csdn.net/weixin_43728138/article/details/115793759), [精简 C# 入门（三）](https://blog.csdn.net/weixin_43728138/article/details/115840788))

**值类型、引用类型在内存分配上的区别**（这部分不重要，可以忽略）
1. 值类型行直接储存在栈之中
2. 引用类型的地址储存在栈之中，但其本体储存与堆之中
![在这里插入图片描述](https://img-blog.csdnimg.cn/20210422153740554.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L3dlaXhpbl80MzcyODEzOA==,size_16,color_FFFFFF,t_70)


**值类型、引用类型在可修改性上的区别** (这个 "可修改性" 的表述可能不太恰当，日后会做修改)。如下图，可得
1. 对于值类型 `double d` 无论在外部函数中怎么修改，其值均为初值
2. 对于引用类型 `string name` 和 `int[] list`：
在外部函数中<span style="background-color: yellow; color: black;">对其整体的修改不会影响它们在 Main 函数中的值</span>，正如 Change 1
在外部函数中<span style="background-color: yellow; color: black;">对其元素的修改会影响</span>，正如 Change 2
(string 可以理解为只允许读不允许写的 char[]，这导致无法对其元素进行修改)
![在这里插入图片描述](https://img-blog.csdnimg.cn/20210422160910594.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L3dlaXhpbl80MzcyODEzOA==,size_16,color_FFFFFF,t_70)

## .3 数组 list
一次性存储多个相同类型的变量

```csharp
数组类型[] 数组名 = new 数组类型[(数组长度)] // （）意味着可以省略
```
**数组的声明**

示例（1）：

```csharp
int[] nums = new int[10]; // 声明一个数组，此时默认数组内 10 个元素均为 0
nums[0] = 1;              // 修改第 0 个元素为 1
```
示例（2）：

```csharp
int[] nums1 = { 1, 2, 3 }；
int[] nums2 = new int[3] { 1, 2, 3 };
```
**数组的属性**

```csharp
nums.Length; // 长度
```
不同于变量，外部函数<span style="background-color: yellow; color: black;">可以直接对传入的数组进行修改，从而改变数组在该函数外部的值</span>。例如以下代码中，`Change` 函数更改了 `Main` 函数中的数组 `nums`，但并未改变变量 `n`:

```csharp
static void Main(string[] args)
{
    int n = 0;
    int[] nums = { 0 };
    Program.Change(n, nums);

    Console.WriteLine(n);
    Console.WriteLine(nums[0]);
    Console.ReadKey();
}

static void Change(int n, int[] nums)
{
    n += 1;
    nums[0] += 1; 
}

"0"
"1"
```

### .3.1 冒泡排序
由于本博客默认读者并不是完全不会其他任何计算机语言的，因此冒泡排序的原理不在这里赘述。直接给出 C# 冒泡排序的实现方式（从小到大）:

```csharp
int[] nums = { 3, 4, 7, 1, 6, 6, 8 };
for (int i = 0; i < nums.Length; i++)
{
    for (int j = 0; j < nums.Length-1-i; j++)
    {
        if (nums[j] > nums[j+1])
        {
            int temp = nums[j+1];
            nums[j+1] = nums[j];
            nums[j] = temp;
        }
    }
}
for (int i = 0; i < nums.Length; i++) { Console.Write(nums[i]); }
Console.ReadKey();

"1346678"
```
当然，C# 中有内置的方法能帮助我们快速实现数组的升序 or 降序排序:

```csharp
Array.Sort(nums);    // 升序
Array.Reverse(nums); // 降序
```

## .4 ArrayList 泛型集合
> 注意：ArrayList 由于在读写的过程中存在类型转换（装箱/拆箱），导致其读写速度较为缓慢，因此一般更多地会 <span style="background-color: yellow; color: black;">**使用 List<> 代替 ArrayList**</span>，详见 Section 8

```csharp
using System.Collections;

ArrayList list = new ArrayList();
```
集合的概念类似于数组，但是<span style="background-color: yellow; color: black;">不同于数组的长度固定、元素类型单一，集合没有这些限制。集合也有缺陷</span>，由于任何添加进集合的元素都会被自动转换为 `object` 类型，因此在之后调用这些元素的时候，需要使用强制类型转换，示例：

```csharp
list.Add(1);
list.Add(2);

int sum = (int)list[0] + (int)list[1];
```
**类方法**：以下代码中 `obj` 表示任意类型的元素

```csharp
list.Count;                   // 查看长度
list.Capacity;                // 查看集合容量
	// 数组容量只能等于 0, 4, 8, 16, 32... 依据集合长度而发生变化
	// 例如 count=4 时 capacity=4, cout=5 时 capacity=8

list.Add(obj);                // 添加元素
list.AddRange(数组、集合);      // 依次添加数组或集合中的每个元素
list.Clear();                 // 清空集合
list.Remove(obj);             // 根据值来删除元素
list.RemoveAt(index);         // 根据 index 删除元素
list.RemoveRange(start, end); // 移除一定范围的元素
list.Reverse();               // 反转
list.Insert(index, obj);      // 插入元素
list.InsertRange(index, 数组、集合);

[bool] list.Contain(obj);     // 判断是否包含  
```
## .5 List<> 泛型集合
创建对象

```csharp
List<数据类型> 对象名 = new List<数据类型>();
```
List<> 泛型集合的大部分类方法同 ArrayList，详见 Section 7。除此以外，泛型集合也有一些独有的类方法:

```csharp
List<int> list = new List<int>();

[int[]] list.ToArray();     // 将 List<> 转换为数组
[List<int>] array.ToList(); // 当然也可以将数组转换为 List<>
```
## .6 HashTable 键值对集合
> 注意：HashTable 由于在读写的过程中存在类型转换（装箱/拆箱），导致其读写速度较为缓慢，因此一般更多地会 <span style="background-color: yellow; color: black;">**使用 Dictionary 代替 HashTable**</span>，详见 Section 10

类似 Python 中的字典，<span style="background-color: yellow; color: black;">键必须唯一，值可以重复</span>

```csharp
using System.Collections;

HashTable ht = new HashTable();
```
**类方法**:

```csharp
ht.Count;         // 长度

ht.Add(键, 值);   // 添加方法 1
ht[键] = 值;      // 添加方法 2
 // 这里的键、值可以是任意类型的元素，类似于 Python 中的 dict[key] = value;
ht.Clear();      // 清空
ht.Remove(键);   // 根据键来移除键值对

[value] ht[key];        // 根据键找值
[collection] ht.Keys;   // 返回所有键
[collection] ht.Values; // 返回所有值
	// 读取键、值时，无法使用 ht.Keys[index] 这样的形式
	// 但可以使用 foreach (var item in ht.Keys) {  } 来读取

[bool] ht.ContainsKey(键);   // 判断是否包含某个键
[bool] ht.COntainsValue(值); // 判断是否包含某个值
```
## .7 Dictionary 键值对集合
创建对象

```csharp
Dictionary<键类型, 值类型> dict = new Dictionary<键类型, 值类型>();
```
Dictionary 键值对集合的大部分类方法同 HashTable，详见 Section 9。

读取 Dictionary 中的键值对的两种方法

```csharp
Dictionary<int, string> dict = new Dictionary<int, string>();

// 方法 1
foreach (var key in dict.Keys)
{
    Console.WriteLine("{0}, {1}", key, dict[key]);
}

// 方法 2
foreach (KeyValuePair<int, string> kv in dict)
{
    Console.WriteLine("{0}, {1}", kv.Key, kv.Value);
}
```

# 输入输出 Read & Write
**Write**
From Section 2:

```csharp
Console.WriteLine(); // 输出一个字符串并换行，当字符串为空时，相当于一个换行符 \n
Console.Write();     // 输出但不换行
```
**Read**
From Section 2:

```csharp
Console.ReadKey();   // 读取输入的一个键
Console.ReadLine();  // 读取输入的一个字符串
```
示例:

```csharp
Console.WriteLine("请输入你的QQ");
string input = Console.ReadLine();
Console.WriteLine("你的QQ为：{0}", input);
Console.ReadKey();
```
## .1 占位符 `{}`
C# 中的占位符有点类似于 Python 中的 `.format`，都需要使用 `{}`。示例:

```csharp
int a = 1;
int b = 11;
Console.WriteLine("{0}+{1}={2}", a, b, a+b);

"12"
```
保留数位：`{0:0.00}` 表示对第 0 个变量保留两位小数

## .2 转义符 `\`
`\n` 换行
`\t` Tab
`\b` Backspace
`\"` 表示 `"`，实现在字符串中显示 `"`
`\\` 表示 `\`，常用于地址字符串中，例如 `"C:\\Users\\Desktop"`
`@"..."` 主要有两个作用：
1. 取消 `\` 的转义作用，例如 `@"C:\Users\Desktop"`
2. 将字符串按照原格式输出，例如（删去 `@` 则会报错）

# 运算符
## .1 算数运算符
`+`, `-`, `*`, `/`, `%` 加，减，乘，除，取余

运算结果（输出）的数据类型，与输入变量中<span style="background-color: yellow; color: black;">范围最大</span>的那个相同，例如 `int % double = double`

## .2 复合运算符 
**`++`, `--`**
`a++` = `a=a+1`

`++`, `--` 除了跟在变量后，还可以放在变量前（如 `++a`），这是其含义也发生了一定程度上的改变，具体可自行查阅。（作者认为理解掌握 `a++` 已经足够了）

**`+=`, `-=`**
`a+=5` = `a=a+5`

当然除此之外还有 `*=`, `/=`, `%=`
## .3 关系运算符
`>`, `<`, `>=`, `<=`,  `==`, `!=`
## .4 逻辑运算符
`&&`, `||`, `!`，与，或，非

逻辑运算符之间存在优先级差异，并且 `&&` 与 `&` 同表示逻辑与但仍有一些不同。但是针对这两点，作者认为是<span style="background-color: yellow; color: black;">可以忽视</span>它们的：
(1) 在优先级方面，<span style="background-color: yellow; color: black;">使用括号来体现优先级</span>，例如：

```csharp
// 由于 || 优先级低于 &&，因此上下两行所表示的含义一致
// good
bool judge = (a > b) || (b > c && c > d);
// bad
bool judge = a > b || b > c && c > d;
```
(2) 对于使用 `&&` or `&`，绝大部分情况使用 `&&` 即可，`||` 同理

# 数据类型转换
## .1 隐式类型转换
特点：自动发生
要求：两种类型兼容，且<span style="background-color: yellow; color: black;">目标类型范围 > 原类型范围</span>，例如 `int` 转 `double`

```csharp
int n1 = 3;
int n2 = n1;
```
## .2 显示类型转换
特点：需要使用特定语法 `(目标类型)原变量`
要求：两种类型兼容，且<span style="background-color: yellow; color: black;">目标类型范围 < 原类型范围</span>，例如 `double` 转 `int`

```csharp
double n1 = 3.14;
int n2 = (int)n1;
```
## .3 `Convert` 强制类型转换
使用 `Convert.ToXXX()`，例如:

```csharp
string str = "123";
int n1 = Convert.ToInt32(str);
double n2 = Convert.ToDouble(str);
```
## .4 `Parse`, `TryParse` 强制类型转换
例如使用 `int.Parse()` 将 `string` 转换为 `int`:

```csharp
string str = "123";
int n1 = int.parse(str);
```
关于 `Parse`, `TryParse` 更详细的示例：由于 `TryParse` 即使转换出错也不会产生报错，因此这两种方法适用于不同的场景
![在这里插入图片描述](https://img-blog.csdnimg.cn/20210418141234225.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L3dlaXhpbl80MzcyODEzOA==,size_16,color_FFFFFF,t_70)

# 选择与循环 if & for
<span style="background-color: yellow; color: black;">使用 `Tab + Tab` 快捷键，实现快速生成结构体格式</span>
## .1 if else

```csharp
if (判断条件 1)
{
    // 代码块
}
else if (判断条件 2)
{
    // 代码块
}
else
{
    // 代码块
}
```
## .2 switch case

```csharp
switch (变量或表达式的值)
{
    case 值1: // 代码
        break;
    case 值2: // 代码
        break;
    default: // 代码
        break;
}
```
## .3 while

```csharp
while (循环条件)
{
    // 代码块
}
```
使用 `break` 可以跳出当前循环
使用 `continue` 跳过本次循环，回到循环条件
## .4 do while
while 循环：先判断再执行
do while 循环：先执行再判断

```csharp
do
{
    // 代码块
}while(循环条件)
```
## .5 for

```csharp
for (int i = 0; i < length; i++)
{
    // 代码块
}
```
## .6 for each

```csharp
foreach (var item in collection)
{
    // 代码块
}
```
`var` 的作用详见 [精简 C# 入门（一）](https://blog.csdn.net/weixin_43728138/article/details/115771081)Section #5.2，可以替换为其他数据类型
`collection` 包含数组（int[]...）与集合（ArrayList, HashTable）
> 以上代码中的关于 `数组` 的介绍位于本博客的 Section #11，而关于 `集合` 这个概念则可以先忽略，其内容在 [精简 C# 入门（四）](https://blog.csdn.net/weixin_43728138/article/details/116014639)Section #7, #8 中会有详细介绍

# 调试
## .1 断点
先加个断点，然后按 `F5` 进行调试
`F11` 逐语句调试（单步调试）
`F10` 逐过程调试。相比于逐语句调试，逐过程调试不会跳入具体函数中去。例如下图中，`F10` 不会跳入函数 `GetMax` 中去，而 `F11` 会逐语句执行每一行代码。
![在这里插入图片描述](https://img-blog.csdnimg.cn/20210418100425974.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L3dlaXhpbl80MzcyODEzOA==,size_16,color_FFFFFF,t_70)
## .2 异常处理 `try-catch`
近似于 Python 的 `try-except`

```csharp
try
{
    // 可能出现异常的代码块
}
catch
{
    // 出现异常后需要执行的代码块
}
```
恰当地使用 `try-catch`，可以实现一些 `if else` 语句无法实现的效果，例如:

```csharp
int n = 0;
Console.WriteLine("请输入一个数字");
try
{
    n = Convert.ToInt32(Console.ReadLine());
}
catch
{
    Console.WriteLine("请不要输入其他字符！");
}
```
## .3 查看运行时间
对于两个不同的算法，可以通过比较其运行时间来判断优劣。示例:

```csharp
using System.Diagnostics; // 需要现在开头引用一个命名空间

Stopwatch sw = new Stopwatch();
sw.Start();
// 算法
sw.Stop();
Console.WriteLine(sw.Elapsed);
```

# 三元表达式
语法:

```csharp
变量 = 表达式1 ? 表达式2 : 表达式3
```
`表达式1` True 就执行 `表达式2`，False 则执行 `表达式3`，例如:

```csharp
int max = n1 > n2 ? n1 : n2;
```

# 产生随机数
这一块是在【参考资料】(1) 的 P61 中突然中途插入的内容，个人感觉其与上下文的关系有点割裂，因此仅做一个简短总结

```csharp
Random r = new Random();    // 创建能够生成随机数的对象
int rndInt = r.Next(1, 10); // 调用该对象的方法，产生一个 1-9 之间的随机数  
```

# 常量

```csharp
const 常量类型 常量名 = 常量值;
const double pi = 3.14;
```
相较于变量，常量不能被修改（重新赋值）

# 枚举 `enum`
枚举类型是一种特殊的类，与类同级，因此直接写在命名空间内，定义:

```csharp
public enum Gender
{
    man,
    woman
}
```
有了 `Gender` 这个类，在之后的 Main 函数中，我们就可以创建类对象，例如:

```csharp
Gender gender = Gender.man;
```
更具体的使用方式如下图：
![在这里插入图片描述](https://img-blog.csdnimg.cn/2021041817040912.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L3dlaXhpbl80MzcyODEzOA==,size_16,color_FFFFFF,t_70)
**枚举类型与 `int` 类型兼容**（可以相互转换），依旧使用刚刚定义好的的 `Gender` 类:

```csharp
Gender gender = Gender.woman;
int n = (int)gender;

"1"
```

```csharp
int n = 0;
Gender gender = (Gender)n;

"man"
```
更复杂的，枚举类型中的变量还可以进行赋值。赋值后，该变量转换成 `int` 时的数值等于该赋值。并且改变量之后的其他变量所对应的 `int` 数值也会发生改变，具体如下图：
![](https://img-blog.csdnimg.cn/2021041818155820.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L3dlaXhpbl80MzcyODEzOA==,size_16,color_FFFFFF,t_70)
**枚举类型与 `string` 不兼容**，因此相互转换要麻烦一些（尤其是 `string` 转枚举）。使用以上 `Animal` 类为例:

```csharp
// 枚举转 string
string str = Animal.dog.ToString();

"dog"
```

```csharp
// string 转枚举
string str = "dog";
Animal animal = (Animal)Enum.Parse(tyepof(Animal), str);

"dog"
```
# 结构 `struct`
一次性声明多个不同类型的变量

```csharp
public struct Person
{
    public string _name,
    public string _gender,
    public int _age,
    
    string _nickname
}
```
`public` 关键字使得其修饰的<span style="background-color: yellow; color: black;">字段</span>能由外部进行访问和修改，例如 _name 这个字段。未由 `public` 修饰的字段默认为 `private`，无法由外部进行修改，例如 _nickname。

**注意**：我们将结构中的“变量”称之为字段。与变量的唯一性不同，字段可以同时存在同名的多个，例如不同人可以有相同的 _name 字段。因此<span style="background-color: yellow; color: black;">为了体现这一差别，一般习惯在字段前加上一个下划线</span>

**示例：`enum` in `struct`**

```csharp
public struct Person
{
    public string _name,
    public Gender _gender,
    public int _age,

    string _nickname
}

public enum Gender
{
    man,
    woman
}

class Program
{
    static void Main(string[] args)
    {
        Person p1;
        p1._name = "小红";
        p1._gender = Gender.woman;
        p1-_age = 99;
    }
}
```


# 函数（方法）
## .1 声明 & 调用
**函数的声明**

```csharp
[public] static 返回值类型 函数名([参数列表])
{
    // 代码块
}
```
1. 我们将用 `static` 关键字修饰的函数称之为静态函数，相反的，如果不用则称之为非静态函数，这两者有相当显著的区别，详见 [博客园：C#中静态与非静态方法比较](https://www.cnblogs.com/NothingIsImpossible/archive/2010/07/28/1786706.html)
2. 返回值类型除了 `int`, `string` 等之外，还可以使用空类型 `void`。返回值为空类型的函数可以不写 `return` 或者用 `return` 来表示函数的执行结束

以 [(C#) 精简 C# 入门（一）](https://blog.csdn.net/weixin_43728138/article/details/115771081)Section 4 中的一段代码为例:

```csharp
class Program
{
    public static int GetMax(int n1, int n2)
    {
        return n1 > n2 ? n1 : n2;
    }
}
```
**函数的调用**

```csharp
类名.函数名([参数列表])
```
示例:

```csharp
int max = Program.GetMax(1, 2);
```
**其他注意事项**

对于一个函数而言，其功能单一并不是缺点，反而是基本要求。

## .2 参数 `out`, `ref`, `params[]`
**`out` 输出参数：** 使函数能够返回多个类型的值。语法:

```csharp
[public] static 返回值类型 函数名([参数列表], out 返回值类型 变量名, ...)
```

示例:

```csharp
class Program
{
    static void Main(string[] args)
    {
    	string str = null;
    	double n = Program.Test(519, out str);
    	
    	Console.WriteLine("{0}, {1}", str, n);
    	Console.ReadKey();
    }

    static double Test(double n1, out string str1)
    {
        str1 = "Hello World";
        return n1 + 1
    }
}

"Hello World 520"
```
**`ref` 引用参数**：使函数内对变量的更改在函数外仍有效。语法：
```csharp
[public] static 返回值类型 函数名([参数列表], ref 返回值类型 变量名, ...)
```

示例:

```csharp
class Program
{
    static void Main(string[] args)
    {
    	int n = 0;
    	Program.Add_1(n);
    	Console.WriteLine(n);
    	Program.Add_2(ref n);
    	Console.WriteLine(n);
    	Console.ReadKey();
    }

    // 不使用 ref
    static void Add_1(int n1) { n1 += 1; }
    // 使用 ref
    static void Add_2(ref int n1) { n1 += 1; }
}

"0"
"1"
```
**`params[]` 可变参数数组**：将输入参数中与可变参数数组类型一致的元素，均当做数组的元素。可变参数数组只能作为输入参数列表中的最后一个元素，示例:

```csharp
class Program
{
    static void Main(string[] args)
    {
    	Program.studentScore("小红", 98, 100, 99);
    	Program.studentScore("小白", 65, 32); // 第三次弃考无成绩
    	Console.ReadKey();
    }

    static void studentScore(string name, params int[] scores) 
    {
    	int sum = 0;
    	for (int i = 0; i < scores.Length; i++) { sum += scores[i]; }
    	Console.WriteLine("{0}'s all score: {1}", name, sum);
    }
}

"小红's all score: 297"
"小白's all score: 97"
```
当然，如果直接填 `int[]` 类型的数组也是 OK 的
## .3 重载 & 递归
**重载：**
重载指的是多个<span style="background-color: yellow; color: black;">名称相同，但参数不同</span>的函数（返回值类型不需要相同），使得计算机能够根据输入参数的类型以及个数，来选择相应的需要执行的函数。

示例：以下代码中对 `Add` 函数的重载使其既可以读取 `double` 类型的数据，也可以读取 `string` 来进行相加操作

```csharp
class Program
{
    static void Main(string[] args)
    {
        double r1 = Add(1, 2);
        double r2 = Add("1", "2");
        Console.WriteLine("Add double: {0}", r1);
        Console.WriteLine("Add string: {0}", r2);
        Console.ReadKey();
    }

    static double Add(double n1, double n2)
    {
        return n1 + n2;
    }
    static double Add(string s1, string s2)
    {
        return Convert.ToDouble(s1) + Convert.ToDouble(s2);
    }
}
```
重载存在限制：
1. 如果参数个数相同，那么参数类型就不能相同
2. 如果参数类型相同，那么参数个数就不能相同

**递归：**
自己调用自己。示例:

```csharp
class Program
{
    public static int currentTurn = 0;
    static void Main(string[] args)
    {
        Program.Repeat(3);
        Console.ReadKey();
    }

    static void Repeat(int maxTurn)
    { 
        if (currentTurn < maxTurn)
        {
            Console.WriteLine("重复一次");
            currentTurn++;
            Program.Repeat(maxTurn);
        }
        return;
    }
}

"重复一次"
"重复一次"
"重复一次"
```
## .4 练习
关于函数的上述知识点，【参考资料】(1) 中的视频教程给了非常多很有帮助的练习，[传送门](https://www.bilibili.com/video/BV1FJ411W7e5?p=86)：（以下红框内的视频中包含的练习都挺不错的）
![在这里插入图片描述](https://img-blog.csdnimg.cn/2021041917165964.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L3dlaXhpbl80MzcyODEzOA==,size_16,color_FFFFFF,t_70)
# 案例：飞行棋游戏
仅使用当前所介绍的知识，就足矣写出一款飞行棋游戏，由于内容比较长，建议感兴趣的读者跳转到【参考资料】(1) 中的案例练习，[传送门](https://www.bilibili.com/video/BV1FJ411W7e5?p=90)。

作者根据自己的理解写了一个类似功能的游戏，目前还没有做代码优化，因此可以看到将近写了 400 行左右（就效果而言总体满意）。以下是代码截图以及运行截图：
<img src="https://img-blog.csdnimg.cn/20210420222859768.png">
<img src="https://img-blog.csdnimg.cn/2021042022354155.png" width="36%"> <img src="https://img-blog.csdnimg.cn/20210420223633109.png" width="61.5%">
<img src="https://img-blog.csdnimg.cn/20210420223717877.png" width="60%">






# 面向过程 $\to$ 面向对象
**面向过程**：分析出解决问题所需要的步骤，然后用函数把这些步骤一步一步实现。

**面向对象**：把构成问题事务分解成各个对象，建立对象的目的不是为了完成一个步骤，而是为了描叙某个事物在整个解决问题的步骤中的行为。
> 以上表述摘自 [CSDN: 面向对象与面向过程的本质的区别](https://blog.csdn.net/jerry11112/article/details/79027834)，个人觉得非常直观易懂。

而在【参考资料】(1) 中，[传送门](https://www.bilibili.com/video/BV1FJ411W7e5?p=98)，讲师也提供了几个能够帮助理解面向对象和面向过程差异的例子。例如，分别用这两者来描述“关门”：
![在这里插入图片描述](https://img-blog.csdnimg.cn/20210420234841543.png)
<span style="background-color: yellow; color: black;">我们使用 `属性` + `方法` 来描述对象</span>。以三个对象，白炽灯、LED灯、小猫为例：
> **白炽灯**
属性：尺寸（20''）、价格（5 $）
方法：发光（黄色）
> **LED灯**
属性：尺寸（18''）、价格（9 $）
方法：发光（白色）
> **小猫**
属性：种类（橘猫）、体重（10kg）、性格（闷骚）
方法：吃喝拉撒、与主人玩

上述三个例子当中，很显然白炽灯与LED灯这两个对象具有非常类似的属性和方法，我们把这样的对象进行进一步的封装，从而抽象出 “**类**” 这一概念






# 类
<span style="background-color: yellow; color: black;">类就是一个模子，确定了某种对象应该具有的属性和方法</span>，因此对象是通过类来创建的，例如白炽灯与LED灯这两个对象可以由 "灯类" 创建 。

类的代码描述:
```csharp
[public] class 类名
{
    Fields 字段;
    Properties 属性;
    Methods 方法
}
```

一个关于类的完整示例:
```csharp
class Pet
{
    // 构造函数
    public Pet(string species, int age)
    {
        this.Species = species;
        this.Age = age;
    }
    public Pet(string species) : this(species, 0) { } // 重载

    // 字段
    private string _species;
    private int _age;

    // 属性
    public string Species { get => _species; set => _species = value; }

    public int Age
    {
        get => _age;
        set
        {
            value = value >= 0 ? value : 0;
            _age = value;
        }
    }

    // 方法
    /// <summary>
    /// 实例方法：介绍由该类创建的对象
    /// </summary>
    public void IntroObj()
    {
        Console.WriteLine("I'm a {0} years old {1}.", this.Age, this.Species);
    }

    /// <summary>
    /// 静态方法：介绍类
    /// </summary>
    public static void IntroClass()
    {
        Console.WriteLine("It's a class about pet, \nincluding some basic properties and functions.");
    }
}
```
以上代码中的新内容将在下列几个 subsection 中依次介绍。
## .1 字段 Fields
<span style="background-color: yellow; color: black;">字段是属于类的变量</span>，它表示了由类所创建的变量的某种属性。定义方式:

```csharp
[private] 字段类型 字段名;
```
**关于字段，我们需要知道：**
1. 关键字 `private` 则表示不可由外界访问 
关键字 `public` 表示可由外界访问（读取、修改）。为了字段的安全性，<span style="background-color: yellow; color: black;">一般不使用 `public`</span>
3. 为了显示字段与方法中的变量的区别，字段名建议以 `_` 开头
4. 使用 `this.字段名` 的形式在类的内部调用字段，例如上例中的 `this._age`
## .2 属性 Properties
<span style="background-color: yellow; color: black;">属性用于保护字段，对其读取、修改操作进行限制</span>。属性由两个方法组成:

```csharp
public 字段类型 属性名 { get => species; set => species = value; }
```
`get()` 表示读取
`set()` 表示修改

**关于属性，我们需要知道：**
1. 属性一般都定义为 `public`
2. 属性名其对应与字段名应该相同（含义相同），例如属性 `Age` 对应字段 `_age`
3. 选中对应的字段后, <span style="background-color: yellow; color: black;">使用快捷键 `Ctrl+R+E` 实现属性的快速生成</span>（更加详细的步骤演示可参考这篇博客：[【.NET】VS2017+C#如何快速生成属性](https://blog.csdn.net/qq_41324483/article/details/93718399)）
4. 为了限制修改，一般情况下会对 `set()` 方法做一定的修改。
例如在以下代码中，`Age` 属性就对年龄的修改做了限制，规定必须要大于等于 0
5. **只读属性** & **只写属性**：顾名思义，只读属性没有 `set()` 方法，只写属性没有 `get()` 方法

**应用示例：**

```csharp
// 类内部
 class Pet
{
    private int _age;
    public int Age { 
        get => _age;             
        set {
            value = value >= 0 ? value : 0; // 限制对年龄的修改必须大于等于 0
            _age = value;
        }
    }
    public void Intro()
    {
        // 读取。在类内部直接使用 this._age 也完全 OK
        Console.WriteLine("I'm {0} years old.", this.Age); 
    }
}

// 类外部
Pet cat = new Pet();
cat.Age = 2; // 修改
Console.WriteLine(cat.Age); // 读取

"2"
```

## .3 方法 Methods
### .3.1 静态 & 非静态
在学习类方法前，首先需要理解 "静态" (`static`) 与 "非静态" (也叫 "实例") 之间的区别：
1. 静态成员包含静态字段、静态属性、静态函数，实例成员同理
2. 静态类中只能有静态成员，不能有实例成员
非静态类中都能有
3. 调用实例成员时，使用 `对象名.实例成员名`
调用静态成员时，使用 `类名.静态成员名`
4. 静态函数只能访问静态成员
实例函数都能访问

在具体使用的时候，如果想要定义一个 “工具类”，可以考虑将其写成静态类。例如 C# 自带的 Console 类
### .3.2 构造函数
作用：初始化对象

```csharp
public 类名([参数列表])
{
    // 赋值
}
```
示例:

```csharp
public Pet(string species, int age)
{
    this.Species = species;
    this.Age = age;
}
```
构造函数当然也可以重载，在重载构造函数时为了减少代码冗余，可以使用 `this` 关键字（之前的已经介绍了 `this` 的两种用法 `this.字段名`、`this.属性名`）:

```csharp
public 类名([参数列表1]):this([参数列表2]) { }
```
构造函数重载的对象一般为最完整的构造函数，因此需要在 `参数列表1` 加入一些默认初值来组成 `参数列表2`，例如下例中第二个构造函数将 age 默认为 0

```csharp
public Pet(string species, int age)
{
    this.Species = species;
    this.Age = age;
}

public Pet(string species):this(species, 0) { }
```
### .3.3 析构函数
作用：在程序结束时会自动调用，帮助释放占用的内存资源

```csharp
~类名() { }
```
示例:

```csharp
~Pet() { }
```

## .4 类的引用
**引用系统类：**
系统类一般都位于名字类似为 `System.XXX` 的命名空间，因此只需直接在代码开头添加:

```csharp
using System.XXX;
```

**引用自定义的类：**
例如想要在 PlaneChess 项目中使用 ConsoleApp2 中定义的 Pet 类（下图红框）：
1. 右键单击 `引用`，选择 `添加引用`
![在这里插入图片描述](https://img-blog.csdnimg.cn/20210422145702789.png)
2. 在弹窗中勾选 `ConsoleApp2`，点击确定
![在这里插入图片描述](https://img-blog.csdnimg.cn/20210422145939668.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L3dlaXhpbl80MzcyODEzOA==,size_16,color_FFFFFF,t_70)
3. 使用 using 添加 `using ConsoleApp2`，然后就能调用其中的 `Pet` 类了。
<span style="background-color: yellow; color: black;">注意！这个该类必须是由 `public` 修饰的，即允许外界访问</span>
<img src="https://img-blog.csdnimg.cn/2021042215022158.png">

# 字符串 string
作者在 [精简 C# 入门（一）](https://blog.csdn.net/weixin_43728138/article/details/115771081)已经对各类基础数据类型进行了简短的概括，包括字符串。但由于字符串存在典型性与特殊性，因此在这里补充对其更细致的介绍。
## .1 字符串的不可变性 & `StringBuilder` 的使用
**字符串为引用类型，其值储存在堆，地址储存在栈**
这一块的内容详见 [精简 C# 入门（一）](https://blog.csdn.net/weixin_43728138/article/details/115771081)Section #5

**值相同的字符串指向同一个堆地址**
如下图，字符串 `s1`, `s2` 均指向同一个 "张三"，不存在第二个 "张三"
![在这里插入图片描述](https://img-blog.csdnimg.cn/20210423231034783.png)

**字符串的不可变性**
当给字符串重新赋值时，原初值并没有销毁，而是在堆中重新开辟一块区域储存。如下图中字符串 `s` 赋新值 "孙权" 后，其初值 "张三" 并未在堆中被销毁。
![在这里插入图片描述](https://img-blog.csdnimg.cn/20210424075611983.png)

不同于栈空间垃圾内存的立即销毁，像这样未被销毁的堆空间垃圾，只有当程序结束时才会被处理。因此<span style="background-color: yellow; color: black;">为了防止程序运行时内存占用过高，要避免大量的对字符串的赋值操作</span>

**使用 `StringBuilder` 避免对字符串的操作占用过量内存**
示例：将 1-100 的整数串成一个字符串

```csharp
// 直接用 string：占用内存且耗时
string s = "";
for (int i = 0: i < 100; i++)
{
    s += i;
}

// 使用 StringBuilder：不占内存且高效
StringBuilder sb = new StringBuilder();
for (int i = 0: i < 100; i++)
{
    sb.Append(i);
}
string s = sb.ToString();
```

## .2 修改字符串
**字符串相当于一个 char 类型的只读数组**
我们可以使用 `字符串名[index]` 的方式来访问该位置的字符，但无法修改。

**使用 `char[]` 与 `string` 的相互转换修改字符串中的字符**
虽然字符串可以看作只读 `char[]`，但是仍然可以通过一些列操作来修改其某个位置的字符，实现 "曲线救国"。示例:

```csharp
string str = "Hello World!"
// 首先将其转化为 char[]
char[] chs = str.ToCharArray();
// 相当于删去 "Hello" 末尾的 "o"
chs[4] = "";
// 再转回字符串
str = new string(chs);

"Hell World!"
```

## .3 字符串的相关方法
以下代码中 `[]` 里的内容表示该方法的返回值类型:

```csharp
[double] str.Length;                        // 长度
[string] str.ToUpper();                     // 转成大写
[string] str.ToLower();                     // 转成小写
[bool] str.Equals(str1);                    // 判断两个字符串是否相同
	// 该函数还有一个枚举类型的可选参数，具体作用百度
	str.Equals(str1, StringComparison.XXX)
		
[bool] str.Contains(substr);                // 判断字符串中是否包含 substr
[bool] str.StartsWith(substr);              // 判断字符串是否以 substr 开头
[bool] str.EndsWith(substr);                // 判断字符串是否以 substr 结尾
[bool] string.IsNullorEmpty(str);           // 判断字符串是否为 null or ""

[int] str.IndexOf(substr);                  // 找 substr 第一次出现的 index
	str.IndexOf(substr, startIndex)         // 从 startIndex 开始找
[int] str.LastIndexOf(substr);              // 找 substr 最后一次出现的 index

[string] str.Trim();                        // 去掉字符串开头与结尾的空格
[string] str.TrimStart();                   // 去开头空格
[string] str.TrimEnd();                     // 去结尾空格

[string] str.Replace(substr1, substr1);     // 将子串 substr1 替换为 substr2
[string] str.Substring(startIndex, length); // 从 startIndex 位置截取长度为 length 的子串
```
应用1：使用 `LastIndexOf`, `Substring` 提取地址中文件名

```csharp
string path = @"C:\file1\file2\1.txt":
int index = path.LastIndexOf("\\"); // "\\" 表示 "\"
string fileName = path.Substring(index+1);

"1.txt"
```
**分割字符串**

```csharp
[string[]] str.Split(chs, StringSplitOptions.None/RemoveEmptyEntries)
```
1. `chs` 为 `char[]` 类型，储存作为分割依据的字符
2. `StringSplitOptions.None/RemoveEmptyEntries` 是一个枚举类型的可选参数
`None` 表示不删除分割后的空值 `""`
`RemoveEmptyEntries` 表示删除

示例:

```csharp
string str = "a b  + c";
char[] chs = { ' ', '+' };

string[] splits = str.Split(chs, StringSplitOptions.RemoveEmptyEntries);

{ "a", "b", "c" }

string[] splits = str.Split(chs, StringSplitOptions.None);

{ "a", "b", "", "", "", "c" }
```
**拼接字符串**

```csharp
[string] string.Split(connection, str);
```
示例：
```csharp
string[] strs = { "a", "b", "c" };
string strJoint = string.Join(" | ", strs);

"a | b | c"
```

# 文件操作之 `File` 类
`File` 类是一个静态的系统类，这里介绍一些其中的方法：

读取文件的每一行

```csharp
using System.IO;
using System.Text;

[string[]] File.ReadAllLines(path, Encoding.XXX);
```
`path` 为 string 类型的路径，
`Encoding.XXX` 为解码方式，常见有 Encoding.Default, Encoding.UTF8 等

# 继承
继承主要是类的继承，通过子类继承父类的形式，使得子类能够沿用父类当中的字段、属性与方法（只能继承 public 的），从而<span style="background-color: yellow; color: black;">降低代码冗余</span>

示例，子类 `Cat` 继承父类 `Animal`:

```csharp
public class Animal
{
    private int _age;
    public int Age { get => _age; set => _age = value; }
}

public class Cat: Animal
{
    // 代码块
}
```
<span style="background-color: yellow; color: black;">继承具有传递性</span>，即子类的子类能够继承父类中的字段、属性与方法。

<span style="background-color: yellow; color: black;">子类不继承父类的构造函数</span>。但是可以通过在子类的构造函数前<span style="background-color: yellow; color: black;">添加 `:base([参数列表])` 来实现构造函数的继承</span>，示例：

```csharp
public class Animal
{
    public Animal(int age)
    {
        this.Age = age;
    }

    private int _age;
    public int Age { get => _age; set => _age = value; }
}

public class Cat: Animal
{
    public Cat(int age, string name)
        : base(age)
    {
        this.Name = name;
    }

    private string _name;
    public string Name { get => _name; set => _name = value; }
}
```
如果在子类中需要写一个与父类中的<span style="background-color: yellow; color: black;">同名的成员</span>，建议为其添加一个关键字 `new`（不加也不会报错，但是加了就看的比较清楚），示例:

```csharp
public class Animal
{
    public void Shout()
    {
        Console.WriteLine("发出了叫声");
    }
}

public class Cat: Animal
{
    public new void Shout()
    {
        Console.WriteLine("喵!");
    }
}
```
# 里式转换
核心含义：
1. 子类可以赋值给父类
2. 如果父类对象中装的是子类对象，那么可已将这个父类强转为子类对象

**子类可以赋值给父类**
依旧以上个代码片段中的 `Animal`, `Cat` 类为例:

```csharp
Cat cat = new Cat();
Animal animal1 = cat;
Animal animal2 = new Cat();
```
作用：当一个地方需要某类的对象时，可以使用其子类的对象替代

**如果父类对象中装的是子类对象，那么可已将这个父类强转为子类对象**
示例:

```csharp
Aniaml animal = new Cat(); // 父类对象中装的是子类对象
Cat cat = (Cat)animal;     // 强转
```

# 访问修饰符
`private`: 仅限于类的内部访问
`public`: 不限访问
`protected`: 仅限于类内部及其子类访问
`internal`: 只能在当前项目中访问（默认）
`protected internal`: 两者取交集

其他注意：
1. 能够修饰类的访问修饰符只有 `public` & `internal`
2. 子类的访问修饰符不能大于父类的访问权限

# 操作文件
## .1 `Path` 类
`Path` 类为静态类，用于操作路径

**类方法：**

```csharp
using System.IO;

[string] Path.GetFileName(path);                 // 获得 path 路径所指代的文件名
[string] Path.GetFileNameWithoutExtension(path); // 获得不包含文件格式的文件名
[string] Path.GetExtension(path);                // 获得文件格式
[string] Path.GetDirectoryName(path);            // 获得文件夹路径

// 示例
string path = @"C:\file1\test.txt";
Path.GetFileName(path)                 // "test.txt"
Path.GetFileNameWithoutExtension(path) // "test"
Path.GetExtension(path)                // ".txt"
Path.GetDirectoryName(path)            // "C:\file1"
```
## .2 `File` 类
`Path` 类为静态类，用于操作文件

```csharp
using System.IO;
using System.Text;

string path = @"C:\file1\test.txt";

[bool] File.Exists(path);                // 判断文件是否存在

File.Create(path);                      // 创建文件
File.Delete(path);                      // 删除文件
File.Copy(path, @"C:\file1\new.txt");   // 复制文件，新文件名为 "new.txt"
File.Move(path, @"C:\file1\new.txt");   // 移动文件至新地址
```
**读取**

```csharp
string path = @"C:\file1\test.txt";

[string] File.ReadAllText(path, Encoding.Default);    // 以字符串格式读取整个文件
[string[]] File.ReadAllLines(path, Encoding.Default); // 以字符串格式一行行读取文件
[byte[]] File.ReadAllBytes(path);                     // 以二进制格式读取文件
[string] Encoding.Default.GetString();                // 将二进制数组转成 string
```
**写入**

```csharp
string path = @"C:\file1\test.txt";
string content = "Hello World!";
string[] contents = { "111", "222" };

// 覆盖写入
File.WriteAllLines(path, contents);
File.WriteAllText(path, content);
File.WriteAllBytes(path, Encoding.Default.GetBytes(content));

// 追加写入
File.AppendAllText(path, content)
```
## .3 文件流
相较于 `File` 类对整体文件的读写，文件流对文件的读写是一点一点分步进行的，因此内存占用更少。

对应于 `File` 类中操作字符（WriteAllLines, WriteAllText）以及操作字节（WriteAllBytes）的方法，在文件流中有以下两种方法：
1. `FileStream`：操作字节
2. `StreamReader` & `StreamWriter`：操作字符

### .3.1 FileStream
```csharp
using System.IO;

FileStream fsRead = new FileStream(path, 
    FileMode.XXX, // 操作系统打开文件的方式
    FileAccess.XXX, // 定义文件读写权限
);
```
![在这里插入图片描述](https://img-blog.csdnimg.cn/20210511110655219.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L3dlaXhpbl80MzcyODEzOA==,size_16,color_FFFFFF,t_70)
![在这里插入图片描述](https://img-blog.csdnimg.cn/20210511110924973.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L3dlaXhpbl80MzcyODEzOA==,size_16,color_FFFFFF,t_70)
**类方法**:

```csharp
// 创建示例（以下是两种常用的创建模式）
FileStream fsRead = new FileStream(path, FileMode.OpenOrCreate, FileAccess.Read);
FileStream fsWrite = new FileStream(path, FileMode.OpenOrCreate, FileAccess.Write);

// 从第 0 个字节开始，读取 buffer.Length 个字节，并存入 buffer
// buffer 为提前创建好的一个字节类型的数组
// 返回值为读取到的有效字节数
[int] fsRead.Read(buffer, 0, buffer.Length);
fsWrite.Write(buffer, 0, buffer.Length); // 将目标文件中 [0, buffer.Length] 个字符替换为 buffer 中储存的字符

fsRead.Close();   // 关闭流
fsRead.Dispose(); // 释放占用的资源
```

示例：使用 FileStream 读写 txt 文档
```csharp
string path = @"C:\file1\test.txt";
byte[] buffer = new byte[1024*1024*5];

// 读取：方法 1
FileStream fsRead = new FileStream(path, FileMode.OpenOrCreate, FileAccess.Read);
int n = fsRead.Read(buffer, 0, buffer.Length);
string s = Encoding.Default.GetString(buffer, 0, n); // 将 buffer 的 [0, n] 个有效字节转换为 string
fsRead.Close();
fsRead.Dispose();

// 读取：方法 2
string s;
using(FileStream fsRead = new FileStream(path, FileMode.OpenOrCreate, FileAccess.Read))
{
    int n = fsRead.Read(buffer, 0, buffer.Length);
    s = Encoding.Default.GetString(buffer, 0, n);
}

// 写入
using(FileStream fsWirte = new FileStream(path, FileMode.OpenOrCreate, FileAccess.Write))
{
    string str = "Hello World!";
    byte[] buffer = Encoding.Default.GetBytes(str);
    fsWrite.Write(buffer, 0, buffer.Length); 
}
```
<span style="background-color: yellow; color: black;">上例中用到的 `using(){ }` 方法类似于 Python 中的 with 语句，即运行完大括号内的代码之后自动释放小括号内的代码所占用的资源</span>

### .3.2 StreamReader & StreamWriter
类方法
```csharp
StreamReader sr = new StreamReader(path);
StreamWriter sw = new StreamWriter(path);

[bool] sr.EndOfStream;  // 指示当前的流位置是否在流结尾
[string] sr.ReadLine(); // 读取输入流中的下一行字符串 

sw.Write("Hello World!"); // 覆盖写入
    // 如果想要继续写入，不覆盖之前的文本，可以在创建对象时添加一个布尔参数
    StreamWriter sw = new StreamWriter(path, true);
```
示例：读写 txt 文档
```csharp
string path = @"C:\Users\Administrator\Desktop\dm.dll";

// 读取
using (StreamReader sr = new StreamReader(path))
{
    while (!sr.EndOfStream)
    {
        Console.WriteLine(sr.ReadLine());
    }
}
```
# 面向对象之多态
<span style="background-color: yellow; color: black;">概念</span>: 让一个对象能够表现出多种状态（类型）

<span style="background-color: yellow; color: black;">为什么要使用多态</span>? 便利性。例如，以下代码的运行结果为：
```csharp
"发出了叫声"
"发出了叫声"
```
![在这里插入图片描述](https://img-blog.csdnimg.cn/20210607083440818.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L3dlaXhpbl80MzcyODEzOA==,size_16,color_FFFFFF,t_70)
这显然同我们的目标结果不符合：
```csharp
"喵"
"汪"
```
在不不了解多态之前，我们可以将 for 循环改为以下形式来实现目标，但问是复杂冗长，而且会随着子类数目的增长变得更复杂：

```csharp
for (int i = 0; i < animals.Length; i++)
{
    if (animals[i] is Cat)
    {
        ((Cat)animals[i]).Shout();
    }
    else if (animals[i] is Dog)
    {
        ((Dog)animals[i]).Shout();
    }
    animals[i].Shout();
}
```
<span style="background-color: yellow; color: black;">多态的实现方式</span>：虚方法、抽象类、接口
## .1 虚方法
步骤：
1. 将父类中的函数标记为虚方法，关键字 `virtual`
2. 将子类中的同名函数标记为重写，关键字 `override`

例如：
```csharp
public class Animal
{
    public virtual void Shout() { Console.WriteLine("发出了叫声"); }
}
public class Cat : Animal
{
    public override void Shout() { Console.WriteLine("喵"); }
}
```
## .2 抽象类
步骤：
1. 将父类标记为抽象类，其中的函数标记为抽象方法，关键字 `abstract`
2. 将子类中的同名函数标记为重写，关键字 `override`

例如：
```csharp
public abstract class Animal
{
    public abstract void Shout();
}
public class Cat : Animal
{
    public override void Shout() { Console.WriteLine("喵"); }
}
```
<span style="background-color: yellow; color: black;">Others for 抽象类</span>
1. 不能单独创建抽象类的对象，但可以创建其子类
2. 当子类继承抽象类时，需要重写其中的抽象方法，否则报错（可以使用 `Alt+Shift+F10` 自动填充），除非这个子类也是抽象类
3. 抽象类中可以包含非抽象成员，即属性、字段、函数
4. 抽象方法所定义的输入和输出，规定了其子类继承的同名函数也必须要有一样的输入和输出









