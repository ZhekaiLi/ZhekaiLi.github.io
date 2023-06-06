Abstract:
This week I focus on realizing a simple simulation model that can be used to see ==the influence of changing the priority of different lots==

### 1. Objective: Minimize the ==total penalty== (lateness $\times$ priority)
$$\min \sum_l W_lL_l$$
- $W_l=$ Weight of lot $l$
- $L_l=\max(0,d_l-C_l)=$ Lateness of lot $l$ 
	- $C_{l}=$ Completion time
	- $d_l=$ due date

---

### 2. Parameters

- $(l,sl)=$ (lot, step)
	- $sl\in\{1,2,...,Sl\}$, $Sl$ is the final step of lot $l$
- $(i, j)=$ (Tool Family, Machine)
- $p_{(l,sl),i}$  : Process time of $(l,sl)$ on family $i$

### 3. Decision Variables
- $w_{(l,sl),i,j} = 1$ IFF $(l,sl)$ is firstly processed at family $i$ machine $j$
- $x_{(l',sl'),(l,sl),i} = 1$ IFF $(l',sl')$ just precedes $(l,sl)$

---

### 4. Constraints

- Each $(l,sl)$ must be ==proceeded== by one process step or be the first
$$\sum_{i,j}w_{(l,sl),i,j} + \sum_{(l',sl')\neq (l,sl),i}x_{(l',sl'),(l,sl),i} = 1\;\;\;\;\forall (l,sl)$$
- Each $(l',sl')$ must be ==succeeded== by at most one process step (zero when as the tail)
$$\sum_{(l,sl)\neq (l',sl'),i} x_{(l',sl'),(l,sl),i} \leq 1\;\;\;\;\forall (l',sl')$$

Other constraints, including many time constraints, are omitted here

---

### Example 1

We assume:
1. **3 Tool Family, 5 Machine**
	- Family 1 contains 2 machines
	- Family 2 contains 2 machines
	- Family 3 contains 1 machine
2. **4 lots, each has 5 steps**
3. Due date of all the lots are set to be the same (2 days)
4. Process time of $(l,sl)$ on different family $i$ is randomly set
5. ==**Priority** is assumed the same for all lots in this example==

---

### Result 1

In the following picture, which is similar to a Gantt chart
- x-axis represent the time (days)
- each line represent one machine
- each color represents one lot 


![500](pics/Pasted_image_20230524102749.png)



==So here we see that the cycle time of blue lot is more than 5 days==

---

### Example 2 & Result 2
- ==Change Priority of lot 4 (blue) to be much higher than others==
- All the others are the same as in Example 1

Now the cycle time of blue lot is less than 5 days because of its high priority
![|500](pics/Pasted_image_20230524111126.png)

```text
Process time of (l,sl) = (4,1) is 1.9898323303467176 on family 1 
Process time of (l,sl) = (4,1) is 1.8126309310042183 on family 2 
Process time of (l,sl) = (4,1) is 1.996957446629187 on family 3 
------------------------------------------------------------ 
Process time of (l,sl) = (4,2) is 1.2339301717548576 on family 1 
Process time of (l,sl) = (4,2) is 0.9521701881803636 on family 2 
Process time of (l,sl) = (4,2) is 0.9366360087680974 on family 3 
------------------------------------------------------------ 
Process time of (l,sl) = (4,3) is 0.6872160719421607 on family 1 
Process time of (l,sl) = (4,3) is 0.9991257691510043 on family 2 
Process time of (l,sl) = (4,3) is 1.8833745964648232 on family 3 
------------------------------------------------------------ 
Process time of (l,sl) = (4,4) is 0.8048027787041501 on family 1 
Process time of (l,sl) = (4,4) is 1.6991406672058882 on family 2 
Process time of (l,sl) = (4,4) is 1.3208451597498774 on family 3
------------------------------------------------------------ 
Process time of (l,sl) = (4,5) is 0.931485896315303 on family 1 
Process time of (l,sl) = (4,5) is 0.6374481424274316 on family 2 
Process time of (l,sl) = (4,5) is 1.6969025289815045 on family 3 
In------------------------------------------------------------
```

--- 
### What's Next?

- Find ways to speed up the simulation above
	- Choosing appropriate parameters
	- Eliminating some useless constraints
- Look for other possible solutions for fab simulation
	- paper working
- Discover the feasibility of discrete-event simulation
	- understand the Scheduler in FPS, mainly the logic of assigning lot to different machines
	- try to built some simple model in Python