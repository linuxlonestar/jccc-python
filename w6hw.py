#makes base array with interchangable numbers.
baseArray = [0, 10, 23, 14, 16, 30, 21, 5, 11, 19]

#initializes all lists for results.
sumArray = []
curArray = []
nxtArray = []

#zips the baseArray list and adds the current value to a list, the next value to a list, and the sums to a list, all of equal length.
for cur, nxt in zip (baseArray, baseArray [1:] ):
    curArray.append(cur)
    nxtArray.append(nxt)
    sumArray.append(cur+nxt)

#finds the index of the largest and smallest numbers in the sumArray. feeds them to their respective variables.
large = max(range(len(sumArray)), key=sumArray.__getitem__)
small = min(range(len(sumArray)), key=sumArray.__getitem__)

#uses the index of the sum to find the corresponding values that add up to sum, feeds values to print command.
print(f"\nThe smallest value pair in the array is {curArray[small]} + {nxtArray[small]} for a total of {sumArray[small]}")
print(f"\nThe largest value pair in the array is {curArray[large]} + {nxtArray[large]} for a total of {sumArray[large]}\n")