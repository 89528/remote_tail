import paramiko
import itertools
#import time
import sys
def ssh_connect(hostname,path):
    ssh = paramiko.SSHClient()
    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    ssh.connect(hostname=hostname, username='xxxx', password='yyyyy', allow_agent=False, look_for_keys=False)
    stdin, stdout, stderr = ssh.exec_command("tail -f \t" + path , get_pty=True)
    for line in stdout: 
       print(line)
    #print(stderr.readlines())
    #sftp.close()
    ssh.close()
if __name__ == '__main__'
    ssh_connect(sys.argv[1], sys.argv[2])
