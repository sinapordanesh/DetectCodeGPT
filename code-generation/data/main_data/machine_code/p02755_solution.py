def find_price(A, B):
    for price in range(1, 1000):
        tax8 = price * 0.08
        tax10 = price * 0.1
        if int(tax8) == A and int(tax10) == B:
            return price
    return -1

A, B = map(int, input().split())
print(find_price(A, B))