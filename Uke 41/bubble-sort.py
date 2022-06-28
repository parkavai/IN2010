def BubbleSort(A):
    har_byttet = True

    while(har_byttet):
        har_byttet = False
        for i in range (len(A) - 1):
            for j in range (len(A) - i - 1):  
                if (A[j] > A[j + 1]):
                    A[j], A[j + 1] = A[j + 1], A[j]
                    har_byttet = True

liste = [19,13,6,2,18,8]
BubbleSort(liste)
print(liste)