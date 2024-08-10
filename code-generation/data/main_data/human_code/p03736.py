import sys
read = sys.stdin.buffer.read
INF = 10**12

class Rmin():
	def __init__(self, size):
		#the number of nodes is 2n-1
		self.n = 1 << (size.bit_length())
		self.node = [INF] * (2*self.n-1)

	def Access(self, x):
		return self.node[x+self.n-1]

	def Update(self, x, val):
		x += self.n-1
		self.node[x] = val
		while x > 0:
			x = (x-1)>>1
			self.node[x] = min(self.node[(x<<1)+1], self.node[(x<<1)+2])
		return

	#[l, r)
	def Get(self, l, r):
		L, R = l+self.n, r+self.n
		s = INF
		while L<R:
			if R & 1:
				R -= 1
				s = min(s, self.node[R-1])
			if L & 1:
				s = min(s, self.node[L-1])
				L += 1
			L >>= 1
			R >>= 1
		return s

n, q, a, b, *qs = map(int, read().split())
dp_l, dp_r = Rmin(n+1), Rmin(n+1)
dp_l.Update(b, -b)
dp_r.Update(b, b)

total_diff = 0
x = a
for y in qs:
	diff = abs(y - x)
	l_min = dp_l.Get(1, y)
	r_min = dp_r.Get(y, n+1)
	res = min(l_min + y, r_min - y)
	dp_l.Update(x, res - diff - x)
	dp_r.Update(x, res - diff + x)
	total_diff += diff
	x = y

N = dp_l.n
print(total_diff + min((l+r)>>1 for l, r in zip(dp_l.node[N:], dp_r.node[N:])))