def lexicographical_comparison():
    n = int(input())
    A = list(map(int, input().split()))
    m = int(input())
    B = list(map(int, input().split()))

    min_length = min(n, m)

    for i in range(min_length):
        if A[i] < B[i]:
            print(1)
            return
        elif A[i] > B[i]:
            print(0)
            return

    if n < m:
        print(1)
    else:
        print(0)

lexicographical_comparison()