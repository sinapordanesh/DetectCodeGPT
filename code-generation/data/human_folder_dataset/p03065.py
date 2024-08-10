import sys,math

def I(): return int(sys.stdin.readline().rstrip())

N = I()
a = [I() for _ in range(N+1)]
a.reverse()

ans = set([])

g = a[0]
for i in range(N):
    g = math.gcd(g,a[i+1])

for p in range(2,int(g**.5)+1):
    if g % p == 0:
        ans.add(p)
        g //= p
if g != 1:
    ans.add(g)

if N == 0:
    ans = list(ans)
    ans.sort()
    print(*ans, sep='\n')
    exit()


def sieve_of_eratosthenes(n):
    prime_list = []  # n以下の素数のリスト
    A = [1]*(n+1)    # A[i] = iが素数なら1,その他は0
    A[0] = A[1] = 0
    for i in range(2,math.floor(math.sqrt(n))+1):
        if A[i]:
            prime_list.append(i)
            for j in range(i**2,n+1,i):
                A[j] = 0
    for i in range(math.floor(math.sqrt(n))+1,n+1):
        if A[i] == 1:
            prime_list.append(i)
    return prime_list


prime_list = sieve_of_eratosthenes(N)

for p in prime_list:  # f(x) が x**p-x で割り切れるかを判定
    if a[0] % p != 0:
        continue
    else:
        for i in range(p-1):
            if i == 0:
                r = 0
                for j in range(p-1,N+1,p-1):
                    r += a[j]
                    r %= p
                if r != 0:
                    break
            else:
                r = 0
                for j in range(i,N+1,p-1):
                    r += a[j]
                    r %= p
                if r != 0:
                    break
        else:
            ans.add(p)

ans = list(ans)
ans.sort()
print(*ans,sep='\n')