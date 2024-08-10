def maxHeapify(A, i):
    l = 2*i + 1
    r = 2*i + 2
    if l < len(A) and A[l] > A[i]:
        largest = l
    else:
        largest = i
    if r < len(A) and A[r] > A[largest]:
        largest = r
    if largest != i:
        A[i], A[largest] = A[largest], A[i]
        maxHeapify(A, largest)

def buildMaxHeap(A):
    for i in range(len(A)//2, -1, -1):
        maxHeapify(A, i)