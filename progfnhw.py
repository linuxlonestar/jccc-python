# code to create a list of 10 values
values =[]
print(f"Please enter 10 values\n")

def inputNumbers():
    for i in range(0,10):
        item = input(f"Please enter item {i + 1}: ")
        values.append(item) 
    print(values)

inputNumbers()


def intPrint():
    print(f"Integer values are:")
    for item in values:
        if item.isnumeric():
            if "." not in item:
                print(item)     

intPrint()

def floatPrint():
    print(f"Float values are:")
    for item in values:
        if "."  in item:
            print(item)        

floatPrint()

def textPrint():
    print(f"text values are:")
    for item in values:
        if not item.isnumeric():
            if "." not in item:
                print(item)

textPrint()

if __name__=='__main__':
    pass
