# AOJ 1200: Goldbach's Conjecture
# Python3 2018.7.19 bal4u

MAX = 32770    # > 2^15
SQRT = 182     # sqrt(MAX)+1

prime = [True]*(MAX+1)
def sieve():
    for i in range(4, MAX, 2): prime[i] = False
    for i in range(3, SQRT, 2):
        if prime[i]:
            for j in range(i*i, MAX, i): prime[j] = False

sieve()
while True:
    n = int(input())
    if n == 0: break
    if n == 4: ans = 1
    else:
        ans = 0
        for i in range(3, 1+(n>>1), 2):
            if prime[i] and prime[n-i]: ans += 1
    print(ans)

