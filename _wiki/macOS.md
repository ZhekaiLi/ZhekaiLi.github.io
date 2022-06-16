---
layout: wiki
title: macOS
cate1: Others
cate2:
description: 
keywords:
---

# Shortcuts
截图

```txt
Cmd + Shift + 3: 全屏截图
Cmd + Shift + 4: 区域截图
```
搜索

```txt
Cmd + Space: Spotlight Search
Control + Cmd + Space: 窗口类型的全局搜索
```
应用 & 屏幕

```txt
Cmd + Tab: 快速切换应用
Control + Cmd + Q: 锁定屏幕（需要指纹或密码解锁）
```


# Terminal
## 路径/目录
```python
cd ~                 # 切换到当前用户的主目录
cd folder1/folder1_1 # 切换到具体文件夹

ls                   # 查看当前目录下所有文件夹和文件
```

## 使用 Conda 进行 Python 包管理
这里使用 miniforge3 的 conda

```python
conda env list                       # 查看所有 python 环境
conda create -n env_name python==3.9 # 创建一个指定版本的 python 环境
conda activate env_name              # 激活环境

conda list # 查看当前环境所安装的所有 python 包
```

