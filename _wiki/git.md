---
layout: wiki
title: Git
cate1: Others
cate2: 
description: 
keywords:
mathjax: True
---




## Init
设置用户名和账号

```bash
git config --global user.name "Zeka"
git config --global user.email "zekalee0523@gmail.com"
```

初始化

```bash
git init
```

## commit
提交代码更新

```bash
git add .
git commit -m "Comments Here"
```


查看日志

```bash
git log

>>>
commit 3473b6ed924834409ce137c8b0714c1e4756e95f (HEAD -> zk01, origin/zk01)   
Author: Zeka <zekalee0523@gmail.com>
Date:   Fri May 19 10:51:23 2023 -0700

    A little change to the excel file.

commit 3e42360279d8fa22f7bef8f2eec8f4278953468d
Author: Zeka <zekalee0523@gmail.com>
Date:   Fri May 19 10:27:38 2023 -0700

    Upload the excel file.
```

回退到老版本

```bash
git rest --hard commit_ID # 硬回退，不推荐，因为会删除之后的 commit
git rest commit_ID        # 默认回退模式
```

## Remote repository
对一个云端仓库，想在在本地修改、提交

```bash
# 克隆一个仓库到本地
# 会在当前目录下生成一个名为仓库名的文件夹
git clone https://...

# 跳转到仓库名文件夹，并在本地初始化仓库
cd Folder_Name
git init

# 修改，commit 到本地
git add .
git commit -m "Comments here"

# 提交到云端
git push
```

## Branch

```bash
# 创建
git branch [branch_name]

# 切换
git checkout branch [branch_name]

# 创建并切换
git checkout -b branch [branch_name]
```

将创建的本地 branch 提交到 remote repository
```bash
git push -u origin [branch_name_created]
```

查看当前所有 branches (本地 + remote)
```bash
git branch -a

>>>
* 0.1
  0.2
  0.3
  master
  remotes/origin/0.1
  remotes/origin/0.2
  remotes/origin/0.3
  remotes/origin/HEAD -> origin/master
  remotes/origin/master
```





