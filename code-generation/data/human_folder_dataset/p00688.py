# AOJ 1106: Factorization of Quadratic Formula
# Python3 2018.7.15 bal4u

def gcd(a, b):
	while b != 0:
		r = a % b
		a, b = b, r
	return a

while True:
	a, b, c = map(int, input().split())
	if a == 0: break
	d = b**2-4*a*c
	if d < 0: print("Impossible"); continue
	d = d**0.5
	if not d.is_integer(): print("Impossible"); continue
	d = int(d)
	d1, d2, a2 = -b+d, -b-d, a<<1
	g1, g2 = gcd(d1, a2), gcd(d2, a2)
	p, q = a2//g1, -d1//g1
	if p < 0: p, q = -p, -q
	r, s = a2//g2, -d2//g2
	if r < 0: r, s = -r, -s
	if (p < r) or (p == r and q < s): p, q, r, s = r, s, p, q
	print(p, q, r, s)

