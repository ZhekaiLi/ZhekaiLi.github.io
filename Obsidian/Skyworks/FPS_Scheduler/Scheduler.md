
# 1. UI 
### Scheduler > Bay Viewer
Name of [[Bays]] (physical or logical areas within the factory)

![[Pasted image 20230523112111.png]]


---

# 2. Algorithm/ Logic

## 2.1 Input Data
- The routing and flow information are combined into the #Problem “WIP Step Future” data
	- This a combination of the flow definition information with the current lot data and predicts where the lot will be in the future
	- The Data Warehouse also uses cycle time data to predict at approximately what time the lot will arrive at those futures steps.
- The WIP Step Future data is then merged with the tool assignment data to generate a list of which tools are allowed for which lots at which steps (WIP Step Future Assignments)
	- The assignment data also include details about the processing of the lot – recipe, various “setup” type conditions, throughput information, and potentially many other data.
- This forms the core input data for generating a schedule.

## 2.2 Define a Scheduler
In most cases, it is infeasible to generate a schedule for all lots and tools for an entire factory at one time. To manage this issue, we ==segregate the factory into different scheduler groups==:
- To allow this separation, each ==“Sched Group”== must be self contained
	- A step on a #Problem (what is the flow) flow must be in one and only one Sched Group
	- A tool must be in one and only one Sched Group
	- Every tool needed to run a step must be in the same Sched Group as that step
	- In most cases, this definition of Sched Group naturally follows fab organization (e.g. Photo, Dry Etch, Wet Etch, Diffusion, Films, etc…)

## 2.3 Objectives - Evaluations or "Sliders"
An important concept in the scheduler is that ==not every area (or toolset) has the same objectives for generating a “good” schedule==
- Implant may want to keep the same species setup
- Photo needs to optimize reticle usage

Because of this, FPS provides a library of evaluations (“sliders”) that represent a scoring of the lot/step/tool vs. some objective:
- Each Sched Group can pick its own sliders
- Each slider can be configured as to whether it is relevant to identifying the “most important” lot or the tool “best process context” or both

例如下图属于某个 Sched Group 的 evaluation criteria, 其中:
- 用于为 Tool 打分: Process Start Time, Process End Time, Same Bay Rule, ...
- 用于为 Lot 打分:  Step Enter Time, Process Start Time, Process End Time, Lot Priority, ...
- Tool 分越高表示越应该优先被用于处理 Lot
- Lot 分越高表示越应该优先被分配给 Tool
![[Pasted image 20230525150426.png]]

## 2.4 Procedure
1. Request data for the Sched Group from the Data Warehouse 
2. Identify the “most important” lot to place on the schedule 
3. ==Assign the most important lot to the best tool based on the best process context== 
4. Return to 2 and Repeat until all the scheduler time window is full or no more lots can be scheduled