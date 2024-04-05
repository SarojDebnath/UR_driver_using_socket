import clr
import time
import numpy as np
clr.AddReference("IRA_UR_SocketCtrl_Prog")
import IRA_UR_SocketCtrl_Prog
robot=IRA_UR_SocketCtrl_Prog.SocketCtrl('192.168.1.251',30002,30020,100,1000)
print(robot.Start())
time.sleep(1)
t1=time.time()
i=0
print(list(robot.ActualPoseCartesianRad))
while time.time() - t1 < 4 :
    robot.SpeedL([0,-0.1,0,0,0,0],False,True,0.3,0.5,0.0)
    time.sleep(0.5)
    j=list(robot.ActualJointAnglesDeg)
    j[5]+=0.5*(-1)**i
    robot.MoveJ(j,True,False,False,0.3,0.5,0.0)
    i+=1
print(list(robot.ActualPoseCartesianRad))
robot.Stop()