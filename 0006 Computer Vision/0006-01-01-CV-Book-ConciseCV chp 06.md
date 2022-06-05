---
layout: post
title: (Book)Concise CV:Chapter 06
categories: Computer-Vision
description:
keywords: CV, Matrix
mathjax: true
---

<style>
img {
	image-rendering:-moz-crisp-edges;
	image-rendering:-o-crisp-edges;
	image-rendering:-webkit-optimize-contrast;
	image-rendering: crisp-edges;
	-ms-interpolation-mode:nearest-neighbor;
}
</style>

# Chapter 6
## 6.1 Cameras
> **Central Projection Equations**
<center>
    <img src="/images/2021-04/Snipaste_2021-04-06_09-47-33.jpg" width="50%"> <br>
    <div style="color: #808080">Figure: Projection</div>
</center><br>

$$\tag{6.2}x_u=\frac{fX_s}{Z_s}\text{ and }y_u=\frac{fY_s}{Z_s}$$

> **The Principle Point**
> 
Let $(c_x, c_y)$ be the intersection point of the optical axis with the image place in $xy$ coordinates

<center>
    <img src="/images/2021-04/Snipaste_2021-03-31_15-39-47.jpg" width="50%"> <br>
    <div style="color: #808080;">Figure: Intersection Point</div>
</center><br>

Then for $xy$ coordinates in the image plane with the origin point $(c_x, c_y)$, the corrodinates of a point becomes:
$$\tag{6.3}(x,y)=(x_u+c_x,y_u+c_y)=\bigg(\frac{fX_s}{Z_s}+c_x,\frac{fY_s}{Z_s}+c_y\bigg)$$

> **Two-Camera System**

A 3D point $P=(X_s,Y_s,Z_s)$ in this system will be:
$$\tag{6.4}p_{uL}=(x_{uL},y_{uL})=\bigg(\frac{fX_s}{Z_s},\frac{fY_s}{Z_s}\bigg)$$

$$\tag{6.5}p_{uR}=(x_{uR},y_{uR})=\bigg(\frac{f(X_s-b)}{Z_s},\frac{fY_s}{Z_s}\bigg)$$



<center>
    <img src="/images/2021-04/Snipaste_2021-03-31_15-53-39.jpg" style="zoom:100%"> <br>
    <div style="color: #808080;">Figure: Canonical Stereo System</div>
</center><br>

## 6.2 Coordinates
### 6.2.1 World Coordinates
> **Affine Transform**
<center>
    <img src="/images/2021-04/Snipaste_2021-04-01_21-32-51.jpg" style="zoom:100%" > <br>
    <div style="color: #808080;">Figure: Affine From World to Camera</div>
</center><br>

<center>
    <img src="/images/2021-04/Snipaste_2021-04-01_21-33-49.jpg" width="60%"></div>
</center><br>

<center>
    <img src="/images/2021-04/Snipaste_2021-04-01_21-41-07.jpg" style="zoom:80%"></div>
</center><br>

<center>
    <img src="/images/2021-04/Snipaste_2021-04-01_21-41-18.jpg" width="60%"></div>
</center><br>

> **Projection from World Coordinates into an Image**
<center>
    <img src="/images/2021-04/Snipaste_2021-04-06_11-12-28.jpg" width="70%"></div>
</center><br>

### 6.2.2 Homogeneous Coordinates


$$\dot{\varepsilon}_{ss}=\frac{\Delta\varepsilon}{\Delta t}$$

Inhomogeneous coordinates in 2D: $(x,y)$ <br>
Homogeneous coordinates in 2D: $(x',y',w)$

An affine could be made frome homo- to inhomo-
$$x=x'/w\text{ and }y=y'/w$$

**Benefits of homo-**: use just one matrix multiplication to replace one matrix multiplication plus one vactor addition in inhomogeneous coordinates

<center>
    <img src="/images/2021-04/Snipaste_2021-04-01_23-24-01.jpg" style="zoom:100%"></div>
</center><br>

> **Lines in 2D Plane** 

Define $\gamma=(a,b,c)$ represent the line $ax+by+c=0$, then for two lines $\gamma_1=(a_1,b_1,c_1), \gamma_2=(a_2,b_2,c_2)$, there **intersection point** is:
$$\tag{6.16}\gamma_1\times \gamma_2=(b_1c_2-b_2c_1,a_2c_1-a_1c_2,a_1b_2-a_2b_1)$$

> **Explain**：
> 1. 二维平面中的点 $(x,y)$ 可以映射至三维空间中的一条穿过原点的直线，该直线与平面 $z=1$ 相交于 $(x, y, 1)$
> 2. 定义三维空间中的的平面 $P=(a,b,c,d),\;ax+by+cz+d=0$，则同理二维平面中的直线 $(a,b,c)$ 可以映射为三维空间中的一个穿过原点的平面 $(a,b,c,0)$
> 3. 两个穿过原点的平面的交线一定过原点，且方向与两平面的法向量垂直 $direction=(a_1,b_1,c_1)\times(a_2,b_2,c_2)$，因此这条线与平面 $z=1$ 相交于 $(b_1c_2-b_2c_1,a_2c_1-a_1c_2,a_1b_2-a_2b_1,1)$
> 4. 最后映射回二维平面，可得 Eqn.6.16 中的交点公式

> **Two Points Define One Line**

In homogeneous coordinates, two points $p_1=(x_1,y_1,w_1),p_2=(x_2,y_2,w_2)$ defines a line which acrosses them: $p_1\times p_2$

> **Explain**：
> 1. 同上，$p_1$ 可映射至三维空间中经过原点、且与平面 $z=w_1$ 相较于 $(x_1,y_1,w_1)$ 的直线，$p_2$ 同理
> 2. 在三维空间中，这两条直线能够定义一个穿过原点、法向量为 $p_1\times p_2$ 的平面
> 3. 在映射回二维平面，可得对应的直线公式


## 6.3 Camera Calibration
### 6.3.1 A User’s Perspective on Camera Calibration
> **Involved Transforms in Camera**

拍照这一看似简单的过程其实蕴含了大量的坐标系转化：
<center>
    <img src="/images/2021-04/Snipaste_2021-04-01_21-32-51.jpg" style="zoom:100%" > <br>
    <div style="color: #808080;">Figure: Affine From World to Camera</div>
</center><br>

1. Coordinate stransform from world coordinates $(X_w,Y_w,Z_w)$ in to camera coordinates $(X_s,Y_s,Z_s)$
2. Projection from camera coordinates $(X_s,Y_s,Z_s)$ to image coorinates $(x_u,y_u)$
3. Lens distortion maps image coorinates $(x_u,y_u)$ to actually valid (distorted) coordinates $(x_d,y_d)$
4. Shift from $(x_d,y_d)$ to sensor coordinates $(x_s,y_s)$, by subtracting the principal point $(c_x,c_y)$

> **Lens Distortion**

上述过程自然而然地发生在拍照的过程中，而在相机校准的过程中，我们需要由 actually valid (distorted) coordinates $(x_d,y_d)$ 反推 image coorinates $(x_u,y_u)$，公式如下：
$$\tag{6.20} x_u = c_x+(x_d-c_x)(1+\kappa_1r_d^2+\kappa_2r_d^4+e_x)$$

$$\tag{6.21} y_u = c_y+(y_d-c_y)(1+\kappa_1r_d^2+\kappa_2r_d^4+e_y)$$

where $(c_x,c_y)$ is the principal point and $r_d=\sqrt{(x_d-c_x)^2+(y_d-c_y)^2}$. The error $e_x,e_y$ are insignificant and can be assumed to be zero

> **Designing a Calibration Method**

General procedure:
1. 已知若干个点的 world coordinates $(X_w, Y_w, Z_w)$ 及其对应的 image coordinates $(x,y)$
2. Unknown values that need to be calibrated: $c_x,c_y,f,r_{11}\text{ to }r_{33},t_1,t_2,t_3$
3. 由于未知数非常少，只要通过少量已知点的联立方程组，就能求得这些未知量

<center>
    <img src="/images/2021-04/Snipaste_2021-04-06_11-12-28.jpg" width="70%"> <br>
    <div style="color: #808080;">Figure: From World to Image</div>
</center><br>

### 6.3.2 Rectification(矫正) of Stereo Image Pairs
> **A Multi-camera System**

Only consider a a general case of a Camera $i$ or Camera $j$, where the numbers $i$ and $j$ identify different cameras in a multi-camera system.

> **The Camera Matrix**

Intrinsic camera parameters of Camera $i$:
1. Edge lengths $e^x_i,e^y_i$ of camera sensor cells
2. Skew parameter $s_i$
3. Coordinates of the principal point $\bf{c}_i=(c_i^x,c_i^y)$ where the optical axis of Camera $i$ and its image plane intersect
4. Focal length $f_i$
   
Instead of simple Eqn.(6.14), defining a camera model just based on the intrinsic parameters $f, c_x, c_y$, we have now a refined projection equation in 4D homogeneous coordinates, mapping a 3D point $P = (Xw,Yw,Zw)$ into the image coordinates $p_i = (x_i,y_i)$ of the ith camera as follows:
<center>
    <img src="/images/2021-04/Snipaste_2021-04-06_22-39-52.jpg" ></div>
</center><br>

where $\bf{R}_i, \bf{t}_i$ denote the rotation matrix and translation vecotr in 3D inhomogeneous world coordinates, $\bf{K_i}$ denotes the intrinsic camera parameters and $\bf{A_i}$ denotes the affine matrix.

> **Common Viewing Direction for Rectifying Cameras $i$ and $j$**
<center>
    <img src="/images/2021-04/Snipaste_2021-04-06_22-45-58.jpg"></div>
</center><br>

As shown in the figure above:
1. $\bf{b}_{ij}$: vector from the projection centre of Camera $i$ to $j$
2. $\Pi$: plane perpendicular to $\bf{b}_{ij}$
3. $\bf{n}_i, \bf{n}_j$: project the unit vectors $z_i^\circ$ and $z_j^\circ$ of both optical axes into $\Pi$, which results in vectors $\bf{n}_i, \bf{n}_j$ (==由于我们的目的是求解 $\bf{z}_{ij}$ 的方向，因此不需要在意向量 $\bf{n}$ 的具体大小，只要保证 $\bf{n}_i, \bf{n}_j$ 等比例即可==)
<center>
    <img src="/images/2021-04/Snipaste_2021-04-06_23-00-50.jpg" style="zoom:100%"></div>
</center><br>
<center>
    <img src="/images/2021-04/Snipaste_2021-04-06_23-01-03.jpg" width="30%"> <br>
    <div style="color: #808080;">Figure: Eqn.(6.24) 的直观理解</div>
</center><br>

4. $\bf{z}_{ij}^\circ$: aiming at balance treatment for both cameras, just directly add $\bf{n}_i, \bf{n}_j$
<center>
    <img src="/images/2021-04/Snipaste_2021-04-06_23-01-02.jpg"></div>
</center><br>

5. $\bf{x}_{ij}^\circ,\bf{y}_{ij}^\circ$: derive the common view direction
<center>
    <img src="/images/2021-04/Snipaste_2021-04-07_08-20-39.jpg" style="zoom:80%"></div>
</center><br>

最后，能够得到旋转矩阵 $\bf{R}_{ij}=(\bf{x}_{ij}, \bf{y}_{ij}, \bf{z}_{ij})^T$ 

> **旋转矩阵 $\bf{R}$ 的一些性质**
> 1. ==旋转矩阵的行表示目标坐标系的基向量==，例如第一行表示目标坐标系的 $x$ 轴
> 2. 旋转矩阵为正交矩阵，因此 ==$R^{-1}=R^T$==

> **Producing the Rectified Image Pair**

Define the roation matrices that rotate both cameras into their new (virtual) viewing direction: (由于 $\bf{R}_i$ 是相机 $i$ 拍照过程过自然进行的坐标系旋转，因此在使用 $\bf{R}_{ij}$ 时需先乘上一个 $R^T=R^{-1}$ 以消去原先的 $R$) 
$$\tag{6.28} \bf{R}_{i}^*=\bf{R}_{ij}\bf{R}_{i}^T\text{ and }\bf{R}_{j}^*=\bf{R}_{ij}\bf{R}_{j}^T$$

In general, when rotating any camera around its projection centre about the matrix $\bf{R}$, the image is transformed by a rotation homography (i.e. a recalculated projective transformation)
$$\tag{6.29} \bf{H}=\bf{K}\cdot\bf{R}\cdot\bf{K}^{-1}$$

where, $\bf{K}_{3\times3}$ denotes intrinsic parameters of this camera:
1. $\bf{K}^{-1}$ transfers pixel coordinates into camera coordinates in world units
2. $\bf{R}$ rotates them into the common plane
3. $\bf{K}$ transfers them back into pixel coordinates

$$\tag{6.30}\hat{p}=\textbf{H} p$$

where $\hat{p}$ is the new value at pixel location and $p$ is the original image values

> **Creating an Identical Twin**

$$\tag{6.31} \bf{H}_{ij}=\bf{K}_i\cdot\bf{R}^*_j\cdot\bf{K}_j^{-1}$$

> **Fundamental and Essential Matrix**

$L$ denotes left camera and $R$ denotes right camera. Let $p_L,p_R$ be corresponding stereo points, i.e. the projections of a 3D point $P$ in the left and right image planes. Assume that $p_L,p_R$ are given in **homogeneous** coordinates. Then we have that:
$$\tag{6.31} p^T_R\cdot\textbf{F}\cdot p_L=0$$

> **Explain**
> 如下图所示，已知左侧 image plane 上的一点 $p_L$，则该点的实际位置一定在 $P-P_1-P_2$ 这条 直线上。再把该直线映射到右侧 image plane 上，得到直线 $l'$。==Fundamental matrix 基础矩阵 $\bf{F}$ 能够将 $p_L$ 映射至 $l'$: $l'=\textbf{F}\cdot p_L$==
> 
> 由于 $p_R$ 一定在直线 $l'$ 上，且在 homogeneous coordinates 中，二维点 $(x,y)$ 被表示为 $(x,y,1)$，直线 $ax+by+c=0$ 被表示为 $(a,b,c)$，因此 $p_R^T\cdot l'=ax+by+c=0$


<center>
    <img src="/images/2021-04/Snipaste_2021-04-07_14-15-55.jpg" width="70%"> <br>
    <div style="color: #808080;">Figure: Eqn.(6.31) 的直观理解</div>
</center><br>

Fundamental matrix $\bf{F}$ 与 camera matrics $\bf{K}_R,\bf{K}_L$ 间存在以下关系：
$$\tag{6.33} \bf{F}=\bf{K}_R^{-T}\cdot\bf{R}[t]_\times\cdot\bf{K}_L^{-1}$$

where
<center>
    <img src="/images/2021-04/Snipaste_2021-04-07_14-32-48.jpg" style="zoom:80%"></div>
</center><br>

Define ==essential matrix $\bf{E}$==:
$$\tag{6.35} \bf{E}=\bf{R}[t]_\times$$


