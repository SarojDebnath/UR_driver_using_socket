import clr
import time
import numpy as np
clr.AddReference("IRA_UR_SocketCtrl_Prog")
import IRA_UR_SocketCtrl_Prog
robot=IRA_UR_SocketCtrl_Prog.SocketCtrl('192.168.1.6',30002,30020,100,1000)
print(robot.Start())
time.sleep(0.5)
print('TCP Off set Cartesian: ',list(robot.TCPOffsetCartesian))
robot.SetTcpOffset(np.array([0,0,0.5,0,0,0]),True)
print('TCP Off set Cartesian: ',list(robot.TCPOffsetCartesian))
robot.SetTcpOffset([0,0,0,0,0,0],True)
print('TCP Off set Cartesian: ',list(robot.TCPOffsetCartesian))
robot.SetTargetPayload(0.0,[0,0,0],[0,0,0,0,0,0])