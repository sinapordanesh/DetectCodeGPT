from collections import defaultdict
import math

def sieve_of_eratosthenes(n):
    sieve = list(range(n+1))
    m = int(math.sqrt(n))
    for i in range(2, m + 1):
        if sieve[i] < i:
            continue
        for j in range(i * i, n + 1, i):
            if sieve[j] == j:
                sieve[j] = i
    return sieve

def factorize_by_sieve(x, sieve):
    factor = dict()
    while x != 1:
        if sieve[x] in factor:
            factor[sieve[x]] += 1
        else:
            factor[sieve[x]] = 1
        x //= sieve[x]
    return factor

mod = 10 ** 9 + 7
n = int(input())
if n == 1:
    print(1)
    quit()

sieve = sieve_of_eratosthenes(n)
dic = defaultdict(int)
for i in range(2, n+1):
    factor = factorize_by_sieve(i, sieve)
    for p, dim in factor.items():
        dic[p] += dim

ans = 1
for _, dim in dic.items():
    ans = ans * (dim + 1) % mod
print(ans)
