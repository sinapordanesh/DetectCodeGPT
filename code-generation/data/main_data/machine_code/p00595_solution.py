def greatest_common_divisor(a, b):
    while b:
        a, b = b, a % b
    return a

# Sample Input
print(greatest_common_divisor(57, 38))
print(greatest_common_divisor(60, 84))