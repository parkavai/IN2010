import math

def Merge(A1, A2, A):
    i = 0
    j = 0
    k = 0
    
    while i < len(A1) and j < len(A2):
        if(A1[i] < A2[j]):
            A[k] = A1[i]
            i += 1

        else:
            A[k] = A2[j]
            j += 1
        k += 1

    while (i < len(A1)): 
        A[k] = A1[i]
        i += 1
        k += 1

    while j < len(A2):  
        A[k] = A2[j]
        j += 1
        k += 1
    return A

def MergeSort(A):
    n = len(A)
    if n <= 1:
        return A
    i = n//2
    A1 = MergeSort(A[0:i])
    A2 = MergeSort(A[i:n])
    return Merge(A1,A2,A)

def main():
    A = [12,11,13,5,6,7,8]
    print(MergeSort(A))
    

main()