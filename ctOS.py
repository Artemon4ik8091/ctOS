import os
fcheck = open("configs/oobe.cfg", "r")
check = fcheck.read()
fcheck.close()
if(check == "true"):
    buffer = input("Hello! Please, enter your base system (Linux/Windows): ")
    oss = open("configs/system.cfg", "w")
    if(buffer == "Windows" or buffer == "windows"):
        oss.write("windows\n")
    if(buffer == "Linux" or buffer == "linux"):
        oss.write("linux\n")
    oss.close()
settings = open("configs/system.cfg", "r")                  #base
buffer = settings.read()
if(buffer == "linux\n"):
    clean = "clear"
    syst = "| base system: LINUX   |"
if(buffer == "windows\n"):
    clean = "cls"
    syst = "| base system: WINDOWS |"
settings.close()                                #основа
lang = open("configs/lang.cfg", "r")
buffer = lang.read()
lg = ""
if(buffer == "eng"):
    lg = "eng"
if(buffer == "rus"):
    lg = "rus"
lang.close()
if(lg == "eng"):
    if(syst == "| base system: LINUX   |"):
        os.system("python3 system/oobe.py")
        os.system("python3 system/core.py")
    if(syst == "| base system: WINDOWS |"):
        os.system("python system/oobe.py")
        os.system("python system/core.py")
if(lg == "rus"):
    if(syst == "| base system: LINUX   |"):
        os.system("python3 system/oobe_rus.py")
        os.system("python3 system/core_ru.py")
    if(syst == "| base system: WINDOWS |"):
        os.system("python system/oobe_rus.py")
        os.system("python system/core_ru.py")