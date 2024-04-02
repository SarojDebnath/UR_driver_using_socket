import clr
import time
clr.AddReference("IRA_UR_SocketCtrl_Prog")
import IRA_UR_SocketCtrl_Prog
robot=IRA_UR_SocketCtrl_Prog.SocketCtrl('192.168.1.6',30002,30020,100,1000)
print(robot.Start())
t_start=time.time()
while True:
    timestamp=robot.Timestamp
    if timestamp !=0:
        t_end=time.time()
        break
print('Time for the robot to respond: ',t_end-t_start)
print('Timestamp: ',timestamp)
print('Robot connection: ',robot.IsRealRobotConnected)
print('Robot enabled: ',robot.IsRealRobotEnabled)
print('Robot Power',robot.IsRobotPowerOn)
print('Is protective stop active:',robot.IsProtectiveStopped)
print('Is Program Running: ',robot.IsProgramRunning)
print('Is Program Paused: ', robot.IsProgramPaused)
print('Master Board Temperature',robot.MasterBoardTemperature)
print('Robot Voltage',robot.RobotVoltage48V)
print('robot Current',robot.RobotCurrent)