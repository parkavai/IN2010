import math 

def BubbleDown(A,i,n):
    largest = i 
    left = 2*i + 1
    right = 2*i + 2
    if(left < n and A[largest] < A[left]):
        largest, left = left, largest 
    if(right < n and A[largest] < A[right]):
        largest, right = right, largest 
    if(i != largest):
        A[i], A[largest] = A[largest], A[i]
        BubbleDown(A,largest,n)
    
def BuildMaxHeap(A,n):
    for i in range(math.ceil(n//2-1), -1, -1):
        BubbleDown(A,i,n)

def HeapSort(A):
    n = len(A)
    BuildMaxHeap(A,n)
    for i in range(n-1, 0, -1):
        A[0], A[i] = A[i], A[0]
        BubbleDown(A,0,i)

liste = [12,11,13,5,6,7]
HeapSort(liste)
print(liste)
