import numpy as np

def convolve(a, b):
	n = 1
	n_a, n_b = len(a), len(b)
	while n < n_a + n_b - 1:
		n <<= 1
	A = np.fft.rfft(a, n)
	B = np.fft.rfft(b, n)

	C = A * B
	c = np.fft.irfft(C, n)
	c = np.rint(c).astype(np.int64)

	return c[:n_a + n_b - 1]

p = 200003
n = int(input())
b = list(map(int, input().split()))
a = [0 for _ in range(p-1)]
ref = [0 for _ in range(p)]
po = [0 for _ in range(p-1)]
y = 1
for i in range(p-1):
	ref[y] = i
	po[i] = y
	y = (y * 2) % p
ans = 0
for x in b:
	if x == 0:
		continue
	a[ref[x]] += 1
	ans -= (x*x) % p
conv = convolve(a, a)
for i in range(2*p-3):
	ans += po[i % (p-1)] * conv[i]
print(ans // 2)