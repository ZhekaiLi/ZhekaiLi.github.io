---
layout: post
title: ISYE6334 Uncertain Demand
categories: Supply-Chain
description:
keywords: SCE, Supply-Chain
mathjax: true
topmost: true
---

# Multi-period Inventory Model with Uncertain Demand
## 1. EOQ with Uncertain Demand

Notations:
- $K=$ set up cost per order
- $h=$ holding cost per item per time
- $L=$ lead time (positive, could be constant or stochastic)
- $D=$ demand (annually, stochastic) 
- $c_B=$ backorder cost per item
- $OHI(t)=$ on-had inventory at time $t$
- $B(t)=$ # backordered items at time $t$
- $I(t)=OHI(t)-B(t)$
- $B_r=$ # backordered items during the lead time with reorder point $r$ 
- ==$q=$ order quantity==
- ==$r=$ reorder point==

> $X$ is a random variable representing ==demand during lead time==
> - If demand during each period is independent and $L$ constant
> $$E[X]=L\cdot E[D]\text{ and }Var(X)=L\cdot Var(D)$$
> - If demand during each period is independent, as well as $L$
> $$E[X]=E[L]E[D]\text{ and }Var(X)=E[L]Var(D)+E[D^2]Var(L)$$

### 1.1 Back-ordered case
