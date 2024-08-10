import math

def max_gcd(N, P):
    max_gcd = math.gcd(N, P)
    return max_gcd

N, P = map(int, input().split())
print(max_gcd(N, P))