import clr
import time
import numpy as np
import subprocess
clr.AddReference("IRA_UR_SocketCtrl_Prog")
import IRA_UR_SocketCtrl_Prog
robot=IRA_UR_SocketCtrl_Prog.SocketCtrl('192.168.1.251',30002,30020,100,1000)
print(robot.Start())
time.sleep(1)


def movel(pos=[],rel=False,a=0.3,v=0.5):
    
    commandpop = 'echo y | plink root@192.168.1.251 -pw easybot "{ echo \\"unlock protective stop\\"; echo \\"quit\\"; } | nc 127.0.0.1 29999"'
    emergency=False
    target=[]
    initjoint=list(robot.ActualJointAnglesDeg)
    if rel==True:
        currentpos=list(robot.ActualPoseCartesianRad)
        for i in range(6):
            target.append(currentpos[i]+pos[i])
    else:
        target=pos
    robot.MoveL(target,True,True,True,a,v,0.0)
    emergency=robot.IsEmergencyStopped or robot.IsProtectiveStopped
    if emergency==True:
        time.sleep(5)
        process = subprocess.Popen(commandpop, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        time.sleep(1)
        stdout, stderr = process.communicate()
        print(stdout.decode())
        angle=list(robot.ActualJointAnglesDeg)
        if angle[5]>=358 or angle[5]<=-358:
            angle[5]=0
            robot.MoveJ(angle,True,True,0.3,0.5,0.0)
            movel(target,False,a,v)
        else:
            robot.Stop()
            raise Exception('Robot_stopped')
    else:
        return 'done'
movel([0,0,0,0,0,0.01],True,0.3,0.5)