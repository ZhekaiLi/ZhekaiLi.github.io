
'''
A simple cycle time simulation

Designed to solve the final example in Chapter 3 of the book

Assumptions:
- no variability
'''

import simpy
import matplotlib.pyplot as plt
import numpy as np


# Factory throughput rate (jobs arrival rate)
list_TH_f = [0.5*i+0.5 for i in range(15)]

# Effective processing rate of machines
EPR_A = 1.8
EPR_B = 0.85
EPR_C = 0.855

EPT_A = 1/EPR_A
EPT_B = 1/EPR_B
EPT_C = 1/EPR_C

transit_time = 5/60


class Factory:
    def __init__(self, env, TH_f=1):
        self.env = env
        self.TH_f = TH_f # factory throughput rate (jobs arrival rate) (jobs/h)
        
        ws_A  = WorkStation(env, m=1, EPT_m=EPT_A) # workstation A
        ws_Ap = WorkStation(env, m=1, EPT_m=EPT_A) # workstation A'
        ws_B  = WorkStation(env, m=2, EPT_m=EPT_B)
        ws_Bp = WorkStation(env, m=2, EPT_m=EPT_B)
        ws_C  = WorkStation(env, m=2, EPT_m=EPT_C)
        ws_Cp = WorkStation(env, m=2, EPT_m=EPT_C)

        self.workstations = [ws_A, ws_B, ws_C, ws_Ap, ws_Bp, ws_Cp]
        self.jobsFinished = 0
        self.jobsCycleTime = []

    def run(self):
        while True:
            yield self.env.timeout(1/self.TH_f)
            self.env.process(self.jobIn())

    def jobIn(self):
        arrival_time = self.env.now

        for workstation in self.workstations:
            yield self.env.timeout(transit_time)
            with workstation.ws.request() as req:
                yield req
                yield self.env.timeout(workstation.EPT_m)

        departure_time = self.env.now
        self.jobsCycleTime.append(departure_time - arrival_time)
        self.jobsFinished += 1

class WorkStation:
    def __init__(self, env, m, EPT_m):
        self.ws = simpy.Resource(env, capacity=m)
        self.EPT_m = EPT_m # effective processing time of each machine




# Average Cycle Time for different arrival rates
list_CT = []

for TH_f in list_TH_f:
    env = simpy.Environment()
    factory = Factory(env, TH_f=TH_f)
    env.process(factory.run())
    env.run(until=168)
    list_CT.append(np.mean(factory.jobsCycleTime))

plt.xlabel('Factory Throughput Rate (jobs/h)')
plt.ylabel('Average Cycle Time (h)')
plt.plot(list_TH_f, list_CT)
plt.show()

