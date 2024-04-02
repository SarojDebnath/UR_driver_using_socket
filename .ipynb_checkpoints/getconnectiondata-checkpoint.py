import clr
import time
clr.AddReference("IRA_UR_SocketCtrl_Prog")
import IRA_UR_SocketCtrl_Prog
robot=IRA_UR_SocketCtrl_Prog.SocketCtrl('192.168.1.251',30002,30020,100,1000)
print(robot.Start())
time.sleep(1)
#robot.Stop()
print('Host IP:',robot.HostIp)
print('Connected Port',robot.Port)
print('connected Interpreter',robot.PortInt)
print('cycle pause: ',robot.CyclePause)
print('Cycle Time:',robot.CycleTime)
print('Time out: ',robot.Timeout)
print('Robot Running status',robot.IsRunning)
print('Robot Connection Status: ',robot.IsRealRobotConnected)
if robot.IsRealRobotConnected==True:
    print('Connected')
robot.Stop()
time.sleep(1)
print(robot.IsRealRobotConnected)