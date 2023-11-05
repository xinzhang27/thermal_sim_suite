import paramiko

hostname = "202.120.49.78"
username = "zhangxin"
password = "zhan2023"
remote_file_path = "/home/zhangxin/Projects/pdf_analyzer/files/test.txt"
local_file_path = "static/test.txt"


ssh = paramiko.SSHClient()
ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
ssh.connect(hostname, username=username, password=password)

sftp = ssh.open_sftp()
sftp.put(local_file_path, remote_file_path)
sftp.close()
stdin, stdout, stderr = ssh.exec_command('ls -l')
print(stdout.read().decode())
ssh.close()
