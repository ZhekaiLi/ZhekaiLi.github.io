
|Acronym| Meaning                            |
|-------|------------------------------------|
|AMU    | Manufactoring Availability         |
|AOU    | Operational Availability           |
|ATU    | Total Availability                 |
|BAW    | Bulk Acoustic Wave                 |
|Bi-    | Bipolar-                           |
|CTM    | Capacitor Top Metal                |
|DPML   | Days per Mask Level                |
|DPS    | Die (or Dice) Processing           |
|ENG    | [Engineering Time](https://help.inficonims.com/display/ETP/Engineering+%28ENG%29+States)                 |
|ETP    | Enhanced Tool Performance          |
|FET    | Field-Effect Transistor            |
|GDPW   | Gross Die Per Wafer (e5)           |
|HBT    | Heterojunction Bipolar Transistors <br> e.g. AlGaAs, GaAs HBT                       |
|HFET   | High-Electron-Mobility Transistor <br> aka. Heterostructure FET (HFET)             |
|IC     | Integrated Circuit                 |
|IT     | Impairment Time                    |
|MFD    | Mean Failure Duration              |
|MRP    | Material Requirements Planning     |
|MSO    | Metrology Sampling Optimizer       | 
|MTBF   | Mean Time Between Failures         |
|MTOL   | Mean Time Off-Line (average of SDT and UDT)
|MTTI   | Mean Time to Interrupt             |
|MTTR   | Mean Time to Repair                |
|MTTQ   | Mean Time to Qualification         |
|MTTPM  | Mean Time to Perform               |
|NST    | Nonscheduled Time                  |
|OEE    | Overall Equipment Effectiveness    |
|PM     | Preemptive Maintanance             |
|POC    | Proof of Conecpt                   |
|prd    | prodcut/ production                |
|SAW    | Surface Acoustic Wave              |
|SBY    | Standby Time                       |
|SDT    | Scheduled Down Time                |
|SOAK   | Second of a Kind                   |
|TFR    | Total Failure Rage                 |
|UDT    | Unscheduled Down Time              |
|UOU    | Total Utilization                  | 
|UTU    | Operational Utilization            |
|WSPD   | Wafter Starts Per Day              |
|WSPM   | Wafer Starts Per Month             |


CTM
- Capacitor Top Metal 半导体内的一种结构层
- Cycle Time: Table [WIP_CTM_FORECAST![](https://help.inficonims.com/images/icons/linkext7.gif)](https://help.inficonims.com/display/SCHEMAS/TABLES?run_1=run&run_1_tablename=WIP_CTM_FORECAST&run_2=run&run_2_tablename=WIP_CTM_FORECAST) contains the forecast of total cycle time by prd for upcoming weeks, months, quarters, and/or years

MSO
- Metrology Sampling Optimizer 计量采样优化器: [MSO Database Tables - Metrology Sampling Optimizer - INFICON IMS Help Site](https://help.inficonims.com/display/MSO/MSO+Database+Tables)

MTBF: Mean Time Between Failures ([Equipment Metrics - Enhanced Tool Performance - INFICON IMS Help Site](https://help.inficonims.com/display/ETP/Equipment+Metrics))
- MTBF_u: Uptime
- MTBF_p: Production


lot
- the process unit in the fab, contains a set of waters (see [[Lot]])

Reservation
- in the [[FPS_Scheduler/Scheduler]], it is designed to minimize changes to the assignments and ordering of lots to tools as their scheduled start times become closer.  Reservation score 作为 [[【A】Scheduler]], ...
- By reserving lots, we can make it more difficult for the scheduler to switch a lot to a new tool or change the order of lots on the tool.  While this may mean we miss some opportunities for a technically better schedule (e.g. could start the lot 30 minutes earlier on another tool), it provides a more consistent list of lots for a given tool and lets operators better plan for their work - e.g. which reticles are needed, which lots need to be moved, what setup changes need to be coordinated, etc....