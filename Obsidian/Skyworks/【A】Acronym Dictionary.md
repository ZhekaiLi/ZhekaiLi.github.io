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



### [EQP_CHAMBERS](https://help.inficonims.com/display/SCHEMAS/TABLES?run_1=run&run_1_tablename=EQP_CHAMBERS&run_2=run&run_2_tablename=EQP_CHAMBERS)

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

### [EQP_TOOLS](https://help.inficonims.com/display/SCHEMAS/TABLES?run_1=run&run_1_tablename=EQP_TOOLS&run_2=run&run_2_tablename=EQP_TOOLS)

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

### [EQP_TOOL_MSO_GROUPS](https://help.inficonims.com/display/SCHEMAS/TABLES?run_1=run&run_1_tablename=EQP_TOOL_MSO_GROUPS&run_2=run&run_2_tablename=EQP_TOOL_MSO_GROUPS)

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



### [RTG_PROCESSES](https://help.inficonims.com/display/SCHEMAS/TABLES?run_1=run&run_1_tablename=RTG_PROCESSES&run_2=run&run_2_tablename=RTG_PROCESSES)

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


### [RTG_ROUTE_STEPS](https://help.inficonims.com/display/SCHEMAS/TABLES?run_1=run&run_1_tablename=RTG_ROUTE_STEPS&run_2=run&run_2_tablename=RTG_ROUTE_STEPS)

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

- **空列**: FUTURE_WIP_STEP, SPEC_ID

| | |
|-|-|
|STEP|A single processing step within a route representing a single tool visit.
|PROCESS|Process defines what occurs at a step. Different steps can share the same process if they are identical. Process should normally determine allowed tools and recipe
|SCRIPT_ID| This column references the name of script used to process lots at this step. Different MES use different terminology but the key to this column is its use to determine batches. Lots with the same script_id and same batch_criteria from RTG_TOOL_ASSIGNMENTS can be batched together. Therefore this is critical column for scheduling on batch tools.


### Empties
EQP_BADGES
[RTG_PRD_CTM_SERIES](https://help.inficonims.com/display/SCHEMAS/TABLES?run_1=run&run_1_tablename=RTG_PRD_CTM_SERIES&run_2=run&run_2_tablename=RTG_PRD_CTM_SERIES)
RTG_TOOL_ASGN_LOT_PRCS_PATH
[RTG_TOOL_ASGN_LOT_PROCESS](https://help.inficonims.com/display/SCHEMAS/TABLES?run_1=run&run_1_tablename=RTG_TOOL_ASGN_LOT_PROCESS&run_2=run&run_2_tablename=RTG_TOOL_ASGN_LOT_PROCESS) (只有三行，很怪)
RTG_TOOL_ASGN_ROUTE_STEP
[WIP_DEMAND![](https://help.inficonims.com/images/icons/linkext7.gif)](https://help.inficonims.com/display/SCHEMAS/TABLES?run_1=run&run_1_tablename=WIP_DEMAND&run_2=run&run_2_tablename=WIP_DEMAND)
[WIP_CTM_FORECAST](https://help.inficonims.com/display/SCHEMAS/TABLES?run_1=run&run_1_tablename=WIP_CTM_FORECAST&run_2=run&run_2_tablename=WIP_CTM_FORECAST)







