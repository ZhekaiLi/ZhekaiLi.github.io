---
layout: post
title: Math415 Week-13
categories: Math415
description: Personal Notes
keywords: [Math415，Calculas，Matrix]
mathjax: true
---

# L23
Left and right inverses. Pseudoinverse

## 23.1 Background

**Theorem 1:** Assume $A_{m\times n}$ has independent columns, then $A^TA$ invertible 
- **Proof:** Since $Ax=0$ only when $x=0$, then $x^TA^TAx=0$ only when $x=0$, finally for $A^TAx=0$

**Theorem 2:** The optimal solution $\hat{x}$ of minimizing $\vert\vert Ax-b\vert\vert$ is
$$\hat{x}=(A^TA)^{-1}A^Tb$$

## 23.2 Left and right inverse
> #### Def 1
