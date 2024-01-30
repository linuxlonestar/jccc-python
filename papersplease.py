import time

print("papers, please\n")

time.sleep(4)

name = input("enter a valid name\n")

if name == "god":
    print("you shouldn't have come.\n\nend")
    exit()

seal = input("enter a valid seal code.\n")

if seal == "1234":
    print("welcome!")

else:
    print("you are not allowed in.\n")
    print("end")
    