def extended_euclid_algorithm(a, b):
    if b == 0:
        return 1, 0
    else:
        x, y = extended_euclid_algorithm(b, a % b)
        return y, x - (a // b) * y

a, b = map(int, input().split())
x, y = extended_euclid_algorithm(a, b)
print(x, y)