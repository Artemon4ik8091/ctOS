import os
import platform
syst = platform.system()
print("-----------------------------------------------------------------------------------------------------------")
print("| ctOS Store - App Store for ctOS. Visit https://github.com/ctOS-Packages and select package for install. |")
print("-----------------------------------------------------------------------------------------------------------")
com = input("Enter package name to install: ")
if (syst == "Linux" or syst == "Darwin"):
    os.system("cd apps; git clone https://github.com/ctOS-Packages/" + com + ";")
if (syst == "Windows"):
    os.system("cd apps & git clone https://github.com/ctOS-Packages/" + com)
print("Done.")