import os
import platform
if platform.system() == "Windows":
    clean = "cls"
    syst = "| base system: WINDOWS |"
elif platform.system() == "Linux":
    clean = "clear"
    syst = "| base system: LINUX   |"
os.system(clean)
print("---------------------------------------------------------------------------------------------------------------------------")
print("|                                                ctOS Installer version 0.6.4                                             |")
print("---------------------------------------------------------------------------------------------------------------------------")
print("| By using this operating system you agree to the rules of its use specified at: http://g90850i2.beget.tech/politics.html |")
print("| Do you agree to the terms and are ready to start installing the operating system?                                       |")
print("---------------------------------------------------------------------------------------------------------------------------")
check = input("(Y/N)")
if (check == "y" or check == "Y"):
    if (syst == "| base system: LINUX   |"):
        os.system(clean)
        print("Installing...")
        os.system("git clone https://github.com/Artemon4ik8091/ctOS.git")
        os.chdir('ctOS')
        os.system("chmod +x *")
        key = open("configs/.perm.cfg", "w")
        key.write("KJRT5-RFEF3-3454F-MHY45-SDKG0\n")
        key.close()
        print("Done.")
    if (syst == "| base system: WINDOWS |"):
        # print("Only for Linux, sorry")
        os.system(clean)
        print("Installing...")
        os.system("git clone https://github.com/Artemon4ik8091/ctOS.git")
        os.chdir('ctOS')
        # os.system("chmod +x *")
        key = open("configs/.perm.cfg", "w")
        key.write("KJRT5-RFEF3-3454F-MHY45-SDKG0\n")
        key.close()
        print("Done.")
if (check != "y" or check != "Y"):
    print()