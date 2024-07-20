def min_total_price(a, b, c):
    return min(a+b, a+c, b+c)

a, b, c = map(int, input().split())
print(min_total_price(a, b, c))