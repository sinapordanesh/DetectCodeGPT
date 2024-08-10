def max_monsters(N, A, B):
    result = 0
    for i in range(N):
        result += min(A[i], B[i])
        A[i+1] -= max(0, B[i] - A[i])
    result += min(A[N], B[N])
    return result

#Input Reading
N = int(input())
A = list(map(int, input().split()))
B = list(map(int, input().split()))

#Function Call
print(max_monsters(N, A, B))