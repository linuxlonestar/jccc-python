A = [5, 7, 2, 9, 12, 4, 14, 6, 3]
print("Unsorted list:", A, "\n")
swapped = False
i = 0
j = i + 1
for z in range(len(A)):
    
    if A[i] > A[j]:
        A[i], A[j] = A[j], A[i]
        swapped = True
    if i < (len(A) - 1):
        i = i + 1
        j = i + 1
    if swapped == True:
        swapped = False
        i = 0
print("sorted list:", A, "\n")
    
        
