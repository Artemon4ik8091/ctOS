#OPERATING SYSTEM ctOS
import os
import time
from datetime import datetime
import platform
com = str("")
buffer1 = ""
buffer2 = 0
start = "true"
clean = ""
if platform.system() == "Windows":
    clean = "cls"
    syst = "| base system: WINDOWS |"
elif platform.system() == "Linux":
    clean = "clear"
    syst = "| base system: LINUX   |"
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