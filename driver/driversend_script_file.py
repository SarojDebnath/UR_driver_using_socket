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
robot.AdvancedModeEnable()
# Create a List<string> and add your commands to it
cmd = List[str]()
script_path = 'C:/Users/sarojd/Documents/driver/demodriver_script.script'
with open(script_path, 'r') as script_file:
    script_content = script_file.read()

cmd.Add(script_content)
robot.SendCommandInt(cmd)
robot.AdvancedModeExit()