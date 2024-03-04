import math

numList = []
for num in range(10):
    keyInput = input(f"please input number {num + 1}\n")
    keyInput = float(keyInput)
    numList.append(keyInput)

averageList = sum(numList) / len(numList)
print(f"\nThe average of the provided numbers is: {averageList}")

larNum = max(numList)
smallNum = min(numList)
print(f"The largest number in the list is {larNum}")
print(f"The smallest number in the list is {smallNum}\n")
