# AOJ 1108: A Long Ride on a Railway
# Python3 2018.7.14 bal4u

def combi(k, a, w):
	global len, ans
	for b in range(1, n+1):
		if b == a: continue
		for i in range(m):
			if not f[i] and ((tbl[i][0] == a and tbl[i][1] == b) or
			                 (tbl[i][0] == b and tbl[i][1] == a)):
				f[i] = 1
				tmp[k] = b
				combi(k+1, b, w + tbl[i][2])
				f[i] = 0
	if w > len:
		len = w
		ans = tmp[:k]	

ans, tmp = [0]*12, [0]*12
while True:
	n, m = map(int, input().split())
	if n == 0: break
	tbl = [list(map(int, input().split())) for i in range(m)]
	f, ans = [0]*m, []
	len = 0
	for a in range(1, n+1):
		for b in range(1, n+1):
			if a == b: continue
			for i in range(m):
				if not f[i] and ((tbl[i][0] == a and tbl[i][1] == b) or
				                 (tbl[i][0] == b and tbl[i][1] == a)):
					f[i] = 1
					tmp[0], tmp[1] = a, b
					combi(2, b, tbl[i][2])
					f[i] = 0
	print(len)
	print(*ans)
