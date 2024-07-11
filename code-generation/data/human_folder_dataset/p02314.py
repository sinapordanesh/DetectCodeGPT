def coin(n, p, c):
    global count
    global m
    if n % c[0] == 0:
        count = min(count, p + n // c[0])
        return count
    elif p + n // c[0] >= count:
        return n
    elif c[0] < n:
        return min(coin(n - c[0], p + 1, c), coin(n, p, c[1:]))
    else:
        return coin(n, p, c[1:])

n, m = map(int, input().split())

mon = list(map(int, input().split()))

mon.sort(reverse = True)

count = n

print(coin(n, 0, mon))
