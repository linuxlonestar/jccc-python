import random

#first list. initial list stuff including random number from the randomint function.
firstList = ["steamed hams", random.randint(1, 3), "I can tell at sight a mauser rifle from a javelin"]

#print the initial list
print("\n", firstList, "\n")

#create and fill new, unorganized list to be sorted and combined with old list.
newList = ["they're digging in the wrong place", random.random(), random.random(), random.random(), random.randint(123, 125), random.randint(10, 15), random.randint(100, 150), "I see a line of cars and they're all painted black", "It's 106 miles to Chicago, we got a full tank of gas, half a pack of cigarettes, it's dark... and we're wearing sunglasses."]

#combine the lists and print message for confirmation.
firstList = firstList + newList
print("Appending new items\n")

#initialize lists for sorting.
intList = []
floatList = []
strList = []

#use a for loop to sort through each item and put them into lists based on type.
for i in firstList:
    if isinstance(i, str):
        strList.append(i)
    elif isinstance(i, float):
        floatList.append(i)
    elif isinstance(i, int):
        intList.append(i)

#combine lists in order, print in neat fassion. (btw I got some stuff from stack overflow for the sep= part and the
#isinstance checks)
finalList = intList + floatList + strList
print("\nFinal list:]\n")
print(*finalList,sep="\n")
print()
