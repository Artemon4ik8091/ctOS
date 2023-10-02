import os
import time
from datetime import datetime
com = str("")
buffer1 = ""
buffer2 = ""
start = "true"
a = float(input("Enter first number: "))
buffer = input("Enter operation (+,-,*,/): ")
b = float(input("Enter second number: "))
if(buffer == "+"):
    buffer2 = a + b
    print(buffer2)
if(buffer == "-"):
    buffer2 = a - b
    print(buffer2)
if(buffer == "*"):
    buffer2 = a * b
    print(buffer2)
if(buffer == "/"):
    buffer2 = a / b
    print(buffer2)