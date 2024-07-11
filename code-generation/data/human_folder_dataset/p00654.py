# AOJ 1069: Squid Multiplication
# Python3 2018.7.10 bal4u

def gcd(a, b):
	while b != 0:
		r = a % b
		a, b = b, r
	return a

while True:
	n = int(input())
	if n == 0: break
	even, odd = [], []
	b = list(map(int, input().split()))
	for i in b:
		if i & 1: odd.append(i)
		else: even.append(i)
	even.sort()
	odd.sort()
	e1, e2, o1 = even[0], even[1], odd[0];
	g = gcd(e1, o1)
	e1, o1 = e1//g, o1//g
	g = gcd(e2, o1)
	e2, o1 = e2//g, o1//g
	g = int((e1 * e2)**0.5)
	print(g)
	print(*[i//g for i in even])

