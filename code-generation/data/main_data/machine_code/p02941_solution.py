def solve(N, A, B):
    for i in range(N):
        total_ops = 0
        for j in range(N):
            a = A[(j-1)%N]
            b = A[j]
            c = A[(j+1)%N]
            if (a+b+c) != B[j]:
                ops = (B[j] - (a+b+c))
                if ops < 0 or ops % N != 0:
                    break
                total_ops += ops // N
        else:
            return total_ops
    return -1

# Input
N = int(input())
A = list(map(int, input().split()))
B = list(map(int, input().split()))

# Output
print(solve(N, A, B))