def min_operations(N, P):
    cnt = 0
    for i in range(N):
        if P[i] == i + 1:
            cnt += 1
    return N - cnt

N = int(input())
P = list(map(int, input().split()))
print(min_operations(N, P))