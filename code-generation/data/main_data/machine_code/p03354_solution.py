def max_number_of_fixed_point(N, M, p, pairs):
    cnt = 0
    fixed_points = set([i+1 for i in range(N) if p[i] == i+1])
    for x, y in pairs:
        if p[x-1] == x and p[y-1] != y:
            fixed_points.remove(x)
            fixed_points.add(y)
        elif p[y-1] == y and p[x-1] != x:
            fixed_points.remove(y)
            fixed_points.add(x)
        cnt = max(cnt, len(fixed_points))
    return cnt

# Input
N, M = map(int, input().split())
p = list(map(int, input().split()))
pairs = [list(map(int, input().split())) for _ in range(M)]

# Output
print(max_number_of_fixed_point(N, M, p, pairs))