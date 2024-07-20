def min_possible_ugliness(N, M, a):
    a.sort()
    res = 0
    for i in range(N):
        res = max(res, (a[i] + a[2*N-1-i]) % M)
    return res

N, M = map(int, input().split())
a = list(map(int, input().split()))
print(min_possible_ugliness(N, M, a))