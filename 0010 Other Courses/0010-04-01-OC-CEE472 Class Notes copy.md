---
layout: post
title: CEE472 - Class Notes
categories: Other-Courses
description: Personal Notes
keywords: CEE472
mathjax: true
---



<img src="/images/2022-02/Screenshot 2022-02-19 at 10.29.21 AM.png" width="50%">

**Equation of Motion (EOM)**:
$$m{\"u}+ku=p(t)$$

**Free Vibration** $p(t)=0$
$$m{\"u}+ku=0$$

$$u(t)=A_1\cos\omega_nt + A_2\sin\omega_nt$$

可求得 $\omega_n$:
$$\omega_n=\sqrt{\frac{k}{m}}$$

代入 $u(0)=u_0, \dot u(0)=v_0$, 可求得 $A_1, A_2$:
$$u(t)=u_0\cos\omega_nt + \frac{v_0}{\omega_n}\sin\omega_nt$$

**Forced Response** $p(t)\neq 0$
$$u(t)=u_c(t)+u_p(t)$$

$u_c$ complementary solution, 格式等于 Free Vibration 下的 $u(t)$

$u_p$ particular solution, 满足 EOM 的任意解。例如当 $p(t)$ 为一次函数时，我们可以假设 $u_p(t)$ 同为一次函数，那么就有 $m\"u_p=0$, 因此 $u_p=p(t)/k$

求出任一 $u_p(t)$ 后，得到：
$$u(t)=A_1\cos\omega_nt + A_2\sin\omega_nt+u_p(t)$$

再根据 $u(0),\dot u(0)$ 的值求解 $A_1,A_2$ ($\omega_n$ 同 Free Vibration)

## 2. Mathematical Models of SDOF Systems
SDOF: Single Degree of Freedom

## 4.

$$m\"{\bar{u}} + c\dot{\bar{u}} + k\bar{u} = \bar{p} = p_0e^{i\Omega t} \tag{4.28}$$

$$\bar{u}(t) = \bar{U}e^{i\Omega t} \tag{4.30}$$

Since $\bar{U}$ is the complex amplitude, it could be written as:
$$\bar{U} = Ue^{-ia} \tag{4.31}$$

Substitute $(4.30)$ into $(4.28)$
$$\bar{U}=\frac{p_0}{(k-m\Omega^2)+ic\Omega}$$

