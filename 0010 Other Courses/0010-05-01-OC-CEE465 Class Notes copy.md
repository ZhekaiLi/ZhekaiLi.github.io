---
layout: post
title: CEE465 - Class Notes
categories: Other-Courses
description: Personal Notes
keywords: CEE465
mathjax: true
---

对于一根杆的两个段点
`load` = `stiffness` * `displacement`
$$q_{6\times 1}=k'_{6\times 6}d_{6\times1}$$

`local coordinate disp` = `rotation` * `gloabl coordinate disp`
$$d=TD$$

`globel load` in `D` = `transposition(rotation)` * `local load` in `d`
$$Q=T^Tq$$

因此有：
$$q=k'TD$$

$$Q=(T^Tk'T)D=kD$$