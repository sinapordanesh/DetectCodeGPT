def is_prime(dataset):
    def is_divisor(m, n, p, q):
        return (m**2 + n**2) * ((m*p) + (n*q)) % (m**2 + n**2) == 0 and (m**2 + n**2) * ((m*q) - (n*p)) % (m**2 + n**2) == 0

    prime_count = 0
    m, n = dataset
    if m**2 + n**2 == 1:
        return 'C'
    for x in [1, 0, -1]:
        for y in [1, 0, -1]:
            if x == 0 and y == 0:
                continue
            if is_divisor(m, n, x, y):
                prime_count += 1
    if prime_count == 8:
        return 'P'
    else:
        return 'C'
        
n = int(input())
for _ in range(n):
    dataset = list(map(int, input().split()))
    print(is_prime(dataset))