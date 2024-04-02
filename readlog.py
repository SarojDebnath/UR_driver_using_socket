import paramiko
commands = ["tail -2 log_history.txt | head -1"]
ssh = paramiko.SSHClient()
ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())

try:
    ssh.connect('192.168.1.251',username='root',password='easybot')
    for command in commands:
        stdin, stdout, stderr = ssh.exec_command(command)
        output = stdout.read().decode()
        print(f"Command '{command}' output:\n{output}")

        # Check for errors (optional)
        if stderr.channel.recv_exit_status() != 0:
            error = stderr.read().decode()
            print(f"Error executing command '{command}':\n{error}")

except paramiko.AuthenticationException as e:
    print("Authentication failed:", e)
except paramiko.SSHException as e:
    print("SSH error:", e)
finally:
    ssh.close()

print("SSH connection closed.")
