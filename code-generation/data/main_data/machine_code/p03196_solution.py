import math

def max_gcd(N, P):
    factors = []
    for i in range(2, int(math.sqrt(P))+1):
        while P % i == 0:
            factors.append(i)
            P //= i
    if P > 1:
        factors.append(P)
    
    gcd = factors[0]
    for factor in factors:
        gcd = math.gcd(gcd, factor)
    
    return gcd

# Input
N, P = map(int, input().split())

# Output
print(max_gcd(N, P))