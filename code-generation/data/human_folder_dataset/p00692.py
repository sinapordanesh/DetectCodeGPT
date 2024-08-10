# AOJ 1110: Patience
# Python3 2018.7.8 bal4u

pair = [[1,4,5], [2,4,5,6], [3,5,6,7], [6,7], [5,8,9],
	[6,8,9,10], [7,9,10,11], [10,11], [9,12,13], [10,12,13,14],
	[11,13,14,15], [14,15], [13,16,17], [14,16,17,18], [15,17,18,19],
	[18,19], [17], [18], [19]]

def combi(cd, n):
	global ans
	ans = min(ans, n)
	if n == 0: return True
	for p in range(n-1):
		a = (cd >> (p*3)) & 7
		for q in pair[p]:
			b = (cd >> (q*3)) & 7
			if a != b: continue
			b1 =  cd             & ((1<<(p*3))-1)
			b2 = (cd >> (p+1)*3) & ((1<<(q-p-1)*3)-1)
			b3 = (cd >> (q+1)*3) & ((1<<(n-q-1)*3)-1)
			nc = b1 | (b2<<(p*3)) | (b3<<(q-1)*3)
			if combi(nc, n-2): return True
	return False

for _ in range(int(input())):
	k = []
	for i in range(5):
		k.extend(list(map(int, input().split())))
	card = 0
	for i in range(19, -1, -1): card = (card<<3)|k[i]
	ans = 20
	combi(card, 20)
	print(ans)

