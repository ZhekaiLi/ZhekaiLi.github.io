

## Basic Definitions

```mermaid
graph LR
A(Raw wafer)
B(Build IC)
C(Probe)
D(Assembly: diced into dies)
E(Package)
F(Final test)

A-->B-->C-->D-->E-->F
```

Wafer fab > work areas > work centers (a set of machines that provide similar processing capabilities) > machines (or tools, can have a buffer to store lots)

Lots: moving entities in wafer fabs (obtained from order)
- Often, several lots will be created to fulfill an order

Tools (machines):
- Single wafer tools: process only a single wafer at a time
- Tools with overlapping process: process lots in an overlapping manner
- Batch processing tools:
    - **batch**: a set of lots that processed at the same time on a single tool
- Cluster tools: 具有不同类型工艺步骤的晶圆可以同时在一个集群工具上循环，也就是说，集群工具可以被看作是一个完全自动化的机器环境。一个集群工具是一个单一的设备，它聚集了几个工艺步骤以及运输和计量

Steps: 沉积 > 光刻 > 显影 > 蚀刻 > 重复
1. **Oxidataion**/**Diffusion**: A layer of material is grown or deposited on the surface of a cleaned wafer. The goal of an oxidation step is to grow a dioxide layer on a single wafer, while diffusion aims at dispersing material on the wafer surface. Diffusion furnaces and rapid thermal equipment are used in the oxidation/diffusion work area. The furnaces are batch processing tools.
2. **Film deposition** (薄膜沉积): Films (dielectric or metal layer) are deposited onto wafers. Deposition can be executed by processes such as physical vapor deposition (PVD) or chemical vapor deposition (CVD).
   在晶圆表面沉积一层 SiO2, SiN 等绝缘介质薄膜和 Al, Cu 等金属导电膜
3. **Photolithography**: 光刻，最重要的步骤
    - 涂抹光刻胶
    - 曝光: 紫外线照射掩膜，穿过透镜设在光刻胶上（被紫外线照射后的光刻胶变得可溶）
4. **Cleaning/Inspection/Measurement**
    - 显影: 使用显影液冲洗可溶的光刻胶
    - 干燥 (evaporation)
5. **Etch**: A wafer is partially covered by photoresist strip after photolithography. Material is removed from the areas of the wafer surface that are not covered by the etching step.
   蚀刻: 把没有光刻胶覆盖的区域的氧化膜(和下方的硅一起)刻掉，形成一个突起的结构，也就是鳍式场效应晶体管的 "鳍" (见下图)
6. **Ion implantation** 离子注入: Doping material is deposited where parts of the wafer have been etched.
7. **Planarization** 平坦化, 类似于抛光: The wafer surface is cleaned and leveled by the planarization step.


<center><img src="/images/2023-05/Snipaste_2023-05-16_13-23-32.png" width="40%"></center>

<center><img src="/images/2023-05/Snipaste_2023-05-16_13-46-19.png" width="90%"></center>

# Building Blocks for a Simulation Model of a Wafer Fab
## Overview
we have to represent in a fab simulation model the following ingredients: 
- resources: equipment, secondary resources, and operators 
- products, technologies and process flows 
- orders, lots, and batches. 

Closely related to the resources are elements of the **control system** (dispatching and batching rules).
- Dispatching rules determine which lot will be processed next at an available tool.
- Batching rules that decide which lots form a batch and which   batch will be processed next are also part of the control system. Batching rules can be considered as extension of dispatching   rules. We refer to (Sarin et al. 2011 and Mönch et al. 2013) for a more detailed discussion of dispatching and batching rules in   semiconductor manufacturing.

## Resource Modeling
The following tool-related information is generally used:
- name of the work center 
- number of tools in the work center 
- name of an individual tool 
- batch-size information 
- batch formation criterion 
- setup time information
- tool qualification and dedication requirements 
- information on preventive maintenance (PM) cycle(s) 
- information on breakdown-repair cycle(s) 
- information related to the dispatching rule used at the tools of the work center. 

More than one lot can be processed on a batch processing tool. The maximum number of lots that can be processed in a single   batch has to be specified. A given minimum number of lots is required in many wafer fabs. This quantity is called minimum   batch size and has to be specified in a simulation model. The batch formation criterion is used to represent the information   which lots can be used to form a batch. Often only lots that refer to the same process step can be batched together.

The setup time is necessary to set up a tool before processing. The setup time can be independent from the current setup   state. In this situation, we have a constant setup time that appears whenever a new process step has to be performed on the tool.   When the setup time depends on the current setup state, sequence-dependent setup times have to be modeled. This requires a   setup matrix.

Since semiconductor equipment is complex, it is important that the equipment is running in an appropriate way.   Therefore, PM activities can be found in most fab simulation models. Weekly, monthly, quarterly, and yearly PM schedules   are possible. Many simulation tools use calendars for modeling PM activities.

Since semiconductor equipment is complex, it is important that the equipment is running in an appropriate way.   Therefore, PM activities can be found in most fab simulation models. Weekly, monthly, quarterly, and yearly PM schedules   are possible. Many simulation tools use calendars for modeling PM activities.

## Product Representation
**A process flow** is represented by a list that contains information for all **process step**s that are required to produce a specific product, also might contain alternative subprocess flows or rework loops. 

The information needed to represent a single process step includes:
- name of the process step 
- name of the tool group where the process step has to be performed 
- $t_{ps}$: processing time given either as a deterministic value or by a probability distribution and information as to whether the processing time refers to the entire lot or a single wafer 
- load and unload time 
- required setup state of the machine when the process step is carried out 
- amount of scrapped material (报废材料)
- required secondary resources 
- operator requirements including skills, availability requirements, quantity of required workers 
- rework loops 
- alternative flows


## Modeling of Working Objects
Lots are the moving entities in wafer fabs:
- name of the lot 
- number of wafers (might influence the processing time of the lot)
- product type (specify which process flow will be used)
- start time 
- due date 
- weight (priority)

In contrast to lots, batches are created only temporary in front of batch processing tools






## Reduced Simulation Models
Simulation studies with full fab models tend to be <u>time-consuming</u> (too much details is modeled). The reduction is carried out by **modeling only process steps on bottleneck machines in detail**. 

The process steps that are not related to bottleneck machines are replaced by fixed time delays: (It's challanging to calculate an appropriate delay, which could be based on historical data, or accurated by the complete simulation)

<center><img src="/images/2023-05/Snipaste_2023-05-16_14-19-05.png" width="80%"></center>



**Route Group**: HBT

**Route Family**: N_6HBT8
- **Route**/ **Flow_type**: N_6HBT8-M3-MC+N_6CUTE-M3-NOSTREET+N_6P07_TWV-ETC+N_6FPOUTS-NS>N_PC
Have a process list (stages)
    - **Stage**
    several process families could be assigned to one stage
        - ==**Process Family**/ **EQPTYPE**/ **Tool_type**==
        a process family could contain several different process steps
        <img src="/images/2023-05/Snipaste_2023-05-17_10-04-01.png" width="100%">
            - **Tool_id**
## Objective

$$\min \sum_l W_lL_l$$

- $W_l$         : Weight (pri) of lot $l$
- $L_l=\max(0,d_l-C_l)=$ Lateness of lot $l$ 
	- $C_{l}=$ Completion time
	- $d_l=$ due date
- $d_{l}$       : Due date of lot $l$   


## Parameters

    
- $p_{(l,sl),i}$: Process time of $(l,sl)$ on family $i$
- $sl\in \{1,2,...,Sl\}$: one step of lot $l$
    - $Sl$: the final step of lot $l$
    - for example, $S3=5$ means that there are $5$ steps total to finish lot $l=3$, and therefore $s3\in\{1,2,...,5\}$

## Decision variables
IFF the step $sl$ of the lot $l$ is assigned to be processed at family $i$:
- $a_{(l,sl),i}=1$, otherwise zero

IFF $(l,sl)$ is firstly processed at family $i$ machine $j$
- $w_{(l,sl),i,j} = 1$, otherwise zero

IFF $(sl',l')$ just precedes $(l,sl)$:
- $x_{(l',sl'),(l,sl),i} = 1$, otherwise zero

Time:
- Start time: $t_{(l,sl)}$
- Completion time: $C_{l}$
- $L_{l} \geq \max(0,C_l-d_l)$

## Constraints
1. Each $(l,sl)$ can be only assigned to one family type

$$\sum_i a_{(l,sl),i} = 1\;\;\;\;\forall (l,sl)$$

2. Each $(l,sl)$ must be ==proceded== by one process step or be the first, 
at the family it assigned to

$$\sum_{i,j}w_{(l,sl),i,j} + \sum_{(l',sl')\neq (l,sl)}x_{(l',sl'),(l,sl),i} = a_{(l,sl),i}\;\;\;\;\forall (l,sl),i$$

3. Each $(l',sl')$ must be ==succeeded== by at most one process step (zero when as the tail), 
at the family it assigned to

$$\sum_{(l,sl)\neq (l',sl')} x_{(l',sl'),(l,sl),i} \leq a_{(l',sl'),i}\;\;\;\;\forall (l',sl'),i$$

4. Atmost one $(l,sl)$ can be the first at family $i$, machine $j$
$$\sum_{(l,sl)}w_{(l,sl),i,j}\leq 1\;\;\;\;\forall (i,j)$$

5. Time constraints:
    - relation between any two steps
    - relation between two consective steps of one lot
    - completion time

$$\begin{aligned}
t_{(l',sl')} + \sum_i p_{(l',sl'),i}x_{(l',sl'),(l,sl),i} + M(\sum_i x_{(l',sl'),(l,sl),i}-1) &\leq t_{(l,sl)}\\
t_{(l,sl)} + \sum_{(l',sl'),i}p_{(l,sl),i}x_{(l',sl'),(l,sl),i} + \sum_{i,j}p_{(l,sl),i}w_{(l,sl),i,j} &\leq t_{(l,sl+1)}\\
t_{(l,Sl)} + \sum_{(l',sl'),i}p_{(l,Sl),i}x_{(l',sl'),(l,Sl),i} + \sum_{i,j}p_{(l,Sl),i}w_{(l,Sl),i,j} &\leq C_l
\end{aligned}$$
