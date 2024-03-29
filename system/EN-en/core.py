#! configs/system.cfg python
# -*- coding: utf-8 -*-
#OPERATING SYSTEM ctOS
import os
import time
from datetime import datetime
import platform
com = str("")
start = "false"
user = "User"
clean = ""
syst = ""
buffer = ""
buffer2 = ""
count = 1
security = ""
key = 0
print("Starting...")
time.sleep(0.3)
if platform.system() == "Windows":
    clean = "cls"
    syst = "| base system: WINDOWS |"
elif platform.system() == "Linux" or platform.system() == "Darwin":
    clean = "clear"
    syst = "| base system: LINUX   |"                    #основа
settings = open("configs/build.cfg", "r")
if (settings == ''):
    settings = 700                                #основа
settings = open("configs/build.cfg", "r")
build = int(settings.read())
build += 1
settings.close()
set = open("configs/build.cfg", "w")
set.write(str(build))
if(syst == "| base system: LINUX   |"):
    os.system("python3 system/loan.py")
if(syst == "| base system: WINDOWS |"):
    os.system("python system/loan.py")
print("ok")
cuser = open("configs/user.cfg", "r")
buffer = cuser.readline()
fix = len(buffer)
user = buffer[:fix-1]
buser = user
buffer3 = cuser.readline()
fix = len(buffer3)
years = buffer3[:fix-1]
city = cuser.readline()
cuser.close()
time.sleep(0.1)
os.system(clean)
comlog = open("logs/comlog.txt", "w")
buflog = open("logs/buflog.txt", "w")
account = open("configs/.perm.cfg")
activ_key = account.readline()
account.close()
if (activ_key != "true"):
    print("Please activating system before you start using ctOS, or press Enter if not have activation key.")
    login = str(input("Key: ") + "\n")
    print("Activating...")
    if(login == activ_key):
        time.sleep(1)
        start = "true"
        os.system(clean)
        account = open("configs/.perm.cfg", "w")
        account.write("true")
        key = 1
    elif(login != activ_key):
        time.sleep(1)
        os.system(clean)
        key = 0
        print("Key incorrect.")
        print("You using not activated system, please contact at developer for give activation key.")
        input("Press Enter to continue..")
        start = "true"
elif(activ_key == "true"):
    start = "true"
    key = 1
while(start == "true"):
    times = datetime.today()
    if(buffer != ""):
        buflog.writelines(str(times) + " buffer: " + str(buffer) + "\n")
    if(buffer2 != ""):
        buflog.writelines(str(times) + " buffer2: " + str(buffer2) + "\n")
    buffer = ""
    buffer2 = ""
    time1 = datetime.now()
    pwd = os.getcwd()
    if (key == 1):
        print(" ╭──["+ user + "@CTOS]────["+ str(time1) +"]────["+ str(build) +"]")
        print("["+ str(count) +"]")
    if (key == 0):
        print("Please activate system.")
        print(" ╭──["+ user + "@CTOS]────["+ str(time1) +"]────["+ str(build) +"]")
        print("["+ str(count) +"]")
    com = input(" ╰──["+ pwd +"]──➤$ ")
    buffer = ""
    buffer2 = ""
    count += 1
    comlog.writelines(str(times) + ": " + com + "\n")   #Глав. строка
    if (com == "apct"):
        if(syst == "| base system: LINUX   |"):
            os.system("python3 system/apct.py")
        if(syst == "| base system: WINDOWS |"):
            os.system("python system/apct.py")
    if (com == 'update'):
        if(syst == "| base system: LINUX   |"):
            os.system("python3 apps/update.py")
        if(syst == "| base system: WINDOWS |"):
            os.system("python apps/update.py")
    if (com == "pip"):
        buffer = input("Enter function for pip: ")
        if(syst == "| base system: LINUX   |"):
            os.system("python3 -m pip " + buffer)
        if(syst == "| base system: WINDOWS |"):
            os.system("python -m pip " + buffer)
    if(com == "lang"):
        if(syst == "| base system: LINUX   |"):
            os.system("python3 system/ed_lg.py")
        if(syst == "| base system: WINDOWS |"):
            os.system("python system/ed_lg.py")
    if(com == "usr edit"):
        print("Enter information about yourself:")
        user = open("configs/user.cfg", "w")
        buffer = input("Enter your name: ")
        user.write(buffer + "\n")
        buffer = input("Enter your years old: ")
        user.write(buffer + "\n")
        buffer = input("Enter your city: ")
        user.write(buffer)
        user.close()
        cuser = open("configs/user.cfg", "r")
        buffer = cuser.readline()
        fix = len(buffer)
        user = buffer[:fix-1]
        buser = user
        buffer3 = cuser.readline()
        fix = len(buffer3)
        years = buffer3[:fix-1]
        city = cuser.readline()
        cuser.close()
        time.sleep(0.3)
        print("Complete!")
    if(com == "usr info"):
        print("Enter user for print information: ")
        print(buser)
        print("ROOT")
        print("--------------------")
        buffer = input("")
        if (buffer == buser):
            print("--------------------")
            print("Name: " + buser)
            print(years + " years old")
            print("City: " + city)
            print("--------------------")
        if (buffer == "ROOT" or buffer == "root" or buffer == "Root"):
            print("This is system user.")
    if(com == "pacman"):
        com = input("Enter command: ")
        if (com == "install"):
            file_name = input("Enter file name for install package: ")
            file = open(file_name, "r", encoding="utf8")
            buffer6 = file.readline(100)
            fix = len(buffer6)
            buffer7 = buffer6[:fix-1]
            buffer5 = file.read()
            print("----------------")
            print("Package name: " + buffer7)
            print("----------------")
            package = open(buffer7, "w", encoding="utf8")
            package.write(buffer5)
            package.close()
            file.close()
        if(com == "new-package"):       
            file_name = input("Enter a file name to convert to an installation package file: ")
            file = open(file_name, "r")
            buffer1 = file.read()
            backup_name = input("Enter the filename of the installation package, but DO NOT USE THE FILE EXTENSION!!!!!! ")
            backup = open(backup_name + ".ct", "w")
            backup.writelines(file_name + "\n")
            backup.write(buffer1)
            file.close()
            backup.close()
    if(com == "cfile"):
        if(user != "ROOT"):                                             
            print("You not have permission for this operation")
        if(user == "ROOT"):            
            buffer = input("Enter old path file: ")
            buffer2 = input("Enter new path file: ")
            os.replace(buffer, buffer2)
    if(com == "fi"):
        if(user == "ROOT"):
            buffer = input("Enter file: ")
            open(buffer, "r")
            print("-----------------------")
            buffer2 = os.stat(buffer)
            print(buffer2)
            print("-----------------------")
            print("st_size — размер файла в байтах")
            print("st_atime — время последнего доступа в секундах (временная метка)")
            print("st_mtime — время последнего изменения")
            print("st_ctime — в Windows это время создания файла, а в Linux — последнего изменения метаданных")
            print("-----------------------")
        if(user != "ROOT"):
            print("You not have permission for this operation")
    if(com == "df"):
        if(user != "ROOT"):
            print("You not have permission for this operation")
        if(user == "ROOT"):            
            buffer = input("Enter file: ")
            os.remove(buffer)
    if(com == "renf"):
        if(user != "ROOT"):
            print("You not have permission for this operation")
        if(user == "ROOT"):            
            buffer = input("Enter file: ")
            buffer2 = input("Enter new file name: ")
            os.rename(buffer, buffer2)
    if(com == "rf"):
        buffer = input("Enter file name: ")
        file = open(buffer, "r")
        print("---------------------")
        print(*file)
        print("---------------------")
        file.close()
    if(com == "wf"):
        buffer = input("Enter file name: ")
        file = open(buffer, "w")
        print("------------------------")
        text = input()
        print("------------------------")
        file.write(text)
        time.sleep(0.1)
        file.close()
        print("Saved!")
    if(com == "dev"):
        if(user == "ROOT"):
            print("------------------------")
            print("| ctOS                 |")
            print(syst)
            print("| Build: " + str(build) + "           |")
            print("------------------------")
        if(user != "ROOT"):
            print("You not have permission for this operation")
    if(com == "cd"):
        buffer = input("Enter the name folder or leave the field blank to go to the root folder: ")
        if (buffer != ""):
            os.chdir(buffer)
        if (buffer == ""):
            os.chdir("../")
    if (com == "usr switch"):
        print("Select username:")
        print(buser)
        print("ROOT [All permissions]")
        buffer = input()
        if(buffer == "ROOT" or buffer == "root" or buffer == "Root"):
            buffer2 = input("Enter password: ")
            if (buffer2 == "5125"):
                user = "ROOT"
                print("------------------------------------------------------------------------------------")
                print("| ATTENTION! We are not responsible for all your actions in this user. Be careful! |")
                print("------------------------------------------------------------------------------------")
                time.sleep(0.5)
                print("Complete")
            if (buffer2 != "5125"):
                print("Password incorrect.")
        if(buffer == buser):
            user = buser
            time.sleep(0.5)
            print("Complete")
    if(com == "ls"):
        if(user != "ROOT"):                                             #Простое разрешение [заметка для разработчика]
            print("You not have permission for this operation")
        if(user == "ROOT"):
            print("--------------------------------------------")
            buffer = os.listdir(pwd)
            print(buffer)
            print("--------------------------------------------")
    if(com == "timer"):
        if(syst == "| base system: LINUX   |"):
            os.system("python3 timer.py")
        if(syst == "| base system: WINDOWS |"):
            os.system("python timer.py")
    if(com == "usr list"):
        print("Users:")
        print(buser)
        print("ROOT [All permissions]")
    if(com == "ver"):
        if(syst == "| base system: LINUX   |"):
            os.system("python3 system/vers.py")
        if(syst == "| base system: WINDOWS |"):
            os.system("python system/vers.py")
    if(com == "openpy"):
        buffer = input("Enter the path to the file or file name: ")
        if(syst == "| base system: LINUX   |"):
            os.system("python3 " + buffer)
        if(syst == "| base system: WINDOWS |"):
            os.system(buffer)
    if(com == "run"):
        if(user != "ROOT"):
            print("You not have permission for this operation")
        if(user == "ROOT"):
            buffer = input("Enter the path to the file, or file name, or other command: ")
            os.system(buffer)
    if(com=="clear"):
        os.system(clean)
    if(com == "md"):
        buffer = input("Enter folder name: ")
        if not os.path.isdir(buffer):
            os.mkdir(buffer)
            time.sleep(0.05)
            print("Complete!")
    if(com == "rd"):
        buffer = input("Enter folder name: ")
        os.rmdir(buffer)
        time.sleep(0.05)
        print("Complete!")
    if(com=="date"):
        print(datetime.today())
    if(com=="help"):
        print("-----------                               ----------")
        print("help - print this list")
        print("date - print date and time")
        print("calc - start calculator program [package]")
        print("echo - print your string")
        print("logout - shutting down the operating system")
        print("clear - Clear screen")
        print("openpy - Starting *.py file")
        print("run - Opening other files [ROOT]")
        print("ver - print system version [package]")
        print("usr list - Print all users in system and his permissions")
        print("usr switch - Switch user")
        print("usr edit - editing information your base user")
        print("timer - start timer program [package]")
        print("ls - Print files and directories for directory [ROOT]")
        print("md - make directory")
        print("rd - delete directory")
        print("wf - write information to file or make new file")
        print("rf - Read file")
        print("df - delete file [ROOT]")
        print("renf - rename file [ROOT]")
        print("fi - Print file information [ROOT]")
        print("cfile - Transfer file [ROOT]")
        print("pacman - install file or package or create new.")
        print("cd - change directory")
        print("usr info - print more info a user")
        print("lang - Change language to Russian")
        print("pip - Enter command for pip")
        print("update - Updating your system to last version")
        print("apct - package downloader")
        print("-----------                               ----------")
    if(com=="calc"):
        if(syst == "| base system: LINUX   |"):
            os.system("python3 calcs.py")
        if(syst == "| base system: WINDOWS |"):
            os.system("python calcs.py")
    if(com == "echo"):
        buffer = input("Input string: ")
        print(buffer)
    if(com=="logout" or com == "exit"):
        os.system(clean)
        print("Goodbye...")
        time.sleep(1)
        start = "false"
        os.system(clean)
        time.sleep(0.1)
        times1 = datetime.today()
        comlog.writelines("Session end to: " + str(times1) + "\n")