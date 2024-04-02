import clr
import time
import numpy as np
clr.AddReference("IRA_UR_SocketCtrl_Prog")
import IRA_UR_SocketCtrl_Prog
robot=IRA_UR_SocketCtrl_Prog.SocketCtrl('192.168.1.6',30002,30020,100,1000)
print(robot.Start())
time.sleep(0.5)
flag=True
for p in range(2):
    if p==0:
        flag=True
    else: flag=False
    for i in range(8):
        robot.SetStandardDigitalOut(i,flag)
        time.sleep(1)
for q in range(2):
    if q==0:
        flag=True
    else: flag=False
    for k in range(2):
        robot.SetToolDigitalOut(k,flag)
        time.sleep(1)
for r in range(2):
    if r==0:
        flag=True
    else: flag=False
    for i in range(8):
        robot.SetConfigurableDigitalOut(i,flag)
        time.sleep(1)
for s in range(2):
    if s==0:
        flag=1
    else: flag=0
    for i in range(2):
        robot.SetStandardAnalogOut(i,flag)
        time.sleep(1)