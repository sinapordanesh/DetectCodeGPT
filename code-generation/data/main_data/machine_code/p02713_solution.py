def gcd(a, b):
    while b != 0:
        a, b = b, a % b
    return a

def sum_gcd(K):
    total = 0
    for a in range(1, K+1):
        for b in range(1, K+1):
            for c in range(1, K+1):
                total += gcd(gcd(a, b), c)
    return total

K = int(input())
print(sum_gcd(K))