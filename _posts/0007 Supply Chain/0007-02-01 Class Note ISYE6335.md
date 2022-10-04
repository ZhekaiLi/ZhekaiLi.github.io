---
layout: post
title: ISYE6335 Class Notes
categories: Supply-Chain
description:
keywords: SCE, Supply-Chain
mathjax: true
topmost: true
---

# L1: Intro to Warehousing

**Lead Time**:
The time from the moment the customer places an order (the moment the supplier learns of the requirement) to the moment it is ready for delivery.

**DC** (distribution center)

## 1.1 Types of warehouse
**Retail**
- Walmart, Target...
- Huge flow of products inbound and outbound
- Able to batch processes (批量处理)

**Service Parts**
- Spare parts for machinery and capital equipment (e.g. 储存飞机零部件的仓库)
- Demand highly unpredictable + long lead time(e.g. 飞机零部件生产时间长) $\implies$ high levels of safety stock
- Able to batch processes
- Need for predictive analytics

**E-commerce**
- very small orders
- high service level expectations
- demand can be spiky but shapable
- smart execution algorithms and optimization help

**3PL** (third party logistics)
- Multiple customers
- Economies of scale
- Subject to contractual constraints

**Perishables**
- Different temp(to store food, flower...)
- Expiration issues - IFFO
- Handling restriction





## 1.2 What is the Warehouse Objectve?
- Max space utlization
- Min labor time (max labor efficiency)

**A systematic way to think about warehouses**
- Inventory characteristics (\# products, size, turn rates)
- Throughput and service requirements (\# lines picked and orders shipped per day)
- Footprint of builidng & cost of equipment
- Cost of labor

# L2: Material Flow, Space, Time

$\Big[$ Receiving $\implies$ Put-away $\Big] \implies$ Inventory $\implies\Big($ Picking $\implies$ Packing $\implies$ Shipping$\Big)$

$[$Inbound$]$: 
- Receiving: about 10% operating costs
- Staging then putaway: 15%

$($OutBound$)$:
- Picking: accounts 55% of the operational warehousing cost
- Shipping: accounts 55% of the order-picking time 


<center>
    <img src="/images/2022-10/Snipaste_2022-10-01_10-24-37.png" width="70%"> <br>
    <div style="color: #808080;">Paths of material flow through a warehouse</div>
</center><br>

<font color="blue">**Key principles: Keep product moving**</font>

Warehouse Objective
- The goal is to move items fast and on the cheap
- Operational obstacles: labor availability, variability, and low visibility
- Accuracy and Qaulity
- Ergonomics
- Flexibility
- Safety

```mermaid
graph LR
A(Space)
B(Time)

A---B
```

## 2.1 Picking terms and considerations
**Order vs. Line vs. Unit** (订单, 生产线, 产品)
- Line: different products within order (SKU)
- Unit: the quantity of each line
- What we care: $avg($line/order, units/line, units/order$)$

<center><img src="/images/2022-10/Snipaste_2022-10-02_18-13-04.png" width="60%"></center>

|Term|Definition|
|-|-
|**SKU**| Stock Keeping Unit
|**Tote**| A container in picking car (手提袋, )
|**Pick List**| A document sent to your warehouse pickers to fulfill a customer order
|**Pick Face**| The pick face is that 2-dimensional surface, the front of storage, from which SKUs are extracted. This is how the skus are presented to the order picker. In general, the more different skus presented per area of the pick face, the less travel required per pick
|**Pick Density**| Depends on how I sort the picks. 订单的实现密度，如果很多订单都能从一个区域pick$\implies$高 pick density
|**Single-line Orders**| \# orders form single line (one SKU). It is almost always better to <span style="background-color: yellow; color: black;">batch</span> single-line orders because no sortation is required.
|**Multi-line Orders**| More complicate than above. Consolidation cost: if lines are sparse $\implies$ more item, more labor (need trade-off!)
|**Picking Productivity**| Efficiency (lines/hr, SKU/hr, Orders/hr lph uph oph)
|**Order Integrity**| Order integrity begins with receiving where each inbound delivery is checked for shelf-life, routing information, quantities and product temperature(when required). e.g. cluster and decrete picking maintain integrity
|**Pick Wave**| release to be picked in wave (set of order release together)


## 2.2 Batch, Cluster, Discrete, Zone Picking
|Picking|Definition|
|-|-
|**Batch Picking**| aka multi-order picking, (<u>pick multiple orders a time in the same container</u>) **Serial Process**: multiple orders but similar SKU in a tote, therefore needs <span style="background-color: yellow; color: black;">sort & consolidation</span> into individual orders later
|**Cluster Picking**| (<u>pick multiple orders a time in same cart, diff container without mixing</u>) **Parallel Process**: pick multiple orders individuallly but in parallel
|**Discrete Picking**| pick one order a time (pick seperately)
|**Zone Picking**| assign loc to workers, then consolidate together


> **Two Primary Types of Zone Picking**
<img src="/images/2022-08/Snipaste_2022-08-29_10-11-14.png" width="100%">

Serial Zone
- Pro: accuracy, integrity
- need more time, low efficiency

## 2.3 (Little's Law) Estimate product velocity
<center><img src="/images/2022-08/Snipaste_2022-08-29_10-36-37.png" width="80%"></center>

**Little’s Law**, in steady state:
Avg(inventory) = Rate of arrival * Avg(time) in system
$$L=\lambda W$$

$W$: avg time in system (wating time, processing time)
$L$: inventory level (storage) of warehouse
$\lambda$: rate of arraival

e.g. 货物到达的频率是 50 pallets/wk, 仓库容量为 5 pallets, then W = 0.1wk

Other Definitions:
- **Inventory turnover rate**(per year): 
  = (yearly sold) / (inventory level)
  = 1 / (wating time $W$)


## 2.4 Dedicated vs. Shared Story
**Dedicated**: slot only for one SKU
- Simple, efficient
- BUT space utilization suffers 

<center><img src="/images/2022-10/Snipaste_2022-10-01_12-02-39.png" width="50%"></center>

max inventory level = 2 * avg inventory level

**Shared**: if any free space, then share different SKUs. 例如下图在 week 3 的时候，shared storage 就会空出一格给其他的 SKU
- Space is recycled sooner than dedicated storage
- BUT needs Warehouse Management System (WMS)
More prone to errors
Requires discipline from workers

<center><img src="/images/2022-10/Snipaste_2022-10-01_12-04-36.png" width="50%"></center>

Avg Inventory Utilization 随着 k 变大而变大

<center><img src="/images/2022-10/Snipaste_2022-10-01_12-08-43.png" width="60%"></center>



<!---------------------------------------------->



# L3: Warehouse activity profiling
## 3.1 Typical types of data
- **Order History**: what was ordered, who ordered, how much, when it ordered($t_o$), picked($t_p$) or shipped($t_s$)
-  **SKUs**: description, product family, unit of measure, wolume, weight, location, data introduced(data arrived to warehouse)
- **Layout**: CAD drawings, locations, dimensions
- **Processes**: warehouse operations, labor, shifts

<center><img src="/images/2022-10/Snipaste_2022-10-01_12-12-15.png" width="100%"></center>

## 3.2 Why do we need warehouse profiling?
Understand the orders (Demand)
- size, frequency, seasonality, varaibility

Userstand the **constraints**
- physical, labor, service agreements

Understand the SKUs
- physical, seanonality, variability

### Step 1: Validate with summary numbers and averages
- Number of locations of each type: pallets, bins, bays, etcs.
- Activity summaries: daily orders, lines, units
- Most popular SKUs by: volume, picks, weight, size

Different statistics provide different perspectives
- Frequency and size of inbound shipment $\to$ unloading and putaway labor
- Number of cartons(cases) moved $\to$ restocking labor
- Number of lines/order $\to$ batching opportunities

### Step 2: Understand the work content
- Work is associated with flow
- Work depends on unit of flow: pallet vs. case vs. each
- Where is the work?
- How much does each SKU contribute to the work?

## 3.3 Order Profiles
**Pareto curves of SKU profiles**: 20% of SKUs account for 75% of picks
<center><img src="/images/2022-10/Snipaste_2022-10-01_12-19-12.png" width="60%"></center>


**Order profiles**: (各种对信息提取有帮助的可视化方法)
- Lines/order
- Order vs. picking distribution: 为啥 30% < 60%? 因为一个 Batch Picking 可以包含多个 single-sku 和 multi-sku orders
- Daily variation in order volume: 帮助判断 when to assign more labor
- Affinity between SKUs or product families (亲和力高的放在一起)

<table><tr>
<td><img src="/images/2022-10/Snipaste_2022-10-01_12-22-46.png" border=0>    <center><div style="color: #808080;">lines/order</div></td>
<td><img src="/images/2022-10/Snipaste_2022-10-01_12-25-06.png" border=0>
<center><div style="color: #808080;">order vs. picking distribution</div></td>
</tr></table>







# L4: Layout of a unit-load warehouse
**Outline**:
- Configuration decisions: Floor or rack; Lane depth
- Storage decisions: Where to store each pallet; Aisle arrangement

<center>
    <img src="/images/2022-10/Snipaste_2022-10-01_15-27-43.png" width="70%"> <br>
    <div style="color: #808080;">Paths of material flow through a unit-load warehouse(蓝色色块和线条)</div>
</center><br>


**Space vs. Time**
- Optimize space: 
metric: max pallets/sq area
- Optimize time:
min labor hours to store and retrieve

## 4.1 Space
Stacked vs Racked(架子):
- racking makes empty pallet positions more quickly available

<center><img src="/images/2022-10/Snipaste_2022-10-01_15-31-29.png" width="70%"></center>

### 4.1.1 Unoccupied and unavailable space
Assume one pallet in each location; and one pallet demand per day. 下图中:
- 红色过道区域永远 unoccupied & unavailable (u&u)
- 最外面的一格只有三分之一时间被占用
- 中间格只有三分之二时间被占用
- 最里面的一格一只被占用
<center><img src="/images/2022-10/Snipaste_2022-10-01_15-36-32.png" width="70%"></center>

上图中的 lane depth = 3. So what's the space-efficient lane depth?

### 4.1.2 Space-efficient lane depth
Denotations:
- $k$: lane depth
- $D_i$: annual demand(pallets) for SKU_i
  &emsp;&emsp; $1/D_i$ is the time(years) to clear one pallet of SKU_i
- $q_i$: \# pallet positions for SKU_i
  &emsp;&emsp; $q_i/D_i$ is the time between inbound shipments to storage(所有存货能卖多久)
- $z_i$: height of the staked pallet for SKU_i
  &emsp;&emsp; $z_i/D_i$ 一个 floor position 放的存货能卖多久
  &emsp;&emsp; $\lceil q_i/z_i\rceil$ is \# floor positions required

> (1) How much space is wasted for **<font color=blue>each line</font>**?

$$w_i=\frac{k(k-1)}{2}\frac{z_i}{D_i}$$

<center><img src="/images/2022-10/Snipaste_2022-10-01_15-56-40.png" width="100%"></center>

> (2) How much space is wasted for **<font color=blue>all linese</font>**?

Denote $\lceil q_i/(z_ik)\rceil$ as the \# required lanes for depth k, then:
$$W_i=\lceil \frac{q_i}{z_ik}\rceil w_i\approx \frac{k-1}{2}\frac{q_i}{D_i}$$

> (3) How much **<font color=blue>aisle spacee</font>** is wasted to access the lanes?

$$W_i^A=\frac{a}{2}\frac{(\frac{q_i}{z_ik}+1)}{2}\frac{q_i}{D_i}$$

<span style="background-color: yellow; color: black;">where $a=$ (ailse's real depth) / (depth of each pallet positions)</span>

> (4) Fiannly, **<font color=blue>Optimize lane depth</font>** for SKU_i

求导 $\frac{d}{dk}(W_i+W_i^A)=0$:
$$\boxed{k^*=\sqrt{(\frac{a}{2})(\frac{q_i}{z_i})}}$$

for all SKUs
$$\sqrt{(\frac{a}{2})(\frac{1}{n}\sum_{i=1}^{n}\frac{q_i}{z_i})}$$



## 4.2 Time
<center><img src="/images/2022-10/Snipaste_2022-10-01_16-52-05.png" width="80%"></center>

**Single-cycle protocol**(上图): 为最简单的存货/取货方式，即每个 Storage, Retrieval 均与 Receiving+Shipping location 产生了一个往返，因此存在大量的 Empty Trip。

解决方式: **Dual-cycle protocol**(下图), Receiving$\to$Storage$\to$Retrieval$\to$Shipping

<center><img src="/images/2022-10/Snipaste_2022-10-01_16-56-10.png" width="80%"></center>

Minimize distance between each pair of storage and retrival location:

$$\min\sum_{i,j}d_{ij}x_{ij}$$

$d_{ij}$: Distance from location i to location j
$x_{ij}=\{0,1\}$: 1 if the forklift is traveling from storage location i to retrieval location j and 0 otherwise
- $\sum_i x_{ij}=1$ for all storage locations i
- $\sum_j x_{ij}=1$ for all retrieval locations j

## 4.3 Where to store SKUs?
**Principle: Fastest movers go into most convenient location**

**Little's Laws**: (回顾)
\# units on hand(inventory) = rate of arrival * avg time spent in location

而 avg time 越短意味着 return rate(turnover rate) 越高，因此 <span style="background-color: yellow; color: black;">low avg time SKU should be assigned to convenienct location is a FIFO warehouse</span> (**First-IN-First-Out assumption** 非常重要，如果货物是后进先出，那么应该 assign high arrival rate SKU to convenince)



<!-------------------------------------------->



# L5: Layout of carton-picking from pallets
**Forward Picking Area**: (下图红色部分) 一般指的是第一层(可以直接拿货，高层则需 forklift) e.g. 宜家的 rack storage 的第一层放着可以供顾客直接拿的东西

<center><img src="/images/2022-10/Snipaste_2022-10-01_18-14-08.png" width="80%"></center>

## 5.1 How much forward space should be assigned to each SKU?
(1) Should a SKU go into the forward pick area?
(2) How many locations in the forward pick area should the SKU get?

Tradeoffs:
- picking efficiency: faster to pick from forward area than bulk storage area
- restocking cost: replenishing the forward area from bulk storage

<center><img src="/images/2022-10/Snipaste_2022-10-01_18-27-07.png" width="80%"></center>

**Decision Varaibles:**
- $x_i\in\{0,1\}$  if there is space in forward area for SKU_i

**Obj: Max benifit to store SKUs in fast pick area**
$$\max \sum_i(sp_i-c_rd_i)x_i$$

- $s$: forward pick saving for each carton pick
- $p_i$: \# carton picks
- $d_i$: \# carton demand <u>in pallets</u> moved to replenish
- $c_r$: cost of restoring a pallet (不包含 unwraping 之类的费用)

**Constraints:**
$$\sum l_ix_i\leq N$$

- $l_i$: minimum locations needed for SKU_i in picking area (一般情况等于 safety stock + 1 (in pallets))
- $N$: \# available pallet locations

Similarly, define **net benefit**(benefit per location) for SKU_i
$$B_i=\frac{sp_i-c_rd_i}{l_i}$$

net benefit less than zero means:
$$\frac{p_i}{d_i}<\frac{c_r}{s}$$

这样就提取出一个不依赖 SKU_i 的常数 $c_r/s$，方便将其与每个 SKU 的 $p_i/d_i$ 直接比较

## 5.2 Alternative: Storing all in forward area

$u_i$ upper bound on inventory of the SKU_i
$D_i$ full pallet picks for SKU_i 

例如对于 SKU_A
order 1: 1.5 pallets
order 2: 2 pallets
order 3: 0.5 pallet

p_i = 2 = 1 + 1 (order_1 的 0.5 pallet 是从 forward area 拿的，算一次 carton pick. 同理对于 order_3)
D_i = 3 (order_1 拿了一个, order_2 拿了两个)
d_1 = 1 (给 order_1 的 forward 补 0.5个，给 order_3 的 forward 补 0.5个)

Net benefit of fully stocking in forward area

$$B_{i,full}=\frac{s(p_i+D_i)}{u_i}$$

So if $B_{i,full}>B_i$, all should be stocked in forward areas


