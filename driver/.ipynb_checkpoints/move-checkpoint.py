import clr
import time
import numpy as np
clr.AddReference("IRA_UR_SocketCtrl_Prog")
import IRA_UR_SocketCtrl_Prog
robot=IRA_UR_SocketCtrl_Prog.SocketCtrl('192.168.1.111',30002,30020,100,1000)
print(robot.Start())
time.sleep(1)

print('Moves in Linear')
robot.MoveL([0.48951839523194907, -0.2968762257132418, 0.4578171192590484, 1.2141989681940373, 1.1915451147864906, 1.1855473084784207],True,True,True,0.1,0.1,0.0)

#Move in linear untill condition
#robot.MoveL([0.39991277529057834, -0.03122391780244967, 0.6939550213760235, -0.18295845516042827, 1.6531562174720869,0.14834675508934117],True,True,True,0.5,0.3,0.0,'tool-di',1,0,True,'==')