---
layout: post
title: Tree Structure
categories: Data-Structures-and-Algorithm
description: Personal Notes
keywords: Data Structure
mathjax: true
mermaid: true
---

# 1. Overview
树的基本术语
- `结点的度`：结点所拥有的子树的数量
- `树的度`：max(所有结点的度)
- `叶结点`：度为0的结点
- `层次`：根结点的层次为1，其余结点的层次等于其父节点层次加一
- `树的高度(深度)`：max(所有结点的层次)
- `有序树`：各子树之间有先后次序
- `祖先结点`：一个结点的祖先结点是指从其自身到根结点路径上的所有结点
- `子孙结点`：所有直接/间接的后继结点
- `森林`：n个互不相交的树的集合

基本操作
<img src="/images/2022-03/Snipaste_2022-03-18_18-12-40.png" width="100%">

# 2. Binary Tree
二叉树的性质
- 每个结点最多只有两个子结点
- 叶结点数 `n0` 和度为2的结点数 `n2`，满足 n0=n2+1

特殊的二叉树
- 满二叉树：深度为$k$，结点数为$2^k-1$。下左图是一个满二叉树的顺序表示
- 完全二叉树：结点序号与顺序表示的满二叉树一一对应，如下右图

<img src="/images/2022-03/Snipaste_2022-03-19_11-27-19.png" width="100%">



