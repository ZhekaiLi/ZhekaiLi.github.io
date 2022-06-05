---
layout: post
title: (Book)Concise CV:Chapter 07-09
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

# Chapter 7: 3D Shape Reconstruction
## 7.1 Surfaces
### 7.1.1 Surface Topology

> **Orientable Surfaces**


> **The Euler Characteristic of a Surface**

$$\tag{7.1} \chi(Z)=\alpha_0-\alpha_1+\alpha_2$$

> **Separations by Jordan Surfaces in 3D Space**


### 7.1.2  Local Surface Parameterizations

> **Representation of Surface Patches**

$$\tag{7.2} Z_S=F_e(X_S,Y_S) = a-\sqrt{r^2-X_S^2-Y_S^2}$$


> **Surface Normals**

$$\tag{7.4} \nabla Z=\textbf{grad }Z=\bigg[\frac{\partial Z}{\partial X}, \frac{\partial Z}{\partial Y}\bigg]^T$$

$$\tag{7.5} \textbf{n}=\bigg[\frac{\partial Z}{\partial X}, \frac{\partial Z}{\partial Y},1\bigg]^T = [a,b,1]$$

$$\tag{7.6} \textbf{n}^\circ=\frac{\textbf{n}}{\Vert \textbf{n}\Vert_2}$$


> **Gradient Space**

$$\tag{7.7} \mathbf{n_1}\cdot\mathbf{n_2}=0=a_1a_2+b_1b_2+1$$



### 7.1.3 Surface Curvature

> **Gaussian Curvature**

> **Normal Curvature**


> **Principal Curvatures**


> **Euler Formula**

$$\tag{7.9} \kappa(p)=\lambda_1\cdot\cos(\eta)^2+\lambda_2\cdot\sin(\eta)^2$$



> **Mean Curvature**

> **Theorem by Meusnier**

$$\tag{7.10} \kappa_\eta = \kappa_c\cdot\cos(\mathbf{n}_P,\mathbf{n}_c)$$


> **Similarity Curvature**

$$\tag{7.11} \kappa_3 = \frac{\min(\vert\kappa_1\vert, \vert\kappa_2\vert)}
{\max(\vert\kappa_1\vert, \vert\kappa_2\vert)}$$

# Chapter 9: Feature Detection and Tracking
## 9.1 Invariance, Features, and Sets of Features
### 9.1.1 Invariance
The process of taking images:
$$I=C(S)$$

$I$ input images
$S$ scenes
$C$ camera
> **Procedure $\mathscr{X}$**

Maps $I$ into some vertical output:
$$\tag{9.1}R(I)=R(C(S))=\bf{r}$$

> **Invariance w.r.t. Changes in the Scene**

定义一个变化函数 $N(S)$，可以包括旋转、明暗等变化：
$$\tag{9.2}R(I_{new})=R(C(N(S)))$$

当 $R(I)=R(I_{new})=\bf{r}$ 时，可以说 ==procedure $\mathscr{X}$ is invariant to the change $N$==

> **Invariance w.r.t. Used Camera**

Similarly, if a modification $M$ in camera $C$ that $C_{mod}=M(C)$ also keep $R(I_{mod})=R(I)$, we call ==procedure $\mathscr{X}$ is invariant to the change $M$==

### 9.1.2 Keypoints and 3D Flow Vectors
**Keypoint** (or interest point) is defined by some particular image intensities “around” it, such as a corner. 
我觉得可以理解为图像的一些特征点

**Descriptor** is a finite vector that summarizes properties for the keypoint. 
A descriptor can be used for classifying the keypoint. 

**Feature**: a keypoint and a descriptor together

---
## 9.2  Examples of Features
### 9.2.1 Scale-Invariant Feature Transform