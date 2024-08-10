def kangaroo_time(X):
    x = abs(X)
    t = 0
    s = 0
    while s < x or (s - x) % 2 != 0:
        t += 1
        s += t
    return t

X = int(input())
print(kangaroo_time(X))