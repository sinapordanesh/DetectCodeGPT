def factorization(n):
    i = 2
    L = []
    num = n
    while i**2 <= n:
        c = 0
        while num%i == 0:
           num //= i
           c += 1 
        
        if c > 0:
            L.append((i, c))
        i += 1

    if num > 1:
        L.append((n, 1))
    return L

N, P = map(int, input().split())
if N == 1:
    print(P)
    exit()
facts = factorization(P)
ans = 1
for p, c in facts:
    a = c//N
    ans *= p**a
print(ans)