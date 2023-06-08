**ABSTRACT**: This week I firstly worked on building a discrete event simulation model to simulate the scheduling and processing in a fab, then I tried to integrate the real data from the FPS database to the simulation model

---

## 1. Discrete-Event Simulation

Define four classes to represent the objects in manufacturing:
1. ***Lot***
	1. **route** = list(process)
	2. **priority**
	3. **dueTime**
	4. ==score = priority * exp(env.now - expectedTime)==
		 For example for a lot with 10 steps, assume it starts at time=0, when it is in the step 5, its expectedTime=dueTime * (5/10), so:
			(1) if env.now > expectedTime, which means the lot is likely to be late, the score will increase exponentially
			(2) if env.now < expectedTime, the score will be small
2. ***Entity***
	1. **initScore**: depends only on entity itself (assume to be constant = 2)
	2. ==score = initScore - length(queue)==
3. ***Family***
	1. **run_entities()**
	2. **run_scheduler()**
		 Reserve the lot with the highest score to the entity with the highest score, until all the lots are reserved.
4. ***Factory***: run_families()

---

## 2. Run on the Real Route

Generate 3 lots for each of 41 long routes (contain hundreds of steps to run), and run simulation on 300+ actual tools. The picture below showing the Gantt Chart for the overall fab, where
- y-axis, or each line represents one tool
- x-axis is the time

For example, we could clearly find that the most of the tools in the range 330 to 600 are not for the previous steps in manufacturing

![[Pasted image 20230601134556.png]]

---

## 3. Degree of Realism

1. route $\to$ process $\to$ eqpType $\to$ all tools inside
2. ***Running Time***: constant for all
3. ***Lots***:                 randomly generated (one wafer per lot)
4. ***Scheduler***:        simple

All others are ideal

---

## 4. What's NEXT?

1. [-] Keep updating the logic of the simulation to make it more close to the real-case, especailly try to update the rule of computing score for both lot and entity (tool)
2. [-] Integrate more real data into the simulation
	1. [-] Use real UPH data for each tool (now it's assumed to be constant)
	2. [-] Use real demand data for generating lots (now the lots are evenly generated for each possile routes, but in the real case, some route will have lots of lots, and many of them even don't have any lots to generate)
