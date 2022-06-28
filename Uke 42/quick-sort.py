import random

def ChoosePivot(A, low, high):
    # Metode 1
    return random.randrange(low,high) 
    

def Partition(A,low,high):
    p = ChoosePivot(A,low,high)
    A[p], A[high] = A[high], A[p]
    pivot = A[high]
    left = low
    right = high - 1
    while left <= right:
        while left <= right and A[left] <= pivot:
            left += 1
        while right >= left and A[right] >= pivot:
            right -= 1
        if(left < right):
            A[left], A[right] = A[right], A[left]
    A[left],A[high] = A[high],A[left]
    return left

def QuickSort(A,low,high):
    if (low >= high):
        return A
    p = Partition(A, low, high)
    QuickSort(A,low, p-1)
    QuickSort(A, p+1, high)
    return A


def main():
    A = [12,11,13,5,6,7,8]
    low = 0
    high = len(A)-1
    print(QuickSort(A,low, high))

main()