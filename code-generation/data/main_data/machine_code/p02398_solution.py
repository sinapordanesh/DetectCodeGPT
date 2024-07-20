def num_divisors(a, b, c):
    count = 0
    for i in range(a, b+1):
        if c % i == 0:
            count += 1
    return count

a, b, c = map(int, input().split())
print(num_divisors(a, b, c))