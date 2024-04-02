import clr
import time
import numpy as np
clr.AddReference("IRA_UR_SocketCtrl_Prog")
import IRA_UR_SocketCtrl_Prog
robot=IRA_UR_SocketCtrl_Prog.SocketCtrl('192.168.1.251',30002,30020,100,1000)
print(robot.Start())
time.sleep(1)
##MoveJ####
#target can be joint angles or pose
#waitComplete=True -->wait until movement has completed;False--> just start the movement
#asPose; True=target is pose; False=Joint angles
#angleInRAD, True=RAD, False=DEG
#a and v has their conventional meaning with r as the blending radius. for r to function properly it is needed to be in advanced mode
print('Moves the robot as pose and waits untill the target is achieved, input is in radians: ')
#robot.MoveJ([-0.6309426820674261, 0.1346950624133441, 0.44055779478986545, 2.202542165167972, 2.1996660210603896, 0.06042015137341795],True,True,True,0.5,0.3,0.0)#(target,waitComplete,asPose,angleInRAD,a,v,r)

#print('Movement with blend radius')
#robot.MoveJ([-0.6309426820674261, 0.2346950624133441, 0.44055779478986545, 2.202542165167972, 2.1996660210603896, 0.06042015137341795],True,True,True,0.5,0.3,0.05)
'''
robot.MoveJ([0.39991277529057834, -0.03122391780244967, 0.6939550213760235, -0.18295845516042827, 1.6531562174720869, 0.14834675508934117],True,True,True,0.5,0.3,0.0)
time.sleep(5)
print('Starts the movement and returns, input is in radians: ')
robot.MoveJ([0.39991277529057834, -0.03122391780244967, 0.4939550213760235, -0.18295845516042827, 1.6531562174720869, 0.14834675508934117],False,True,True,0.1,0.1,0.0)
time.sleep(2)
robot.MoveJ([0.39991277529057834, -0.03122391780244967, 0.6939550213760235, -0.18295845516042827, 1.6531562174720869, 0.14834675508934117],True,True,True,0.1,0.1,0.0)
'''
print('Robot moves in degrees space')
#robot.MoveJ([90, -109.8346134567458, -72.92665376827816, -90.00651965468543, 89.99902578742686, -0.00015390662741124436],True,False,False,0.1,0.1,0.0)

##Move untill a condition is true###
print('Moves untill condition')
#robot.MoveJ([-0.5309426820674261, 0.2346950624133441, 0.44055779478986545, 2.202542165167972, 2.1996660210603896, 0.06042015137341795],True,True,True,0.5,0.3,0.0,'tool-di',1,1,True,'==')
print('Moves untill condition done')
#MoveL, Almost all the variables means the same through out the program

print('Moves in Linear')
robot.MoveL([0.08207569584798071, -0.6919808277563158, 1.0396597231235445, 1.5621460432748966, 0.021108842594916945, 0.04907752500906153],True,True,True,0.1,0.1,0.0)
#robot.MoveL([0.37249127347980887, -0.6314002416474964, 0.8763216443562318, -0.01801552418993641, -2.221331247094123, 2.1730565661950942],True,True,True,0.1,0.1,0.0)

#Move in linear untill condition
#robot.MoveL([0.39991277529057834, -0.03122391780244967, 0.6939550213760235, -0.18295845516042827, 1.6531562174720869,0.14834675508934117],True,True,True,0.5,0.3,0.0,'tool-di',1,0,True,'==')
#pos12=list(robot.ActualPoseCartesianRad)
#pos12[1]+=0.001
#robot.MoveL(pos12,True,True,True,0.5,0.03,0.0)
#pos12[0]+=0.05
#robot.MoveC([0.025,0.05,0,0,0,0],True,pos12,True,True,True,1.0,0.01,0.0,1)
'''
t1=time.time()
while True:
    robot.SpeedL([0,-0.002,0,0,0,0],False,True,0.3,0.5)
    if time.time()-t1 >=5:
        robot.SpeedL([0,0,0,0,0,0],False,True,0.3,0.5)
        break

robot.StopL(20.0)
'''
robot.Stop()