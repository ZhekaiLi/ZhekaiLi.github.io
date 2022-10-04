---
layout: post
title: Input Modeling
categories: Probability-Theory
description: Personal Notes
keywords: Risk-Analysis，Probability, Decision
mathjax: true
---

## Physical Basis of Distribution
#### Discrete:
- **Binomial**: model \#“success” in $n$ trials
when the trials are iid with success probability $p$
e.g. $n$ 个产品中有多少不合格
- **Negative Binomial**: model \#trials needed to achieve $k$ ”success“
e.g. 需要检测多少个产品才能检测出 $k$ 个不合格的
- **Geometric**: model \#trials until 1st "success"
- **Possion**: model #independent events that occur in a fixed time or space
e.g. 一个小时内到访商店的顾客数量。

#### Continuous:
- **Normal**: models the distrubution of process that can be thought as the <span style="background-color: yellow; color: black;">sum of a number of component process</span> (from Central Limit Theorem)
- **Weibull**: model the time to failure for components, with increasing/constant/decreasing failure rate
e.g. 常应用于描述电子元器件故障所需的时间，因为电子元器件的故障概率会随着自身的老化而上升(increasing failure rate)
- **Exponential**: model the time between independent events, or a process which is <span style="background-color: yellow; color: black;">memoryless</span>
e.g. the time to failure for a system that has constant failure ratio over time 
(1) "memoryless" 类似于马尔可夫链，即任意时刻 $P(t\vert t-1)=P(t-1\vert t-2)$。例如假设公交车等待时间满足指数分布，那么 P(再等5分钟|上辆车刚走10分钟) = P(再等五分钟|上两车刚走30分钟)。这是因为 $P(T>15\vert T>10)=P(T>35\vert T>30)$
(2) <span style="background-color: yellow; color: black;">Exponential is a special case of Weibull with constant rate</span>
- **Erlang**: model the sum of $k$ exponential random variables
(1) Erlang is a special case of gamma
- **Gamma($\alpha, \beta$)**: an extremely <span style="background-color: yellow; color: black;">flexible</span> distribution used to model nonnegative random variables
- **Beta($\alpha, \beta$)**: an extremely flexible distribution used to model bounded (fixed upper and lower limits) random variables
- **Uniform**: model complete uncertainty, since all outcomes are equally likely (suitable to worst-case analysis)
- **Triangular**: model a process when only the minimum, most likely and maximum values of the distribution are known
e.g. the minimum, most likely and maximum inflation rate we will have this year
