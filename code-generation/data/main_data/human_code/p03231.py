from fractions import gcd
def lcm(a, b):
    return (a*b)//gcd(a, b)
N,M = map(int, input().split())
S = input()
T = input()
L = gcd(N,M)

if all([S[i*N//L] == T[i*M//L] for i in range(L)]):
    print(lcm(N,M))
else:
    print('-1')
    
