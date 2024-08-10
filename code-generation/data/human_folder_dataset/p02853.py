def plus(x):
    yen = 0
    if x < 4:
        yen = yen + 100000
    if x < 3:
        yen = yen + 100000
    if x < 2:
        yen = yen + 100000
    return yen

x, y = map(int, input().split())

res = plus(x) + plus(y)

if x == 1 and y == 1:
    res = res + 400000

print(res)