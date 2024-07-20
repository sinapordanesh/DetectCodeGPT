def power_calculus(n):
    if n == 0:
        return 0
    if n % 2 == 0:
        return power_calculus(n // 2) + 1
    else:
        return power_calculus(n - 1) + 1

for line in iter(input, '0'):
    n = int(line)
    result = power_calculus(n)
    print(result)