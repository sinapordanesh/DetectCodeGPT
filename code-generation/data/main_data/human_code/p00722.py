# AOJ 1141: Dirichlet's Theorem on Arithmetic Progre...
# Python3 2018.7.15 bal4u

MAX = 1000000
SQRT = 1000     # sqrt(MAX)

prime = [True]*MAX
def sieve():
	prime[1] = 0
	for i in range(4, MAX, 2): prime[i] = False
	for i in range(3, SQRT, 2):
		if prime[i]:
			for j in range(i*i, MAX, i): prime[j] = False
sieve()
while True:
	a, d, n = map(int, input().split())
	if a == 0: break
	a -= d
	while n > 0:
		a += d
		if prime[a]: n -= 1
	print(a)

