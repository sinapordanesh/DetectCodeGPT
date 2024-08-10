def f(L, R):
    return (R - L + 1) * (R - L + 2) // 2

N = int(input())
edges = [list(map(int, input().split())) for _ in range(N-1)]

result = 0
for L in range(1, N+1):
    for R in range(L, N+1):
        result += f(L, R)

print(result)