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
Concurrent with the flow of jobs through a factory are **events that occur within the factory’s workstations**. These events serve to <u>reduce the availability</u> of the machines that form the workstation and, subsequently, the overall availability of the workstation itself. The degradation imposed by such events on the workstation—and the factory—in turn, will have an impact on factory performance.

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
- **automobile assembly** lines have little, if any,reentrancy (<u>the ideal assembly line has none</u>)
- **semiconductor wafer** fabrication facilities, or “fabs”, typically have factory DoR values ranging from 3 to 5 or even more—with individual nests that may have DoRs in the double digits.

We next consider two other, more traditional (in that they *do not include reentrancy*) workstation-centric models:

**<font color='blue'>(1) Flowshop factory</font>**

<center><img src="/images/2023-03/Snipaste_2023-04-04_11-14-53.png"  width="80%"><br>
    <div style="color: #808080;">Figure 3.2</div></center>

- Each job follows precisely the same pathway
- Each workstation supports just one process step
- **No passing of jobs**: if two jobs enter the factory in, say, the job sequence J1 and J2 they must enter and leave each workstation in that same sequence

**<font color='blue'>(1) Jobshop factory</font>**

<center><img src="/images/2023-03/Snipaste_2023-04-04_11-18-56.png"  width="80%">
<br>
    <div style="color: #808080;">Figure 3.3</div></center>

- Each job that enters the factory may follow a different process flow path (J1 vs. J2)

### 3.2.2 Process-step-centric Model
According to *Figure 3.1*, if we know which machines are capable of supporting (e.g., qualified to conduct or be assigned to) each process step, we can convert that workstation-centric model into a process-step-centric model:

<img src="/images/2023-03/Snipaste_2023-04-04_11-34-59.png"  width="80%">

Why this model is important:
- it indicates not only the process step flow but also <u>the precise support responsibilities of each machine</u> in the factory.


## 3.3 Factory Definitions and Terminology
### 3.3.1 Factory Types
■ Flowshops
■ Jobshops
■ Factories without reentrancy (i.e., DoR = 1)
■ Factories with reentrancy (i.e., DoR > 1)
■ Synchronous factories (e.g., every job flows through the factory at the same constant speed, such as bottles in a beverage bottling plant)
■ Asynchronous factories (e.g., each job—as in semi-conductor fabrication—may flow through the factory at different speeds and in addition may remain temporarily held in a queue)
■ High-mix factories (e.g., those that process numerous job types)
■ Low-mix factories (e.g., those that process only a limited number of job types)
■ Low-volume factories (e.g., those that process only a relatively limited number of jobs per time period, such as aircraft manufacturers or research and development factories that produce only prototypes of a product)
■ High-volume factories (e.g., those that process a large number of jobs per time period, such as high-volume semiconductor wafer fabrication facilities)
■ High-mix, low-volume factories
■ High-mix, high-volume factories
■ Low-mix, low-volume factories
■ Low-mix, high-volume factories
■ Factories involving various combinations of the preceding features

### 3.3.2 Jobs and Events


# 5. Variability






<img src="/images/2023-03/.png"  width="80%">
<img src="/images/2023-03/.png"  width="80%">
<img src="/images/2023-03/.png"  width="80%">