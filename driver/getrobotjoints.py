import clr
import time
clr.AddReference("IRA_UR_SocketCtrl_Prog")
import IRA_UR_SocketCtrl_Prog
robot=IRA_UR_SocketCtrl_Prog.SocketCtrl('192.168.1.111',30002,30020,100,1000)
print(robot.Start())
time.sleep(1)
qr=list(robot.ActualJointAnglesRad)
print('Actual Joint Angles in Radians: ',qr)
print('Actual Joint Angles Degrees: ',list(robot.ActualJointAnglesDeg))
print('Actual Pose Cartesian Rad: ',list(robot.ActualPoseCartesianRad))
print('Actual Pose Cartesian Deg: ',list(robot.ActualPoseCartesianDeg))
print('TCP Off set Cartesian: ',list(robot.TCPOffsetCartesian))
print(robot.Stop())