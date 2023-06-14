
# Batch Configuration

[Batching Configuration - Scheduler - INFICON IMS Help Site](https://help.inficonims.com/display/SCHED/Batching+Configuration)


## Batch Scoring Algorithm

Algorithm takes into account:
- the number of lots already scheduled to the tool (current lots)
- the number of lots expected to join the batch (incoming lots by start time) #Problem Different between 2 and 3?
- the number of lots within the scheduler horizon, but not expected to arrive in time to join the batch (incoming lots on schedule)
- a measure of "completeness" of the batch (i.e. whether all possible lots for the batch within the horizon are in the batch)

**(1) Prefer to wait for future lots/bigger batches**
- BATCH_SIZE_WEIGHTS_CURRENT = 2
- BATCH_SIZE_WEIGHTS_FUTURE = 2
- BATCH_SIZE_WEIGHTS_COMING = -0.5
**(2) Do not prefer to wait for future lots:**
- BATCH_SIZE_WEIGHTS_CURRENT = 2
- BATCH_SIZE_WEIGHTS_FUTURE = 2
- BATCH_SIZE_WEIGHTS_COMING = 0


Batch Criteria

refers to the method the scheduler uses to determine that different lots can join together as part of a larger batch (什么含义？是说明同样的 criteria 的 lot 可以被放在一起处理吗)

Minimum and Maximum Batch Size

for a batch to be considered valid, the size should be between min and max
however, since each lot may have different min and max requirement, we define:
min = the smallest min
max = the smallest max
for example, for the following 3 lots, min = 2, max = 4

|Lot ID|Min Size Lots|Max Size Lots|
|---|---|---|
|A|4|6|
|B|4|4|
|C|2|6|
