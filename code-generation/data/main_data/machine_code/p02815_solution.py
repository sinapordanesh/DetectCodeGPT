MOD = 10**9 + 7

def f(S, T):
    cost = 0
    for i in range(len(S)):
        if S[i] != T[i]:
            cost += 1
    return cost

def sum_f(N, C):
    total_cost = 0
    for i in range(1, 2**N):
        for j in range(1, 2**N):
            S = [int(x) for x in bin(i)[2:].zfill(N)]
            T = [int(x) for x in bin(j)[2:].zfill(N)]
            total_cost = (total_cost + f(S, T) * C[i-1]) % MOD
    return total_cost

N = int(input())
C = list(map(int, input().split()))
print(sum_f(N, C))