user = open("test.txt", "w")
buffer = input("Enter your name: ")
user.write(buffer + "\n")
buffer = input("Enter your years old: ")
user.write(buffer + "\n")
buffer = input("Enter your city: ")
user.write(buffer)
user.close()


file = open("test.txt", "r")
buffer = file.readline()
fix = len(buffer)
name = buffer[:fix-1]
print("Name: " + name)
buffer3 = file.readline()
fix = len(buffer3)
years = buffer3[:fix-1]
print(years + " years old")
buffer5 = file.readline()
print("City: " + buffer5)
file.close()




#print("-----------------------")
#if (buffer == "This is line1"):
#    print("YES")
#if (buffer != "This is line1"):
#    print("NO")