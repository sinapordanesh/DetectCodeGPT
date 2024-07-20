def solve(N, A):
    for k in range(N):
        count = 0
        for i in range(N):
            if i != k:
                count += A.count(A[i]) - 1
        print(count // 2)