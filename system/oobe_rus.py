#OPERATING SYSTEM ctOS _Linux_or_macOS_
import os
import time
from datetime import datetime
com = str("")
start = "true"
user = "User"
clean = ""
syst = ""
fcheck = open("configs/oobe.cfg", "r")
check = fcheck.read()
fcheck.close()
if(check == "true"):
    settings = open("configs/system.cfg", "r")                  #base
    buffer = settings.read()
    if(buffer == "linux\n"):
        clean = "clear"
        syst = "| base system: LINUX   |"
    if(buffer == "windows\n"):
        clean = "cls"
        syst = "| base system: WINDOWS |"
    settings.close()                                #основа
    os.system(clean)
    print("Введи информацию о себе:")
    user = open("configs/user.cfg", "w")
    buffer = input("Введи свою имя и фамилию: ")
    user.write(buffer + "\n")
    buffer = input("Введи свой возраст: ")
    user.write(buffer + "\n")
    buffer = input("Введи город проживания: ")
    user.write(buffer)
    user.close()
    time.sleep(0.3)
    os.system(clean)
    print("Спасибо!")
    time.sleep(0.5)
    fcheck = open("configs/oobe.cfg", "w")
    fcheck.write("false")
    fcheck.close()
    os.system(clean)
    print("Добро пожаловать в ctOS!!")
    time.sleep(1)
    os.system(clean)
    print("░█████╗░████████╗░█████╗░░██████╗")
    print("██╔══██╗╚══██╔══╝██╔══██╗██╔════╝")
    print("██║░░╚═╝░░░██║░░░██║░░██║╚█████╗░")
    print("██║░░██╗░░░██║░░░██║░░██║░╚═══██╗")
    print("╚█████╔╝░░░██║░░░╚█████╔╝██████╔╝")
    print("░╚════╝░░░░╚═╝░░░░╚════╝░╚═════╝░")
    time.sleep(1)
