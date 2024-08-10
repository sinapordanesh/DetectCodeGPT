def minkowski_distance(n, x, y):
    p1 = sum([abs(x[i] - y[i]) for i in range(n)]) ** (1/1)
    p2 = sum([abs(x[i] - y[i]) ** 2 for i in range(n)]) ** (1/2)
    p3 = sum([abs(x[i] - y[i]) ** 3 for i in range(n)]) ** (1/3)
    pinf = max([abs(x[i] - y[i]) for i in range(n)])
    return p1, p2, p3, pinf

n = int(input())
x = list(map(int, input().split()))
y = list(map(int, input().split()))

result = minkowski_distance(n, x, y)
for val in result:
    print("{:.6f}".format(val))