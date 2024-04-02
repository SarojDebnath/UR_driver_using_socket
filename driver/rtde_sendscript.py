import rtde_control
import time
ip = "192.168.1.6"
rtde_c = rtde_control.RTDEControlInterface(ip)
rtde_c.sendCustomScriptFile("C:/Users/sarojd/Documents/driver/rtde_script.script")
print('Waiting')
time.sleep(5)
print("test")