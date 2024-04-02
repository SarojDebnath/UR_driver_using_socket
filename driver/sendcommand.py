import clr
import time
#import numpy as np
clr.AddReference("IRA_UR_SocketCtrl_Prog")
clr.AddReference('System.Collections')
from System.Collections.Generic import List
import IRA_UR_SocketCtrl_Prog
robot=IRA_UR_SocketCtrl_Prog.SocketCtrl('192.168.1.111',30002, 30020, 100, 1000)
print(robot.Start())
time.sleep(0.5)
##MoveJ####
#target can be joint angles or pose
#waitComplete=True -->wait until movement has completed;False--> just start the movement
#asPose; True=target is pose; False=Joint angles
#angleInRAD, True=RAD, False=DEG
#a and v has their conventional meaning with r as the blending radius. for r to function properly it is needed to be in advanced mode
#print('Moves the robot as pose and waits untill the target is achieved, input is in radians: ')
#robot.MoveJ([0.39991277529057834, -0.03122391780244967, 0.7939550213760235, -0.18295845516042827, 1.6531562174720869, 0.14834675508934117],True,True,True,0.1,0.1,0.0)
#robot.MoveWait(100,30000)

robot.AdvancedModeEnable()
cmd2=List[str]()
cmd2.Add('def z():\n  movel([0.48951839523194907,-0.2968762257132418,0.4578171192590484,1.2141989681940373,1.1915451147864906,1.1855473084784207], a=0.1, v=0.1, t=0, r=0)\n end\n')
# Send the concatenated command string to the robot
robot.SendCommand(cmd2)
robot.AdvancedModeExit()