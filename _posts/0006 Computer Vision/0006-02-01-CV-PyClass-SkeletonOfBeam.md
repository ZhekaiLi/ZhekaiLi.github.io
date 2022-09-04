---
layout: post
title: PyClass SkeletonOfBeam Documentation
categories: Computer-Vision
description:
keywords: CV, Matrix, Python
mathjax: true
topmost: true
---

> This class is designed for reconstructing beam model from 3d object (or point cloud). The class mainly contains a workflow from loading data, constructing beam skeleton through step slicing, recoordinating and projecting, and finally reconstrut the model in a required coordinate.
> 
> Athor: Zeka(Zhekai) Li
> Time: Jun 2021

# Simple example
```py
import trimesh
import numpy as np
import sympy as sy
import scipy as sp

from SkeletonOfBeam import SkeletonOfBeam
from SkeletonOfBeam import GeometryToolBox

# Read mesh infos from object file
mesh = trimesh.load_mesh("beam.stl")

# Initialize beam object
roughVector = [1, 0, 0]
sob = SkeletonOfBeam(mesh, roughVector)

# Main process
## Find out a set of rough skeleton points from the input vector
sob.getScaleAlongSkeletonVec()
sob.getIntersectionsFromStep(step=1) # slice per step length
sob.getSkeletonPoints()

## Project the rough skeleton points onto x-y and x-z planes
sob.getNewCoordinate()
sob.getProjections()

## Fit the curve equations in these two planes separately
sob.getSkeletonEqs()
sob.getDerivativeSkeletonEqs()

## Recalculate the skeleton points, also get the cross-sections
sob.getNewSkeletonPoints()
sob.getNewIntersections()
```

# 1. Properties
## 1.1 Overal properties
> **mesh**

The initial mesh data as input.
- **Return type:** trimesh.Trimesh

> **centroid**

Beam's centroid point.
- **Return type:** (, 3) float

> **nVec**

Rough axial vector as input.
- **Return type:** (, 3) float
  
> **SkeletonPoints**

List of skeleton points along the beam axis.
- **Return type:** (n, 3) float

> **L**

Length of the projection of the skeleton curve on the axial vector.
- **Return type:** float

## 1.2 Cross-sections
> **IntersectionScale**

Range between top and bottom sufaces in the axial vector direction.
- **Return type:** (, 2) float

> **Intersections**

Cross-section cutted on each skeleton point.
- **Return type:** (, n) trimesh.Path3D

> **Intersections2D**

Cross-sections in 2D.
- **Return type:** (, n) trimesh.Path2D


## 1.3 Coordinate
> **XYZCoordinate**

New coordinate system constructed for the target beam.
- **Return type:** (3, 3) float

> **coorOrigin**

Origin point of the new coordinate.
- **Return type:** (, 3) float

> **XYProjections**

Positions of skeleton points on x-y plane of new coordinate.
- **Return type:** (n, 2) float

> **XZProjections**

Positions of skeleton points on x-z plane of new coordinate.
- **Return type:** (n, 2) float

## 1.4 Curve Functions

> **u_xyPlane**

Curve function of skeleton's projection on x-y plane.
- **Return type:** A *sympy* symbolic expression with a parameter `xi`.

This function could be used to get the u value at any parameter `xi` ($\xi$) in $[0, 1]$:
```py
[float] sob.u_xyPlane.evalf(subs={'xi': 0.5})
```

> **u_xzPlane**

Curve function of skeleton's projection on x-z plane.
- **Return type:** A sympy symbolic expression with a parameter `xi`

> **alpha_xyPlane**

The parameters fitted for the curve function on x-y plane.
- **Return type:** (, 4) float

> **alpha_xzPlane**

The parameters fitted for the curve function on x-y plane.
- **Return type:** (, 4) float

> **dudx_xyPlane**

Derivation of the skeleton curve on x-y plane.
- **Return type:** A *sympy* symbolic expression with a parameter `xi`.

This function could be used to get the du/dx value at any parameter `xi` ($\xi$) in $[0, 1]$:
```py
[float] sob.dudx_xyPlane.evalf(subs={'xi': 0.5})
```

> **dudx_xzPlane**

Derivation of the skeleton curve on x-z plane.
- **Return type:** A *sympy* symbolic expression with a parameter `xi`.



# 2. Methods

## 2.1 Process
> **getScaleAlongSkeletonVec()**

Get the scale of the target beam along the axial vector.
- **Parameters:** None
- **Returns:** None
- **Properties refreshed:** **IntersectionScale**(*(, 2) float*)

> **getIntersectionsFromStep(self, step=1)**

Slice one cross-section of the bean per step length along the axial vector.
- **Parameters:** step (*float*)
- **Returns:** None
- **Properties refreshed:** **Intersections**(*(, n) trimesh.Path3D*)

> **getIntersectionsFromSliceNum(sliceNum=5)**

Slices a specific number of cross-sections uniformly along the axial vector.
- **Parameters:** sliceNum (*int*) - number of slices
- **Returns:** None
- **Properties refreshed:** **Intersections**(*(, n) trimesh.Path3D*)

> **getSkeletonPoints()**

Get the skeleton points, which are the centroids of cross-sections.
- **Parameters:** None
- **Returns:** None
- **Properties refreshed:** **SkeletonPoints**(*(n, 3) float*)

> **getNewCoordinate()**

Construct a new coordinate, whose x-axis is the property **nVec**.
- **Parameters:** None
- **Returns:** None
- **Properties refreshed:** **XYZCoordinate**(*(3, 3) float*)

> **getProjections()**

Project the rough skeleton points onto x-y and x-z planes.
- **Parameters:** None
- **Returns:** None
- **Properties refreshed:** 
- - **XYProjections**(*(n, 2) float*)
- - **XZProjections**(*(n, 2) float*)

> **getSkeletonEqs()**

Fit the curve equations for projections points in x-y and x-z planes separately
- **Parameters:** None
- **Returns:** None
- **Properties refreshed:** 

> **getDerivativeSkeletonEqs()**

Take the derivative of the skeleton curve equations.
- **Parameters:** None
- **Returns:** None
- **Properties refreshed:** 

> **getNewSkeletonPoints()**

> **getNewIntersections()**

## 2.2 Functional methods

> **returnTangentVectorAtXi(xi_value)**

Return the tangent vector at xi=xi_value


    
> **returnSkeletonPointsInXiRange(xi_s, xi_e, pNum=10)**

        
> **showIntersections(ifOverlapped=True)**

Visualize the intersections in one graph
                
> **_H(xs, L, ifsymbol=False)**
        
> **H(xs, L, ifsymbol=False)**
