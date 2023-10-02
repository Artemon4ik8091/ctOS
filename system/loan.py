#OPERATING SYSTEM
import os
import time
from datetime import datetime
com = str("")
buffer = ""
buffer2 = ""
start = "true"
clean = ""
settings = open("configs/system.cfg", "r")
buffer = settings.read()
if(buffer == "linux\n"):
    clean = "clear"
    syst = "| base system: LINUX   |"
if(buffer == "windows\n"):
    clean = "cls"
    syst = "| base system: WINDOWS |"
settings.close()
os.system(clean)
print("/")
time.sleep(0.085)
os.system(clean)
print("-")
time.sleep(0.085)
os.system(clean)
print("\\")
time.sleep(0.085)
os.system(clean)
print("|")
time.sleep(0.085)
os.system(clean)
print("/")
time.sleep(0.085)
os.system(clean)