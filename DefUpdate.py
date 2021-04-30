from DefEqn import eqns
import numpy as np
import math as ma

class update:
    def __init__(self,x,p,alphax1,alphap1,alphax2,alphap2,alphax3,alphap3,time):
   
        self.x = x
        self.p = p
        self.alphax1 = alphax1
        self.alphax2 = alphax2
        self.alphax3 = alphax3
        self.alphap1 = alphap1
        self.alphap2 = alphap2
        self.alphap3 = alphap3
        self.time = time
   

    def __repr_(self):
        return 'x{0}, p{1}, alphax1{2}alphax2{3},alphax3{4}, alphap1{5},alphap2{6},alphap3{7}, time{8}'.format(self.x,self.p,self.alphax1,self.alphap1,self.alphax2,self.alphap2,self.alphax3,self.alphap3,self.time)

    def RunKut(self,step):

        ax1k1 = step * eqns.axdot1(self,self.time,self.alphax1,self.alphap1)
        ax2k1 = step * eqns.axdot2(self,self.time,self.alphax2,self.alphap2)
        ax3k1 = step * eqns.axdot3(self,self.time,self.alphax3,self.alphap3)
        ap1k1 = step * eqns.apdot1(self,self.time)
        ap2k1 = step * eqns.apdot2(self,self.time)
        ap3k1 = step * eqns.apdot3(self,self.time)

        ax1k2 = step * eqns.axdot1(self, self.time + (step/2), self.alphax1 + (ax1k1/2), self.alphap1 + (ap1k1/2))
        ax2k2 = step * eqns.axdot2(self, self.time + (step/2), self.alphax2 + (ax2k1/2), self.alphap2 + (ap2k1/2))
        ax3k2 = step * eqns.axdot3(self, self.time + (step/2), self.alphax3 + (ax3k1/2), self.alphap3 + (ap3k1/2))
        ap1k2 = step * eqns.apdot1(self,self.time + (step/2))
        ap2k2 = step * eqns.apdot2(self,self.time + (step/2))
        ap3k2 = step * eqns.apdot3(self,self.time + (step/2))

        ax1k3 = step * eqns.axdot1(self, self.time + (step/2), self.alphax1 + (ax1k2/2), self.alphap1 + (ap1k2/2))
        ax2k3 = step * eqns.axdot2(self, self.time + (step/2), self.alphax2 + (ax2k2/2), self.alphap2 + (ap2k2/2))
        ax3k3 = step * eqns.axdot3(self, self.time + (step/2), self.alphax3 + (ax3k2/2), self.alphap3 + (ap3k2/2))
        ap1k3 = step * eqns.apdot1(self,self.time + (step/2))
        ap2k3 = step * eqns.apdot2(self,self.time + (step/2))
        ap3k3 = step * eqns.apdot3(self,self.time + (step/2))

        ax1k4 = step * eqns.axdot1(self, self.time + (step), self.alphax1 + (ax1k3), self.alphap1 + (ap1k3))
        ax2k4 = step * eqns.axdot2(self, self.time + (step), self.alphax2 + (ax2k3), self.alphap2 + (ap2k3))
        ax3k4 = step * eqns.axdot3(self, self.time + (step), self.alphax3 + (ax3k3), self.alphap3 + (ap3k3))
        ap1k4 = step * eqns.apdot1(self,self.time + (step))
        ap2k4 = step * eqns.apdot2(self,self.time + (step))
        ap3k4 = step * eqns.apdot3(self,self.time + (step))

        self.alphax1 = self.alphax1 + ( (1/6) * ( ax1k1 + (2*ax1k2) + (2*ax1k3) + ax1k4 ) )
        self.alphax2 = self.alphax2 + ( (1/6) * ( ax2k1 + (2*ax2k2) + (2*ax2k3) + ax2k4 ) )
        self.alphax3 = self.alphax3 + ( (1/6) * ( ax3k1 + (2*ax3k2) + (2*ax3k3) + ax3k4 ) )
        self.alphap1 = self.alphap1 + ( (1/6) * ( ax1k1 + (2*ap1k2) + (2*ap1k3) + ap1k4 ) )
        self.alphap2 = self.alphap2 + ( (1/6) * ( ap2k1 + (2*ap2k2) + (2*ap2k3) + ap2k4 ) )
        self.alphap3 = self.alphap3 + ( (1/6) * ( ap3k1 + (2*ap3k2) + (2*ap3k3) + ap3k4 ) )

        self.x = ma.cos(self.alphax1) + ma.cos(self.alphax2) + ma.cos(self.alphax3)
        self.p = ma.cos(self.alphap1) + ma.cos(self.alphap2) + ma.cos(self.alphap3)

        self.time = self.time + step