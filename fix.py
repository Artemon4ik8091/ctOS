def fix_y():
    file = open("configs/build.cfg", "w")
    file.write("546")
    file.close()
    file = open("configs/lang.cfg", "w")
    file.write("eng")
    file.close()
    file = open("configs/system.cfg", "w")
    file.write("linux\n")
    file.close()
    
def fix_n():
    return "Exiting..."

print("This script fixing ctOS.")
work = input("Fix? (Y/n) ")
if (work == "n" or work == "R"):
    fix_n()
if (work == "y" or work == "Y"):
    fix_y()