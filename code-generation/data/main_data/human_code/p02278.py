def calcurate_cost(A, B, n):
    cost = 0
    s = min(A)
    V = [False] * n
    T = { j:i for i, j in enumerate(B) }
    for i in range(n):
        if V[i]:
            continue
        cur = i
        S = 0
        an = 0
        m = 10000
        while True:
            V[cur] = True
            an += 1
            v = A[cur]
            m = min(m, v)
            S += v
            cur = T[v]
            if V[cur]:
                break
        cost += min(S + (an - 2) * m, m + S + (an + 1) * s)
    return cost
    
def minimum_cost_sort(A, n):
    B = sorted(A)
    return calcurate_cost(A, B, n)

n = int(input())
A = [int(i) for i in input().split()]
print(minimum_cost_sort(A, n))
