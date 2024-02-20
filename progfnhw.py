# code to create a list of 10 values
values =[]
print(f"Please enter 10 values\n")

def input_numbers():
    for i in range(0,10):
        item = input(f"Please enter item {i + 1}: ")
        values.append(item) 
    print(values)

input_numbers()


def int_print():
    print(f"Integer values are:")
    for item in values:
        if item.isnumeric():
            if "." not in item:
                print(item)     

int_print()

def float_print():
    print(f"Float values are:")
    for item in values:
        if "."  in item:
            print(item)        

float_print()

def text_print():
    print(f"text values are:")
    for item in values:
        if not item.isnumeric():
            if "." not in item:
                print(item)

text_print()

if __name__=='__main__':
    pass
