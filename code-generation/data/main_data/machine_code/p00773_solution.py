def max_after_tax_price(x, y, s):
    max_price = -1
    for p1 in range(1, s):
        p2 = s - p1
        price1 = (p1 * (100 + x)) // 100
        price2 = (p2 * (100 + x)) // 100
        after_tax_price = price1 + price2
        max_price = max(max_price, (price1 * (100 + y) // 100) + (price2 * (100 + y) // 100))
    return max_price

while True:
    x, y, s = map(int, input().split())
    if x == 0 and y == 0 and s == 0:
        break
    print(max_after_tax_price(x, y, s))