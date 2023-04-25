
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

# Jobs arrival time (time between two arrivals)
list_AT = [1/TH_f for TH_f in list_TH_f]

# Effective processing rate of machines
EPR_A = 1.8
EPR_B = 0.85
EPR_C = 0.855

EPT_A = 1/EPR_A
EPT_B = 1/EPR_B
EPT_C = 1/EPR_C

transit_time = 5/60


class Factory:
    def __init__(self, env):
        self.env = env
        self.m_A = simpy.Resource(env, capacity=1) 
        self.m_Ap = simpy.Resource(env, capacity=1) # workstation A'
        self.m_B = simpy.Resource(env, capacity=2)
        self.m_Bp = simpy.Resource(env, capacity=2)
        self.m_C = simpy.Resource(env, capacity=2)
        self.m_Cp = simpy.Resource(env, capacity=2)

        self.jobsFinished = 0
        self.jobsCycleTime = []

    def run(self):
        while True:
            yield self.env.timeout(AT)
            self.env.process(self.jobIn())

    def jobIn(self):
        arrival_time = self.env.now

        yield self.env.timeout(transit_time)
        with self.m_A.request() as req:
            yield req
            yield self.env.timeout(EPT_A)
        yield self.env.timeout(transit_time)
        with self.m_B.request() as req:
            yield req
            yield self.env.timeout(EPT_B)
        yield self.env.timeout(transit_time)
        with self.m_C.request() as req:
            yield req
            yield self.env.timeout(EPT_C)
        yield self.env.timeout(transit_time)
        with self.m_Ap.request() as req:
            yield req
            yield self.env.timeout(EPT_A)
        yield self.env.timeout(transit_time)
        with self.m_Bp.request() as req:
            yield req
            yield self.env.timeout(EPT_B)
        yield self.env.timeout(transit_time)
        with self.m_Cp.request() as req:
            yield req
            yield self.env.timeout(EPT_C)

        departure_time = self.env.now
        self.jobsCycleTime.append(departure_time - arrival_time)
        self.jobsFinished += 1

# Average Cycle Time for different arrival rates
list_CT = []

for AT in list_AT:
    env = simpy.Environment()
    factory = Factory(env)
    env.process(factory.run())
    env.run(until=168)
    list_CT.append(np.mean(factory.jobsCycleTime))

plt.plot(list_TH_f, list_CT)
plt.show()

