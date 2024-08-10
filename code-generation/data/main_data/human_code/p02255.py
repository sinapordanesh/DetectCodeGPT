
n = int(input())
a = list(map(int,input().split()))

print(" ".join(list(map(str,a))))
def insertionSort(A,N):
    for i in range(1,N):
        v = A[i]
        j = i-1
        while j>=0 and A[j]>v:
            A[j+1]=A[j]
            j-=1
        A[j+1]=v
        print(" ".join(list(map(str,A))))

insertionSort(a,n)
