import clr
import time
import numpy as np
clr.AddReference("IRA_UR_SocketCtrl_Prog")
import IRA_UR_SocketCtrl_Prog
robot=IRA_UR_SocketCtrl_Prog.SocketCtrl('192.168.1.6',30002,30020,100,1000)
print(robot.Start())
time.sleep(1)
pos=list(robot.ActualPoseCartesianRad)
print(pos)
pos[1]+=0.1
print(pos)
robot.MoveC([-0.05,0.05,0,0,0,0],True,pos,True,True,True, 1.0, 0.1,0.0,0)
print(list(robot.ActualPoseCartesianRad))