import clr
import time
import numpy as np
clr.AddReference("IRA_UR_SocketCtrl_Prog")
import IRA_UR_SocketCtrl_Prog
robot=IRA_UR_SocketCtrl_Prog.SocketCtrl('192.168.1.6',30002,30020,100,1000)
print(robot.Start())
time.sleep(0.5)
##MoveJ####
#target can be joint angles or pose
#waitComplete=True -->wait until movement has completed;False--> just start the movement
#asPose; True=target is pose; False=Joint angles
#angleInRAD, True=RAD, False=DEG
#a and v has their conventional meaning with r as the blending radius. for r to function properly it is needed to be in advanced mode
print('Moves the robot as pose and waits untill the target is achieved, input is in radians: ')
robot.MoveJ([0.39991277529057834, -0.03122391780244967, 0.7939550213760235, -0.18295845516042827, 1.6531562174720869, 0.14834675508934117],True,True,True,0.1,0.1,0.0)
time.sleep(2)
robot.StopJ(2.0)
robot.MoveL([0.39991277529057834, -0.03122391780244967, 0.4939550213760235, -0.18295845516042827, 1.6531562174720869, 0.14834675508934117],True,True,True,0.1,0.1,0.0)
time.sleep(2)
robot.StopL(20.0)


