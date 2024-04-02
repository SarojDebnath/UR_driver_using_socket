import clr
import time
import numpy as np
clr.AddReference("IRA_UR_SocketCtrl_Prog")
clr.AddReference('System.Collections')
from System.Collections.Generic import List
import IRA_UR_SocketCtrl_Prog
robot=IRA_UR_SocketCtrl_Prog.SocketCtrl('192.168.1.6',30002,30020,100,1000)
print(robot.Start())
time.sleep(1)
robot.MoveUntilContact([0.05,0,0,0,0,0],[1,0,0,0,0,0],True,True, 0.15,3)
robot.Stop()
