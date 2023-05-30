
# Summary

## 1. Flow_Type

> **Sheet**: Summary
> **Table**: Flow_Type
![[Pasted image 20230518114753.png]]
==以上这张表格的前两列会重复出现在所有的 Tool_Type Sheets 中, 并和另外两列新的一起, 被命名为 Tool_Type_Flows==

## 2. Tool_Type

> **Sheet**: Summary
> **Table**: Tool_Type
![[Pasted image 20230518104939.png]]

### Target
depends on **Location**

### WSPW
对指定 Tool_Type_Flows 中的 "Outs" 列求和

> Sheet: Liftoff
> Table: Liftoff_Flows
> ![[Pasted image 20230518105350.png]]

```c
=IFERROR(
	SUM(
		# 返回 Table Liftoff_Flows 中的 "Outs" 列
		INDEX(
		    # 指向 Liftoff_Flows
	        INDIRECT(CONCATENATE([@[Tool_Type]],"_Flows")),
	        # 行号: 0 说明返回整列
	        0,
	        # 列号: 3 (对应的是 "Outs" 在指定 Array 中排第几个)
	        MATCH("Outs",
		        # 指向 Liftoff_Flows 的 Headers ([Flow_Type, Demand, Outs, % of WSPW])
		        INDIRECT(CONCATENATE([@[Tool_Type]],"_Flows[#Headers]")),
		        0
		    )
		)
	),
	0
)

```

### Future Capacity
Manually input

### Location
Front or TWV #Problem meaning?

### Total Capacity

### Availability
对指定 Tool_Type_Tools 中的 "Availability" 列求均值

> **Sheet**: Liftoff
> **Table**: Liftoff_Tools 
![[Pasted image 20230518104613.png]]

#Problem any reasaon for using `@Tool_Type[@[Tool_Type]:[Tool_Type]]` instead of just `[@[Tool_Type]]`?
```c
=IFERROR(
	AVERAGE(
		INDEX(
			# 指向 Liftoff_Tools
			INDIRECT(CONCATENATE(@Tool_Type[@[Tool_Type]:[Tool_Type]],"_Tools")),
			0,
			# 列号: 4 (对应的是 Headers 中 "Availability" 所在的位置)
			MATCH(
				# 指向 Tool_Type 表格(在 Summary Sheet 中)的 Headers 中的 Availability 所对应的单元格中的内容 (实际上也就是 "Availability")
				Tool_Type[[#Headers],[Availability]],
				INDIRECT(CONCATENATE(@Tool_Type[@[Tool_Type]:[Tool_Type]],"_Tools[#Headers]")),
				0
			)
		)
	),
	0%
)
```

### Utilization, **Planning Factor**, **Rework**
similar to **Availability**

### % of Target 
:= WSPW / Target

### Weighted Layers
把 "Weighted Layer?", "Sampling Rate", "%" 这三列每行元素相乘然后再加起来

> Sheet: Liftoff
> Table: Liftoff (最大的一张和 Sheet 同名的 Table)
![[Pasted image 20230518112538.png]]

```c
=IFERROR(IF(
	[@[Tool_Type]]="Lift_Off",
	# 如果 Tool_Type == Lift_Off, 运行以下 (但是好像没找到有 Tool_Type 叫做这个名字)
	SUMPRODUCT(...),
	# 否则运行以下
	SUMPRODUCT(
		INDEX(
			INDIRECT(CONCATENATE(@Tool_Type[@[Tool_Type]:[Tool_Type]])),0,
			MATCH("Weighted Layer?",INDIRECT(CONCATENATE(@Tool_Type[@[Tool_Type]:[Tool_Type]],"[#Headers]")),0)
		),
		INDEX(
			INDIRECT(CONCATENATE(@Tool_Type[@[Tool_Type]:[Tool_Type]])),0,
			MATCH("Sampling Rate",INDIRECT(CONCATENATE(@Tool_Type[@[Tool_Type]:[Tool_Type]],"[#Headers]")),0)
		),
		INDEX(
			INDIRECT(CONCATENATE(@Tool_Type[@[Tool_Type]:[Tool_Type]])),0,
			MATCH("%",INDIRECT(CONCATENATE(@Tool_Type[@[Tool_Type]:[Tool_Type]],"[#Headers]")),0)
		)
	)
),
0%)
```

### # of Tools
统计满足要求的(Tool_ID != Tool_Type_Placeholder) Entity 的数量

> **Sheet**: Liftoff
> **Table**: Liftoff_Tools 
![[Pasted image 20230518104613.png]]

```c
=COUNTIF(
	# 返回 Liftoff_Tools 的 "Tool" 列
	INDEX(
		INDIRECT(CONCATENATE(@Tool_Type[@[Tool_Type]:[Tool_Type]],"_Tools")),
		0,
		MATCH("Tool",INDIRECT(CONCATENATE(@Tool_Type[@[Tool_Type]:[Tool_Type]],"_Tools[#Headers]")),0)
	),
	# 筛选出名字不等于 Liftoff_Placeholder 的 Entity
	"<>" & CONCATENATE([@[Tool_Type]],"_Placeholder")
)
```

### Errors
把 Tool_Type 和 Tool_Type_Tools 的 "Errors" 列全都加起来

>**Sheet**: Liftoff
>**Table1**: Liftoff 
>**Table2**: Liftoff_Tools 
![[Pasted image 20230518104613.png]]

```c
=IFERROR(
	# 求和 Liftoff 的 "Errors" 列
	SUM(INDEX(
		INDIRECT([@[Tool_Type]]), 0,
		MATCH(Tool_Type[[#Headers],[Errors]],INDIRECT(CONCATENATE([@[Tool_Type]],"[#Headers]")),0)
	)) + 
	# 求和 Liftoff_Tools 的 "Errors" 列
	SUM((INDEX(
			INDIRECT(CONCATENATE([@[Tool_Type]],"_Tools")), 0,
			MATCH(Tool_Type[[#Headers],[Errors]],INDIRECT(CONCATENATE([@[Tool_Type]],"_Tools[#Headers]")),0)
	)),
	0
)
```




# Promis Equipment
Mapping between "EQPTYPE" and "Tool_Type"

![[Pasted image 20230518115120.png]]



# Tool_Type: Liftoff

## 1. Liftoff_Outs

> Sheet: Liftoff
> Table: Liftoff_Outs
![[Pasted image 20230518140359.png]]

## 2. Liftoff_Flows

> Sheet: Liftoff
> Table: Liftoff_Flows
![[Pasted image 20230518115650.png]]

### Flow_Type, Demand
照搬 Summary Sheet --> Flow_Type Table 的前两行

### Outs


## 3. Liftoff

All the values in the following table part are manual input
- ==除了 Sampling Rate, 例如 Acid_Bench_BS 需要梳理一下== #todo
- 红色方框内的数据指的是？ #Problem 

> Sheet: Liftoff
> Table: Liftoff (left part)
![[Pasted image 20230518120307.png]]

> Sheet: Liftoff
> Table: Liftoff (mid part)
![[Pasted image 20230518120613.png]]

### %
从 `Flow_Comparison` 表格中查找满足条件 (stage, tool_type 相同) 的数据填进来

```c
=IFERROR(
	LOOKUP(
		2,
		1/((Flow_Comparison[STAGE]=[@Stage]) * (Flow_Comparison[Tool_Type]=Liftoff_Outs[Tool_Type])),
		Flow_Comparison[%]
	),
	1
)
```

这个函数需要一步步拆解来看，我们假设
- `Flow_Comparison[STAGE]` = {"st1", "st2", "st2", "st3"}
- `Flow_Comparison[Tool_Type]` = {"t1", "t1", "t2", "t3"}
- `[@Stage]` = "st2"
- `Liftoff_Outs[Tool_Type]` = "t1"

那么
1. `(Flow_Comparison[STAGE]=[@Stage])`  = {False, True, True, False} = {0, 1, 1, 0}
2. `(Flow_Comparison[Tool_Type]=Liftoff_Outs[Tool_Type])` = {True, True, False, False} = {1, 1, 0, 0}
3. `((1) * (2))` = {0, 1, 0, 0}
4. `1/((1) * (2))` = {**#DIV/0!**, 1, **#DIV/0!**, **#DIV/0!**}

由于 `LOOKUP(2, 1/((1) * (2)), Flow_Comparison[%])` 会首先查找 `1/((1) * (2))` 中等于 2 的元素的 index, 然后返回 `Flow_Comparison[%]` 中对应 index 的元素。==但如果没找到==, 则会查找 the index of the ==LAST== value in the array which is less than the lookup_value, 然后返回 `Flow_Comparison[%]` 中对应 index 的元素。因此
- `LOOKUP(2, 1/((1) * (2)), Flow_Comparison[%])` 会返回 `Flow_Comparison[%]` 的第二个元素


## 4. Liftoff_Tools
储存 Tool_Type (Liftoff) 所包含的所有 Entity ID 及其其他信息

> Sheet: Liftoff
> Table: Liftoff_Tools
![[Pasted image 20230519110235.png]]

### Availability - Hours Per Week
都是 manual input

### Actual Hours Per Week
= [Hours Per Week] 依次乘上前面四个 factors



