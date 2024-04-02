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
print(list(robot.ActualPoseCartesianRad))
robot.AdvancedModeEnable()
cmd = List[str]()
cmd1=List[str]()
cmd.Add('def x():\n  speedl([-0.01,0.0,0,0.0,0,0], 1, 1)\n end\n')
cmd1.Add('def x():\n  stopl(20)\n end\n')
# Send the concatenated command string to the robot
for i in range(10):
    robot.SendCommandInt(cmd)
    time.sleep(1)
    if i>=4:
        robot.SendCommandInt(cmd1)
        break
        time.sleep(1)
robot.AdvancedModeExit()

