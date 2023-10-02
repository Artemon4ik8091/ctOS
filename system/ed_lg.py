print("Do you want to change the system language?")
query = input("Хотите сменить язык системы? (Y/N) ")
if(query == "Y" or query == "y"):
    lang = open("configs/lang.cfg", "r")
    buffer = lang.read()
    lg = ""
    if(buffer == "eng"):
        lg = "eng"
    if(buffer == "rus"):
        lg = "rus"
    lang.close()
    langed = open("configs/lang.cfg", "w")
    if(lg == "eng"):
        langed.write("rus")
    if(lg == "rus"):
        langed.write("eng")
    print("Язык системы изменён, перезапустите систему для применения параметров.")
    print("The system language has been changed, restart the system to apply the settings.")
if(query == "n" or query == "N"):
    print("Exiting...")