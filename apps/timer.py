#OPERATING SYSTEM
import os
import time
from datetime import datetime
import platform
com = str("")
buffer1 = ""
buffer2 = 0
start = "true"
clean = ""
if platform.system() == "Windows":
    clean = "cls"
    syst = "| base system: WINDOWS |"
elif platform.system() == "Linux":
    clean = "clear"
    syst = "| base system: LINUX   |"
os.system(clean)
buffer = int(input("Enter time(in seconds): "))
os.system(clean)
buffer += 1
while(start == "true"):
    buffer -= 1
    print(buffer)
    time.sleep(1)
    os.system(clean)
    if(int(buffer) <= int(0)):
        while(start=="true"):
            print("ВРЕМЯ ВЫШЛО!!!")
            time.sleep(0.15)
            print("ВРЕМЯ ВЫШЛО!!!")
            time.sleep(0.15)
            print("ВРЕМЯ ВЫШЛО!!!")
            time.sleep(0.15)
            print("ВРЕМЯ ВЫШЛО!!!")
            time.sleep(0.15)
            print("ВРЕМЯ ВЫШЛО!!!")
            time.sleep(0.15)
            os.system(clean)
            buffer2 += 1
            if(buffer2 >= 5):
                os.system(clean)
                print("Exiting...")
                start = "false"
                time.sleep(0.5)