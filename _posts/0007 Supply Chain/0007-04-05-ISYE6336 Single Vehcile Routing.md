---
layout: post
title: ISYE6336 Ocean Freight
categories: Supply-Chain
description:
keywords: SCE, Supply-Chain, ISYE6336
mathjax: true
---

<center>

# ISYE6336 - Single Vehicle Routing
</center>

---

## Heuristic Solution Methods
- Alternatives to exact optimization by MIP
- a heuristic solution may not minimize cost

$$c(T^*)\leq c(T^H)$$

where $c(T*)$ is the optimal cost, $c(T^H)$ is the cost of the heuristic solution. Define the **Solution Optimiality Gap** as:
$$\frac{c(T^*)-c(T^H)}{c(T^*)}$$

## Heuristic for TSP
- **Greedy**: make a "best choice" each iteration based on "current conditions". Finalize that choice, and move on!

- **Construction**: start with no solution, and construct a feasible route $T^H$ (for example, $T^{NN}$, the nearest neighbor solution)

