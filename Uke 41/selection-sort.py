def SelectionSort(A):
    for i in range(len(A)):
        k = i
        for j in range(i+1, len(A)):
            if (A[j] < A[k]):
                k = j
        if (i != k):
            A[i], A[k] = A[k], A[i]
    

liste = [19,13,6,2,18,8]
SelectionSort(liste)
print(liste)