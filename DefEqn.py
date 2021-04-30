import math as ma

class eqns:

    def axdot1(self,t,alphax,alphap):
        return 1.5 * 2 * ma.pi * ( 1 + ( (1/(2 * ma.pi)) * ma.sin ( 0.016 * ma.pi * t ) ) ) * ma.sin ( alphax - alphap )

    def axdot2(self,t,alphax,alphap):
        return 1.5 * 0.3 * ma.pi * ( 1 + ( (0.15/(0.3 * ma.pi)) * ma.sin ( 0.005 * ma.pi * t ) ) ) * ma.sin ( alphax - alphap )

    def axdot3(self,t,alphax,alphap):
        return 1.5 * 0.05 * ma.pi * ( 1 + ( (0.025/(0.05 * ma.pi)) * ma.sin ( 0.001 * ma.pi * t ) ) ) * ma.sin ( alphax - alphap )

    def apdot1(self,t):
        return 2 * ma.pi * ( 1 + ( (1/(2 * ma.pi)) * ma.sin ( 0.016 * ma.pi * t ) ) )

    def apdot2(self,t):
        return 0.3 * ma.pi * ( 1 + ( (0.15/(0.3 * ma.pi)) * ma.sin ( 0.005 * ma.pi * t ) ) )

    def apdot3(self,t):
        return 0.05 * ma.pi * ( 1 + ( (0.025/(0.05 * ma.pi)) * ma.sin ( 0.001 * ma.pi * t ) ) )
    