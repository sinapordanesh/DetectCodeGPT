def selectionSort(N, A):
    count = 0
    for i in range(N):
        minj = i
        for j in range(i, N):
            if A[j] < A[minj]:
                minj = j
        if i != minj:
            k = A[i]
            A[i] = A[minj]
            A[minj] = k
            count += 1
    print(" ".join(map(str, A)))
    print(count)


n = int(input())
a = list(map(int, input().split()))
selectionSort(n, a)
