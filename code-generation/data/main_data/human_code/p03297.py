def solve(P):
    A, B, C, D = P
    if A<B or D<B:
        return False
    if C >= B-1:
        return True
    g = gcd(B,D)
    return A%B+(B-A%B-1)//g*g <= C

from math import gcd

T = int(input())
for _ in range(T):
    P = map(int, input().split())
    print("Yes" if solve(P) else "No")