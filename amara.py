import os


print("System inventory please wait...")
os.system('nproc')
os.system('uname -r')
os.system('free -m')
os.system('lsblk')
os.system('cat /etc/os-release')
os.system('uname')