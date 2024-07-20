# AOJ 1172: Chebyshev's Theorem
# Python3 2018.7.14 bal4u

MAX = 250000
SQRT = 500     # sqrt(MAX)

prime = [True]*MAX
def sieve():
	for i in range(2, MAX, 2): prime[i] = False
	for i in range(3, SQRT, 2):
		if prime[i]:
			for j in range(i*i, MAX, i): prime[j] = False
			
sieve()
while True:
	n = int(input())
	if n == 0: break
	ans, m = 0, n << 1
	if n == 1: ans += 1         # for 2
	i = n + 1
	if (i&1) == 0: i += 1       # for odd num only
	while i <= m:
		if prime[i]: ans += 1
		i += 2
	print(ans)

