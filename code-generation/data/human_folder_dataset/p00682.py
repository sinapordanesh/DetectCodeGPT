# AOJ 1100: Area of Polygons
# Python3 2018.7.14 bal4u

from decimal import Decimal, ROUND_HALF_UP, ROUND_HALF_EVEN

def calc_area(pp):
	n = len(pp)
	if n < 3: return 0
	s = 0
	for i in range(n):
		s += (pp[i].real-pp[(i+1)%n].real)*(pp[i].imag+pp[(i+1)%n].imag)
	return abs(s)/2

cno = 0
while True:
	n = input()
	if n == '': n = input()
	n = int(n);
	if n == 0: break
	pp = []
	for i in range(n):
		x, y = map(int, input().split())
		pp.append(complex(x, y))
	cno += 1
	print(cno, Decimal(str(calc_area(pp))).quantize(Decimal('0.1'), rounding=ROUND_HALF_UP))

