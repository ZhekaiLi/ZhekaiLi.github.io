---
layout: post
title: Layout of Piece-Picking from Cartons
categories: Supply-Chain
description:
keywords: SCE, Supply-Chain, ISYE6335, Warehouse
mathjax: true
topmost: true
---

# Layout of piece-picking from cartons (ISYE6335)

<center><img src="/images/2022-11/Snipaste_2022-11-07_15-05-48.png" width="70%"> <br>
    <b><div style="color: #808080;">Paths of material flow in a piece-distribution center</div></b>
</center>



**Layout decisions when designing piece(each) forward pick area**
- **How much of each SKU should be stored in forward pick area**
  3 stocking strategies
- **Which SKUs to store forward?**
  Ranking the SKUs by **bang-for-buck**
- **How large should the forward pick area be?**

Easy extensions:
- Product families
- Multiple forward areas

## 1. How much forward space should a SKU get?
### 1.1 Common stocking strategies: EQS vs. EQT

<center><img src="/images/2022-11/Snipaste_2022-11-07_15-13-31.png" width="70%"></center>

### 1.2 Obj: Minimize Laybor Costs
- **Picking time**: Picking from forward area is more efficient, most of the time
- **Restocking time**: Number of restocks * restocking cost per restock


Denote **estimated number of retocks** (**approximated restocking frequency**):
$$\frac{f_i}{v_i} = \frac{\text{flow in cubic-ft/yr}}{\text{volume stored in forward-pick area}}$$

**Why say $f_i/v_i$ is an estimation/approximatiom?**
- Ignores the need to safety stock $\to$ underestimate restock frequency
- Ignores  possible batching in restocking when an order line for SKU_i > $v_i\to$ overestimates restock frequency

### 1.3 Fraction of space allocated to each SKU

If $n$ SKUs in forward area, each with flow $f_i$, suppose the total space is <font color='red'>normalized to be $V=1$</font>
- EQS: $v_i=1/n$
- EQT: we want $f_i/v_i$ identical for all SKUs
$$v_i=\frac{f_i}{C}=\frac{f_i}{\sum^n_{j=1}f_j}$$


### 1.4 Number of restocks
#### EQS
$$\frac{f_i}{v_i}=\frac{f_i}{1/n}=nf_i$$

- Total restocks across all $n$ SKUs $=n\sum_{j=1}^nf_j$
- Fraction of restocks to SKU_i $=f_i/\sum_jf_j$


#### EQT
(number of restocks for every SKU is identical)
$$\frac{f_i}{v_i}=\frac{f_i}{f_i/\sum f_j}=\sum_{j=1}^n f_j$$

- Total restocks across all $n$ SKUs $=n\sum_{j=1}^nf_j$
- Fraction of restocks to SKU_i $=1/n$

到这里不难发现，对于 EQS vs. EQT
1. section 1.3 中的 fraction of space allocated 和这里的 fraction of restocks 的公式正好相互对调
2. 两种方式的 total restockes 一样 $\to$ <span style="background-color: yellow; color: black;">same amount of work!</span>

### 1.5 Optimal space allocation strategy
If $n$ SKUs in forward area, each with flow $f_i$, suppose the total space is <font color='red'>normalized to be $V=1$</font>

$$\min\sum_{i=1}^n \frac{f_i}{v_i}$$

where, $\sum_{i=1}^n v_i\leq 1$, $v_i\geq 0$

$$\boxed{v^*_i=\frac{\sqrt{f_i}}{\sum^n_{j=1}\sqrt{f_j}}}$$

- Restocks of SKU_i $=\sqrt{f_i}\sum^n_{j=1}\sqrt{f_j}$
- Total restocks across all $n$ SKUs $=(\sum_{j=1}^n\sqrt{f_j})^2$
- Fraction of restocks to SKU_i $=\sqrt{f_i}/\sum\sqrt{f_j}$

Note that here <span style="background-color: yellow; color: black;">fraction of restocks is **equal to** location allocated $v_i$</span>

### 1.6 Comparing EQS vs. EQT vs. OPT

<img src="/images/2022-11/Snipaste_2022-11-07_22-15-25.png" width="70%">

<img src="/images/2022-11/Snipaste_2022-11-07_22-16-29.png" width="70%">


### 1.7 Example
<img src="/images/2022-10/Snipaste_2022-10-26_09-49-46.png" width="80%">

$V = 80-40 = 40 \\
v^*_A=\sqrt{90}/(\sqrt{90}+\sqrt{250}+\sqrt{490})=0.2 \\
V^*_A=0.2*40=8<10\implies V^*_A=10$

$V=80-40-10=30\\
v^*_B=\sqrt{250}/(\sqrt{250}+\sqrt{490})=0.42\\
V^*_B=0.42*30=12.6>10\\
V^*_C=17.4>15$

therefore, $\boxed{V^*_A=10, V^*_B=12.6, V^*_C=17.4}$

## 2. Which SKUs should go into the forward area?
### 2.1 Obj:  Maximize Net Benefit
If $n$ SKUs in forward area, each with flow $f_i$, suppose the total space is <font color='red'>normalized to be $V=1$</font>

$$\max \sum_i(sp_i-c_r\frac{f_i}{v_i})x_i$$

$$s.t.\begin{cases}
\sum_i v_ix_i &\leq 1\\
v_i&\geq 0\\
x_i&\in\{0,1\}
\end{cases}$$

> **Bang-for-buck**
> $$(sp_i-\frac{c_rf_i}{v_i})/v_i$$

$p_i$: number of picks
$x_i$: whether or not to store SKU_i

<center><img src="/images/2022-11/Snipaste_2022-11-07_22-44-29.png" width="70%"></center>

<span style="background-color: yellow; color: black;">**Knapsack**: $v_i,x_i$ are all decision variables, which make the first constraint hard to consider</span>

### 2.2 Determine $v_i$
To solve the knapsack above, we need to determine(fix) $v_i$. There are three possible ways including EQS, EQT and OPT, here we choose OPT:

$$\max \sum_i(sp_i-c_r\frac{f_i}{\frac{\sqrt{f_i}}{\sum\sqrt{f_i}}})x_i$$


<span style="background-color: yellow; color: black;">Sorting by $\frac{p_i}{\sqrt{f_i}}$ is equivalent	to	sorting	by	bang-for-buck =</span> (这里式子很复杂，就是把 OPT 的 $v_i$ 带入 bang-for-buck 的公式中去)





# Guest Lecture: FORTNA
**DC Design Methodology with a Focus of Picking Activity**

Measure of Success
improve our design
- quality and repeatability
- ability to scale the organization

improve our client's ability to operate

Knowledge:

SKills:
- How to compare one picking methodology to another in terms of laber contnet
- 

## Picking Methodologies
Three main steps of Design Methodology
- **Inputs**: Design, Requirements
- **Construction**: Picking, Methodology Selection and Feasibility
- **Improvement**: Technology & Refinement Optimization

Picking Methodologies:
- Cluster Picking (Discrete Orders)
  picking one or multiple orders at a time directly to individual orders
  does not require an extra-touch process to created the order
- Batch Picking
  picking multiple SKUs at a time without regrad to order integrity
  requires an extra-touch process coordinated over multiple areas to create the order
  优点: larger picking density, higher productivity

Extra-Touch Methodologies
- Manual
- Automated Sortation w/no buffer (Unit Sorter)
- Automated Sortation with buffer (Pocket/Pouch Sorter) (可以减少储存后再出去的麻烦)

How to compare?
|Cluster Picking| Batch Picking
|-|-|
|Cluster pick cart| Batch pick cart
|Units per hour(UPH) 60 units/ 0.75 hr = 80 UPH| 40 units/ 0.4 hr = 100 UPH
|No extra-touch| Manual put wall @ 200 UPH

Blended UPH = (1/UPH_P + 1/UPH_ET)^(-1)
Cluster Picking is better because $1/80 > (1/100+1/200)$

Solution Design
- Tri-delima: Cycle Time, Equipment & Systems, Productivity
- 

## Picking Technologies (Goods to Person)
### Autonomous Mobile Robotics with Movable Racks
**Pros**: 
- Flexibility in storage of product
- Ease of deployment
- Reduce walking time
- Smaller warehouse size (save space)

**Cons**:
- Utilization of cubic space
- No ergonomic enhancements to picking

### Aisle-Based Shuttle Systems
**Pros**:
- Vertical Utilization
- High throughout possible
- Ergonomic picking
- Produt can be stored in totes, cases or cases on trays

**Cons**:
- High capital, especially conveyor loop to network aisles to workstations
- Cannot scale storage and throughput independently

### Rack-Based Storage with Robots
**Pros**:
- ergonomic
- can scale storage and throughput independently
- eliminate need for a conveyor loop
- product can be stored in totes or cases on trays

**Cons**:
- aisles for AMR travel decrease storage density

### Top-Loading Bins with Robots
**Pros**:
- highest cubic density of any GTP
- ergonomic
- can scale storage and throughput independently
- is often the lowest-cost solution

**Cons**:
- product must be stored in totes
- floors must be very flat
- workstations cannot achieve rate of some other GTPs
- digging buried bins increases the number of required robots
- well-publicized fire has...


  

