import clr
import time
clr.AddReference("IRA_UR_SocketCtrl_Prog")
import IRA_UR_SocketCtrl_Prog
robot=IRA_UR_SocketCtrl_Prog.SocketCtrl('192.168.1.251',30002,30020,100,100)
robot.Start()
time.sleep(1)
print('Pose Radian:',list(robot.ActualPoseCartesianRad))
print('joint Degrees:',list(robot.ActualJointAnglesDeg))
print('joint Rad:',list(robot.ActualJointAnglesRad))
robot.Stop()