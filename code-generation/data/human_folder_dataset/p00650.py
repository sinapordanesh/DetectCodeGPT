# AOJ 1065 The House of Huge Family
# Python3 2018.7.10 bal4u

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

while True:
	n, m = map(int, input().split())
	if n == 0: break
	u = UnionSet(n)
	ans, tbl = 0, []
	for i in range(m):
		x, y, c = map(int, input().split())
		if c < 0: ans += c
		else: tbl.append((c, x, y))
	tbl.sort(reverse=True)
	for c, x, y in tbl:
		if not u.connected(x, y):
			if n > 2:
				n -= 1
				u.unite(x, y)
			else: ans += c
	print(ans)

