# AOJ 1103: Board Arrangements for Concentration Gam...
# Python3 2018.7.14 bal4u

def combi(k):
	global ans
	if k == 9:
		ans += 1
		return
	for y in range(4):
		for x in range(4):
			if arr[y][x]: continue
			arr[y][x] = k
			for i in range(4):
				x2, y2 = x + a[i<<1], y + a[(i<<1)+1]
				if x2 < 0 or x2 >= 4 or y2 < 0 or y2 >= 4 or arr[y2][x2]: continue
				arr[y2][x2] = k
				combi(k+1)
				arr[y2][x2] = 0
			arr[y][x] = 0
			return;

while True:
	a = list(map(int, input().split()))
	if len(a) == 1: break
	arr = [[0 for i in range(4)] for j in range(4)]
	ans = 0
	arr[0][0] = 1
	for i in range(4):
		x, y = a[i<<1], a[(i<<1)+1]
		if x >= 0 and y >= 0:
			arr[y][x] = 1
			combi(2)
			arr[y][x] = 0
	print(ans)

