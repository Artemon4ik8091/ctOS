#OPERATING SYSTEM ctOS
import os
import time
from datetime import datetime
com = str("")
buffer1 = ""
buffer2 = 0
start = "true"
clean = ""
settings = open("configs/system.cfg", "r")
buffer = settings.read()
if(buffer == "linux\n"):
    clean = "clear"
    syst = "| base system: LINUX   |"
if(buffer == "windows\n"):
    clean = "cls"
    syst = "| base system: WINDOWS |"
settings.close()
os.system(clean)
while(start == "true"):
    time.sleep(0.085)
    print("[           ]")
    time.sleep(0.2)
    os.system(clean)
    print("[-          ]")
    time.sleep(0.085)
    os.system(clean)
    print("[--         ]")
    time.sleep(0.085)
    os.system(clean)
    print("[---        ]")
    time.sleep(0.085)
    os.system(clean)
    print("[----       ]")
    time.sleep(0.085)
    os.system(clean)
    print("[-----      ]")
    time.sleep(0.085)
    os.system(clean)
    print("[------     ]")
    time.sleep(0.085)
    os.system(clean)
    print("[-------    ]")
    time.sleep(0.085)
    os.system(clean)
    print("[--------   ]")
    time.sleep(0.085)
    os.system(clean)
    print("[---------  ]")
    time.sleep(0.085)
    os.system(clean)
    print("[---------- ]")
    time.sleep(0.085)
    os.system(clean)
    print("[-----------]")
    time.sleep(0.085)
    os.system(clean)
    buffer2 += 1
    if(buffer2 >= 5):
        os.system(clean)
        print("Exiting...")
        start = "false"
        time.sleep(0.5)