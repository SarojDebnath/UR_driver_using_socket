import socket
import time
k=0
def Activate():
    global k
    HOST = "192.168.1.6" # The UR IP address
    PORT = 30002 # UR secondary client
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect((HOST, PORT))
    f_activate = open ("C:/Users/sarojd/Documents/driver/test_script.script", "rb")
    l_activate = f_activate.read(1024)
    while (l_activate):
        k=s.send(l_activate)
        print(k)
        l_activate = f_activate.read(1024)
    s.close()
Activate()
time.sleep(20)
print(k)