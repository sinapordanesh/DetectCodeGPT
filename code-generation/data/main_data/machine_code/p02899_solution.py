def reconstruct_order(N, A):
    order = [0]*N
    for i in range(N):
        order[A[i]-1] = i+1
    return order

N = int(input())
A = list(map(int, input().split()))
result = reconstruct_order(N, A)
print(*result)