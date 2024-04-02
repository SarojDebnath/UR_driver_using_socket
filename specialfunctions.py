import clr
import time
import numpy as np
clr.AddReference("IRA_UR_SocketCtrl_Prog")
clr.AddReference('System.Collections')
from System.Collections.Generic import List
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
#robot.MoveJ([0.39991277529057834, -0.03122391780244967, 0.7939550213760235, -0.18295845516042827, 1.6531562174720869, 0.14834675508934117],True,True,True,0.1,0.1,0.0)
#robot.MoveWait(100,30000)

robot.AdvancedModeEnable()

print('Freedrive in advance Mode for 20 seconds')
p=robot.FreedriveMode(True)
print(p.Msg)
time.sleep(2)
robot.FreedriveMode(False)
print('No freedrive')

# Create a List<string> and add your commands to it
cmd = List[str]()
cmd1=List[str]()
#cmd.Add('def x():\n  set_standard_digital_out(0, True)\n end\n')
cmd.Add('def x():\n  set_standard_digital_out(0, True)\n  set_standard_digital_out(1, True)\n end\n')
cmd1.Add('def y():\n  set_standard_digital_out(0, False)\n  set_standard_digital_out(1, False)\n end\n')
# Send the concatenated command string to the robot
for i in range(10):
    robot.SendCommandInt(cmd)
    time.sleep(1)
    robot.SendCommandInt(cmd1)
    time.sleep(1)
robot.AdvancedModeExit()

