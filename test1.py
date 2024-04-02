import clr
import time
clr.AddReference("IRA_UR_SocketCtrl_Prog")
import IRA_UR_SocketCtrl_Prog
def robot(ip):
    robot=IRA_UR_SocketCtrl_Prog.SocketCtrl(ip,30002,30020,100,100)
    robot.Start()
    time.sleep(1)
    objectadress=id(robot)
    print(objectadress)
    return objectadress