---
layout: post
title: Six Sigma - Intro
categories: Supply-Chain
description:
keywords: SCE, Supply-Chain
mathjax: true
---

<center>

# Six Sigma - Intro
</center>

# 1. Introduction
The goal of Lean Six Sigma is to design or improve products and processes to do what they are supposed to do with very high reliability.

*Lean Six Sigma is uniquely driven by a close understanding of customer needs, disciplined use of facts, data, and statistical analysis, and diligent attention to managing, improving, and reinventing business processes.* --- The Six Sigma Way

## 1.1 Overview
<center><img src="/images/2022-11/Snipaste_2022-12-02_16-22-23.png" width="70%"></center>

> **Six Sigma**
- a quality management philosophy and a methodology that focuses on **reducing variability**, measure defects, and improving the **quality** and **reliability** of products, processes and services
- **it's a project methodology for improvement**

> **Lean**
- to maximize customer value while minimizing waste

Lean Methods were developed to attack the waste associated with the **flow** of material and information - the **velocity, or speed** of a process from beginning to end. Lean consists of five key principles:
- Identify customers & specify value
- Map the value stream
- Improve flow
- Respond to customer pull, or demand
- Pursue perfection



## 1.2 The Cost of Poor Quality

> **1:10:100 Rule**: 
> the cost of poor quality increases exponentially as a product or service moves along the value stream from creation to consumption.
> <img src="/images/2023-03/Snipaste_2023-03-18_14-21-20.png" width="60%">

**Cost of Poor Quality** can be broken down into four categories:
- **Prevention Cost**: The cost of investing in doing it right the first time. Training, error-proofing, pre-production pilots, design for capability (DFSS - Design For Six Sigma).
- **Appraisal Cost** (评价): The cost of testing and inspection to detect defects internally.
- **Internal Failure Cost**: The cost of detecting and correcting defects internally: Scrap, rework, and "Seconds" sold off-price.
- **External Failure Cost**: The cost of defects being detected by customers, including warranties, replacements, allowances, product liability, customer dissatisfaction and lost revenue.


## 1.3 The 5 Lean Principles

(1) Identify Cusotmers and Specify Value

(2) Map the Value Stream
Identify and map the value stream

A **value stream** is the complete sequence of activities an organization performs in order to produce and deliver its end product or service.

A **value stream map** is 

(3) Create Flow
Create flow by eliminating waste and achieving a lot size of one

(4) Respond to Pull

(5) Pursue Perfection


<img src="/images/2023-03/.png" width="70%">
<img src="/images/2023-03/.png" width="70%">
<img src="/images/2023-03/.png" width="70%">
<img src="/images/2023-03/.png" width="70%">
<img src="/images/2023-03/.png" width="70%">
<img src="/images/2023-03/.png" width="70%">
<img src="/images/2023-03/.png" width="70%">



---

# 2. Key Concepts in Six Sigma
## 2.1 Critical to Quality Metrics
**(1) VOC (Voice of the Customer)**: needs and expectations expressed in the customer's language

**(2) CTQs (Critial-to-Quality Requirements)**: the performance characteristics of a process, product, or service critically important to customers

<span style="background-color: yellow; color: black;">It's important to translate VOC to CTQs</span>

For example, for a pizza store:
|VOC|CTQs|Metrics|CTQs Target|
|-|-|-|-|
|"Don't want to wait too long"|On-time delivery|Order to delivery (mins)|<= 30 mins|
|"Don't want cold pizza"|Hot pizza when delivered|Pizza temperature (degrees)|>= 32 degrees|

**Six Sigma Basic Premise**:
$$Y=f(X)$$

- $Y_1=$ delivery time
- $Y_2=$ pizza temperature
- $X=$ factors affecting $Y_1,Y_2$

## 2.2 Defect Opportunities
(1) For a **marker**, there might be **5** defect opportunities such as leak, ink color, cap...

(2) For a **PC**, there might be **1000** defect opportunies

Let's assume either marker or PC have 2 defects per unit, then

> **DPO (defects per opportunity)**
- Marker: 2/5 = 0.4 DPO
- PC: 2/1000 = 0.002 DPO

> **DPMO (defects per million opportunities)**
- Marker: 0.4 DPO * 1,000,000 = 400,000 DPMO
- PC: 0.002 DPO * 1,000,000 = 2,00 DPMO

## 2.3 Sigma Level
A performance metric used to indicate the quality level of a product, process, or service

<img src="/images/2022-12/Snipaste_2023-01-14_16-37-00.png" width="70%">








# 2. DMAIC: A Six Sigma Methodology
**DMAIC**: Define, Measure, Analyze, Improve, Control

## 2.1 Define

> **(1) Develop problem and goal statements**

**Problem Statement**
- Requirements: <u>Reccuring, Specific, and Measurable</u>
- Example: the problem stated below is a chronic, reccuring problem, stated in specific and measurable terms
  <img src="/images/2022-12/Snipaste_2023-01-21_15-49-25.png" width="60%">

**Goal Statement**
- Ask ourselves: What measurable perforance outcome must the project accomplish? By when?
- Be SMART:
  <img src="/images/2022-12/Snipaste_2023-01-21_15-52-42.png" width="60%">
- Example:
  <img src="/images/2022-12/Snipaste_2023-01-21_15-54-12.png" width="60%">

We need to define what is the $Y$, the performance measure to improve, in the equation of $Y=f(x)$

> **(2) Develop project charter**

A document providing direction and focus to the team:
- Project name
- Problem and goal statements (based on step one above)
- Key Metric $Y=f(x)$
- Expected benefits (operational and finantial)
- Project scope (project boundary)
- Milestones (check point datas)
- Signatures
  - Project leader: agrees to take on project
  - Finance: validates expected financial benefits
  - Champion: approves launch of the project

> **(3) Develop a SIPOC diagram**

Purpose is to document and communicate overall scope of processes related to the project on one page

<img src="/images/2022-12/Snipaste_2023-01-21_15-43-14.png" width="60%">


## 2.2 Measure
**Steps**:
1. Develop data collection plan
2. Map relevant processes
3. Validate measurement system
4. Measure the $Y$ in $Y=f(X)$

> **(1) Data collection plan**:

1. List specific questions regarding $Y$
2. Tools needed
3. Sources of data
4. Type (continuous/discrete) and quantity of data required

**Continuous** data graphs:
<img src="/images/2022-12/Snipaste_2023-01-27_23-26-31.png" width="60%">

**Discrete** data graphs:
<img src="/images/2022-12/Snipaste_2023-01-27_23-27-40.png" width="40%">


> **(2) Process Map**: 

A visual representation of the steps that take place in a process, from start to finish. Ex: <u>Wake-up-and-get-to-work Process</u>
<img src="/images/2022-12/Snipaste_2023-01-27_23-16-44.png" width="90%">

> **(3) Validate Data: use Measurement system analysis (MSA)**

Requirements of a valid measurement: (using an example of weight scale 体重秤)
- <u>Accurate with no bias</u>: the scale should be calibrated
- <u>Repeatable</u>: if I weigh myself twice in a short time, the results should be same
- <u>Reproducible</u>: my weight in my home should be the same as my weight in my doctor's office

## 2.3 Analyze
**Purpose**: Determine which $X$(s) impact $Y$ in $Y=f(X)$

**Steps**:
1. List potential $X$(s) that impact $Y$
2. Organize potential $X$(s)
3. Shortlist and select key $X$(s)
4. Develop data collection plan for the analysis
5. Prove the key $X$(s) in $Y=f(X)$

> **(1) List potential $X$(s) that impact $Y$**: brainstorm

> **(2) Organize potential $X$(s)**: use <u>Cause-effect diagram (fishbone)</u>

**Ex: CE Diagram for Pizza Crust Problem (饼皮太硬)**
- Fishbone:
<img src="/images/2022-12/Snipaste_2023-01-28_09-07-48.png" width="70%">
- Treemap (use Excel):
<img src="/images/2022-12/Snipaste_2023-01-28_09-10-19.png" width="75%">

> **(3) Shortlist and select key $X$(s)**: based on the upper diagram

> **(4) Develop data collection plan for the analysis**

- Which hypotheses to test
- What data to collect
- How much data we need
- Collect from whom, when, where

> **(5) Prove the key $X$(s) in $Y=f(X)$**: Validation Process

- Inferential statistics
- Hypothesis test

**Ex: Analyze and validate throught graphs and charts**, using Pizza Crust Problem (饼皮太硬问题). To validate two potential $X$
- $X_1$: one or two resteraunt at fault
- $X_2$: Variation in oven temperatures

$X_1$ is proved using <u>Pareto Chart for Crust Complaints by Store Location</u>

<img src="/images/2022-12/Snipaste_2023-01-28_09-29-34.png" width="50%">

$X_2$ is proved using <u>Dotplot and Boxplot for Temp Variation by Chef</u>

<img src="/images/2022-12/Snipaste_2023-01-28_09-37-39.png" width="80%">

## 2.4 Improve
**Purpose**: Address proven key $X$(s) and find solutions (best combination of key $X$(s)) to improve $Y$

**Steps**:
1. Potential solutions for proven key $X$(s)
2. Solution alternatives
3. Right set of solutions to implement

> **Generate, evaluate, and select solutions**

Evaluate solutions:

<img src="/images/2022-12/Snipaste_2023-01-28_10-33-55.png" width="70%">

Select solutions: Pugh Matrix (Criteria selection matrix)

<img src="/images/2022-12/Snipaste_2023-01-28_10-34-50.png" width="55%">

> **Reduce the risk of failure through FMEA**

**FMEA** (Failure Modes and Effect Analysis) is a tool to help anticipate and mitigate risk of failure.

Order failure modes by <u>Risk Priority Number (RPN)</u>:

$$RPN=\text{Severity}\times\text{Occurrence}\times\text{Detection}$$

- $\text{Severity}$: What's the effect? How severe is it (1-10)?
- $\text{Occurrence}$: What are potential causes? How likely is the occurrence of potential causes (1-10)?
- $\text{Detection}$: What process controls are in place to detect cause or failure mode? What's the likelihood of detection (1-10)?

> **Mistake proofing (防范错误)**

Adding mistake proofing to projects will be helpful. Three levels of mistake proofing:
1. **Prevention**
   - Ex: Change the <u>operation sequence of ATM to prevent forgeting to remove card after taking cash</u>
   - Swap steps 4 and 6, that is, can only take cash after removing card
  <img src="/images/2022-12/Snipaste_2023-01-28_10-58-24.png" width="30%">
2. **Facilitation**: if prevention is not applicable
   - Ex: To avoid the cashier typing an inccorect price, try to scan Bar Code instead
3. **Detection**:
   - Ex: Spelling error detection in Word

### 2.4 Control phase:
**Purpose**: Control of key $X$ factors to ensure improved $Y$ is <u>sustainable</u>

**Steps**:
1. Develop plan (Monitor, control, regulate performance)
2. Work with owners to update procedures
3. Implement and monitor performance
4. Validate financial impact
5. Secure project completion sign-off

> **Control Plan**

Control plan is the blueprint to ensure the right controls are implemented to achieve sustainable targets:
1. Control subject: what needs to be controlled
   - Ex: oven temperature
2. Specification, target, or desired range
   - Ex: target 22C, hot more than 24C, cold less than 19C
3. How feedback is provided
4. When and what action to take
   - Ex: when temp above 25, turn off AC; when below 15, turn off AC, or turn on heat if needed
5. Who is authorized to monitor and take action?


<img src="/images/2022-12/.png" width="60%">
<img src="/images/2022-12/.png" width="60%">
<img src="/images/2022-12/.png" width="60%">
<img src="/images/2022-12/.png" width="60%">
<img src="/images/2022-12/.png" width="60%">
<img src="/images/2022-12/.png" width="60%">
<img src="/images/2022-12/.png" width="60%">
<img src="/images/2022-12/.png" width="60%">












