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
|PM     | Preemptive Maintanance             |
|prd| prodcution|
|SAW    | Surface Acoustic Wave 表面声波滤波器|
|SOAK   | Second of a Kind                   |
|WSPD   | Wafter Starts Per Day              |
|WSPM   | Wafer Starts Per Month             |


CTM
- Capacitor Top Metal 半导体内的一种结构层
- Cycle Time: Table [WIP_CTM_FORECAST![](https://help.inficonims.com/images/icons/linkext7.gif)](https://help.inficonims.com/display/SCHEMAS/TABLES?run_1=run&run_1_tablename=WIP_CTM_FORECAST&run_2=run&run_2_tablename=WIP_CTM_FORECAST) contains the forecast of total cycle time by prd for upcoming weeks, months, quarters, and/or years

[RTG_ROUTE_STEPS]([TABLES - Data Dictionary - INFICON IMS Help Site](https://help.inficonims.com/display/SCHEMAS/TABLES?run_1=run&run_1_tablename=RTG_ROUTE_STEPS&run_2=run&run_2_tablename=RTG_ROUTE_STEPS)):
关联 route - step - process
- 空列: FUTURE_WIP_STEP, SPEC_ID
- ROUTE: 路径名
- STEP: A single processing step within a route representing a single tool visit.
- PROCESS: Process defines what occurs at a step. Different steps can share the same process if they are identical. Process should normally determine allowed tools and recipe
- SCRIPT_ID: This column references the name of script used to process lots at this step. Different MES use different terminology but the key to this column is its use to determine batches. Lots with the same script_id and same batch_criteria from RTG_TOOL_ASSIGNMENTS can be batched together. Therefore this is critical column for scheduling on batch tools.




空表格:
[RTG_PRD_CTM_SERIES](https://help.inficonims.com/display/SCHEMAS/TABLES?run_1=run&run_1_tablename=RTG_PRD_CTM_SERIES&run_2=run&run_2_tablename=RTG_PRD_CTM_SERIES)

[WIP_DEMAND![](https://help.inficonims.com/images/icons/linkext7.gif)](https://help.inficonims.com/display/SCHEMAS/TABLES?run_1=run&run_1_tablename=WIP_DEMAND&run_2=run&run_2_tablename=WIP_DEMAND)
[WIP_CTM_FORECAST](https://help.inficonims.com/display/SCHEMAS/TABLES?run_1=run&run_1_tablename=WIP_CTM_FORECAST&run_2=run&run_2_tablename=WIP_CTM_FORECAST)







