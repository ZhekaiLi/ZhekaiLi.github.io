---
layout: wiki
title: Latex
cate1: Others
cate2:
description: 
keywords: Latex
mathjax: true
---

The derivative of $-\frac{1}{2}\Bigg(np\log2\pi+n\log\vert\Sigma\vert+\sum_{i=1}^n(x_i-\mu)^T\Sigma^{-1}(x_i-\mu)\Bigg)$ with respect to $\Sigma$ can be found as follows:

First, calculate the derivative of the log determinant of $\Sigma$:
$$\frac{\partial}{\partial \Sigma} \log\vert\Sigma\vert = \frac{\partial}{\partial \Sigma} \text{tr}(\log\Sigma) = \text{tr}(\Sigma^{-1})$$

Next, calculate the derivative of the quadratic term:
$$\frac{\partial}{\partial \Sigma} (x_i-\mu)^T\Sigma^{-1}(x_i-\mu) = -\Sigma^{-1}(x_i-\mu)(x_i-\mu)^T\Sigma^{-1}$$

Finally, sum over all data points to get the derivative of the total objective:
$$\frac{\partial}{\partial \Sigma}-\frac{1}{2}\Bigg(np\log2\pi+n\log\vert\Sigma\vert+\sum_{i=1}^n(x_i-\mu)^T\Sigma^{-1}(x_i-\mu)\Bigg) = -\frac{n}{2}\Sigma^{-1} + \frac{1}{2}\sum_{i=1}^n\Sigma^{-1}(x_i-\mu)(x_i-\mu)^T\Sigma^{-1}$$

So, the derivative of the negative log-likelihood function with respect to $\Sigma$ is:
$$\frac{\partial}{\partial \Sigma}-\frac{1}{2}\Bigg(np\log2\pi+n\log\vert\Sigma\vert+\sum_{i=1}^n(x_i-\mu)^T\Sigma^{-1}(x_i-\mu)\Bigg) = -\frac{n}{2}\Sigma^{-1} + \frac{1}{2}\sum_{i=1}^n\Sigma^{-1}(x_i-\mu)(x_i-\mu)^T\Sigma^{-1}$$
The derivative of $\log \vert\Sigma\vert$ with respect to $\Sigma$ can be found as follows:

The derivative of the determinant of $\Sigma$:
$$\frac{\partial}{\partial \Sigma} \vert\Sigma\vert = \text{adj}(\Sigma)^T$$

The derivative of the logarithm of the determinant of $\Sigma$:
$$\frac{\partial}{\partial \Sigma} \log \vert\Sigma\vert = \frac{1}{\vert\Sigma\vert} \frac{\partial}{\partial \Sigma} \vert\Sigma\vert = \frac{1}{\vert\Sigma\vert} \text{adj}(\Sigma)^T$$

So, the derivative of $\log \vert\Sigma\vert$ with respect to $\Sigma$ is:
$$\frac{\partial}{\partial \Sigma} \log \vert\Sigma\vert = \frac{1}{\vert\Sigma\vert} \text{adj}(\Sigma)^T$$

The derivative of $\sum_{i=1}^n(x_i-\mu)^T\Sigma^{-1}(x_i-\mu)$ with respect to $\Sigma$ can be found as follows:

The derivative of $(x_i-\mu)^T\Sigma^{-1}(x_i-\mu)$ with respect to $\Sigma$:
$$\frac{\partial}{\partial \Sigma} (x_i-\mu)^T\Sigma^{-1}(x_i-\mu) = -\Sigma^{-1}(x_i-\mu)(x_i-\mu)^T\Sigma^{-1}$$

Sum over all data points to get the derivative of the total expression:
$$\frac{\partial}{\partial \Sigma} \sum_{i=1}^n(x_i-\mu)^T\Sigma^{-1}(x_i-\mu) = -\sum_{i=1}^n\Sigma^{-1}(x_i-\mu)(x_i-\mu)^T\Sigma^{-1}$$

So, the derivative of $\sum_{i=1}^n(x_i-\mu)^T\Sigma^{-1}(x_i-\mu)$ with respect to $\Sigma$ is:
$$\frac{\partial}{\partial \Sigma} \sum_{i=1}^n(x_i-\mu)^T\Sigma^{-1}(x_i-\mu) = -\sum_{i=1}^n\Sigma^{-1}(x_i-\mu)(x_i-\mu)^T\Sigma^{-1}$$

---

The expression $(x_i-\mu)^T\Sigma^{-1}(x_i-\mu)$ is the Mahalanobis distance between the $i$th data point and the mean, given the covariance matrix $\Sigma$. It measures the distance between the two points in terms of the variance and covariance of the data.

The derivative of this expression with respect to $\Sigma$ gives the sensitivity of this distance to changes in the covariance matrix.

The derivative can be calculated using the chain rule of differentiation. First, we calculate the derivative of $(x_i-\mu)^T\Sigma^{-1}$ with respect to $\Sigma$, which is given by:

$$\frac{\partial}{\partial \Sigma} (x_i-\mu)^T\Sigma^{-1} = -\Sigma^{-1}(x_i-\mu)^T$$

Next, we calculate the derivative of $(x_i-\mu)^T\Sigma^{-1}(x_i-\mu)$ with respect to $(x_i-\mu)^T\Sigma^{-1}$:

$$\frac{\partial}{\partial (x_i-\mu)^T\Sigma^{-1}} (x_i-\mu)^T\Sigma^{-1}(x_i-\mu) = (x_i-\mu)$$

Finally, we combine these derivatives using the chain rule to get the derivative of $(x_i-\mu)^T\Sigma^{-1}(x_i-\mu)$ with respect to $\Sigma$:

$$\frac{\partial}{\partial \Sigma} (x_i-\mu)^T\Sigma^{-1}(x_i-\mu) = \frac{\partial}{\partial (x_i-\mu)^T\Sigma^{-1}} (x_i-\mu)^T\Sigma^{-1}(x_i-\mu) \cdot \frac{\partial}{\partial \Sigma} (x_i-\mu)^T\Sigma^{-1} = (x_i-\mu)(x_i-\mu)^T\Sigma^{-1}$$

Multiplying both sides by $-\Sigma^{-1}$ gives the final result:

$$\frac{\partial}{\partial \Sigma} (x_i-\mu)^T\Sigma^{-1}(x_i-\mu) = -\Sigma^{-1}(x_i-\mu)(x_i-\mu)^T\Sigma^{-1}$$

# 一、$\LaTeX$ 的基本概念

## 1.1 第一次使用 $\LaTeX$
一份最短的 $\LaTeX$ 源代码示例
```tex
\documentclass{article}
\begin{document}
``Hello world!'' from \LaTeX.
\end{document}
```

## 1.2 $\LaTeX$ 命令和代码结构
### 1.2.1 $\LaTeX$ 命令和环境

字母形式的 $\LaTeX$ 命令忽略其后的所有连续空格。如果要人为引入空格，需要在命令后面，加一对花括号阻止其忽略空格：
![pic](/images/2021-01/Snipaste_2021-01-11_14-17-43.jpg)

$\LaTeX$ 中还包括环境，用以令一些效果在局部生效，或是生成特殊的文档元素。$\LaTeX$ 环境
的用法为一对命令 `\begin` 和 `\end`：
```tex
\begin{⟨environment name⟩}[⟨optional arguments⟩]{⟨mandatory arguments⟩} 
…
\end{⟨environment name⟩}
```

### 1.2.2 $\LaTeX$ 源代码结构
$\LaTeX$ 源代码以一个 `\documentclass` 命令作为开头，它指定了文档使用的**文档类**。document
环境当中的内容是文档正文。
在 `\documentclass` 和 `\begin{document}` 之间的位置称为**导言区**。在导言区中一般会使用
\usepackage 命令调用**宏包**，还会进行文档的全局设置。
```tex
\documentclass{...} % ... 为某文档类
% 导言区
\begin{document}
% 正文内容
\end{document}
% 此后内容会被忽略
```

## 1.3 $\LaTeX$ 宏包和文档类
### 1.3.1 文档类
文档类规定了 $\LaTeX$ 源代码所要生成的文档的性质——普通文章、书籍、演示文稿、个人简
历等等。$\LaTeX$ 源代码的开头须用 `\documentclass` 指定文档类：
```tex
\documentclass[⟨options⟩]{⟨class-name⟩}
```
其中 ⟨class-name⟩ 为文档类的名称，如 LATEX 提供的 article, book, report，在其基础上派
生的一些文档类如支持中文排版的 ctexart / ctexbook / ctexrep，或者有其它功能的一些文档类，
如 moderncv / beamer 等。

可选参数 ⟨options⟩ 为文档类指定选项，以全局地规定一些排版的参数，如字号、纸张大小、
单双面等等。比如调用 article 文档类排版文章，指定纸张为 A4 大小，基本字号为 11pt，双面
排版：
```tex
\documentclass[11pt,twoside,a4paper]{article}
```

### 1.3.2 宏包
在使用 $\LaTeX$ 时，时常需要依赖一些扩展来增强或补充 LATEX 的功能，比如排版复杂的表
格、插入图片、增加颜色甚至超链接等等。这些扩展称为宏包。调用宏包的方法非常类似调用文
档类的方法：
```tex
\usepackage[⟨options⟩]{⟨package-name⟩}

% 一次性调用三个排版表格常用的宏包
\usepackage{tabularx, makecell, multirow}
```

宏包（包括前面所说的文档类）可能定义了许多命令和环境，或者修改了 $\LaTeX$ 已有的命
令和环境。它们的用法说明记在相应宏包和文档类的帮助文档。在 Windows 命令提示符或者
Linux 终端下输入命令可查阅相应文档：
```
texdoc ⟨pkg-name⟩
```

## 1.4 文件的组织方式
当编写长篇文档时，例如当编写书籍、毕业论文时，单个源文件会使修改、校对变得十分困
难。将源文件分割成若干个文件，例如将每章内容单独写在一个文件中，会大大简化修改和校对
的工作。

LATEX 提供了命令 `\include` 用来在源代码里插入文件：
```tex
\include{⟨filename⟩} 
```
```tex
\include{chapters/a.tex} % 相对路径
\include{/home/Bob/file.tex} % *nix （包含 Linux、macOS（OS X））绝对路径
\include{D:/file.tex} % Windows 绝对路径，用正斜线
```
值得注意的是 `\include` 在读入 `⟨filename⟩` 之前会另起一页。有的时候我们并不需要这样，而是用 `\input` 命令，它纯粹是把文件里的内容插入：
```tex
\input{⟨filename⟩}
```

# 二、用 $\LaTeX$ 排版文字
|功能|实现方式|
|---|---
|换行| 空行，或在行末输入 `\par`
|注释| `%`
|单、双引号| `` `text'``, ` ``text''`
|连字号、短破折号和长破折号| 连字号 `-` 用来组成复合词；<br> 短破折号 `--` 用来连接数字表示范围；<br> 长破折号 `---` 用来连接单词，语义上类似中文的破折号。
|省略号| `\ldots`
|手动断行| `\\[⟨width⟩]`, `\\*[⟨width⟩]`, `\newline` <br> 带星号的断行命令表示禁止在断行处分页
|手动断页| `\newpage`, `\clearpage`

![pic](/images/2021-01/Snipaste_2021-01-11_14-55-33.jpg)

# 附 1: 实用宏包
## 1.1 syntonly
加载这个宏包后，在导言区使用 `\syntaxonly` 命令，可令 $\LaTeX$ 编译后不生成 DVI 或者 PDF 文档，只排查错误，编译速度会快不少：
```tex
\usepackage{syntonly}
\syntaxonly
```
如果想生成文档，则用 `%` 注释掉 `\syntaxonly` 命令即可。

# 三、文档元素
## 3.1 章节和目录
### 3.1.1 章节标题
```tex
\chapter{⟨title⟩}  % 只在 book 和 report 文档类有定义
\section{⟨title⟩} 
\subsection{⟨title⟩}
\subsubsection{⟨title⟩} 
\paragraph{⟨title⟩} 
\subparagraph{⟨title⟩}

\part  % 将整个文档分割为大的分块，但不影响 \chapter 或 \section 等的编号
```
上述命令除了生成带编号的标题之外，还向目录中添加条目，并影响页眉页脚的内容。每个命令有两种变体：
- 带可选参数的变体：`\section[⟨short title⟩]{⟨title⟩}`
标题使用 `⟨title⟩` 参数，在目录和页眉页脚中使用 `⟨short title⟩` 参数；
- 带星号的变体：`\section*{⟨title⟩}`
标题不带编号，也不生成目录项和页眉页脚。

较低层次如 `\paragraph` 和 `\subparagraph` 即使不用带星号的变体，生成的标题默认也不
带编号，事实上，除 `\part` 外：
- article 文档类带编号的层级为 `\section / \subsection / \subsubsection` 三级；
- report/book 文档类带编号的层级为 `\chapter / \section / \subsection` 三级。

### 3.1.2 目录
在 $\LaTeX$ 中生成目录非常容易，只需在合适的地方使用命令：
```tex
\tableofcontents
```
就会生成单独的一章（book / report）或一节（article），标题默认为 “Contents”

## 3.2 标题页


