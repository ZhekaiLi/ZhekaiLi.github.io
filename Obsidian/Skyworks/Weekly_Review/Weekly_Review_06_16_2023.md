**ABSTRACT**: Keep updating the simulation.

---

## 1. Discrete-Event Simulation

Define four classes to represent the objects in manufacturing:
1. ***Lot*** 
	1. **route_eqpTypes** = list(eqpType) 
	2. **route_recipes** = list(recipe)
	3. **route_toolsList** = list(list(tool))
	4. **route_samplingRates** = list(samplingRate) [[#Explains#1. Four route lists]]
	5. **priority**
	6. **startTimeInHour**
	7. **dueTimeInHour**
	8. ==score = priority * (12 - log(expectedTime - now + 1))== when expectedTime > now
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

---

## 2. Run on the Real Route

Using the real production data of Q3 2023 to generate lots with the following rows:
- divide by 13x20 (num weeks per quater, num wafers per lot)
	For example,  13603/260=52 lots of product ZT003-J1NS are generated for simulation ![[Pasted image 20230608152603.png]]

### 2.1 Gantt Chart
![[Pasted image 20230616131038.png]]
### 2.2 Animation

video

---

## 3. Degree of Realism

1. route $\to$ recipe + eqpType $\to$ tools inside that can run the recipe
2. ***Running Time***: {tool: {recipe: MPU}} 
3. ***Lots***:                 generated according to the real schedule
			      ***Dispatcher***: dispatch lots evenly (every hour)
4. ***Scheduler***\:       simple (a little improvement)

All others are ideal

---

## 4. What's NEXT?

1. [-] Keep updating the logic of the simulation to make it more close to the real-case, especailly try to update the rule of computing score for both lot and entity (tool)
2. [ ] Test the application value by comparing results from different priority
3. [-] Try to fix the data missing problem with other engineers
4. [-] Try animation
5. [-] Keep improving the degree of realism by adding:
	2. [-] make it available for different startTime of different lot
	3. [ ] variance of MPU
	4. [-] include number of wafers per lot
	5. [-] include sampling rate
       5. [ ] try to consider about the ==availbility, utilization, breakdown event== (MTTF)
	6. [ ] try to consider about the transition time
	7. [ ] try to consider about the ==re-work (model in Promis) & inspection== process, which requires to write a function about lot (how to make, break, and reform a lot)
	8. [ ] try to consider about the bank
	9. [ ] ==try to consider chambers== (already considered in UPH in FPS?) (batch)
	11. [-] add ==initialization status== (add lots in the beginning to the fab)
	12. [ ] understand the "Start" Module


---

## Explains

### 1. Four route lists
The element in `route_eqpTypes`, `route_recipes`, and `route_tools` ==with the same index are relevant==
e.g.:
- `route_eqpTypes[0]` = the equipment type to run the first step
- `route_recipes[0]`   = the recipe of the first step
- `route_toolsList[0]`        = the list(tool) that could be used for the first step
- `route_samplingRates[0]` = the samplingRate of the first step








### 2. Karen's team (IE) 
the wip on the tool level (current wip, real time)


others
ask sam to ask for the oneNote ()
