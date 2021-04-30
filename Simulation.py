from Process import Process as pro 
from DefUpdate import update as up
import math as ma

situation = up(0,0,0,0,0,0,0,0,0)
forward = pro(40,8000,situation)

forward.movement()