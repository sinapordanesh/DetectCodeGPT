def greatest_common_divisor(a, b):
    if b == 0:
        return a
    else:
        return greatest_common_divisor(b, a % b)

a, b = map(int, input().split())
print(greatest_common_divisor(a, b))