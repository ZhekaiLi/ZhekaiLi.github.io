## Relation Map

==Eqp_type = Process_family = Tool_group (和前两者略有不同，会更多一些，但是可以理解为相同)==

#Problem 实际上, eqp_type 和 process_family 是不同的，详见 [[#FPSBASE#RTG_PROCESS_RCP_EQPTYPES]]。而且，一个 process 可以运行在多个 eqp_type 上（当然一个 process 肯定是只属于一个 process_family 的）

#### Route

| From| To| Relation| Source|
|--|--|--|--|
| ***Route*** | Process - Recipe | (1-n)| [[#FPSINPUT#RTG_ROUTE_STEPS]]|
|***Route***| Eqp_type - Process - Recipe | (1-n)| [[#FPSBASE#RTG_ROUTE_STEPS_PLUS]]|

#### Eqp_type
***(Tool_group)***

| | | | |
|--|--|--|--|
| Tool                       | ***Eqp_type*** and Bay | |  [[#FPSINPUT#EQP_TOOLS]]
| ***Tool_group***            | Module             |   | [[#EQP_TOOL_MSO_GROUPS]] 174 rows
| ***Eqp_type*** and Recipe| UPH                    | (1-1) | [[#CM_P_RORP_STEP_EQPTYPES]]
|***Eqp_type***, Process, and Recipe| UPH/MPU| (1-1)| [[#FPSBASE#RTG_PROCESS_RCP_EQPTYPES]]

#### Tool

| | | | |
|--|--|--|--|
| Chamber |***Tool***              |       | [[#EQP_CHAMBERS]]
| ***Tool***    | Eqp_type and Bay |       | [[#FPSINPUT#EQP_TOOLS]]
| ***Tool***    | Process          | (n-n) | [[#RTG_TOOL_ASSIGNMENTS]]
| Recipe  | ***Tool***             | (n-n) | [[#FPSINPUT#RTG_PROCESS_RCP_TOOL_BASE]]

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



---
## FPSAPP

### CM_P_RORP_STEP_EQPTYPES
[CM_P_RORP_STEP_EQPTYPES](https://help.inficonims.com/display/SCHEMAS/FPSAPP+Schema#cmprorpstepeqptypes)

map ([[#Recipe]] - [[#Eqp_type]]) to ==UPH==/MPU
- e.g. `dict_recipe2eqpTypeMUP[recp_1][eqpT_1]=5` means that for the Tools in `eqpT_1` that can process `recp_1`, their average MPU is 5 mins per unit (wafer)
- Recipe to Eqp_type is n2n relation

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
[RTG_ROUTE_STEPS_PLUS](https://help.inficonims.com/display/SCHEMAS/TABLES?run_1=run&run_1_tablename=RTG_ROUTE_STEPS_PLUS&run_2=run&run_2_tablename=RTG_ROUTE_STEPS_PLUS), compared to [[#FPSINPUT#RTG_ROUTE_STEPS]], contain Eqp_type but with less data（17300 < 20723）

map [[#Route]] to list([[#Eqp_type]] - [[#Process]] - [[#Recipe]])

| |route|eqp_type|process|recipe|seq_num|
|---|---|---|---|---|---|
|0|N_6BIFET4-PA-P2_1+N_6TWV+N_6P07_TWV-ETC+N_6FPO...|NA|SM|SM|1.0|
|1|N_6BIFET4-PA-P2_1+N_6TWV+N_6P07_TWV-ETC+N_6FPO...|N_SAPST|SAP LOT START|1N982|2.0|
|2|N_6BIFET4-PA-P2_1+N_6TWV+N_6P07_TWV-ETC+N_6FPO...|N_SAPST|LOTS KITTED AND READY FOR SCRIBE|1NN02|3.0|
|3|N_6BIFET4-PA-P2_1+N_6TWV+N_6P07_TWV-ETC+N_6FPO...|N_LASER|LS WAFER SCRIBE|2S053|4.0|
|4|N_6BIFET4-PA-P2_1+N_6TWV+N_6P07_TWV-ETC+N_6FPO...|N_TOFAB|MOVE LOT TO FAB|2S405|5.0|
(17300 rows)
```sql
SELECT route, eqp_type, process, RTG_PARM1 as recipe, seq_num
FROM FPSBASE.RTG_ROUTE_STEPS_PLUS
ORDER BY route, seq_num
```
#Problem 这里的 RTG_PARM1 是否就指的是 recipe，有没有可能包含其他类型的数据
#Problem 这里的 RTG_PARM1 内包含 None，是否可以直接忽略
#Problem 去除 NULL 后还剩下 263 个 RTG_PARM1 无法在 FPSBASE > RTG_PROCESS_RCP_TOOL_BASE 中找到，代码如下
```sql
SELECT distinct rtg_parm1 FROM FPSBASE.RTG_ROUTE_STEPS_PLUS
WHERE rtg_parm1 IS NOT NULL AND rtg_parm1 NOT IN (
    SELECT est_machine_recipe FROM FPSBASE.RTG_PROCESS_RCP_TOOL_BASE
)
```
#Problem 这些 263 个无法在 RTG_PROCESS_RCP_TOOL_BASE 中找到的 RTG_PARM1 出现在了 49 个 route 中，只有另外 12 个 route 不包含这些遗失值，代码如下
```sql
WITH T1 AS (
    SELECT route FROM FPSBASE.RTG_ROUTE_STEPS_PLUS
    WHERE rtg_parm1 IS NOT NULL AND rtg_parm1 NOT IN (
        SELECT est_machine_recipe FROM FPSBASE.RTG_PROCESS_RCP_TOOL_BASE
    )
)
SELECT DISTINCT route FROM FPSBASE.RTG_ROUTE_STEPS_PLUS
WHERE route IN (SELECT route FROM T1)
```





### THP_EQPTYPE_SUMMARY
[THP_EQPTYPE_SUMMARY](https://help.inficonims.com/display/SCHEMAS/TABLES?run_1=run&run_1_tablename=THP_EQPTYPE_SUMMARY&run_2=run&run_2_tablename=THP_EQPTYPE_SUMMARY)

**Empty Columns**:
- mpu_trusted
- mpu_lcl
- mpu_ucl


#Problem 有时间注意以下 THP_TOOL_AUTO 和 SUMMARY

```sql
with T1 as (
    SELECT process, count(distinct eqp_type)
    FROM FPSBASE.THP_TOOL_AUTO
    group by process
    having count(distinct eqp_type) > 1
), T2 as (
    SELECT PROCESS, PROCESS_GROUP
    FROM FPSINPUT.RTG_PROCESSES
), T3 as (
    select T.process, T.eqp_type, T2.process_group
    from FPSBASE.THP_TOOL_AUTO T
    left join T2
    on T.process = T2.process
    where T.process in (select process from T1) and T.eqp_type = T2.process_group
), T4 as (
    select *
    from T1
    where T1.process not in (select process from T3)
)
select process, eqp_type, tool, actual_machine_recipe
from FPSBASE.THP_TOOL_AUTO
where process in (select process from T4)
order by process, eqp_type


# 这些 process 不仅对应多个 eqp_type
# 并且这些 eqp_type 还无法在 process --- process_family 的 process_family 那一栏找到
# 因此需要单独指定
df = pd.read_sql(query, engine)
df
```

以及
```sql
with T1 as (
    SELECT process, count(distinct eqp_type)
    FROM FPSBASE.THP_TOOL_AUTO
    group by process
    having count(distinct eqp_type) > 1
), T2 as (
    SELECT PROCESS, PROCESS_GROUP
    FROM FPSINPUT.RTG_PROCESSES
), T3 as (
    select T.process, T.eqp_type, T2.process_group
    from FPSBASE.THP_TOOL_AUTO T
    left join T2
    on T.process = T2.process
    where T.process in (select process from T1) and T.eqp_type = T2.process_group
)
from T3
```

以及 
```sql
SELECT process, eqp_type, count(distinct tool)
FROM FPSBASE.THP_TOOL_AUTO
where process <> 'DL HBTMIM PRE CLEAN' and process <> 'GL NITRIDE CLEAN'
group by process, eqp_type
having count(distinct tool) > 2
```

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
[EQP_TOOLS](https://help.inficonims.com/display/SCHEMAS/TABLES?run_1=run&run_1_tablename=EQP_TOOLS&run_2=run&run_2_tablename=EQP_TOOLS), the same as FPSBASE.[EQP_TOOLS_PLUS](https://help.inficonims.com/display/SCHEMAS/TABLES?run_1=run&run_1_tablename=EQP_TOOLS_PLUS&run_2=run&run_2_tablename=EQP_TOOLS_PLUS)

map [[#Tool]] to [[#Eqp_type]] and [[#Bay]]

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

map Tool_group ([[#Eqp_type]]) to Module

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

Module could contain several Tool_groups:

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

map [[#Process]] to [[#Process_family]]

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

map [[#Process_family]] to Module

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
[RTG_PROCESS_RCP_TOOL_BASE](https://help.inficonims.com/display/SCHEMAS/TABLES?run_1=run&run_1_tablename=RTG_PROCESS_RCP_TOOL_BASE&run_2=run&run_2_tablename=RTG_PROCESS_RCP_TOOL_BASE), same as FPSBASE > [RTG_PROCESS_RCP_TOOL_BASE](https://help.inficonims.com/display/SCHEMAS/TABLES?run_1=run&run_1_tablename=RTG_PROCESS_RCP_TOOL_BASE&run_2=run&run_2_tablename=RTG_PROCESS_RCP_TOOL_BASE)

map [[#Recipe]] to [[#Tool]] (n2n)

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
[RTG_ROUTE_STEPS](https://help.inficonims.com/display/SCHEMAS/TABLES?run_1=run&run_1_tablename=RTG_ROUTE_STEPS&run_2=run&run_2_tablename=RTG_ROUTE_STEPS), compared to [[#FPSBASE#RTG_ROUTE_STEPS_PLUS]], 不包含 Eqp_type 但数据总量更大（20723 > 17300）

map [[#Route]] to list([[#Process]] - [[#Recipe]])

**Empty Columns**:
- FUTURE_WIP_STEP
- SPEC_ID

| |route|step|process|recipe|seq_num|
|---|---|---|---|---|--|
|0|N_6AOI_INSPECT|001.000=2S291|AOI INSPECTION|2S291|1.0|
|1|N_6AOI_INSPECT|001.100=2S533|ENG REVIEW OF CL LOT|2S533|2.0|
|2|N_6AOI_SMPL_AA|002.000,N_6AOI_SMPL_AA:001.000=2S576|AA SAMPLE AOI|2S576|1.0|
|3|N_6AOI_SMPL_AA|002.000,N_6AOI_SMPL_AA:001.700=2S576|AA SAMPLE AOI|2S576|2.0|
|4|N_6AOI_SMPL_AA|002.000,N_6AOI_SMPL_AA:002.500=2S576|AA SAMPLE AOI|2S576|3.0|
```sql
SELECT ROUTE, STEP, PROCESS, RTG_PARM1 as recipe, SEQ_NUM
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



---
## Empties

### FPSINPUT
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







