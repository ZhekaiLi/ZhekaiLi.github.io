---
layout: post
title: Clustering Algorithm 03 - DBSCAN
categories: Machine-Learning
description: Personal Notes
keywords: [Machine-Learning, Python]
---

# DBSCAN

DBSCAN, Density-based spatial clustering of applications with noise, 是一种基于密度的聚类方法


$$
\begin{aligned}
&\text{Input: Data Set }D=(x_1,x_2,...,x_m), \text{Neighborhood Parameter }(\epsilon, minPts) \\
&\text{1. Initialize the core objects sets: } \Omega=\text{\O} \\
&\text{2. For }j=1,2,...,m,\text{ find all core objects and add them to }\Omega \\
&\text{3. Initialize the number of clusters: }k=0 \\
&\text{4. Initialize the set of unaccessed samples: }\Gamma=D \\
&\text{5. while }\Omega\neq\text{\O}\text{ do}\\
&\qquad\text{Record the recent unaccessed samples set: }\Gamma_{old}=\Gamma\\
&\qquad\text{Select a core object }o\in\Omega,\text{ initialize a queue }Q=<o> \\
&\qquad\text{while }Q\neq\text{\O}\text{ do}\\
&\;\;\;\qquad\text{Pop out the first sample }q\text{ from }Q\\
&\;\;\;\qquad\text{if }q\in\Omega\text{ then}\\
&\;\;\;\;\;\;\qquad\text{Define }\Delta=\Gamma\bigcap\text{Neighbors of }q\\
&\;\;\;\;\;\;\qquad\text{Add }\Delta\text{ into }Q\\
&\;\;\;\;\;\;\qquad\text{}\Gamma=\Gamma-\Delta\\
&\;\;\;\qquad\text{end if}\\
&\qquad\text{end while}\\
&\qquad\text{}k=k+1,\text{ generate the cluster }C_k=\Gamma_{old}-\Gamma\\
&\qquad\text{}\Omega=\Omega-C_k\\
&\;\;\;\;\text{end while}\\
&\text{Output: Cluster Division }C
\end{aligned}
$$