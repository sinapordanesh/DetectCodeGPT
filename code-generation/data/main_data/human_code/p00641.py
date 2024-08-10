# AOJ 1055 Huge Family
# Python3 2018.7.7 bal4u

# UNION-FIND library
class UnionSet:
	def __init__(self, nmax):
		self.size = [1]*nmax
		self.id = [i for i in range(nmax+1)]
	def root(self, i):
		while i != self.id[i]:
			self.id[i] = self.id[self.id[i]]
			i = self.id[i]
		return i
	def connected(self, p, q): return self.root(p) == self.root(q)
	def unite(self, p, q):
		i, j = self.root(p), self.root(q)
		if i == j: return
		if self.size[i] < self.size[j]:
			self.id[i] = j
			self.size[j] += self.size[i]
		else:
			self.id[j] = i
			self.size[i] += self.size[j]
# UNION-FIND library

def check(k, f):
	if cnt[k] == 0 or f > vmax[k]: cnt[k], vmax[k] = 1, f
	elif f == vmax[k]: cnt[k] += 1

while True:
	n = int(input())
	if n == 0: break
	u = UnionSet(n)
	f = [[0 for j in range(2)] for i in range(n)]
	cnt, vmax = [0]*n, [0]*n
	for i in range(n):
		a, f[i][0], b, f[i][1] = map(int, input().split())
		u.unite(i, a)
		u.unite(i, b)
	for i in range(n):
		k = u.root(i)
		check(k, f[i][0])
		check(k, f[i][1])
	ans = 1
	for i in range(n):
		if cnt[i]: ans = ans * (cnt[i] >> 1) % 10007
	print(ans)

