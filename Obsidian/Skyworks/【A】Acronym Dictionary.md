|Acronym| Definition                         |
|-------|------------------------------------|
|BAW    | Bulk Acoustic Wave 散装声波滤波器   |
|Bi-    | Bipolar- 双极的                    |
|CTM| Capacitor Top Metal 半导体内的一种结构层|
|DPS    | Die (or Dice) Processing           |
|FET    | Field-Effect Transistor            |
|GDPW   | Gross Die Per Wafer (e5)           |
|HBT    | Heterojunction Bipolar Transistors 异质结双极晶体管   <br> e.g. AlGaAs, GaAs HBT                   |
|HFET   | High-Electron-Mobility Transistor <br> aka. Heterostructure FET (HFET)
|IC     | Integrated Circuit                 |
|MRP    | Material Requirements Planning     |
|MSO| Metrology Sampling Optimizer 计量采样优化器| 
|PM     | Preemptive Maintanance             |
|prd| prodcution|
|SAW    | Surface Acoustic Wave 表面声波滤波器|
|SOAK   | Second of a Kind                   |
|WSPD   | Wafter Starts Per Day              |
|WSPM   | Wafer Starts Per Month             |


CTM
- Capacitor Top Metal 半导体内的一种结构层
- Cycle Time: Table [WIP_CTM_FORECAST![](https://help.inficonims.com/images/icons/linkext7.gif)](https://help.inficonims.com/display/SCHEMAS/TABLES?run_1=run&run_1_tablename=WIP_CTM_FORECAST&run_2=run&run_2_tablename=WIP_CTM_FORECAST) contains the forecast of total cycle time by prd for upcoming weeks, months, quarters, and/or years

MSO
- Metrology Sampling Optimizer 计量采样优化器: [MSO Database Tables - Metrology Sampling Optimizer - INFICON IMS Help Site](https://help.inficonims.com/display/MSO/MSO+Database+Tables)



## Relation Map

==Eqp_type = Process_family = Tool_group (和前两者略有不同，会更多一些，但是可以理解为相同)==

#Problem 实际上, eqp_type 和 process_family 是不同的，详见 [[#FPSBASE#RTG_PROCESS_RCP_EQPTYPES]]。而且，一个 process 可以运行在多个 eqp_type 上（当然一个 process 肯定是只属于一个 process_family 的）

#### Route

| From| To| Relation| Source|
|--|--|--|--|
| ***Route*** | Process | (1-n)| [RTG_ROUTE_STEPS](###RTG_ROUTE_STEPS)|
|***Route***| Recipe | (1-n)| FPSBASE > RTG_ROUTE_STEPS_PLUS|

#### Eqp_type
***(Tool_group)***

| | | | |
|--|--|--|--|
| Tool                       | ***Eqp_type*** and Bay | |  [[#EQP_TOOLS]]
| ***Tool_group***            | Module             |   | [[#EQP_TOOL_MSO_GROUPS]] 174 rows
| ***Eqp_type*** and Recipe| UPH                    | (1-1) | [[#CM_P_RORP_STEP_EQPTYPES]]
|***Eqp_type***, Process, and Recipe| UPH/MPU| (1-1)| [[#FPSBASE#RTG_PROCESS_RCP_EQPTYPES]]

#### Tool

| | | | |
|--|--|--|--|
| Chamber |***Tool***          |             |         [[#EQP_CHAMBERS]]
| ***Tool***      | Eqp_type and Bay       | |  [[#EQP_TOOLS]]
|***Tool***         | Process              |   (n-n) | [[#RTG_TOOL_ASSIGNMENTS]]
|Recipe     | ***Tool***                   |   (n-n) | [[#RTG_PROCESS_RCP_TOOL_BASE]]

#### Process_family

| | | | |
|--|--|--|--|
| ***Process_family***      | Module                | | [[#RTG_PROCESS_FAMILIES]]    84 rows
| Process                  | ***Process_family***   | | [[#RTG_PROCESSES]]

#### Process

| | | | |
|--|--|--|--|
|Route    | list(***Process***)     |   |      [[#RTG_PROCESSES]]
|***Process*** | Process_family | (n-1) |[[#RTG_PROCESSES]]
|Tool      | ***Process***        |    (n-n) |[[#RTG_TOOL_ASSIGNMENTS]]
|Eqp_type, ***Process***, and Recipe| UPH/MPU| (1-1)| [[#FPSBASE#RTG_PROCESS_RCP_EQPTYPES]]

#### Recipe

| | | | |
|--|--|--|--|
| ***Recipe***                    | Tool |(n-n) | [[#RTG_PROCESS_RCP_TOOL_BASE]]
| Eqp_type and ***Recipe*** | ==UPH==          |(1-1) | [[#FPSAPP#CM_P_RORP_STEP_EQPTYPES]]
|Eqp_type, Process, and ***Recipe***| UPH/MPU| (1-1)| [[#FPSBASE#RTG_PROCESS_RCP_EQPTYPES]]

#### Bay

| | | | |
|--|--|--|--|
| Tool | Eqp_type and ***Bay*** | | [[#EQP_TOOLS]]


## FPSAPP
### CM_P_RORP_STEP_EQPTYPES
[CM_P_RORP_STEP_EQPTYPES](https://help.inficonims.com/display/SCHEMAS/FPSAPP+Schema#cmprorpstepeqptypes)
关联 Recipe, Eqp_type 到 ==UPH==
- 在同一个 Eqp_type 中的使用同一个 Recipe 的 Tool 的 UPH 相同
- 同一个 Recipe 可以出现在不同的 Eqp_type 中，此时他们的 UPH 也可能不同

---

## FPSBASE
### RTG_PROCESS_RCP_EQPTYPES
[RTG_PROCESS_RCP_EQPTYPES](https://help.inficonims.com/display/SCHEMAS/TABLES?run_1=run&run_1_tablename=RTG_PROCESS_RCP_EQPTYPES&run_2=run&run_2_tablename=RTG_PROCESS_RCP_EQPTYPES)
map [[#Eqp_type]], [[#Process]], and [[#Recipe]] to UPH/MPU

| |eqp_type|process|est_machine_recipe|mpu|
|---|---|---|---|---|
|0|N_EVAP|CC METAL DEPOSITION|7S332|4.3617|
|1|N_EVAP|CC METAL DEPOSITION|8S347|4.9096|
|2|N_EVAP|CC METAL DEPOSITION|9S428|3.9575|
|3|N_EVAP|CC METAL DEPOSITION|T1046|4.5121|
|4|N_EVAP|CC METAL DEPOSITION|U0233|4.5121|
(3926 rows)
```sql
SELECT eqp_type, process, EST_MACHINE_RECIPE, mpu
FROM FPSBASE.RTG_PROCESS_RCP_EQPTYPES
```

### RTG_ROUTE_STEPS_PLUS
[RTG_ROUTE_STEPS_PLUS](https://help.inficonims.com/display/SCHEMAS/TABLES?run_1=run&run_1_tablename=RTG_ROUTE_STEPS_PLUS&run_2=run&run_2_tablename=RTG_ROUTE_STEPS_PLUS)
map [[#Route]] to [[#Process]] and [[#Recipe]]

```sql

```

### THP_EQPTYPE_SUMMARY
[THP_EQPTYPE_SUMMARY](https://help.inficonims.com/display/SCHEMAS/TABLES?run_1=run&run_1_tablename=THP_EQPTYPE_SUMMARY&run_2=run&run_2_tablename=THP_EQPTYPE_SUMMARY)

**Empty Columns**:
- mpu_trusted
- mpu_lcl
- mpu_ucl

### THP_TOOL_SUMMARY

---

## FPSINPUT
### EQP_CHAMBERS 
[EQP_CHAMBERS](https://help.inficonims.com/display/SCHEMAS/TABLES?run_1=run&run_1_tablename=EQP_CHAMBERS&run_2=run&run_2_tablename=EQP_CHAMBERS)

| |chamber|tool|
|---|---|---|
|0|N_ACID9D|N_ACID09|
|1|N_ACID9M|N_ACID09|
|2|N_ACI19L|N_ACID19|
|3|N_ACI19R|N_ACID19|
(110 rows)
```sql
SELECT CHAMBER, TOOL
FROM FPSINPUT.EQP_CHAMBERS
ORDER BY TOOL
```

==粗浅理解:== chamber 为 tool 的一部分，大多数 tool 都只有一个 chamber，因此不会出现在这张表中。对于同一个 tool 中的不同 chamber，它们可以被用于处理不同的 process





### EQP_TOOLS
[EQP_TOOLS](https://help.inficonims.com/display/SCHEMAS/TABLES?run_1=run&run_1_tablename=EQP_TOOLS&run_2=run&run_2_tablename=EQP_TOOLS)
关联 tool 到 eqp_type, bay
**Empty Columns**:
- max_carriers_to_reserve

| |tool|eqp_type|bay|
|---|---|---|---|
|0|N_GOLF15|N_GOLF|GOLF|
|1|N_ASYHLD|N_ASYHLD|N_ASSY|
|2|N_DUMASY|N_DUMMYA|N_ASSY|
|3|N_FOI02|N_FOI|N_ASSY|
|4|N_FOI01|N_FOI|N_ASSY|
(588 rows)
```sql
SELECT DISTINCT TOOL, EQP_TYPE, BAY
FROM FPSINPUT.EQP_TOOLS
ORDER BY BAY, EQP_TYPE
```





### EQP_TOOL_MSO_GROUPS 
[EQP_TOOL_MSO_GROUPS](https://help.inficonims.com/display/SCHEMAS/TABLES?run_1=run&run_1_tablename=EQP_TOOL_MSO_GROUPS&run_2=run&run_2_tablename=EQP_TOOL_MSO_GROUPS)
关联 tool_group (eqp_type) 到 module

| |tool_mso_group|tool_mso_module|
|---|---|---|
|0|N_CHILL|N_CHILL|
|1|N_GOLF|N_GOLF|
|2|N_OFF|N_OFF|
|3|N_AOI|METROLOG|
|4|N_POLVAR|N_POLVAR|
(174 rows)
```sql
SELECT TOOL_MSO_GROUP, TOOL_MSO_MODULE
FROM FPSINPUT.EQP_TOOL_MSO_GROUPS
```

|   |   |
|---|---|
|TOOL_MSO_GROUP|TOOL_MSO_GROUP is the grouping of tools used for Metrology Sampling Optimizer. This grouping is used in the Sampling Dashboard and for assigning event based sampling rules for a tool group. This group is similar to process family but allows a tool grouping specific to the MSO.|||||
|TOOL_MSO_MODULE|TOOL_MSO_MODULE is the module responsible for the tool_mso_groups used for the Metrology Sampling Optimizer. The module is used for building the tool hierarchy for the Sampling Dashboard.|

Module 可以包含多个 Group:

| |tool_mso_module|COUNT|
|---|---|---|
|0|START|3|
|1|PHOTO|6|
|2|FINAL|23|
|3|DRY ETCH|4|
|4|TWV|13|
|5|METROLOG|11|
|6|CLEAN|7|
|7|LIFT|3|
|8|PROBE|7|
|9|METALS|2|
|10|NA|22|
```sql
SELECT TOOL_MSO_MODULE, COUNT(*)
FROM FPSINPUT.EQP_TOOL_MSO_GROUPS
GROUP BY TOOL_MSO_MODULE
HAVING COUNT(*) > 1
```





### RTG_PROCESSES 
[RTG_PROCESSES](https://help.inficonims.com/display/SCHEMAS/TABLES?run_1=run&run_1_tablename=RTG_PROCESSES&run_2=run&run_2_tablename=RTG_PROCESSES)
关联 process 到 process_group (tool_group, eqp_type)

| |process|process_group|
|---|---|--|
|0|Tape Lift (42nd)|N_TAPE|
|1|FP PREP FOR DEBOND|N_PKG|
|2|GL INTEGRATED ETCH|N_ACIDE|
|3|GL PRE METAL CLEAN|N_ACIDM|
|4|CRYSTAL BOND BONDING/INSPECTION|N_WAXMNT|
(1246 rows)
```sql
SELECT PROCESS, PROCESS_GROUP
FROM FPSINPUT.RTG_PROCESSES
```





### RTG_PROCESS_FAMILIES
[RTG_PROCESS_FAMILIES](https://help.inficonims.com/display/SCHEMAS/TABLES?run_1=run&run_1_tablename=RTG_PROCESS_FAMILIES&run_2=run&run_2_tablename=RTG_PROCESS_FAMILIES)
关联 Process_family 到 Module
**Empty Columns**:
- default_qty_meas
- max_step_sec
- min_step_sec
- MAX_PROC_TIME_SEC

| |process_family |module|
|---|---|--|
|0|N_ACIDD|CLEAN|
|1|N_DUMMYP|PHOTO|
|2|N_SCOPE|FINAL|
|3|N_SEM|METROLOG|
|4|N_PVETCH|DRY ETCH|
(84 rows)
```sql
SELECT process_family, module
FROM FPSINPUT.RTG_PROCESS_FAMILIES
```




### RTG_PROCESS_RCP_TOOL_BASE
[RTG_PROCESS_RCP_TOOL_BASE](https://help.inficonims.com/display/SCHEMAS/TABLES?run_1=run&run_1_tablename=RTG_PROCESS_RCP_TOOL_BASE&run_2=run&run_2_tablename=RTG_PROCESS_RCP_TOOL_BASE)
关联 Recipe 到 Tool (n2n): 同一个 Recipe 可以被运行在多个 Tool，同一个 Tool 也可以运行多个 Recipe

| |est_machine_recipe|tool|
|---|---|---|
|0|5S445|N_CND01|
|1|5S445|N_CND02|
|2|5S445|N_NIKO09|
|3|5S445|N_NIKO11|
|4|5S445|N_NIKO16|
(17584 rows)
```sql
SELECT est_machine_recipe, tool
FROM FPSINPUT.RTG_PROCESS_RCP_TOOL_BASE
```




### RTG_ROUTE_STEPS 
[RTG_ROUTE_STEPS](https://help.inficonims.com/display/SCHEMAS/TABLES?run_1=run&run_1_tablename=RTG_ROUTE_STEPS&run_2=run&run_2_tablename=RTG_ROUTE_STEPS)
关联 Route 到 list(Process)

**Empty Columns**:
- FUTURE_WIP_STEP
- SPEC_ID

|-|route|step|process|seq_num|script_id|
|---|---|---|---|---|---|
|0|N_6AOI_INSPECT|001.000=2S291|AOI INSPECTION|1.0|N_6AOI_INSPECT:001.000|
|1|N_6AOI_INSPECT|001.100=2S533|ENG REVIEW OF CL LOT|2.0|N_6AOI_INSPECT:001.100|
|2|N_6AOI_SMPL_AA|002.000,N_6AOI_SMPL_AA:001.000=2S576|AA SAMPLE AOI|1.0|N_6AOI_SMPL_AA:001.000|
|3|N_6AOI_SMPL_AA|002.000,N_6AOI_SMPL_AA:001.700=2S576|AA SAMPLE AOI|2.0|N_6AOI_SMPL_AA:001.700|
```sql
SELECT ROUTE, STEP, PROCESS, SEQ_NUM, SCRIPT_ID
FROM FPSINPUT.RTG_ROUTE_STEPS
ORDER BY ROUTE, SEQ_NUM
```

| | |
|-|-|
|STEP|A single processing step within a route representing a single tool visit.
|PROCESS|Process defines what occurs at a step. Different steps can share the same process if they are identical. Process should normally determine allowed tools and recipe
|SCRIPT_ID| This column references the name of script used to process lots at this step. Different MES use different terminology but the key to this column is its use to determine batches. Lots with the same script_id and same batch_criteria from RTG_TOOL_ASSIGNMENTS can be batched together. Therefore this is critical column for scheduling on batch tools.



### RTG_TOOL_ASSIGNMENTS
[RTG_TOOL_ASSIGNMENTS](https://help.inficonims.com/display/SCHEMAS/TABLES?run_1=run&run_1_tablename=RTG_TOOL_ASSIGNMENTS&run_2=run&run_2_tablename=RTG_TOOL_ASSIGNMENTS)
关联 Tool 到 Process (==n2n==)

| |TOOL|PROCESS|
|---|---|---|
|0|N_PLSH71|SLOPED THROUGH WAFER VIA ETCH RECOVERY|
|1|N_PLSH71|THROUGH WAFER VIA ETCH RECOVERY|
|2|N_PLSH71|VA 20x40 VIA ICP ETCH|
|3|N_PLSH71|VA SLOPED ICP ETCH|
|4|N_PLSH73|SLOPED THROUGH WAFER VIA ETCH RECOVERY|
(6651 rows)
```sql
SELECT TOOL, PROCESS
FROM FPSINPUT.RTG_TOOL_ASSIGNMENTS
```




### Empties
EQP_BADGES
RTG_OVR_CS_SORT_RT_FAM_SEG

[RTG_PRD_CTM_SERIES](https://help.inficonims.com/display/SCHEMAS/TABLES?run_1=run&run_1_tablename=RTG_PRD_CTM_SERIES&run_2=run&run_2_tablename=RTG_PRD_CTM_SERIES)
RTG_PRD_STEP_OVR

RTG_PROCESS_COUNTER_ASGNS

RTG_ROUTE_STEP_EQPTYPE_OVR

RTG_TOOL_ASGN_LOT_PRCS_PATH
[RTG_TOOL_ASGN_LOT_PROCESS](https://help.inficonims.com/display/SCHEMAS/TABLES?run_1=run&run_1_tablename=RTG_TOOL_ASGN_LOT_PROCESS&run_2=run&run_2_tablename=RTG_TOOL_ASGN_LOT_PROCESS) (只有三行，很怪)
RTG_TOOL_ASGN_ROUTE_STEP

THP_EXTERNAL
THP_MANUAL

[WIP_DEMAND![](https://help.inficonims.com/images/icons/linkext7.gif)](https://help.inficonims.com/display/SCHEMAS/TABLES?run_1=run&run_1_tablename=WIP_DEMAND&run_2=run&run_2_tablename=WIP_DEMAND)
[WIP_CTM_FORECAST](https://help.inficonims.com/display/SCHEMAS/TABLES?run_1=run&run_1_tablename=WIP_CTM_FORECAST&run_2=run&run_2_tablename=WIP_CTM_FORECAST)







