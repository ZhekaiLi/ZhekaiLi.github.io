---
layout: post
title: Week-7
categories: Math415
description: Personal Notes
keywords: Math415，Calculas，Matrix
---

# L11 Orthogonality
## 11.1 Normed vector spaces
> ##### Def 1: Normed vector space
> $X$ is normed if there is a function $\|\cdot\|:X\to\mathbb{R}$, such that
$$\begin{aligned}
\|x\| &\geq 0 \\
\|x+y\| &\leq \|x\|+\|y\|
\end{aligned}$$
**Example**
1. When $X=\mathbb{R}^2$
$\|x\|_1=\vert x_1\vert+\vert x_2\vert$
$\|x\|_2=\sqrt{x_1^2+x_2^2}$
2. When $X=\{\text{all polynomials on }[0,1]\}$
$\|x\|_1=\int_0^1 \vert x(t)\vert dt$
$\|x\|_2=\sqrt{\int_0^1  x^2(t) dt}$

## 11.2 Euclidean norm in $\mathbb{R}^n$
