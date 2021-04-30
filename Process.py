import numpy as np
import copy as cp
import math as ma
from DefUpdate import update as up
import pandas as pd

class Process:
    '''Defining the parameters of the simulatoin.'''
    def __init__(self,freq,iters,Situation):
        '''This is the step size, in seconds'''
        self.freq = freq
        '''This is the amount of iterations that will be completed in the simulation'''
        self.iters = iters
        '''This is where the system will be entered'''
        self.Situation = Situation
        
    def movement (self):
        '''This is an empty list where the data for the xc data at every iteration will be added'''
        xElapse = []
        '''This is an empty list where the data for the xr data at every iteration will be added'''
        pElapse = []
        '''This is an empty list where the time point at every iteration will be added'''
        TimeElapse = []

        '''This ensure that the update function is performed the amount of times specified when defining it.'''
        for i in range(self.iters):
            '''This applies the Runge-Kutta method to the the defined system'''
            self.Situation.RunKut(1/self.freq)
            '''this makes of copy of the xc componenet at a given iteration'''
            datax = cp.deepcopy(self.Situation.x)
            '''this makes of copy of the xr componenet at a given iteration'''
            datap = cp.deepcopy(self.Situation.p)

            dataTime = i*(1/self.freq)
            '''This adds the xc data for a particular time to it's respective list'''
            xElapse.append(datax)      
            '''This adds the xr data for a particular time to it's respective list'''         
            pElapse.append(datap)

            TimeElapse.append(dataTime)

        '''This saves the xrElapse list as a .npy file so it can be called upon in the analysis'''
        np.save("xData",xElapse)
        '''This saves the xcElapse list as a .npy file so it can be called upon in the analysis'''
        np.save("pData",pElapse)

        np.save("timeData",TimeElapse)



        '''This saves the respective list as a data frame using the pandas function, this then converts them into a cvs file, this then saves them in the file described by the file path'''
        '''If anyone else is having to use this to put collected data into MODA, you will have to change the file directory so that it saves in a file on your computer.'''
        '''The none part of the header and index is so that the .cvs file is just the information, and no index, this is so it can be inputted into MODA, as it produces a column form'''
        pd.DataFrame(xElapse).to_csv(r'C:\Users\Admin\Documents\SimulationData\xdataframe.csv', header = None, index = None)
        pd.DataFrame(pElapse).to_csv(r'C:\Users\Admin\Documents\SimulationData\pdataframe.csv', header = None, index = None)
        pd.DataFrame(TimeElapse).to_csv(r'C:\Users\Admin\Documents\SimulationData\timedataframe.csv', header = None, index = None)
       