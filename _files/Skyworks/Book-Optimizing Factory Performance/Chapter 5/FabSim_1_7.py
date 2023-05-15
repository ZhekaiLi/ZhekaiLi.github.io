'''Edit date 2023.5.6
'''


import numpy as np

class Factory:
    '''This class is used to define the factory
    '''
    def __init__(self, TH_f):
        self.TH_f = TH_f # Throughput rate of the factory
        self.CT_f = 0 # total cycle time of the factory
        self.WIP_f = 0 # total WIP of the factory
        self.ProcessTime = 0 # total process time of the factory

        self.TH_f_max = None # max throughput rate (capacity) of the factory = min(TH_ws)

        self.workstations = []

    def add_workstation(self, workstation):
        self.workstations.append(workstation)
        self.CT_f += workstation.CT_ws
        self.WIP_f += workstation.WIP_ws
        self.ProcessTime += workstation.CT_processing

        if self.TH_f_max is None:
            self.TH_f_max = workstation.EPR_ws
        else:
            self.TH_f_max = min(self.TH_f_max, workstation.EPR_ws)

    def add_workstations(self, workstations):
        for workstation in workstations:
            self.add_workstation(workstation)

    def calLACET(self):
        if self.TH_f_max is None:
            return "ERROR: TH_f_max is None"
        else:
            return self.ProcessTime/self.CT_f * self.TH_f/self.TH_f_max


class WorkStation:
    '''This class is used to define the workstation

    Assume:
        1. All machines are identical, and each is capable of supporting the single process step
    '''

    def __init__(self,
            TH_f,
            cov_AR, cov_EPT,
            m, EPR_m
        ):
        # Factory Level
        # ---------------------------------------------------------
        self.TH_f = TH_f # Throughput rate of the factory

        # Machine Level
        # ---------------------------------------------------------
        self.m = m # number of machines
        self.EPR_m = EPR_m # Effective Process Rate (max theoretical capacity) of each machine

        # Workstation Level
        # ---------------------------------------------------------
        self.cov_AR = cov_AR # cov of inter-arrival time
        self.cov_EPT = cov_EPT # cov of effective process time
        
        self._update()



    def _update(self):
        TH_f = self.TH_f

        cov_AR = self.cov_AR
        cov_EPT = self.cov_EPT

        m = self.m
        EPR_m = self.EPR_m

        # Effective Process Rate of the workstation (TH capacity)
        EPR_ws = m * EPR_m
        # Utilization of the workstation
        rho = TH_f / EPR_ws
        # cov of inter-departure time
        cov_DR = np.sqrt(1 + (1-rho**2)*(cov_AR**2-1) + (rho**2/np.sqrt(m))*(cov_EPT**2-1))
        # mean of cycle time in processing
        CT_processing = 1/EPR_m
        # mean of cycle time in queue
        CT_queue = ((cov_AR**2+cov_EPT**2)/2) * (rho**(np.sqrt(2*(m+1))-1) / m / (1-rho)) * (1/EPR_m)
        # mean of cycle time in workstation
        CT_ws = CT_processing + CT_queue
        # mean of WIP in workstation
        WIP_ws = CT_ws * TH_f

        self.EPR_ws = EPR_ws
        self.rho = rho
        self.cov_DR = cov_DR
        self.CT_processing = CT_processing
        self.CT_queue = CT_queue
        self.CT_ws = CT_ws
        self.WIP_ws = WIP_ws






    
