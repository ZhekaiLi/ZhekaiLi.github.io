**ABSTRACT**: This week I continued working on the discrete-event simulation model based on last week. I sucessfully extract and apply the **real data** from the FPS database as the parameters of the model, although 8% data is missing or problem, which is omitted right now. Also, I greatly re-designed my initial model to make it suitable to the real data.

==Although the current model still based on tons of assumptions, BUT it might can already provide some meaningful infos with the results of changing priority==

---

## 1. Discrete-Event Simulation

Define four classes to represent the objects in manufacturing:
1. ***Lot***
	1. **route_eqpTypes** = list(eqpType) 
	2. **route_recipes** = list(recipe)
	3. **route_tools** = list(list(tool)) [[#Explains#1. Three route lists]]
	5. **priority**
	6. **dueTime**
	7. ==score = priority * (12 - log(expectedTime - now + 1))== when expectedTime > now
	                                (12+ log(now - expectedTime + 1)) when expectedTime <= now
		 For example for a lot with **10 steps** (priority=1), assume
		 - it starts at time=0, dueTime = 100
		 - now it's in step 5, and the currentTime=60
		 - expectedTime = 100 * (5/10) = 50 < 60, means late
		 - score = 1 * (12 + log(11)) = 14.4
1. ***Entity***
	1. **initScore** = {recipe: 1/MPU}
		 where MPU = the time (min) the entity need to finish one wafer using that recipe
	1. ==score = initScore - length(queue)==
2. ***Family***
	1. **run_entities()**
	2. **run_scheduler()**
		 Reserve the lot with the highest score to the entity (*that could be used to run that step of lot*) with the highest score, until all the lots are reserved.
4. ***Factory***: run_families()

---

## 2. Run on the Real Route

Using the real production data of Q3 2023 to generate lots with the following rows:
- any product with lots < 100 is eliminated
- others are divided by 100. For example, 136 lots of product ZT003-J1NS are generated for simulation ![[Pasted image 20230608152603.png]]
- so in total, there are 247 lots generated for 14 routes

![[Pasted image 20230608152239.png]]

---

## 3. Degree of Realism

1. route $\to$ recipe + eqpType $\to$ tools inside that can run the recipe
2. ***Running Time***: {tool: {recipe: MPU}} 
3. ***Lots***:                 generated according to the proportion of the actual production (one wafer per lot)
4. ***Scheduler***\:        simple (a little improvement)

All others are ideal

---

## 4. What's NEXT?

1. [ ] Keep updating the logic of the simulation to make it more close to the real-case, especailly try to update the rule of computing score for both lot and entity (tool)
2. [ ] Test the application value by comparing results from different priority
3. [ ] Try to fix the data missing problem with other engineering
4. [ ] Keep improving the degree of realism by adding:
	1. [ ] different priority of differnt lot
	2. [ ] different startTime and dueTime of different lot
	3. [ ] variance of MPU
	4. [ ] increase number of wafers per lot
	5. [ ] try to consider about the availbility, breakdown event
	6. [ ] try to consider about the transition time
	7. [ ] try to consider about the ==re-work & inspection== process, which requires to write a function about lot (how to make, break, and reform a lot)
	8. [ ] try to consider about the bank
	9. [ ] try to consider chambers


---

## Explains

### 1. Three route lists
The element in `route_eqpTypes`, `route_recipes`, and `route_tools` ==with the same index are relevant==
e.g.:
- `route_eqpTypes[0]` = the equipment type to run the first step
- `route_recipes[0]`   = the recipe of the first step
- `route_tools[0]`      = the list(tool) that could be used for the first step