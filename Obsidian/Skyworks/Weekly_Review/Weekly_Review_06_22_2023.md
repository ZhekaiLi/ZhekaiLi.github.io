**ABSTRACT**: Keep updating the simulation.

---

## 1. Discrete-Event Simulation

Define four classes to represent the objects in manufacturing:
1. ***Lot*** 
	1. **route_recipes** = list(recipe)
	2. **route_eqpTypes** = list(eqpType)
	4. **route_samplingRates** = list(samplingRate)
	5. **route_toolsList** = list(list(tool)) [[#Explains#1. Four route lists]]
	6. **waferNum**
	7. **priority**
	8. **startTimeInHour**
	9. **dueTimeInHour**
	10. ==score = priority * (12 - log(expectedTime - now + 1))== when expectedTime > now
	                                (12+ log(now - expectedTime + 1)) when expectedTime <= now
		 For example for a lot with **10 steps** (priority=1), assume
		 - it starts at time=0, dueTime = 100
		 - now it's in step 5, and the currentTime=60
		 - expectedTime = 100 * (5/10) = 50 < 60, means late
		 - score = 1 * (12 + log(11)) = 14.4
2. ***Entity*** $\to$ Tool
	1. **initScore** = {recipe: 1/MPU}
		 where MPU = the time (min) the entity need to finish one wafer using that recipe
	1. ==score = initScore - length(queue)==
3. ***Family*** $\to$ eqpType
	1. **run_entities()**
	2. **run_scheduler()**
		 Reserve the lot with the highest score to the entity (*that could be used to run that step of lot*) with the highest score, until all the lots are reserved.
		
1. ***Factory***: run_families()
2. ***Module***: collect data for animation (WIP, Avg QT)
3. ==***Dispatcher***:==
	1. initialize and send lots into the fab
	2. #TODO keep dispatching in the other following weeks

---

## 2. Run on the Real Route

Using the real production data of Q3 2023 to generate lots with the following rows:
- divide by 13x20 (num weeks per quater, num wafers per lot)
	For example,  13603/260=52 lots of product ZT003-J1NS are generated for simulation ![[Pasted image 20230608152603.png]]

### 2.1 Gantt Chart

omitted, no need

### 2.2 Animation

video

---

## 3. Degree of Realism

1. route $\to$ recipe + eqpType $\to$ tools inside that can run the recipe
2. ***Running Time***: {tool: {recipe: MPU}} 
3. ***Lots***: generated according to the real schedule
	1. ***Dispatcher***: 
		1. initialize the lots
		2. dispatch lots evenly (every hour) for the first week
		3. keep dispatching lots evenly in the other following weeks
4. ***Scheduler***\: simple (a little improvement)

All others are ideal

---

## 4. What's NEXT?

1. [-] Keep updating the logic of the simulation to make it more close to the real-case, especailly try to update the rule of computing score for both lot and entity (tool)
2. [ ] Test the application value by comparing results from different priority
3. [-] Try to fix the data missing problem with other engineers
4. [-] Keep developing animation
5. [ ] Keep improving the degree of realism by adding:
	3. [ ] variance of MPU
       5. [ ] try to consider about the ==availbility, breakdown event== (MTTF)
	6. [ ] try to consider about the transition time
	7. [ ] try to consider about the ==re-work (model in Promis) & inspection== process, which requires to write a function about lot (how to make, break, and reform a lot) #TODO batch with MPU
	8. [ ] try to consider about the bank
	9. [ ] ==try to consider chambers== (already considered in UPH in FPS?) (batch)
	11. [-] add function to keep dispatching wafers in the following weeks after 1st week
	12. [-] understand the "Start" Module
	13. [ ] calculate utilization of each machine per 40 hrs
	14. [-] speed up the simulation by using threading
	15. 

周末把 sql 那个 pdf 学完


---

## Explains

### 1. Four route lists
The element in `route_eqpTypes`, `route_recipes`, and `route_tools` ==with the same index are relevant==
e.g.:
- `route_eqpTypes[0]`          = the equipment type to run the first step
- `route_recipes[0]`            = the recipe of the first step
- `route_toolsList[0]`        = the list(tool) that could be used for the first step
- `route_samplingRates[0]` = the samplingRate of the first step

POC: proof of conecpt

**What fps means?**
two level sampling
- lot-level sampling
- wafer-level sampling 10 wafers
the number of points to measure defines the UPH

1. Chambers & Batching: 
	1. now the lowest level we could find in FPS database about the UPH is the recipe-to-tool level. How could we know any infomation about chambers?
	2. From FPS table: ETP_ENTITY_E10_PW_HIST, we have lots of tool-to-entity pairs. For are these entities include chambers? If so how could we know their UPH value?
	3. 
	

#Problem  way to model sampling rate (now just multiply)
	
#Problem  chambers? how to model the chamber, any data and suggestions
#Problem  Start
#Problem  how to model availability (breakdown schedule down time frequency),
unscheduler schedular, (vary variable)
decide to continue, 
batch tool
previous step to rework, 
	
3% of lots of the stop twice

historcial data --> E10 Table

sampling:
one sample per run, two lot per run
depend on technology (route family)

Chambers: specific to the tool
- spt tools: some four chambers are different
- sput: chambers different from

table show how many lots can be loaded per tool (IE team)
cascading 
batching
serial 

#Problem change of the route, maybe rework? ()

excel, change the material accord the process

test-run: metrology -> check the wafer and the tool (after maintainance, to check the tool if good or not)
(test-run maybe only 4 steps, significant for metrology tools)

FabTime -> there is chart average mtbf Suyra

recipe have parameter to decide MPU based on the product
(recipe)


how peam find the utilization data 


ETP_ENTITY_E10_PW_HIST 
1. contains tool-to-entity
	but we have not find any table to show the entity-to-recipe, and also entity-to-MPU relations
2. 


