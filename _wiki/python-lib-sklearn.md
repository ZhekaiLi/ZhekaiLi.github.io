---
layout: wiki
title: sklearn
cate1: Python
cate2: -libs
description: 
keywords: Python
mathjax: true
---

## sklearn.datasets
### .1 生成数据

```py
from sklearn import datasets
```
团状样本点集

```py
X, y = datasets.make_blobs(n_samples=1000, 
    centers=10,     # 团的个数
        # 默认随机生成分布, 也可以自定义质心
        # 例如 centers=[[1,2], [2,3]] 
    n_features=2,  # 数据维度
    cluster_std=0.5, 
    random_state=4,
    s=10  # 样本点的大小
)
```
内外两个环状分布的样本点集

```py
X, y = datasets.make_circles(n_samples=1000, 
    factor=0.5, # 内外环距离，取值 [0, 1)
        # ->0, 内环在中央聚合成一个团; ->1, 内环外扩与外环合并
    noise=0.05  # 噪音
)
```

### 其他数据类型
波士顿房价数据

```py
X, y = datasets.load_boston(return_X_y=True) # X, y np.array()
```
一般情况下会把 X 转化为 pd.DataFrame()，因此需要给 Column Headers 赋值（来源于[官方文档](https://scikit-learn.org/stable/datasets/toy_dataset.html#boston-dataset)）

```py
X = pd.DataFrame(X)
X.columns = [...]
```


## sklearn.linear_model

```py
from sklearn.linear_model import LinearRegression

lr = LinearRegression()
lr.fit(X, y)
```

```py
lr.coef_      # 系数
lr.intercept_ # 截距
```


## sklearn.matrics
### .1 Value the clustering 检查聚类算法的性能

```py
sklearn.matrics.silhouette_score(X_blobs,  # 原数据
    class_prediction  # 分类标签, 例如以下表示有三类 array([0, 1, 2, 1, 1, 2])
)
```


## sklearn.model_selection

```py
from sklearn.model_selection import ...
```
划分训练集/测试集

```py
# By deafult, sklearn use 75/25 split
X_train, X_test, y_train, y_test = train_test_split(X, y, random_state=0)
```


## sklearn.processing

```py
from sklearn.processing import ...
```
### Scale Data
LINKs Back
[Jupyter Notebook: Simple_neural_network_with_sklearn](../jupyterNotebooks/Simple_neural_networks_with_sklearn.ipynb)


**Standard Scale**
$$z=\frac{x-\mu}{\sigma}$$

```py
scaler = StandardScaler()

# Scale X_train
# 基于 X_train 的 mu/sigma 创建一个 Scale transform，并应用
X_train_scaled = scaler.fit_transform(X_train)

# Scale X_test: 把由 X_train 创建的 transfrom 应用于 X_test
x_test_scaled = scaler.transform(X_test)
```


## sklearn.neural_network

```py
from sklearn.neural_network import ...
```
Standard multi-layer perceptron regressor

```py
reg = MLPRegressor(random_state=0, max_iter = 100000, learning_rate_init=0.0001)
```
- `learning_rate_init`: 学习速率（步长），一般取 [0.0001, 0.01]

```py
reg.fit(X_train_scaled, y_train)
reg.score(X_test_scaled, y_test) # return R2 score

```



