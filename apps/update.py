import os
import platform
if platform.system() == "Windows":
    clean = "cls"
    syst = "| base system: WINDOWS |"
elif platform.system() == "Linux":
    clean = "clear"
    syst = "| base system: LINUX   |"
print("----------------------------------------------------------------------")
print("| Please make backup your data and programms before updating system. |")
print("| Are you sure want to update the system?                            |")
print("----------------------------------------------------------------------")
work = input("(Y/N) ")
if (work == "Y" or work == "y"):
    if (syst == "| base system: LINUX   |"):
        os.system(clean)
        print("Updating...")
        os.chdir('..')
        os.system("rm -rf ctOS")
        os.system("git clone https://github.com/Artemon4ik8091/ctOS.git")
        os.chdir('ctOS')
        os.system("chmod +x *")
        key = open("configs/.perm.cfg", "w")
        key.write("KJRT5-RFEF3-3454F-MHY45-SDKG0\n")
        key.close()
        os.system(clean)
        print("Completed!")
    if (syst == "| base system: WINDOWS |"):
        os.system(clean)
        print("Updating...")
        os.chdir('..')
        os.system("rmdir \"ctOS\" /s /q")
        os.system(clean)
        print("Updating...")
        os.system("git clone https://github.com/Artemon4ik8091/ctOS.git")
        os.chdir('ctOS')
        #os.system("chmod +x *")
        key = open("configs/.perm.cfg", "w")
        key.write("KJRT5-RFEF3-3454F-MHY45-SDKG0\n")
        key.close()
        os.system(clean)
        print("Completed!")
else:
    print("Abort.")