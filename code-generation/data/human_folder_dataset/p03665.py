def cmb(n, r):
    if n - r < r: r = n - r
    if r == 0: return 1
    if r == 1: return n

    numerator = [n - r + k + 1 for k in range(r)]
    denominator = [k + 1 for k in range(r)]

    for p in range(2,r+1):
        pivot = denominator[p - 1]
        if pivot > 1:
            offset = (n - r) % p
            for k in range(p-1,r,p):
                numerator[k - offset] /= pivot
                denominator[k] /= pivot

    result = 1
    for k in range(r):
        if numerator[k] > 1:
            result *= int(numerator[k])

    return result


N, P = map(int, input().split())
A = list(map(int, input().split()))

odd = 0
even = 0
for i in range(N):
    if A[i] % 2 == 0:
        even += 1
    else:
        odd += 1
        
ans = 0
for i in range(P, odd+1, 2):
    ans += cmb(odd, i)
    
ans *= 2 ** even

print(ans)