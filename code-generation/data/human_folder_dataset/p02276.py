def printAns( A, index ):
    n = len(A)
    for i in range(0, index):
        print( str( A[i] ), end=" ")
    print( "[" + str(A[index]), end="] ")
    for i in range(index+1, n-1):
        print( str( A[i] ), end=" ")
    print( str( A[n-1] ) )

def partition(A, p, r):
    tmp = 0
    x = A[r]
    i = p-1
    for j in range(p, r):
        if A[j] <= x:
            i += 1
            tmp = A[j]
            A[j] = A[i]
            A[i] = tmp
    tmp = A[i+1]
    A[i+1] = A[r]
    A[r] = tmp
    printAns(A, i+1)
    return i+1

def main():
    n = int( input() )
    A = [int(x) for x in input().split()]
    index = partition(A, 0, n-1)

if __name__ == "__main__":
    main()

