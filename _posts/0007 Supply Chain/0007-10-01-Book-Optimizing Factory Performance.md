---
layout: post
title: Book - Optimizing Factory Performance
categories: Supply-Chain
description:
keywords: SCE, Supply-Chain
mathjax: true
---

<center>

# Optimizing Factory Performance

</center>









Three primary enemies of factory (or supply chain or organizational):
- Complexity
- Variability
- Lackluster leadership



# C3: Terminology, Notation, and Definitions
## 3.1 Factory: Definition and Purpose

A factory is a **processing network** through which jobs and information flow and within which events take place.

From a more scientific perspective, an alternate and more revealing definition of a factory may be developed, specifically:
- A factory is a **nonlinear, dynamic, stochastic system with feedback**.

### (1) Job process
**Job process steps** (a.k.a. operations) include
- *<font color='blue'>Assembly or transformation</font>*: an activity resulting in or directly supporting a physical and measurable change to the job
- *<font color='blue'>Transit</font>* of the job from one machine to the next
- *<font color='blue'>Inspection</font>* of the job

### (2) Workstation events
Concurrent with the flow of jobs through a factory are **events that occur within the factory’s workstations**. These events serve to <u>reduce the availability</u> of the machines that form the workstation and, subsequently, the overall availability of the workstation itself. The degradation imposed by such events on the workstation—and the factory—in turn, will have an impact on factory performance. (例如机器的维护和检查)

**Workstation events** are:
- Maintenance of a machine
- Repair of a machine
- Inspection of a machine
- Qualification of a machine
- Setup of a machine

For example, a maintenance event may occur according to a schedule (e.g., perform a maintenance event every week), or according to usage (e.g., perform a maintenance event on the completion of every 500 jobs)


## 3.2 Factory Process-Flow Models
Every factory (or supply chain or business process) supports a process flow. There are several ways to represent this flow, for example:
- **Workstation-centric model**:
a workstation consists of one or more machines that support *identical or nearly identical* processing functions
- **Process-step-centric model**:
an operation conducted *within a workstation* (and, quite possibly, by means of the support of only a subset of the machines in the workstation) or is a *transit step between workstations*.

### 3.2.1 Workstation-centric Model and Reentrancy

The following picture depicts a simple factory consisting of:
- 3 **work stations** (A, B, and C) (包括 transit operations)
- 7 **machines** (A1, A2, ...)
- 5 **operations** (arrows 1, 2, ...) (这里的箭头表示的不是 intralogistics)

<center><img src="/images/2023-03/Snipaste_2023-04-04_10-51-58.png"  width="70%"><br>
    <div>Figure 3.1</div></center>

> **Def: Degree of Reentrancy (DoR)**
> $$\text{DoR}=\frac{\text{\# operations}}{\text{\# work stations}}=\frac{5}{3}$$

DoR differs a lot for different types of factory:
- **automobile assembly** lines have little, if any, reentrancy (<u>the ideal assembly line has none</u>)
- **semiconductor wafer** fabrication facilities, or “fabs”, typically have factory DoR values ranging from 3 to 5 or even more—with individual nests that may have DoRs in the double digits.

We next consider two other, more traditional (in that they *do not include reentrancy*) workstation-centric models:

**<font color='blue'>(1) Flowshop factory</font>**

<center><img src="/images/2023-03/Snipaste_2023-04-04_11-14-53.png"  width="80%"><br>
    <div style="color: #808080;">Figure 3.2</div></center>

- Each job follows precisely the same pathway
- Each workstation supports just one process step
- **No passing of jobs**: if two jobs enter the factory in, say, the job sequence J1 and J2 they must enter and leave each workstation in that same sequence

**<font color='blue'>(2) Jobshop factory</font>**

<center><img src="/images/2023-03/Snipaste_2023-04-04_11-18-56.png"  width="80%">
<br>
    <div style="color: #808080;">Figure 3.3</div></center>

- Each job that enters the factory may follow a different process flow path (J1 vs. J2)

### 3.2.2 Process-step-centric Model
According to *Figure 3.1*, if we know which machines are capable of supporting (e.g., qualified to conduct or be assigned to) each process step, we can convert that workstation-centric model into a process-step-centric model:

<center><img src="/images/2023-03/Snipaste_2023-04-04_11-34-59.png"  width="80%"></center>

Why this model is also important:
- it indicates not only the process step flow but also <u>the precise support responsibilities of each machine</u> in the factory.


## 3.3 Factory Definitions and Terminology

**Factory Types**
- Flowshops
- Jobshops
- Factories without reentrancy (i.e., DoR = 1)
- Factories with reentrancy (i.e., DoR > 1)
- Synchronous factories (e.g., every job flows through the factory at the same constant speed, such as bottles in a beverage bottling plant)
- Asynchronous factories (e.g., each job—as in semi-conductor fabrication—may flow through the factory at different speeds and in addition may remain temporarily held in a queue)
- High-mix factories (e.g., those that process numerous job types)
- Low-mix factories (e.g., those that process only a limited number of job types)
- Low-volume factories (e.g., those that process only a relatively limited number of jobs per time period, such as aircraft manufacturers or research and development factories that produce only prototypes of a product)
- High-volume factories (e.g., those that process a large number of jobs per time period, such as high-volume semiconductor wafer fabrication facilities)
- High-mix, low-volume factories
- High-mix, high-volume factories
- Low-mix, low-volume factories
- Low-mix, high-volume factories
- Factories involving various combinations of the preceding features

## 3.4 Jobs and Events

<center>

#### Job Types
</center>

Jobs may require either assembly, transformation, the combination. Furthermore, a job may flow through the factory as a <u>single unit</u> (e.g., as an automobile), as a <u>lot</u> (e.g., as a “container” consisting of a number of silicon wafers), or as a <u>batch</u> (e.g., a group of either individual jobs or lots).

Two primary types of **batches**:
- *parallel batch*: batch 中的 jobs 会被同时处理 (same process time). Batch 的目的在于 reduce setup time (each batch undergoes just one setup in front of the batching machine). 例如, 陶瓷烧制机器允许同时烧制多个陶瓷坯
- *series batching* or *cascading*: batch 中的 jobs 会被顺序处理. 同样能够 reduce setup time because each cascade undergoes just one setup prior to entry into the cascading machine or workstation.


<center>

#### Job States
</center>

**<font color=blue>Value-added processing</font>**:
an actual assembly or transformation operation

**<font color=blue>Non-value-added processing</font>**:
- Rework
- Transit
- Inspection/test
- Waiting, including
    - Waiting as an individual job for processing at a nonbatching/noncascading process step
    - Waiting for a batch (or cascade) to form in front of a batching/cascading process step
    - Waiting in a batch (or cascade) as part of the queue formed in front of a batching/cascading process step
    - Waiting in a “set aside” state (e.g., the job is removed temporarily from the production line)

<center><img src="/images/2023-03/Snipaste_2023-04-17_16-12-09.png"  width="100%"></center>

如图所有，在很多真实工厂中, non-value-added processing 的时间占了相当大的一部分

<center>

#### Event Types
</center>

Events are activities that are <u>conducted within a workstation rather than on a job</u>

**<font color=blue>Preemptive Events</font>**:
occurs during the processing of a given job (or batch). The processing of the job must stop and cannot proceed until recovery from the preemptive event:
- Unscheduled downs
- Power outages or voltage/current spikes
- Unanticipated supply outages and replenishment

**<font color=blue>Nonpreemptive Events</font>**:
one that occurs (or can be scheduled to occur) during a period in which the machine is not processing a job:
- Scheduled maintenance
- Unscheduled downs (i.e., those that happen to not occur
during processing)
- Inspections and engineering tests
- Qualifications
- Setups
- Scheduled operator breaks (e.g., biobreaks or meetings)

## 3.5 Workstations, Machines, and Process Steps

<center>

#### Workstations
</center>

A given workstation consists of one or more machines, each dedicated to an identical or nearly identical processing function.

<center>

#### Process Steps
</center>

The key attributes of **<font color=blue>capacity</font>** and **<font color=blue>cycle time</font>** are determined by the support provided to each individual process step rather than each functional area. 

$$\text{CT}_f = \sum_{ps=1}^P \text{CT}_{ps}$$

- $\text{CT}_f$: cycle time of the entire factory
- $\text{CT}_{ps}$: cycle time of process step $ps$
- $P$: total number of process steps in the factory

The **<font color=blue>capacity</font>** of a factory is determined by the bottleneck (i.e., constraint or choke point) process step, not necessarily a bottleneck workstation

## 3.6 Performance Measures

<center>

### Notation
</center>

Define the performance measure for an entity as the following format:

$$\text{Measure}_{\text{entity}}\text{(specific entiry designation)}$$

For example:
- $\text{CT}_{ps}(9)$ cycle time of process step number 9
- $\text{PR}_{m}(B3)$ process rate of machine 3 in workstation B (B3)

**<font color=blue>entity</font>**

$$\begin{aligned}
ps &= \text{process step, where }ps=1,...,P\\
m  &= \text{machines, where }m=1,...,M\\
ws &= \text{workstations, where }ws=1,...,W\\
f  &= \text{factory}
\end{aligned}$$

<center>

### Process-Step Performance
</center>

- $\text{TH}_{ps}$ (jobs/ time): Process-step <u>average throughput rate</u>
- $\text{SC}_{ps}$ (jobs/ time): Process-step <u>maximum sustainable (可持续的) capacity</u>
- $\text{EPR}_{ps}$: Process-step <u>maximum theoretical capacity</u>
    the capacity of the machines supporting that step in the *absence of any variability*. (*upper bound* of the process-step capacity)
- $\text{CT}_{ps}$: Process-step <u>cycle time</u>
    the elapsed time between the arrival of the job at the queue (if one exists) in front of the process step and its departure on completion of the operation
- $\text{AR}_{ps}$ (jobs/ time): <u>Arrival rate</u> at the process step
- $\text{DR}_{ps}$: <u>Departure rate</u> from the process step


**$\text{SC}$ (max sustainable capacity) vs. $\text{EPR}$ (max theoretical capacity)** 
<center><img src="/images/2023-03/Snipaste_2023-04-17_21-18-49.png" width="60%"></center>

<center>

### Machine Performance
</center>

- $\text{TH}_{m}$
- $\text{SC}_{m}$
- $\text{A}_{m}$: Availability
- $\text{PR}_{m}$: Raw process rate
- $\text{EPR}_{m}$: Effective process rate (maximum theoretical capacity)
- $\text{B}_{m}$: Busy time rate
- $\text{DT}_{m}$ (time per time): Machine downtime rate
- $\rho_{m}$: Machine occupancy rate (utilization)
- $\text{PCC}_{m}$: Machine production control channel width
- $\text{MTBE}_{m}$: Mean time between machine down events (但这期间 machine 不一定在运行)
- $\text{MTTR}_{m}$: Mean time to recover from machine down events

***Machine Availability***
the <u>percenrage</u> of the time the machine is up, running, and qualified to process jobs. = 可用时间 / (可用时间 + 维修时间), 注意这里的<span style="background-color: yellow; color: black;">可用时间不等于工作时间</span> (busy time)

$$\text{A}_{m} = \frac{\text{MTBE}_{m}}{\text{MTBE}_{m}+\text{MTTR}_{m}}$$

***Machine Raw Process Rate***
the maximum number of jobs per unit time the machine can process under ideal conditions.

Using $\text{PT}_{m}$ to denote a machine's raw process time,

$$\text{PT}_{m} = \frac{1}{\text{PR}_{m}}$$

***Machine Effective Process Rate***:
machine maximum theoretical capacity

$$\text{EPR}_{m} = \text{A}_{m}\times\text{PR}_{m}$$

Using $\text{EPT}_{m}$ to denote a machine's effective process time,

$$\text{EPT}_{m} = \frac{1}{\text{EPR}_{m}}$$

***Machine Busy Rate***:
the percent of time, over a given time period, spent in the busy state

$$\text{B}_{m} = \frac{\text{AR}_{m}}{\text{PR}_{m}}=\text{AR}_{m}\times\text{PT}_{m}$$

- $\text{AR}_{m}=$ Arrival rate at the machine
- $\text{PR}_{m}=$ Raw process rate of the machine
- $\text{PT}_{m}=$ Raw process time of the machine

***Machine Occupancy Rate***:
percentage of the available time in the busy state

$$\rho_{m} = \frac{\text{B}_{m}}{\text{A}_{m}}$$

$$\rho_{m} = \frac{\text{AR}_{m}}{\text{EPR}_{m}}$$

***Machine Production Control Channel***

$$\text{PCC}_{m} = \frac{\text{A}_{m}-\text{B}_{m}}{\text{A}_{m}} = 1-\rho_{m}$$


<center>

### Workstation Performance
</center>

A discussion of the performance measures of a workstation will make sense in general <u>only if the workstation supports a single process step</u> and every machine in the workstation is qualified to support that process step and only that process step. (对于不符合这种假设的其他 workstation, 会在之后的章节讨论到)

$$\begin{aligned}
\text{TH}_{ws} &= \sum_{m=1}^M \text{TH}_{m} & \text{throughput rate}\\
\text{EPR}_{ws} &= \sum_{m=1}^M \text{EPR}_{m} & \text{theoretical capacity}\\
\text{A}_{ws} &= \sum_{m=1}^M \text{A}_{m}/M & \text{availability}\\
\text{B}_{ws} &= \frac{\text{AR}_{ws}}{\text{PR}_{ws}} & \text{busy time rate}\\
\rho_{ws} &= \frac{\text{B}_{ws}}{\text{A}_{ws}} = \frac{\text{AR}_{ws}}{\text{EPR}_{ws}} & \text{occupancy rate}\\
\text{PCC}_{ws} &= 1-\rho_{ws}
\end{aligned}$$


需要注意的是: <span style="background-color: yellow; color: black;">$\text{SC}_{ws}$ sustainable capacity, 和 $\text{SC}_{m}$ 没有求和相等的关系, 收到多种其他情况的影响</span>

<center>

### Factory Performance
</center>

- $\text{CT}_{f}$: Factory cycle time
- $\text{CTE}_{f}$: Factory cycle-time efficiency
- $\text{TH}_{f}$: Factory throughput rate (rate of flow of jobs through the entire factory)
- $\text{SC}_{f}$: Factory maximum sustainable capacity, <u>determined by the maximum factory cycle time that the firm can tolerate</u>
- $\text{EPR}_{f}$: Factory maximum theoretical capacity
- Product lead time
- Factory moves
- $\text{WIP}_{f}$: Factory inventory

***Factory Cycle Time***

$$\text{CT}_{f} = \sum_{ps=1}^P \text{CT}_{ps}$$

***Factory Cycle-Time Efficiency***

$$\text{CTE}_{f} = \frac{\text{Process Time}_f}{\text{CT}_{f}}$$

***Factory Inventory***
Little's Law:

$$\text{WIP}_{f} = \text{TH}_{f}\times\text{CT}_{f}$$

## 3.7 Put It All Together
A simple but meaningful example. 这个例子不仅展示了工厂内部各种性能指标的计算和相互关系, 更重要是, **它强调了 降低 dor**

### 3.7.1 Workstation-Centric Model (Initial)

<center><img src="/images/2023-03/Snipaste_2023-04-18_20-14-03.png" width="60%"></center>

Let's consider a factory with:
- arrival rate $\text{AR}_f=1.5$ jobs/ hr
- operates $168$ hrs/ week
- degree of reentrancy $\text{DoR}=2$
- **no variability**

<center><img src="/images/2023-03/Snipaste_2023-04-18_20-24-56.png"  width="80%"> </center>

Using the above data, we may compute the effective process rate $\text{EPR}_m$ of each machine:

$$A_m = \frac{T-(\text{DT}_m + \text{BT}_m)}{T}$$

$$\text{EPR}_m = A_m\times\text{PR}_m$$

For example, for machine $\text{A1}$:

- $A_m(\text{A1}) = (168-16.8)/168 = 0.9$
- $\text{EPR}_m(\text{A1}) = 0.9\times 2 = 1.80$ jobs/ hr

Then after calulating for each machine, we can update the table above as follows:

<center><img src="/images/2023-03/Snipaste_2023-04-18_21-02-47.png" width="80%"></center>

The throughput rate imposed on each workstation is $1.5+1.5=3$ jobs/ hr. And the maximum theoretical of each workstation can be calculated using the table above:
- $\text{EPR}_{ws}(\text{A}) = 2\times 1.8=3.6$ jobs/ hr
- $\text{EPR}_{ws}(\text{B}) = 4\times 0.85=3.4$ jobs/ hr
- $\text{EPR}_{ws}(\text{C}) = 4\times 0.855=3.42$ jobs/ hr

All these $\text{EPR}_{ws}$ is larger than $3$, which seems to show that each workstation is capable of supporting the job flow.

### 3.7.2 Proccess-Step-Centric Model

We have to firstly allocate machines to process steps in each workstation, for example:
- Process step 1 $\to$ machine A1
- Process step 2 $\to$ machines B1 and B2
- Process step 3 $\to$ machines C1 and C2
- Process step 4 $\to$ machine A2
- Process step 5 $\to$ machines B3 and B4
- Process step 6 $\to$ machines C3 and C

<center><img src="/images/2023-03/Snipaste_2023-04-18_21-15-28.png" width="80%"></center>

Using the above allocated process-step-centric model, a new <span style="background-color: yellow; color: black;">fully decoupled workstation-centric model</span> can be constructed.

### 3.7.3 Workstation-Centric Model (Decoupled)

<center><img src="/images/2023-03/Snipaste_2023-04-18_21-21-17.png" width="80%"></center>

小括号里的数据表示新的的 workstation 的 $\text{EPR}_{ws}$ (基于 Section 3.7.1 的第二张 machine 表计算)

Then we can calculate the workstation ***occupancy rate***:

$$\rho_{ws} = \frac{\text{TH}_{ws}}{\text{EPR}_{ws}}$$

<img src="/images/2023-03/Snipaste_2023-04-18_21-25-33.png" width="55%">

where the ***bottleneck*** is workstation $\text{B}$ and $\text{B}'$, or process steps $2$ and $5$

Finally, let's determine the **<font color="blue">cycle time</font>** of the factory. Assuming:
- no varaiablity in machines, procee rates, and throughput rates
- the time required to move from one nontransit process step to another is 5 minutes

(以下公式中的 $\text{EPR}_{ps}$ 来自于本 Section 第一张图的小括号)

$$\text{CT}_{f} = 6\times\frac{5}{60}+\sum_{p=1}^{6} \text{CT}_{ps}(p) = 0.5 + \sum_{p=1}^{6}\frac{1}{\text{EPR}_{ps}(p)}=3.5972\text{ hrs}$$

$$\text{WIP}_{f} = \text{TH}_{f}\times\text{CT}_{f} = 1.5\times 3.5972 = 5.9358\text{ jobs}$$

在这个例子中, 我们通过从 initial workstatio-centric model 到 decoupled workstation-centric model 的转变, 把 $\text{DoR}$ 降低到了 $1$. 尽管对于绝大多数 real factories, 我们无法实现 $\text{DoR}=1$, 但是我们仍可以通过尽可能的降低 $\text{DoR}$, 来简化计算复杂度


# 4. Running a Factory: In Two Dimensions



<center><img src="/images/2023-03/.png" width="80%"></center>
<center><img src="/images/2023-03/.png" width="80%"></center>
<center><img src="/images/2023-03/.png" width="80%"></center>
<center><img src="/images/2023-03/.png" width="80%"></center>




# 5. Variability

- $C_{AR}$: COV of Arrivals
- $C_{PT}$: COV of Raw Process Times
- $C_{EPT}$: COV of Effective Process Times





<center><img src="/images/2023-03/.png" width="80%"></center>
<center><img src="/images/2023-03/.png" width="80%"></center>
<center><img src="/images/2023-03/.png" width="80%"></center>
<center><img src="/images/2023-03/.png" width="80%"></center>
<center><img src="/images/2023-03/.png" width="80%"></center>
<center><img src="/images/2023-03/.png" width="80%"></center>
<center><img src="/images/2023-03/.png" width="80%"></center>




<img src="/images/2023-03/.png"  width="80%">
<img src="/images/2023-03/.png"  width="80%">
<img src="/images/2023-03/.png"  width="80%">
<img src="/images/2023-03/.png"  width="80%">
<img src="/images/2023-03/.png"  width="80%">
<img src="/images/2023-03/.png"  width="80%">
<img src="/images/2023-03/.png"  width="80%">
<img src="/images/2023-03/.png"  width="80%">
<img src="/images/2023-03/.png"  width="80%">
<img src="/images/2023-03/.png"  width="80%">
<img src="/images/2023-03/.png"  width="80%">
<img src="/images/2023-03/.png"  width="80%">
<img src="/images/2023-03/.png"  width="80%">