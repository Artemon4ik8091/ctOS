import os
settings = open("configs/system.cfg", "r")
buffer = settings.read()
if(buffer == "linux\n"):
    clean = "clear"
    syst = "| base system: LINUX   |"
if(buffer == "windows\n"):
    clean = "cls"
    syst = "| base system: WINDOWS |"
settings.close()
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
    print("Completed!")