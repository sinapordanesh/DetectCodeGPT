def takoyaki_festival(N, d):
    total_health_points = 0
    for i in range(N):
        for j in range(i+1, N):
            total_health_points += d[i] * d[j]
    return total_health_points

# Sample Input
N = 3
d = [3, 1, 2]
print(takoyaki_festival(N, d))

N = 7
d = [5, 0, 7, 8, 3, 3, 2]
print(takoyaki_festival(N, d))