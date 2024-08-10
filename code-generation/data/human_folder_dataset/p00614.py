# AOJ 1028: ICPC: Ideal Coin Payment and Change
# Python3 2018.7.5 bal4u

c = (500, 100, 50, 10, 5, 1)

def pay(p):
	cnt = 0
	for i in range(6):
		if c[i] <= p:
			k = p//c[i]
			if k > n[i]: k = n[i]
			cnt += k
			p -= c[i]*k
	return -1 if p > 0 else cnt

k = [0]*1001
for p in range(1, 1001):
	cnt, q = 0, p
	for j in range(6):
		if c[j] <= q:
			cnt += q//c[j]
			q %= c[j]
	k[p] = cnt;

while True:
	a = list(map(int, input().split()))
	p = a[0]
	if p == 0: break
	del a[0]
	n = a[::-1]
	ans = 0x7fffffff
	for i in range(p, p+1001):
		j = pay(i)
		if j < 0: continue
		ans = min(ans, j + k[i-p])
	print(ans)
