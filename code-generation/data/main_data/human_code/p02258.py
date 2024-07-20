def max_profit(A, n):
    minv = A[0]
    for j in range(1, n):
        if j == 1:
            maxv = A[j] - A[j-1]
        if maxv < A[j] - minv:
            maxv = A[j] - minv
        if minv > A[j]:
            minv = A[j]
    print(maxv)

n=int(input())
A=[int(input()) for i in range(n)]

max_profit(A, n)
