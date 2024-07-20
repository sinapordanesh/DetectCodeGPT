def printAns( A ):
    n = len(A)
    for i in range(1, n-1):
        print( str( A[i] ), end=" ")
    print( str( A[n-1] ) )

def main():
    n = int( input() )
    A = [0]
    list = [int(x) for x in input().split()]
    A.extend(list)
    B = []
    C = []
    k = max(A)

    for i in range(k + 1):
        C.append(0)

    for i in range(n+1):
        B.append(0)

    for j in range(1, n+1):
        C[ A[j] ] += 1

    for i in range(1, k+1):
        C[i] = C[i] + C[i-1]

    for j in reversed(range(n+1)):
        B[ C[ A[j] ] ] = A[j]
        C[ A[j] ] -= 1

    printAns(B)

if __name__ == "__main__":
    main()

