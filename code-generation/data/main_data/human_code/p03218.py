N = int(input())
a = list(map(int,input().split()))
Mod = 998244353

def gcd(a, b):
	while b:
		a, b = b, a % b
	return a

a.sort()

ans = 1
for i in range(N):
    ans *= gcd(a[i],i)
    ans %= Mod

print(ans)