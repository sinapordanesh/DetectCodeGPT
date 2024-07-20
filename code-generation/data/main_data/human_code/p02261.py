# 配列の宣言
A = []
B = []

# 文字列の取得と加工
LENGTH =int(input())
A = input().split()
B = A.copy()

def bubble (A, LENGTH):
    N = 0
    M = LENGTH - 1
    CHANGE = 0

    while N <= LENGTH -1:
        M = LENGTH - 1
        while M >= N + 1:
            if int(A[M][1:]) < int(A[M-1][1:]):
                tmp = A[M-1]
                A[M-1] = A[M]
                A[M] = tmp
                CHANGE += 1
            M -= 1
        N += 1

    print(" ".join(map(str,A)))
    print("Stable")

def selection (B, LENGTH):
    i = 0
    CHANGE_COUNT = 0

    while i <= LENGTH -1:
        j = i + 1
        mini = i
        while j <= LENGTH -1:
            if int(B[j][1:]) < int(B[mini][1:]):
                mini = j
            j += 1
        if mini != i:
            tmp = B[i]
            B[i] = B[mini]
            B[mini] = tmp
            CHANGE_COUNT += 1
        i += 1

    print(" ".join(map(str,B)))
    if A == B:
        print("Stable")
    else:
        print("Not stable")

bubble (A, LENGTH)
selection (B, LENGTH)
