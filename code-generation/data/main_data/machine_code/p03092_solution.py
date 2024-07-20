def min_cost_sort(N, A, B, p):
    def cost_sort(p):
        cost = [0] * (N + 1)
        for i in range(N):
            cost[i + 1] = min(cost[j] + A if j != 0 else 0 for j in range(i + 1))
            for j in range(i):
                cost[j + 1] = min(cost[j + 1], cost[j] + B)
            while i + 1 < N and p[i + 1] == p[i] + 1:
                i += 1
        return cost[N]
    
    return cost_sort(p)

N, A, B, *p = map(int, input().split())
print(min_cost_sort(N, A, B, p))