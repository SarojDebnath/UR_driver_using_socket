import clr
import time
clr.AddReference("IRA_UR_SocketCtrl_Prog")
import IRA_UR_SocketCtrl_Prog
robot=IRA_UR_SocketCtrl_Prog.SocketCtrl('192.168.1.6',30002,30020,100,1000)
print(robot.Start())
time.sleep(1)
print('Digital Output State: ',list(robot.DigitalOutputState))
print('Digital Input State: ',list(robot.DigitalInputState))
print('Config Output State: ',list(robot.ConfigOutputState))
print('Config Input State: ',list(robot.ConfigInputState))
print('Reserved Output State: ',list(robot.ReservedOutputState))
print('Reserved Input State: ',list(robot.ReservedInputState))
print('Analog Output State: ',list(robot.AnalogOutput))
print('Analog Input State: ',list(robot.AnalogInput))
print('Tool Output State: ',list(robot.ToolOutputState))
print('Tool Input State: ',list(robot.ToolInputState))
print('Tool Analog Input',list(robot.ToolAnalogInput))
print('Tool Temperature: ',robot.ToolTemperature)
print('Tool Voltage: ',robot.ToolVoltage48V)
print('Tool Current: ',robot.ToolCurrent)