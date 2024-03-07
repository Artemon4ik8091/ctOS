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
key = 0
print("Запуск...")
time.sleep(0.3)
if platform.system() == "Windows":
    clean = "cls"
    syst = "| base system: WINDOWS |"
elif platform.system() == "Linux":
    clean = "clear"
    syst = "| base system: LINUX   |"                    #основа
settings = open("configs/build.cfg", "r")
if (settings == ''):
    settings = 700
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
time.sleep(0.1)
os.system(clean)
comlog = open("logs/comlog.txt", "w")
buflog = open("logs/buflog.txt", "w")
account = open("configs/.perm.cfg")
activ_key = account.readline()
account.close()
if (activ_key != "true"):
    print("Пожалуйста, активируйте ctOS перед использованием")
    login = str(input("Ключ активации: "))
    print("Активация...")
    if(login == activ_key):
        time.sleep(1)
        start = "true"
        os.system(clean)
        account = open("configs/.perm.cfg", "w")
        account.write("true")
        account.close()
        key = 1
    elif(login != activ_key + "\n"):
        time.sleep(1)
        os.system(clean)
        print("Ключ активации неверный.")
        print("Свяжитесь с разработчиком для получения ключа активации")
        print("Нажмите enter для продолжения.")
        input()
        key = 0
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
        print("Пожалуйста активируйте систему.")
        print(" ╭──["+ user + "@CTOS]────["+ str(time1) +"]────["+ str(build) +"]")
        print("["+ str(count) +"]")
    com = input(" ╰──["+ pwd +"]──➤$ ") 
    buffer = ""
    buffer2 = ""
    comlog.writelines(str(times) + ": " + com + "\n")
    count += 1                                       #Глав. строка
    if (com == 'update'):
        if(syst == "| base system: LINUX   |"):
            os.system("python3 apps/update.py")
        if(syst == "| base system: WINDOWS |"):
            os.system("python apps/update.py")
    if (com == "pip"):
        buffer = input("Введите комманду для pip: ")
        if(syst == "| base system: LINUX   |"):
            os.system("python3 -m pip " + buffer)
        if(syst == "| base system: WINDOWS |"):
            os.system("python -m pip " + buffer)
    if(com == "usr edit"):
        print("Введи информацию о себе:")
        user = open("configs/user.cfg", "w")
        buffer = input("Введи своё имя: ")
        user.write(buffer + "\n")
        buffer = input("Введи свой возраст: ")
        user.write(buffer + "\n")
        buffer = input("Введи свой город: ")
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
        print("Успех!")
    if(com == "lang"):
        if(syst == "| base system: LINUX   |"):
            os.system("python3 system/ed_lg.py")
        if(syst == "| base system: WINDOWS |"):
            os.system("python system/ed_lg.py")
    if(com == "usr info"):
        print("Введите имя пользователя для получения информации: ")
        print(buser)
        print("ROOT")
        print("--------------------")
        buffer = input("")
        if (buffer == buser):
            print("--------------------")
            print("Имя: " + user)
            print(years + " лет")
            print("Город: " + city)
            print("--------------------")
        if (buffer == "ROOT" or buffer == "root" or buffer == "Root"):
            print("Это системный пользователь.")
    if(com == "pacman"):
        com = input("Введите команду: ")
        if (com == "install"):
            file_name = input("Введите имя файла для установки пакета: ")
            file = open(file_name, "r", encoding="utf8")
            buffer6 = file.readline(100)
            fix = len(buffer6)
            buffer7 = buffer6[:fix-1]
            buffer5 = file.read()
            print("----------------")
            print("Наименование пакета: " + buffer7)
            print("----------------")
            package = open(buffer7, "w", encoding="utf8")
            package.write(buffer5)
            package.close()
            file.close()
        if(com == "new-package"):       
            file_name = input("Введите имя файла для преобразования в файл установочного пакета: ")
            file = open(file_name, "r")
            buffer1 = file.read()
            backup_name = input("Введите имя файла установочного пакета, но НЕ ИСПОЛЬЗУЙТЕ РАСШИРЕНИЕ ФАЙЛА!!!!!! ")
            backup = open(backup_name + ".ct", "w")
            backup.writelines(file_name + "\n")
            backup.write(buffer1)
            file.close()
            backup.close()
    if(com == "cfile"):
        if(user != "ROOT"):                                             
            print("У вас нет разрешения на эту операцию")
        if(user == "ROOT"):            
            buffer = input("Введите старый путь к файлу: ")
            buffer2 = input("Введите новый путь к файлу: ")
            os.replace(buffer, buffer2)
    if(com == "fi"):
        if(user == "ROOT"):
            buffer = input("введите название файл (с расширением): ")
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
            print("У вас нет разрешения на эту операцию")
    if(com == "df"):
        if(user != "ROOT"):
            print("У вас нет разрешения на эту операцию")
        if(user == "ROOT"):            
            buffer = input("Введите название файла (с расширением): ")
            os.remove(buffer)
    if(com == "renf"):
        if(user != "ROOT"):
            print("У вас нет разрешения на эту операцию")
        if(user == "ROOT"):            
            buffer = input("Введите название файла (с расширением): ")
            buffer2 = input("Введите новое название файла (можно с расширением или без) ")
            os.rename(buffer, buffer2)
    if(com == "rf"):
        buffer = input("Введите название файла (с расширением): ")
        file = open(buffer, "r")
        print("---------------------")
        print(*file)
        print("---------------------")
        file.close()
    if(com == "wf"):
        buffer = input("Введите имя файла (с расширением): ")
        file = open(buffer, "w")
        print("------------------------")
        text = input()
        print("------------------------")
        file.write(text)
        time.sleep(0.1)
        file.close()
        print("Сохранено!")
    if(com == "dev"):
        if(user == "ROOT"):
            print("------------------------")
            print("| ctOS                 |")
            print(syst)
            print("| Build: " + str(build) + "           |")
            print("------------------------")
        if(user != "ROOT"):
            print("У вас нет разрешения на эту операцию")
    if(com == "cd"):
        buffer = input("Введите НАЗВАНИЕ папки, или оставьте поле пустым, чтобы перейти к корневой папке: ")
        if (buffer != ""):
            os.chdir(buffer)
        if (buffer == ""):
            os.chdir("../")
    if (com == "usr switch"):
        print("Введите имя профиля:")
        print(buser)
        print("ROOT [Все возможности]")
        buffer = input()
        if(buffer == "ROOT" or buffer == "root" or buffer == "Root"):
            buffer2 = input("Введите пароль: ")
            if (buffer2 == "5125"):
                user = "ROOT"
                print("------------------------------------------------------------------------------------------------------------")
                print("| ВНИМАНИЕ! Мы не несем ответственности за все ваши действия в этом аккаунте пользователя. Будь осторожен! |")
                print("------------------------------------------------------------------------------------------------------------")
                time.sleep(0.5)
                print("Замена  пользователя прошла успешно.")
            if (buffer2 != "5125"):
                print("Пароль не правильный.")
        if(buffer == buser):
            user = buser
            time.sleep(0.5)
            print("Замена  пользователя прошла успешно.")
    if(com == "ls"):
        if(user != "ROOT"):                                             #Простое разрешение [заметка для разработчика]
            print("У вас нет разрешения на эту операцию")
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
        print("ROOT [Все возможности]")
    if(com == "ver"):
        if(syst == "| base system: LINUX   |"):
            os.system("python3 system/vers.py")
        if(syst == "| base system: WINDOWS |"):
            os.system("python system/vers.py")
    if(com == "openpy"):
        buffer = input("Введите путь к файлу или имя файла: ")
        if(syst == "| base system: LINUX   |"):
            os.system("python3 " + buffer)
        if(syst == "| base system: WINDOWS |"):
            os.system("python " + buffer)
    if(com == "run"):
        if(user != "ROOT"):
            print("У вас нет разрешения на эту операцию")
        if(user == "ROOT"):
            buffer = input("Введите путь к файлу, или имя файла (С РАСШИРЕНИЕМ), или другую команду: ")
            os.system(buffer)
    if(com=="clear"):
        os.system(clean)
    if(com == "md"):
        buffer = input("Введите имя папки: ")
        if not os.path.isdir(buffer):
            os.mkdir(buffer)
            time.sleep(0.05)
            print("Завершено!")
    if(com == "rd"):
        buffer = input("Введите имя папки ")
        os.rmdir(buffer)
        time.sleep(0.05)
        print("Завершено!")
    if(com=="date"):
        print(datetime.today())
    if(com=="help"):
        print("-----------                               ----------")
        print("help - Показать этот список")
        print("date - Вывод даты и времени")
        print("calc - калькулятор - Старт калькулятора [package]")
        print("echo - Выведите свой текст")
        print("logout - Выключение данной операционной системы")
        print("clear - Очистка экрана")
        print("openpy - Запуск *.py файлов")
        print("run - Открытие других файлов [ROOT]")
        print("ver - Вывод версии ОС [package]")
        print("usr list - Вывод всех пользователей в системе и их разрешения")
        print("usr switch - Выбор пользователя")
        print("usr edit - Изменение информации о вашем базовом пользователе")
        print("timer - запуск программы 'таймер' [package]")
        print("ls - Вывод файлов и каталогов [ROOT]")
        print("md - Создать каталог (папку)")
        print("rd - Удалить каталог (папку)")
        print("cd - переход между папками и каталогами")
        print("wf - Записать информацию в файл или создать новый файл")
        print("rf - Прочитать файл")
        print("df - Удалить файл [ROOT]")
        print("renf - Переименовать файл [ROOT]")
        print("fi - Вывод ифнормации о файл [ROOT]")
        print("cfile - Перенос файла [ROOT]")
        print("pacman - установить (install) новый пакет или создать новый (new-package)")
        print("lang - Смена языка на английский.")
        print("pip - Ввод комманды для pip")
        print("update - обновляет систему до последней версии")
        print("-----------                               ----------")
    if(com=="calc"):
        if(syst == "| base system: LINUX   |"):
            os.system("python3 calcs.py")
        if(syst == "| base system: WINDOWS |"):
            os.system("python calcs.py")
    if(com == "echo"):
        buffer = input("Введите текст: ")
        print(buffer)
    if(com=="logout" or com == "exit"):
        os.system(clean)
        print("До свидания...")
        time.sleep(1)
        start = "false"
        os.system(clean)
        time.sleep(0.1)
        times1 = datetime.today()
        comlog.writelines("Завершение сеанса до: " + str(times1) + "\n")