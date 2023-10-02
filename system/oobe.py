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
    print("Hello!")
    print("Enter information about yourself:")
    user = open("configs/user.cfg", "w")
    buffer = input("Enter your name: ")
    user.write(buffer + "\n")
    buffer = input("Enter your years old: ")
    user.write(buffer + "\n")
    buffer = input("Enter your city: ")
    user.write(buffer)
    user.close()
    time.sleep(0.3)
    os.system(clean)
    print("Thanks!")
    time.sleep(0.5)
    fcheck = open("configs/oobe.cfg", "w")
    fcheck.write("false")
    fcheck.close()
    os.system(clean)
    print("Welcome to ctOS!!")
    time.sleep(1)
    os.system(clean)
    print("░█████╗░████████╗░█████╗░░██████╗")
    print("██╔══██╗╚══██╔══╝██╔══██╗██╔════╝")
    print("██║░░╚═╝░░░██║░░░██║░░██║╚█████╗░")
    print("██║░░██╗░░░██║░░░██║░░██║░╚═══██╗")
    print("╚█████╔╝░░░██║░░░╚█████╔╝██████╔╝")
    print("░╚════╝░░░░╚═╝░░░░╚════╝░╚═════╝░")
    time.sleep(1)
