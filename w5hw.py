A = [6, 4, 12, 9, 45, 23, 2, 43, 56, 17, 20, 11, 7]
print("\nUnsorted list:", A, "\n")

smallValueIndex = 0
largeValueIndex = 0
smallValue = A[0]
largeValue = A[len(A)-1]

for i in range(len(A)):
    if A[i] < smallValue:
        smallValue = A[i]
        smallValueIndex = i
    if A[i] > largeValue:
        largeValue = A[i]
        largeValueIndex = i

A[smallValueIndex] = A[0]
A[largeValueIndex] = A[len(A) - 1]
A[len(A) - 1] = largeValue

print("Sorted list:", A, "\n")
