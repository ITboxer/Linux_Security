import paramiko
import sys

netip = sys.argv[1]
user = sys.argv[2]
password = sys.argv[3]

try:
    isshell = sys.argv[4]
except:
    isshell = None
    
    
if isshell == None:

    try:
        netinfo = netip
        account = user
        account_pass = password
        
        ssh = paramiko.SSHClient()
        
        
        ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy)
        ssh.connect(netinfo, username = account, password = account_pass)
        stdin, stdout, sterr = ssh.exec_command("cat /etc/passwd")
       
        lines = stdout.readlines()
        for i in lines:
            re = str(i).replace('\n', '')
            print(re)
            
            
        ssh.close()
       
    except Exception as err:
        print(err)
        
elif isshell == "-noshell":
    try:
        netinfo = netip
        account = user
        account_pass = password
        onlyshell = isshell
        
        ssh = paramiko.SSHClient()
        
        ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy)
        ssh.connect(netinfo, username = account, password = account_pass)
        stdin, stdout, sterr = ssh.exec_command("cat /etc/passwd | grep -v '/sbin/nologin' | grep -v '/bin/false'")
        
        lines1 = stdout.readlines()
        for a in lines1:
            re = str(a).replace('\n', '')
            print(re)
            
        ssh.close()
        
        
    except Exception as err:
        print()
            

            
            
            
            
            