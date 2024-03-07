import os
import platform
fcheck = open("configs/oobe.cfg", "r")
check = fcheck.read()
fcheck.close()                #base
if platform.system() == "Windows":
    clean = "cls"
    syst = "| base system: WINDOWS |"
elif platform.system() == "Linux":
    clean = "clear"
    syst = "| base system: LINUX   |"                             #основа
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
        os.system("python3 system/EN-en/oobe.py")
        os.system("python3 system/EN-en/core.py")
    if(syst == "| base system: WINDOWS |"):
        os.system("python system/EN-en/oobe.py")
        os.system("python system/EN-en/core.py")
if(lg == "rus"):
    if(syst == "| base system: LINUX   |"):
        os.system("python3 system/RU-ru/oobe_rus.py")
        os.system("python3 system/RU-ru/core_ru.py")
    if(syst == "| base system: WINDOWS |"):
        os.system("python system/RU-ru/oobe_rus.py")
        os.system("python system/RU-ru/core_ru.py")