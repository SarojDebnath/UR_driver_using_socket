import paramiko
import time
import socket

class remotedashboard:
    def __init__(self,ip,username,password):
        self.pi_ip = ip
        self.pi_username = username
        self.pi_password = password
        self.ssh = paramiko.SSHClient()
        self.ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        self.ssh.connect(self.ip, username=self.username, password=self.password)
        self.channel = self.ssh.get_transport().open_session()
        self.channel.get_pty()  # Allocate a pseudo-terminal
        self.channel.exec_command('nc 127.0.0.0.1 29999')
        
        
    def recvpi(self):
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.connect((self.pi_ip,65535))
        full_msg = ''
        while True:
            msg = s.recv(8)
            if len(msg) <= 0:
                break
            full_msg += msg.decode("utf-8")
        s.close()
        return full_msg
    def send_command(self,user_input):
        if user_input[0:4]=='push':
            self.channel.send(user_input + '\n')
            status=self.recvpi()
            time.sleep(1)
            return status
        else:
            self.channel.sendall(user_input + '\n')
            time.sleep(1)
            return 'nopush'
    def disconnect(self):
        #self.ssh.exec_command('exit')
        if self.ssh:
            print('ssh closed')
            self.ssh.close()