MOD = 998244353

def sum_of_f(T):
    total = 0
    for i in range(1, len(T)+1):
        total += i * (len(T) - i + 1)
    return total % MOD

N = int(input())
points = []
for _ in range(N):
    x, y = map(int, input().split())
    points.append((x, y))

result = 0
for i in range(N):
    for j in range(i+1, N):
        result += sum_of_f(points[i:j+1])

print(result % MOD)