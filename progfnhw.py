# code to create a list of 10 values
values =[]
print(f"Please enter 10 values\n")
for i in range(0,10):
    item = input(f"Please enter item {i + 1}: ")
    values.append(item) 

print(values)

print(f"Integer values are:")
for item in values:
    if item.isnumeric():
        if "." not in item:
            print(item)     

print(f"Float values are:")
for item in values:
    if "."  in item:
        print(item)        

print(f"text values are:")
for item in values:
    if not item.isnumeric():
        if "." not in item:
            print(item)


if __name__=='__main__':
    pass
