#Breadyfetch v3.2 by CyberBr3ad
import os
import platform
import socket
import time
import subprocess, re
from datetime import datetime
com = str("")
buffer1 = ""
buffer2 = ""
start = "true"
ver="0.6.3" #set by the maintainer
import os

def get_cpu_model_name_windows():
    return os.popen('wmic cpu get name').read().decode()

local_ip=socket.gethostbyname(socket.gethostname())

def get_processor_name():
    if platform.system() == "Windows": #Windows 7 works but other versions im not sure
        vitiacatgay=os.popen('wmic cpu get name').read()
        return vitiacatgay.split("\n")[2]
    elif platform.system() == "Darwin":
        os.environ['PATH'] = os.environ['PATH'] + os.pathsep + '/usr/sbin'
        command ="sysctl -n machdep.cpu.brand_string"
        return subprocess.check_output(command).strip()
    elif platform.system() == "Linux":
        command = "cat /proc/cpuinfo"
        all_info = subprocess.check_output(command, shell=True).decode().strip()
        for line in all_info.split("\n"):
            if "model name" in line:
                return re.sub( ".*model name.*:", "",line,1)
    return "idk"

def get_uptime():
    if platform.system()=="Linux":
        return subprocess.check_output("uptime -p", shell=True).decode().strip()
    else:
        return "Only for Linux..."
print("")
print("░█████╗░████████╗░█████╗░░██████╗", "OS: ctOS", ver, platform.machine())
print("██╔══██╗╚══██╔══╝██╔══██╗██╔════╝", "Host:", platform.platform())
print("██║░░╚═╝░░░██║░░░██║░░██║╚█████╗░", "CPU:", get_processor_name())
print("██║░░██╗░░░██║░░░██║░░██║░╚═══██╗", "Kernel:", platform.version())
print("╚█████╔╝░░░██║░░░╚█████╔╝██████╔╝", "Uptime:", get_uptime())
print("░╚════╝░░░░╚═╝░░░░╚════╝░╚═════╝░", "Local IP:", local_ip)
print("")
