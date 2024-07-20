# AOJ 1059 Mysterious Onslaught
# Python3 2018.7.7 bal4u

def calc(b):
	if b == 0: return 0;
	if memo[b] >= 0: return memo[b]
	f = False
	for r1 in range(n):
		for c1 in range(n):
			if b & (1<<(5*r1+c1)):
				f, rr, cc = True, r1, c1
				break
		if f: break
	if not f:
		memo[b] = 0
		return 0

	ans = 25;
	for r2 in range(rr, n):
		for c2 in range(cc, n):
			k = b ^ arr[rr][cc][r2][c2]
			ans = min(ans, calc(k)+1)
	memo[b] = ans
	return ans

memo = [-1]*(1<<25)
arr = [[[[0 for c2 in range(5)] for r2 in range(5)] \
		    for c1 in range(5)] for r1 in range(5)]
for r1 in range(5):
	for c1 in range(5):
		for r2 in range(r1, 5):
			for c2 in range(c1, 5):
				for r in range(r1, r2+1):
					for c in range(c1, c2+1):
						arr[r1][c1][r2][c2] |= (1<<(r*5+c))

while True:
	n = int(input())
	if n == 0: break
	a = [list(map(int, input().split())) for i in range(n)]
	b = 0;
	for r in range(n):
		for c in range(n):
			if a[r][c]: b |= 1 << (5*r+c)
	print("myon"*calc(b))
