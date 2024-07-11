from bisect import bisect
n = int(input())
P = [list(map(int, input().split())) for i in range(n)]

M = 10**5+1

def policy1(P):
    A = [a for a, b in P]
    B = [b for a, b in P]
    A.sort(); B.sort()
    ans = 1
    for a, b in P:
        left = bisect(B, a)
        right = n - bisect(A, b-1)
        ans = max(ans, n - (left + right))
    return ans

def policy2(P):
    D = [0]*M
    for a, b in P:
        D[a] += 1
        D[b] -= 1
    for i in range(1, M):
        D[i] += D[i-1]
    return max(D)

print(policy1(P), policy2(P))