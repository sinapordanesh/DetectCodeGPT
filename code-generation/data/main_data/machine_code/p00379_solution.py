def dudeney_number(a, n, m):
    count = 0
    for x in range(1, m+1):
        y = sum([int(d) for d in str(x)])
        if x == (y + a) ** n:
            count += 1
    return count

a, n, m = map(int, input().split())
print(dudeney_number(a, n, m))