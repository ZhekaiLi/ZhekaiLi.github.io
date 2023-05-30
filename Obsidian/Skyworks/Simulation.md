## Approach one: consecutive time simulation

### 1.1 Parameters
- $W_l$      : Weight of lot $l$
- $d_{l}$        : Due date of lot $l$      
- $p_{(l,sl),i}$  : Process time of $(l,sl)$ on family $i$
- $sl\in \{1,2,...,Sl\}$ : one step of lot $l$
    - $Sl=$ the final step of lot $l$
    - for example, $S3=5$ means that there are $5$ steps total to finish lot $l=3$, and therefore $s3\in\{1,2,...,5\}$

### 1.2 Decision variables
IFF the step $sl$ of the lot $l$ is assigned to be processed at family $i$:
- $a_{(l,sl),i}=1$, otherwise zero
  
IFF $(l,sl)$ is firstly processed at family $i$ machine $j$
- $w_{(l,sl),i,j} = 1$, otherwise zero

IFF $(l',sl')$ just precedes $(l,sl)$:
- $x_{(l',sl'),(l,sl),i} = 1$, otherwise zero

Time:
- Start time: $t_{(l,sl)}$
- Completion time: $C_{l}$
- $L_{l} \geq \max(0,C_l-d_l)$

### 1.3 Objective
Minimize the total penalty (lateness $\times$ priority)
$$\min \sum_l W_lL_l$$
### 1.4 Constraints
1. Each $(l,sl)$ can be only assigned to one family type
$$\sum_i a_{(l,sl),i} = 1\;\;\;\;\forall (l,sl)$$
2. Each $(l,sl)$ must be ==proceeded== by one process step or be the first,
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
### 



```py
random.seed(0)
# #lots
L = 6
# #steps of lot l (firstly assume it same for all the lots)
Sl = 10
# #families
I = 3
# #machines in each family, e.g., family 3 has 1 machine
Js = [3,2,1]

M = 120
```


```py
        # -------------------
        # -------------------
        for lp,slp in itertools.product(range(1, L+1), range(1, Sl+1)):
            prob += x[lp,slp,l,sl,i] <= a[l,sl,i]

        for j in range(1, Js[i-1]+1):
            prob += w[l,sl,i,j] <= a[l,sl,i]
        # -------------------
        # -------------------


        # --------------------------------
        #---------------------------------
        for slp in range(sl+1,Sl+1):
            prob += x[l,slp,l,sl,i] == 0
        # --------------------------------
        #---------------------------------
```